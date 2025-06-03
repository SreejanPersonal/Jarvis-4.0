"""
Configuration settings for the speech interface.

This module contains configuration parameters for the speech recognition,
text-to-speech systems, and dialog providers.
"""
from core.logger import get_logger

logger = get_logger(__name__)

VOSK_CONFIG = {
    "model_name": "english-small"
    # Alternatively, use model_path directly:
    # "model_path": "voice/voices/assets/models/vosk/vosk-model-small-en-us-0.15"
}

SELENIUM_STT_CONFIG = {
    "language": "en-US",
    "quiet_timeout_seconds": 7.0
    # "website_path": "https://realtime-stt-devs-do-code.netlify.app/"  # Example: to force online version if needed
}

STT_PROVIDER = "selenium_stt"
TTS_PROVIDER = "tiktok"
DIALOG_PROVIDER = "gemini_live" # Example: "gemini_live" or None