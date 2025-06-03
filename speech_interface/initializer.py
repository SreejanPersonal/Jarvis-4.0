"""
Speech system initialization module.

This module handles the initialization of speech recognition,
text-to-speech systems, and dialog providers based on configuration settings.
"""

from core.logger import get_logger
from voice.recognition.active_provider import recognition_manager
from voice.text_to_speech.active_provider import tts_manager
from core.config import AppConfig
from speech_interface.config import (
    STT_PROVIDER, 
    VOSK_CONFIG, 
    SELENIUM_STT_CONFIG, 
    TTS_PROVIDER,
    DIALOG_PROVIDER
)
from voice.dialog.manager.dialog_manager import dialog_manager

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
        logger.error("PICOVOICE_API_KEY is not set in .env or core.config.AppConfig. Hotword detection will fail if non-dialog provider is used.")
    else:
        logger.info("Picovoice API key found and loaded. Hotword detection is available if non-dialog provider is used.")

def initialize_dialog_system():
    """Initialize the dialog system if configured."""
    if DIALOG_PROVIDER:
        logger.info(f"Attempting to initialize Dialog Provider: {DIALOG_PROVIDER}")
        try:
            dialog_manager.initialize(provider_name=DIALOG_PROVIDER)
        except Exception as e:
            logger.critical(f"Fatal error during Dialog Provider '{DIALOG_PROVIDER}' initialization: {e}", exc_info=True)
            raise
    else:
        logger.info("No dialog provider configured (DIALOG_PROVIDER is empty or None). Skipping dialog system initialization.")

def initialize_speech_systems():
    """Initialize speech recognition, text-to-speech, hotword config check, and dialog system."""
    logger.info("Initializing speech systems...")
    
    initialize_hotword_config_check()

    try:
        initialize_dialog_system()
    except Exception:
        logger.info("Exiting initialize_speech_systems due to fatal error in dialog system initialization.")
        return

    if dialog_manager.is_active():
        active_dialog_provider_name = "Unknown"
        provider = dialog_manager.get_provider()
        if provider:
            active_dialog_provider_name = provider.get_provider_name()
        logger.info(f"Dialog provider '{active_dialog_provider_name}' is active. Standard STT/TTS initialization will be skipped.")
    else:
        logger.info("No active dialog provider. Proceeding with standard STT and TTS initialization.")
        initialize_tts()
        initialize_stt()

    logger.info("Speech systems initialization process complete.")