import os
import sys
from core.logger import get_logger
from voice.text_to_speech.active_provider import tts_manager, speak

logger = get_logger(__name__)

def main():
    """
    Main entry point for the Jarvis application.
    """
    try:
        logger.info("Starting Jarvis...")
        
        # Initialize the TTS provider
        tts_manager.initialize(provider_name="deepgram", default_voice="aura_arcas")
        
        # Test the TTS functionality
        speak("Hello, I am Jarvis. Your personal AI assistant. How can I help you today?")
        
        # List available providers
        providers = tts_manager.list_providers()
        logger.info(f"Available TTS providers: {providers}")
        
        # Get the active provider
        provider = tts_manager.get_provider()
        
        # List available voices
        voices = provider.list_available_voices()
        logger.info(f"Available voices for {provider.get_provider_name()}: {voices}")
        
        # Test with a different voice
        speak("I can speak in different voices too.", "aura_luna")
        
        logger.info("Jarvis initialized successfully.")
        
    except Exception as e:
        logger.error(f"Error starting Jarvis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()