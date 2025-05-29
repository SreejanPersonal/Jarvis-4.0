"""
Configuration settings for the speech interface.

This module contains configuration parameters for the speech recognition
and text-to-speech systems.
"""

from core.logger import get_logger

logger = get_logger(__name__)

# Speech recognition provider configuration
STT_PROVIDER = "selenium_stt"

# Provider-specific configurations
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

# Text-to-speech provider configuration
TTS_PROVIDER = "tiktok"
