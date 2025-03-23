import sys
from core.logger import get_logger
from voice.recognition.active_provider import recognition_manager
from voice.text_to_speech.active_provider import tts_manager, speak

logger = get_logger(__name__)

def main():
    """
    Main entry point for the Jarvis speech interface.
    
    This function initializes the speech recognition and text-to-speech systems
    and creates a simple speech loop where the user can speak, have their speech
    recognized, and receive a spoken response.
    """
    try:
        # Initialize text-to-speech with DeepGram
        logger.info("Initializing Tiktok TTS...")
        tts_manager.initialize(provider_name="tiktok")
        
        stt_provider = "selenium_stt"
        
        if stt_provider == "vosk":
            logger.info("Initializing Vosk speech recognition...")
            recognition_manager.initialize(
                provider_name="vosk",
                model_name="english-small"
                # Alternatively, use model_path directly:
                # model_path="voice/voices/assets/models/vosk/vosk-model-small-en-us-0.15"
            )
        elif stt_provider == "selenium_stt":
            logger.info("Initializing Selenium speech recognition...")
            recognition_manager.initialize(provider_name="selenium_stt", language="en-US")
        
        print("\033[94mSpeech loop activated. Say 'exit' to quit...\033[0m")
        
        while True:
            print("\033[93mListening...", end='', flush=True)
            text = recognition_manager.listen(prints=True)
            
            if text:
                print(f"\n\033[92mRecognized: {text}\033[0m")
                speak(f"You said: {text}")
                
                if "exit" in text.lower():
                    print("\033[91mExiting speech loop...\033[0m")
                    break
                    
    except KeyboardInterrupt:
        print("\n\033[91mExiting speech loop...\033[0m")
    except Exception as e:
        logger.error(f"Error in speech loop: {e}")
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
