"""
Main entry point for the Jarvis application.

This module serves as the primary entry point for the Jarvis application,
delegating to the speech interface system.
"""

from speech_interface.main import main as speech_main

if __name__ == "__main__":
    speech_main()
