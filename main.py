import os
import sys
import asyncio
from core.logger import get_logger
from voice.text_to_speech.active_provider import tts_manager, speak

logger = get_logger(__name__)


def test_deepgram():
    """Test Deepgram TTS provider."""
    try:
        tts_manager.initialize(provider_name="deepgram", default_voice="aura_arcas")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"Deepgram voices: {voices}")

        speak("Hello, I am using Deepgram's Aura Arcas voice.", "aura_arcas")
    except Exception as e:
        logger.error(f"Deepgram test failed: {e}")


def test_speechify():
    """Test Speechify TTS provider."""
    try:
        tts_manager.set_provider("speechify", default_voice="mrbeast")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"Speechify voices: {voices}")

        speak("Hey guys, MrBeast here!", "mrbeast")
    except Exception as e:
        logger.error(f"Speechify test failed: {e}")


async def test_hearling():
    """Test Hearling TTS provider."""
    try:
        tts_manager.set_provider("hearling", email_prefix="jarvis")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"Hearling available voices: {voices}")

        hindi_text = "नमस्ते, मैं जार्विस हूं। आप कैसे हैं?"
        speak(hindi_text, "hi-IN-Wavenet-D")

        # Ensure proper asynchronous cleanup
        await provider.cleanup()
    except Exception as e:
        logger.error(f"Hearling test failed: {e}")


def test_tiktok_api():
    """Test the new tiktok API TTS provider (using the WeilByte variant)."""
    try:
        # Initialize the new provider (Gesserit/WeilByte are handled internally)
        tts_manager.set_provider("tiktok", variant="weilbyte", default_voice="en_us_rocket")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"tiktok API Provider voices: {voices}")
        speak("This is a test using the tiktok API TTS Provider using WeilByte Rocket voice.", "en_us_rocket")

        tts_manager.set_provider("tiktok", variant="gesserit", default_voice="en_male_funny")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"tiktok API Provider voices: {voices}")

        speak("This is a test using the tiktok API TTS Provider using Gesserit Funny voice.", "en_male_funny")
    except Exception as e:
        logger.error(f"tiktok API test failed: {e}")


def test_edge_tts():
    """Test the new Edge TTS provider."""
    try:
        tts_manager.set_provider("edge_tts", default_voice="en-US-JennyNeural")
        provider = tts_manager.get_provider()
        voices = provider.list_available_voices()
        logger.info(f"Edge TTS Provider voices: {voices}")

        speak("Hello, this is a test of the Edge TTS provider using Jenny Neural voice.", "en-US-JennyNeural")
    except Exception as e:
        logger.error(f"Edge TTS test failed: {e}")


async def main():
    """
    Main entry point for the Jarvis TTS tests.
    
    Tests multiple providers one by one.
    """
    try:
        logger.info("Starting Jarvis TTS tests...")

        logger.info("Testing Deepgram...")
        test_deepgram()

        logger.info("Testing Speechify...")
        test_speechify()

        logger.info("Testing Hearling...")
        await test_hearling()

        logger.info("Testing tiktok API Provider...")
        test_tiktok_api()

        logger.info("Testing Edge TTS Provider...")
        test_edge_tts()

        logger.info("All TTS tests completed successfully.")
    except Exception as e:
        logger.error(f"Error in TTS tests: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())