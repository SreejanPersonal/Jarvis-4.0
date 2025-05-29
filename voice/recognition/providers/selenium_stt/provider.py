import os
from typing import Optional, Dict, Any

from core.logger import get_logger
from voice.recognition.base import BaseRecognitionProvider
from voice.recognition.providers.selenium_stt.driver_manager import DriverManager
from voice.recognition.providers.selenium_stt.recognition import RecognitionHandler

logger = get_logger(__name__)

class SeleniumSTTProvider(BaseRecognitionProvider):
    PROVIDER_NAME = "selenium_stt"

    LANGUAGE_OPTIONS = {
        "en-US": "English (United States)",
        "en-IN": "English (India)",
        "hi-IN": "Hindi (India)",
    }

    def __init__(self, language: str = "en-US", wait_time: int = 10, quiet_timeout_seconds: float = 7.0, website_path: Optional[str] = None):
        super().__init__()
        self.language = language
        self.wait_time = wait_time
        self.quiet_timeout_seconds = quiet_timeout_seconds

        default_local_html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "index.html")
        if website_path is None:
            self.raw_website_path = default_local_html_path
        else:
            self.raw_website_path = website_path
        
        self.driver_manager = DriverManager(wait_time)
        self.recognition_handler = RecognitionHandler(self)

    def listen(self, prints: bool = False) -> Optional[str]:
        result = self.recognition_handler.main()

        if result is None:
            logger.error("Speech recognition failed critically. WebDriver might be re-initialized on next call.")
            return None
        
        if result == "":
            return ""

        if prints:
            print(f"\033[92mYOU SAID: {result}\033[0m\n", flush=True)
        
        return result

    def get_available_languages(self) -> Dict[str, Any]:
        return self.LANGUAGE_OPTIONS

    def __del__(self):
        if hasattr(self, 'driver_manager'):
            logger.info("Closing SeleniumSTTProvider resources...")
            self.driver_manager.cleanup()
