from typing import Optional, Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from core.logger import get_logger
from voice.recognition.base import BaseRecognitionProvider

logger = get_logger(__name__)

class SeleniumSTTProvider(BaseRecognitionProvider):
    """Speech-to-Text provider using Selenium for real-time transcription.
    
    This provider interfaces with a web-based speech recognition service
    to convert spoken words into text in real-time. It uses Selenium WebDriver
    to automate browser interactions and handle the audio stream.
    
    The provider supports multiple languages and provides real-time feedback
    during the transcription process.
    """

    PROVIDER_NAME = "selenium_stt"

    LANGUAGE_OPTIONS = {
        "en-IN": "English (India)",
        "hi-IN": "Hindi (India)",
        # Add more language options as needed
    }

    def __init__(self, language: str = "en-IN", wait_time: int = 10):
        """Initialize the Selenium-based STT provider.

        Args:
            language (str): The language code for speech recognition.
            wait_time (int): Maximum time to wait for web elements.
        """
        super().__init__()
        self.website_path = "https://realtime-stt-devs-do-code.netlify.app/"
        self.language = language
        self.wait_time = wait_time
        self._setup_driver()

    def _setup_driver(self) -> None:
        """Configure and initialize the Chrome WebDriver for browser automation.
        
        This method sets up a headless Chrome instance with necessary permissions
        and configurations for audio capture and web interaction.
        
        Raises:
            WebDriverException: If Chrome driver initialization fails
            Exception: For other unexpected setup errors
        """
        chrome_options = Options()
        
        # Configure browser for audio capture and automation
        chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Allow microphone access
        chrome_options.add_argument("--headless=new")  # Run in background
        
        # Set a modern user agent to ensure compatibility
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, self.wait_time)
            logger.info("Chrome WebDriver initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            raise

    def _stream(self, content: str) -> None:
        """Print the transcribed content in real-time.

        Args:
            content (str): The content to print.
        """
        print("\033[96m\rUser Speaking: \033[93m" + f" {content}", end='', flush=True)

    def _get_text(self) -> str:
        """Get the transcribed text from the webpage.

        Returns:
            str: The transcribed text.
        """
        return self.driver.find_element(By.ID, "convert_text").text

    def _select_language(self) -> None:
        """Select the language using JavaScript."""
        self.driver.execute_script(
            f"""
            var select = document.getElementById('language_select');
            select.value = '{self.language}';
            var event = new Event('change');
            select.dispatchEvent(event);
            """
        )

    def _verify_language_selection(self) -> bool:
        """Verify if the language is correctly selected.

        Returns:
            bool: True if language is correctly selected, False otherwise.
        """
        language_select = self.driver.find_element(By.ID, "language_select")
        selected_language = language_select.find_element(By.CSS_SELECTOR, "option:checked").get_attribute("value")
        return selected_language == self.language

    def _main(self) -> Optional[str]:
        """Main speech recognition logic.
        
        This method handles the core functionality of speech recognition:
        1. Navigates to the recognition service website
        2. Configures language settings
        3. Initiates recording
        4. Streams real-time transcription
        5. Returns final transcribed text
        
        Returns:
            Optional[str]: The transcribed text, or None if recognition failed
        
        Note:
            The method implements a continuous listening loop that breaks only when
            the recording status changes or an error occurs.
        """
        try:
            # Navigate to the recognition service and wait for it to load
            self.driver.get(self.website_path)
            self.wait.until(EC.presence_of_element_located((By.ID, "language_select")))
            
            # Configure language settings
            self._select_language()
            if not self._verify_language_selection():
                logger.error(f"Failed to select language: {self.language}")
                return None
            
            # Start recording
            self.driver.find_element(By.ID, "click_to_record").click()
            is_recording = self.wait.until(EC.presence_of_element_located((By.ID, "is_recording")))
            
            # Indicate recording status
            logger.info("Started listening...")
            print("\033[94m\rListening...", end='', flush=True)
            
            # Main recognition loop
            while is_recording.text.startswith("Recording: True"):
                text = self._get_text()
                if text:
                    self._stream(text)
                is_recording = self.driver.find_element(By.ID, "is_recording")
            
            # Return final transcription
            return self._get_text()
            
        except Exception as e:
            logger.error(f"Error during speech recognition: {e}")
            return None

    def listen(self, prints: bool = False) -> Optional[str]:
        """Start the listening process and return transcribed text.

        Args:
            prints (bool): Whether to print the transcribed text.

        Returns:
            Optional[str]: The transcribed text, or None if recognition failed.
        """
        while True:
            result = self._main()
            if result and len(result) != 0:
                print("\r" + " " * (len(result) + 16) + "\r", end="", flush=True)
                if prints:
                    print("\033[92m\rYOU SAID: " + f"{result}\033[0m\n")
                break
        return result

    def get_available_languages(self) -> Dict[str, Any]:
        """Get available languages for this provider.

        Returns:
            Dict[str, Any]: Dictionary of available languages.
        """
        return self.LANGUAGE_OPTIONS

    def __del__(self):
        """Clean up resources when the provider is destroyed."""
        if hasattr(self, 'driver'):
            try:
                self.driver.quit()
                logger.info("Chrome WebDriver closed successfully")
            except Exception as e:
                logger.error(f"Error closing Chrome WebDriver: {e}")