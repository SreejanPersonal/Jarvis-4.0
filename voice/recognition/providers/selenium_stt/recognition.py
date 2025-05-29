import os
import time
from pathlib import Path
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from core.logger import get_logger
from voice.recognition.providers.selenium_stt.language_handler import LanguageHandler
from voice.recognition.providers.selenium_stt.utils import stream_text

logger = get_logger(__name__)

class RecognitionHandler:
    def __init__(self, provider):
        self.provider = provider
        self.language_handler = LanguageHandler(provider)
    
    def get_text(self) -> str:
        if not self.provider.driver_manager.driver:
            return ""
        try:
            return self.provider.driver_manager.driver.find_element(By.ID, "convert_text").text
        except Exception:
            return ""
    
    def main(self) -> Optional[str]:
        if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
            try:
                self.provider.driver_manager.setup_driver()
            except Exception as e:
                logger.error(f"Failed to setup driver in main: {e}")
                return None
            if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
                logger.error("WebDriver not available for listening cycle after setup attempt.")
                return None

        try:
            url_to_load: str
            if "://" in self.provider.raw_website_path:
                url_to_load = self.provider.raw_website_path
            else:
                abs_path = os.path.abspath(self.provider.raw_website_path)
                if not os.path.exists(abs_path):
                    logger.error(f"HTML file not found: {abs_path}")
                    return None
                url_to_load = Path(abs_path).as_uri()
            
            current_url = ""
            try:
                current_url = self.provider.driver_manager.driver.current_url
            except WebDriverException: 
                logger.warning("WebDriver connection lost, attempting to re-initialize.")
                self.provider.driver_manager.setup_driver() 
                if not self.provider.driver_manager.driver: 
                    logger.error("Failed to re-initialize WebDriver.")
                    return None
                current_url = "" 

            if current_url != url_to_load:
                self.provider.driver_manager.driver.get(url_to_load)
            else: 
                try:
                    text_area = self.provider.driver_manager.driver.find_element(By.ID, "convert_text")
                    if text_area:
                        text_area.clear()
                    self.provider.driver_manager.driver.execute_script("document.getElementById('is_recording').innerHTML = 'Recording: False';")
                except Exception:
                    logger.debug("Could not clear text area or reset recording status on existing page.")
                    pass 

            self.provider.driver_manager.wait.until(EC.presence_of_element_located((By.ID, "language_select")))
            self.provider.driver_manager.wait.until(EC.element_to_be_clickable((By.ID, "language_select")))
            self.provider.driver_manager.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#language_select option[value='en-US']"))) 
            self.language_handler.select_language()

            if not self.language_handler.verify_language_selection():
                logger.error(f"Failed to select language: {self.provider.language}. Please check language code and HTML options.")
                return None

            self.provider.driver_manager.driver.find_element(By.ID, "click_to_record").click()
            try:
                self.provider.driver_manager.wait.until(EC.text_to_be_present_in_element((By.ID, "is_recording"), "Recording: True"))
            except TimeoutException:
                logger.warning("Recording did not start in time.")
                self.provider.driver_manager.try_stop_js_recognition()
                return "" 

            print("\033[94m\rListening...", end='', flush=True)
            time_of_last_speech_or_start = time.time()
            last_processed_text = ""

            while True:
                is_recording_status_text = ""
                try:
                    is_recording_element = self.provider.driver_manager.driver.find_element(By.ID, "is_recording")
                    is_recording_status_text = is_recording_element.text if is_recording_element else "Recording: False"
                except WebDriverException: 
                    logger.error("WebDriver connection lost during recording.")
                    self.provider.driver_manager.driver = None 
                    return None 
                except Exception: 
                    logger.debug("Could not get recording status, assuming recording stopped.")
                    break 

                if not is_recording_status_text.startswith("Recording: True"):
                    break 

                current_text_from_page = self.get_text()
                if current_text_from_page and current_text_from_page != last_processed_text:
                    stream_text(current_text_from_page)
                    last_processed_text = current_text_from_page
                    time_of_last_speech_or_start = time.time()
                else:
                    if not last_processed_text and (time.time() - time_of_last_speech_or_start) > self.provider.quiet_timeout_seconds:
                        print("\r" + " " * 70 + "\r", end="", flush=True) 
                        print("Quiet timeout: No speech detected in this attempt.", flush=True)
                        self.provider.driver_manager.try_stop_js_recognition()
                        return "" 
                time.sleep(0.1) 
            
            self.provider.driver_manager.try_stop_js_recognition() 
            final_text = self.get_text()

            clear_length = 70
            if last_processed_text:
                clear_length = len(last_processed_text) + 30
            print("\r" + " " * clear_length + "\r", end="", flush=True)
            
            return final_text

        except WebDriverException as e:
            logger.error(f"WebDriverException in listening cycle: {e}. Attempting to re-initialize on next call.")
            self.provider.driver_manager.driver = None 
            return None
        except Exception as e:
            logger.error(f"Unexpected error in listening cycle: {e}")
            if hasattr(self.provider.driver_manager, 'driver') and self.provider.driver_manager.driver:
                self.provider.driver_manager.try_stop_js_recognition()
            return None
