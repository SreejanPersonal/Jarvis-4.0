import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    PICOVOICE_API_KEY = os.getenv("PICOVOICE_API_KEY")
    HOTWORD_KEYWORDS = ["jarvis"]

    # Construct paths relative to this config file's directory, then go up to project root
    _PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SOUND_START_UP = os.path.join(_PROJECT_ROOT, "data", "sounds", "start_up_sound.wav")
    SOUND_END_SESSION = os.path.join(_PROJECT_ROOT, "data", "sounds", "end_up_sound.wav")

    # Example of how to access these:
    # from core.config import AppConfig
    # api_key = AppConfig.PICOVOICE_API_KEY
    # start_sound = AppConfig.SOUND_START_UP

