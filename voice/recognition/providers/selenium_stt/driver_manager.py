from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

from core.logger import get_logger

logger = get_logger(__name__)

class DriverManager:
    def __init__(self, wait_time: int = 10):
        self.wait_time = wait_time
        self.driver = None
        self.wait = None
        self.setup_driver()
    
    def setup_driver(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            try:
                self.driver.quit()
            except Exception:
                logger.warning("Error quitting previous driver instance.")
            finally:
                self.driver = None
        
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, self.wait_time)
            logger.info("Chrome WebDriver initialized/re-initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            self.driver = None
            self.wait = None
            raise
    
    def try_stop_js_recognition(self):
        if not hasattr(self, 'driver') or not self.driver:
            return
        try:
            self.driver.execute_script("""
                if (window.currentRecognitionInstance && typeof window.currentRecognitionInstance.stop === 'function') {
                    try { window.currentRecognitionInstance.stop(); } catch (e) { /* ignore */ }
                }
            """)
        except Exception:
            logger.warning("Failed to execute script to stop JS recognition.")
            pass
    
    def cleanup(self):
        if hasattr(self, 'driver') and self.driver:
            self.try_stop_js_recognition()
            try:
                self.driver.quit()
                logger.info("Chrome WebDriver closed successfully")
            except Exception as e:
                logger.error(f"Error closing Chrome WebDriver: {e}")
            finally:
                self.driver = None
