"""
Speech system initialization module.

This module handles the initialization of speech recognition and
text-to-speech systems based on configuration settings.
"""

from core.logger import get_logger
from voice.recognition.active_provider import recognition_manager
from voice.text_to_speech.active_provider import tts_manager
from core.config import AppConfig # Added for PICOVOICE_API_KEY check
from speech_interface.config import (
    STT_PROVIDER, 
    VOSK_CONFIG, 
    SELENIUM_STT_CONFIG, 
    TTS_PROVIDER
)

logger = get_logger(__name__)

def initialize_tts():
    """Initialize the text-to-speech system."""
    logger.info(f"Initializing {TTS_PROVIDER} TTS...")
    tts_manager.initialize(provider_name=TTS_PROVIDER)

def initialize_stt():
    """Initialize the speech recognition system."""
    if STT_PROVIDER == "vosk":
        logger.info("Initializing Vosk speech recognition...")
        recognition_manager.initialize(
            provider_name="vosk",
            model_name=VOSK_CONFIG["model_name"]
        )
    elif STT_PROVIDER == "selenium_stt":
        logger.info("Initializing Selenium speech recognition...")
        recognition_manager.initialize(
            provider_name="selenium_stt", 
            language=SELENIUM_STT_CONFIG["language"],
            quiet_timeout_seconds=SELENIUM_STT_CONFIG["quiet_timeout_seconds"]
        )
    else:
        logger.error(f"Unknown STT provider: {STT_PROVIDER}")
        raise ValueError(f"Unknown STT provider: {STT_PROVIDER}")

def initialize_hotword_config_check():
    """Check if the Picovoice API key is configured."""
    if not AppConfig.PICOVOICE_API_KEY:
        logger.error("PICOVOICE_API_KEY is not set in .env or core.config.AppConfig. Hotword detection will fail.")
    else:
        logger.info("Picovoice API key found and loaded for hotword detection.")

def initialize_speech_systems():
    """Initialize speech recognition, text-to-speech, and hotword config check."""
    initialize_hotword_config_check() # Added
    initialize_tts()
    initialize_stt()

