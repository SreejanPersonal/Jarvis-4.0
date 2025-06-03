"""
Speech loop module with hotword detection and state management,
or direct dialog provider session.
"""
import time 
import asyncio 
from core.logger import get_logger
from core.config import AppConfig
from utils.helpers import play_audio

from voice.wake_word import WakeWordDetector
from voice.recognition.active_provider import recognition_manager
from voice.text_to_speech.active_provider import speak

from voice.dialog.manager.dialog_manager import dialog_manager

logger = get_logger(__name__)

STATE_HOTWORD_DETECTION = "HOTWORD_DETECTION"
STATE_SPEECH_RECOGNITION = "SPEECH_RECOGNITION"

def run_speech_loop():
    """
    Run the main speech loop. 
    If a dialog provider is active, it runs its session directly.
    Otherwise, it runs the hotword detection and standard STT/TTS loop.
    """
    if dialog_manager.is_active():
        provider = dialog_manager.get_provider()
        if provider:
            provider_name = provider.get_provider_name()
            logger.info(f"Dialog provider '{provider_name}' is active. Starting its session directly (bypassing hotword).")
            print(f"\033[92mStarting interactive session with {provider_name}... (Press Ctrl+C to exit)\033[0m")
            try:
                asyncio.run(provider.run_session()) 
            except KeyboardInterrupt:
                logger.info(f"Dialog session for '{provider_name}' interrupted by user (Ctrl+C).")
                print(f"\n\033[91mSession with {provider_name} ended by user.\033[0m")
            except Exception as e:
                logger.critical(f"Critical error during dialog provider session '{provider_name}': {e}", exc_info=True)
                print(f"\033[91mCRITICAL ERROR in dialog session with {provider_name}: {e}\033[0m")
            finally:
                logger.info(f"Dialog provider session ({provider_name}) process finished.")
            return
        else:
            logger.error("Dialog manager reported as active, but no provider instance found. Fallback to standard loop or investigate error.")

    logger.info("No active dialog provider, or fallback triggered. Initializing standard speech loop with hotword detection...")

    wake_word_detector = None
    try:
        if not AppConfig.PICOVOICE_API_KEY:
            logger.error("PICOVOICE_API_KEY is not set. Standard hotword detection loop cannot start.")
            print("\033[91mERROR: PICOVOICE_API_KEY is not set. Hotword detection is disabled.\033[0m")
            print("\033[93mTo use the standard voice assistant, please set PICOVOICE_API_KEY in your .env file, or use a DIALOG_PROVIDER.\033[0m")
            return

        wake_word_detector = WakeWordDetector(
            access_key=AppConfig.PICOVOICE_API_KEY,
            keywords=AppConfig.HOTWORD_KEYWORDS
        )
    except ValueError as ve:
        logger.error(f"Failed to initialize WakeWordDetector: {ve}")
        print(f"\033[91mERROR: Hotword detector initialization failed: {ve}. Check PICOVOICE_API_KEY and logs.\033[0m")
        return
    except Exception as e:
        logger.error(f"Unexpected error during WakeWordDetector initialization: {e}", exc_info=True)
        print("\033[91mERROR: Hotword detector failed to initialize unexpectedly. Check logs.\033[0m")
        return

    current_state = STATE_HOTWORD_DETECTION
    logger.info(f"Standard speech loop initial state: {current_state}")
    print(f"\033[94mSystem active (standard mode). Current state: {current_state}. Listening for wake word...\033[0m")

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
                    print("\033[91mHotword detector runtime error. Resetting cycle...\033[0m")
                    time.sleep(1) 
                except Exception as e:
                    logger.error(f"Error during hotword detection cycle: {e}", exc_info=True)
                    print("\033[91mError in hotword detection. Resetting...\033[0m")
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
                    print(f"\033[92mWake word detected! Transitioning to: {current_state}\033[0m")

            elif current_state == STATE_SPEECH_RECOGNITION:
                logger.info("State: Speech Recognition. Listening for command...")
                print("\033[93mListening for command...", end='', flush=True)
                
                if not recognition_manager.get_provider():
                    logger.error("Speech recognition provider not initialized for standard loop.")
                    print("\r\033[91mError: STT not ready. Returning to hotword detection.\033[0m" + " "*20)
                    current_state = STATE_HOTWORD_DETECTION
                    time.sleep(1)
                    continue

                text_input = recognition_manager.listen(prints=False)
                print("\r" + " " * 40 + "\r", end="", flush=True) 

                if text_input is not None:
                    if text_input:
                        logger.info(f"Speech recognized: '{text_input}'")
                        print(f"\033[96mRecognized: {text_input}\033[0m")
                        if not tts_manager.get_provider():
                             logger.error("TTS provider not initialized. Cannot speak response.")
                             print("\033[91mError: TTS not ready.\033[0m")
                        else:
                            speak(f"You said: {text_input}") 

                        if "exit" in text_input.lower() or "jarvis stop" in text_input.lower():
                            logger.info("Exit command received. Shutting down speech loop.")
                            print("\033[91mExit command received. Shutting down...\033[0m")
                            break
                        logger.info("Command processed. Remaining in Speech Recognition state.")
                    else: 
                        logger.info("No speech detected by STT (silence timeout).")
                        print("\033[93mNo speech detected. Returning to hotword listening...\033[0m")
                        try:
                            play_audio(AppConfig.SOUND_END_SESSION)
                        except Exception as e_sound:
                            logger.error(f"Failed to play end_session_sound: {e_sound}")
                        current_state = STATE_HOTWORD_DETECTION
                        logger.info(f"Transitioning back to {STATE_HOTWORD_DETECTION} state.")
                        print(f"\033[94mCurrent state: {current_state}. Listening for wake word...\033[0m")
                else: 
                    logger.error("Speech recognition error (STT returned None).")
                    print("\033[91mSpeech recognition error. Returning to hotword listening...\033[0m")
                    try:
                        play_audio(AppConfig.SOUND_END_SESSION)
                    except Exception as e_sound:
                        logger.error(f"Failed to play end_session_sound on STT error: {e_sound}")
                    current_state = STATE_HOTWORD_DETECTION
                    logger.info(f"Error in STT, transitioning back to {STATE_HOTWORD_DETECTION} state.")
                    print(f"\033[94mCurrent state: {current_state}. Listening for wake word...\033[0m")
            
            time.sleep(0.05) 

    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received. Shutting down standard speech loop...")
        print("\n\033[91mKeyboard interrupt. Shutting down standard speech loop...\033[0m")
    except Exception as e_main:
        logger.critical(f"Critical error in main standard speech loop: {e_main}", exc_info=True)
        print(f"\033[91mCRITICAL ERROR in standard speech loop: {e_main}\033[0m")
    finally:
        logger.info("Standard speech loop ended. Cleaning up hotword detector...")
        if wake_word_detector:
            wake_word_detector.stop_detector()
        print("\033[94mStandard speech loop terminated.\033[0m")