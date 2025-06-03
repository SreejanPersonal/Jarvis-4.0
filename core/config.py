import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    PICOVOICE_API_KEY = os.getenv("PICOVOICE_API_KEY")
    HOTWORD_KEYWORDS = ["jarvis"]

    _PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SOUND_START_UP = os.path.join(_PROJECT_ROOT, "data", "sounds", "start_up_sound.wav")
    SOUND_END_SESSION = os.path.join(_PROJECT_ROOT, "data", "sounds", "end_up_sound.wav")

    GEMINI_LIVE_MODEL_NAME = "models/gemini-2.5-flash-preview-native-audio-dialog"
    GEMINI_LIVE_SYSTEM_INSTRUCTION = "You are a helpful assistant. Be concise and friendly."
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_LIVE_VIDEO_MODE = "none" # Options: "camera", "screen", "none"