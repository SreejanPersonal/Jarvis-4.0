# speech_interface/speech_loop.py
"""
Speech loop module with hotword detection and state management.
"""
import time # For potential brief pauses

from voice.wake_word import WakeWordDetector
from voice.recognition.active_provider import recognition_manager
from voice.text_to_speech.active_provider import speak
from core.config import AppConfig
from utils.helpers import play_audio
from core.logger import get_logger

logger = get_logger(__name__)

# States
STATE_HOTWORD_DETECTION = "HOTWORD_DETECTION"
STATE_SPEECH_RECOGNITION = "SPEECH_RECOGNITION"

def run_speech_loop():
    """
    Run the main speech loop with hotword detection and state management.
    """
    logger.info("Initializing speech loop with hotword detection...")

    wake_word_detector = None
    try:
        wake_word_detector = WakeWordDetector(
            access_key=AppConfig.PICOVOICE_API_KEY,
            keywords=AppConfig.HOTWORD_KEYWORDS
        )
    except ValueError as ve:
        logger.error(f"Failed to initialize WakeWordDetector: {ve}")
        logger.error("Please ensure PICOVOICE_API_KEY is correctly set in your .env file.")
        print("\\033[91mERROR: Hotword detector initialization failed. Check PICOVOICE_API_KEY.\\033[0m")
        return
    except Exception as e:
        logger.error(f"Unexpected error during WakeWordDetector initialization: {e}")
        print("\\033[91mERROR: Hotword detector failed to initialize unexpectedly.\\033[0m")
        return

    current_state = STATE_HOTWORD_DETECTION
    logger.info(f"Initial state: {current_state}")
    print(f"\\033[94mSystem active. Current state: {current_state}. Listening for wake word...\\033[0m")

    try:
        while True:
            if current_state == STATE_HOTWORD_DETECTION:
                logger.info("State: Hotword Detection. Attempting to start detector...")
                hotword_detected = False
                try:
                    wake_word_detector.start_detector()
                    logger.info(f"Listening for hotword(s): {AppConfig.HOTWORD_KEYWORDS}...")
                    hotword_detected = wake_word_detector.listen_for_wake_word()
                except RuntimeError as r_err:
                    logger.error(f"RuntimeError in hotword detection: {r_err}. Attempting to recover.")
                    print("\\033[91mHotword detector runtime error. Resetting cycle...\\033[0m")
                    time.sleep(1) # Brief pause before full stop/restart attempt
                except Exception as e:
                    logger.error(f"Error during hotword detection cycle: {e}")
                    print("\\033[91mError in hotword detection. Resetting...\\033[0m")
                    time.sleep(1)
                finally:
                    logger.debug("Ensuring hotword detector is stopped to release microphone.")
                    wake_word_detector.stop_detector()

                if hotword_detected:
                    logger.info("Hotword detected!")
                    try:
                        play_audio(AppConfig.SOUND_START_UP)
                    except Exception as e_sound:
                        logger.error(f"Failed to play start_up_sound: {e_sound}")
                    current_state = STATE_SPEECH_RECOGNITION
                    logger.info(f"Transitioning to {STATE_SPEECH_RECOGNITION} state.")
                    print(f"\\033[92mWake word detected! Transitioning to: {current_state}\\033[0m")

            elif current_state == STATE_SPEECH_RECOGNITION:
                logger.info("State: Speech Recognition. Listening for command...")
                print("\\033[93mListening for command...", end='', flush=True)
                
                text_input = recognition_manager.listen(prints=False)
                
                print("\\r" + " " * 40 + "\\r", end="", flush=True) # Clear listening line

                if text_input is not None:
                    if text_input:
                        logger.info(f"Speech recognized: '{text_input}'")
                        print(f"\\033[96mRecognized: {text_input}\\033[0m")
                        speak(f"You said: {text_input}") # Process command here

                        if "exit" in text_input.lower() or "jarvis stop" in text_input.lower():
                            logger.info("Exit command received. Shutting down speech loop.")
                            print("\\033[91mExit command received. Shutting down...\\033[0m")
                            # speak("Goodbye!") # Optional
                            break
                        # After processing a command (that is not 'exit'),
                        # remain in SPEECH_RECOGNITION state to listen for the next command.
                        # The loop will call recognition_manager.listen() again.
                        logger.info("Command processed. Remaining in Speech Recognition state for further commands.")
                    else: # Empty string from STT (silence)
                        logger.info("No speech detected by STT (silence timeout).")
                        print("\\033[93mNo speech detected. Returning to hotword listening...\\033[0m")
                        try:
                            play_audio(AppConfig.SOUND_END_SESSION)
                        except Exception as e_sound:
                            logger.error(f"Failed to play end_session_sound: {e_sound}")
                        current_state = STATE_HOTWORD_DETECTION
                        logger.info(f"Transitioning back to {STATE_HOTWORD_DETECTION} state.")
                        print(f"\\033[94mCurrent state: {current_state}. Listening for wake word...\\033[0m")
                else: # None from STT (error)
                    logger.error("Speech recognition error (STT returned None).")
                    print("\\033[91mSpeech recognition error. Returning to hotword listening...\\033[0m")
                    try:
                        play_audio(AppConfig.SOUND_END_SESSION)
                    except Exception as e_sound:
                        logger.error(f"Failed to play end_session_sound on STT error: {e_sound}")
                    current_state = STATE_HOTWORD_DETECTION
                    logger.info(f"Error in STT, transitioning back to {STATE_HOTWORD_DETECTION} state.")
                    print(f"\\033[94mCurrent state: {current_state}. Listening for wake word...\\033[0m")
            
            time.sleep(0.05) # Small delay to prevent tight CPU loops on rapid errors

    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received. Shutting down speech loop...")
        print("\\n\\033[91mKeyboard interrupt. Shutting down...\\033[0m")
    except Exception as e_main:
        logger.critical(f"Critical error in main speech loop: {e_main}", exc_info=True)
        print(f"\\033[91mCRITICAL ERROR in speech loop: {e_main}\\033[0m")
    finally:
        logger.info("Speech loop ended. Cleaning up hotword detector...")
        if wake_word_detector:
            wake_word_detector.stop_detector()
        print("\\033[94mSpeech loop terminated.\\033[0m")

# For direct testing:
# if __name__ == '__main__':
#     from speech_interface.initializer import initialize_speech_systems
#     print("Running speech_loop.py directly for testing...")
#     initialize_speech_systems()
#     run_speech_loop()
