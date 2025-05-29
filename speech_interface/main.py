"""
Main entry point for the Jarvis speech interface.

This module serves as the entry point for the speech interface system,
coordinating the initialization and execution of the speech loop.
"""

import sys
from core.logger import get_logger
from speech_interface.initializer import initialize_speech_systems
from speech_interface.speech_loop import run_speech_loop

logger = get_logger(__name__)

def main():
    """
    Main entry point for the Jarvis speech interface.
    
    This function initializes the speech recognition and text-to-speech systems
    and creates a simple speech loop where the user can speak, have their speech
    recognized, and receive a spoken response.
    """
    try:
        initialize_speech_systems()
        run_speech_loop()
    except KeyboardInterrupt:
        print("\n\033[91mExiting speech loop...\033[0m")
    except Exception as e:
        logger.error(f"Error in speech loop: {e}", exc_info=True)
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
