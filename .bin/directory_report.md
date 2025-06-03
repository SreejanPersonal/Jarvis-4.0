# 📁 Directory Structure Report

## 📌 Overview

* **Base Directory :** `C:\Users\sreej\OneDrive\Desktop\PROJECTS\REVERSE ENGINEER\JARVIS 4.0\YT\DAY 3 REBASE`
* **Report Generated :** `2025-05-29 19:41:49`

---

## 📂 Directory Structure

## 📁 ai/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/__init__.py

```

#### 📄 agent_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/agent_manager.py
# Multi-agent coordination
class AgentManager:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name, agent):
        self.agents[agent_name] = agent

    def get_agent(self, agent_name):
        return self.agents.get(agent_name)

```

### 📁 agents/

##### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/agents/__init__.py

```

##### 📄 coding_agent.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/agents/coding_agent.py
# Coding agent
class CodingAgent:
    def __init__(self):
        pass

    def generate_code(self, description):
        pass

```

##### 📄 search_agent.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/agents/search_agent.py
# Search agent
class SearchAgent:
    def __init__(self):
        pass

    def search_online(self, query):
        pass

```

---

#### 📄 content_generator.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/content_generator.py
# Generate content
class ContentGenerator:
    def __init__(self):
        pass

    def generate_text(self, prompt):
        pass

```

#### 📄 content_verifier.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/content_verifier.py
# Detect fake content
class ContentVerifier:
    def __init__(self):
        pass

    def verify_content(self, text):
        pass

```

#### 📄 context_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/context_manager.py
# Maintain conversation context
class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, key, value):
        self.context[key] = value

    def get_context(self, key):
        return self.context.get(key)

```

#### 📄 conversation.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/conversation.py
# Conversation management
class ConversationManager:
    def __init__(self):
        self.history = []

    def add_message(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history

```

#### 📄 llm_interface.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ai/llm_interface.py
# LLM connection
class LLMInterface:
    def __init__(self):
        pass

    def query_llm(self, prompt):
        pass

```

---

## 📁 communication/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/__init__.py

```

#### 📄 contact_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/contact_manager.py
# Contact profiles
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email):
        self.contacts[name] = email

    def get_contact(self, name):
        return self.contacts.get(name)

```

#### 📄 email.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/email.py
# Email management
class EmailManager:
    def __init__(self):
        pass

    def send_email(self, recipient, subject, body):
        pass

```

#### 📄 meeting.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/meeting.py
# Meeting tools
class MeetingManager:
    def __init__(self):
        pass

    def schedule_meeting(self, participants, time):
        pass

```

#### 📄 messaging.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/messaging.py
# Messaging platforms
class Messaging:
    def __init__(self):
        pass

    def send_message(self, platform, recipient, message):
        pass

```

#### 📄 notification.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/communication/notification.py
# Notification system
class NotificationManager:
    def __init__(self):
        pass

    def send_notification(self, message):
        pass

```

---

## 📁 core/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/core/__init__.py

```

#### 📄 config.py

* Last Modified : `2025-05-29 18:51:18`

```python
import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    PICOVOICE_API_KEY = os.getenv("PICOVOICE_API_KEY")
    HOTWORD_KEYWORDS = ["jarvis"]

    # Construct paths relative to this config file's directory, then go up to project root
    _PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SOUND_START_UP = os.path.join(_PROJECT_ROOT, "data", "sounds", "start_up_sound.wav")
    SOUND_END_SESSION = os.path.join(_PROJECT_ROOT, "data", "sounds", "end_up_sound.wav")

    # Gemini Live Provider Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_LIVE_MODEL_NAME = os.getenv("GEMINI_LIVE_MODEL_NAME", "models/gemini-2.5-flash-preview-native-audio-dialog")
    GEMINI_LIVE_SYSTEM_INSTRUCTION = os.getenv("GEMINI_LIVE_SYSTEM_INSTRUCTION", "You are a helpful assistant. Be concise and friendly.") # Default instruction
    GEMINI_LIVE_VIDEO_MODE = os.getenv("GEMINI_LIVE_VIDEO_MODE", "none") # Options: "camera", "screen", "none"
```

#### 📄 constants.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/core/constants.py
# Global constants
class Constants:
    JARVIS_NAME = "Jarvis"

```

#### 📄 jarvis.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/core/jarvis.py
# Main Jarvis class
class Jarvis:
    def __init__(self):
        pass

    def run(self):
        pass

```

#### 📄 logger.py

* Last Modified : `2025-03-23 15:21:34`

```python
import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "data", "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
LOG_FILE = os.path.join(log_dir, "jarvis.log")
print(f"Log directory: {log_dir}")  # Print log directory path
print(f"Log file path: {LOG_FILE}")  # Print log file path
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

# Configure the root logger
try:
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            RotatingFileHandler(LOG_FILE, maxBytes=10485760, backupCount=5),  # 10MB max file size
            logging.StreamHandler()  # Also log to console
        ]
    )
except Exception as e:
    print(f"Error configuring logger: {e}")

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger configured with the standard settings.
    
    Args:
        name (str, optional): Name for the logger, usually __name__.
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)

```

#### 📄 state_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/core/state_manager.py
# Manage application state
class StateManager:
    def __init__(self):
        self.state = {}

    def get_state(self, key):
        return self.state.get(key)

    def set_state(self, key, value):
        self.state[key] = value

```

---

## 📁 data/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/data/__init__.py

```

### 📁 cache/

---

### 📁 models/

---

### 📁 sounds/

##### 📄 end_up_sound.wav

* Last Modified : `2024-05-19 17:57:47`

> ⚠️ Unable To Read File Contents : 'utf-8' codec can't decode byte 0xef in position 5: invalid continuation byte

##### 📄 start_up_sound.wav

* Last Modified : `2024-05-19 17:57:39`

> ⚠️ Unable To Read File Contents : 'utf-8' codec can't decode byte 0xe2 in position 5: invalid continuation byte

---

### 📁 user_data/

---

---

## 📁 devices/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/devices/__init__.py

```

#### 📄 device_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
## Device Manager - Devices Module - Jarvis 4.0

### Overview

The `device_manager.py` file within the Devices module is responsible for handling the lifecycle and control of devices connected to Jarvis 4.0. It provides functionalities for device discovery, registration, command execution, and status monitoring. This component acts as the central hub for device interactions within the Jarvis 4.0 ecosystem.

### Functionality

1.  **Device Discovery**:
    *   Automatically discovers devices on local networks or via supported protocols.
    *   Supports various discovery methods (e.g., UPnP, Bonjour, custom protocols).
    *   Provides interfaces for manual device addition if automatic discovery fails.

2.  **Device Registration**:
    *   Registers discovered devices with Jarvis 4.0, assigning unique IDs and storing device metadata.
    *   Manages device profiles, including device type, capabilities, and communication protocols.
    *   Persists device registration information for system restarts.

3.  **Device Control**:
    *   Provides a unified API for controlling registered devices, abstracting device-specific protocols.
    *   Supports sending commands to devices to perform actions (e.g., turn on/off, set volume, change settings).
    *   Handles command queuing and execution management, ensuring reliable device control.

4.  **Device Status Monitoring**:
    *   Monitors the status and health of registered devices.
    *   Periodically polls devices for status updates or utilizes push notifications from devices.
    *   Detects device disconnections and reconnections, updating device status accordingly.

5.  **Device Grouping and Management**:
    *   Allows grouping devices for easier management and control (e.g., "Living Room Lights", "Office Devices").
    *   Supports batch commands to control groups of devices simultaneously.
    *   Provides tools for organizing and managing a large number of devices.

### Class: `DeviceManager`

The main class in this file is `DeviceManager`, which encapsulates the functionalities described above.

*   **Methods**:
    *   `discover_devices()`: Initiates device discovery process.
    *   `register_device(device_info)`: Registers a new device.
    *   `unregister_device(device_id)`: Unregisters a device.
    *   `control_device(device_id, command, parameters)`: Sends a control command to a specific device.
    *   `get_device_status(device_id)`: Retrieves the current status of a device.
    *   `get_all_devices()`: Returns a list of all registered devices.
    *   `create_device_group(group_name, device_ids)`: Creates a new device group.
    *   `delete_device_group(group_id)`: Deletes a device group.
    *   `control_device_group(group_id, command, parameters)`: Sends a control command to a group of devices.

### Usage

The `DeviceManager` is instantiated and used by other modules within Jarvis 4.0 that require device interaction, such as the `home_automation.py` module or user interface components. It provides a clean and consistent interface for managing and controlling devices, simplifying device integration throughout the system.

### Dependencies

*   Potentially depends on libraries for specific device communication protocols (e.g., `requests` for HTTP, `socket` for network communication, specific libraries for smart home platforms).
*   Utilizes the `core.config` module for configuration settings related to device management.
*   Relies on the `core.logger` module for logging device-related events and errors.

This component is essential for Jarvis 4.0's ability to interact with and control external devices, providing a foundation for home automation, device synchronization, and other device-centric features.

```

#### 📄 home_automation.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/devices/home_automation.py
# Smart home integration
class HomeAutomation:
    def __init__(self):
        pass

    def control_home_device(self, device_name, action):
        pass

```

#### 📄 sync_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/devices/sync_manager.py
# Cross-device sync
class SyncManager:
    def __init__(self):
        pass

    def sync_devices(self):
        pass

```

---

## 📁 files/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/__init__.py

```

#### 📄 data_extractor.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/data_extractor.py
# Data extraction
class DataExtractor:
    def __init__(self):
        pass

    def extract_data(self, file_path):
        pass

```

#### 📄 finder.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/finder.py
# Smart file search
class FileFinder:
    def __init__(self):
        pass

    def find_file(self, query):
        pass

```

#### 📄 ocr.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/ocr.py
# Text extraction from images
class OCR:
    def __init__(self):
        pass

    def extract_text_from_image(self, image_path):
        pass

```

#### 📄 organizer.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/organizer.py
# File organization
class FileOrganizer:
    def __init__(self):
        pass

    def organize_files(self, directory):
        pass

```

#### 📄 parser.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/files/parser.py
# Document parsing
class DocumentParser:
    def __init__(self):
        pass

    def parse_document(self, file_path):
        pass

```

---

## 📁 input/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/__init__.py

```

#### 📄 audio_detection.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/audio_detection.py
# Clap detection etc.
class AudioDetector:
    def __init__(self):
        pass

    def detect_clap(self):
        pass

```

#### 📄 facial_recognition.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/facial_recognition.py
# Face ID
class FacialRecognizer:
    def __init__(self):
        pass

    def recognize_face(self):
        pass

```

#### 📄 gesture_recognition.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/gesture_recognition.py
# Gesture control
class GestureRecognizer:
    def __init__(self):
        pass

    def recognize_gesture(self):
        pass

```

#### 📄 interrupt_handler.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/interrupt_handler.py
# Command interruption
class InterruptHandler:
    def __init__(self):
        pass

    def handle_interrupt(self):
        pass

```

#### 📄 minimal_input.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/input/minimal_input.py
# Brief command processing
class MinimalInputProcessor:
    def __init__(self):
        pass

    def process_command(self, command):
        pass

```

---

## 📄 main.py

* Last Modified : `2025-05-29 07:15:26`

```python
"""
Main entry point for the Jarvis application.

This module serves as the primary entry point for the Jarvis application,
delegating to the speech interface system.
"""

from speech_interface.main import main as speech_main

if __name__ == "__main__":
    speech_main()

```

---

## 📄 requirements.txt

* Last Modified : `2025-05-29 14:43:52`

```text
requests
playsound
aiohttp
aiofiles
vosk
pygame
pyaudio
selenium>=4.9.0
webdriver-manager>=3.8.6
pvporcupine
python-dotenv
opencv-python
pillow 
mss
google-genai
```

---

## 📁 speech_interface/

#### 📄 config.py

* Last Modified : `2025-05-29 19:19:06`

```python
"""
Configuration settings for the speech interface.

This module contains configuration parameters for the speech recognition,
text-to-speech systems, and dialog providers.
"""
from core.logger import get_logger

logger = get_logger(__name__)

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

STT_PROVIDER = "selenium_stt"
TTS_PROVIDER = "tiktok"
DIALOG_PROVIDER = "gemini_live" # Example: "gemini_live" or None
```

#### 📄 initializer.py

* Last Modified : `2025-05-29 19:07:01`

```python
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
    DIALOG_PROVIDER # Added
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
            # Success/failure is logged within dialog_manager.initialize
        except Exception as e:
            # This makes dialog provider initialization failure fatal.
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
        # If initialize_dialog_system raises, it's considered fatal and execution stops here.
        # No need for further checks on dialog_manager.is_active() in this path.
        logger.info("Exiting initialize_speech_systems due to fatal error in dialog system initialization.")
        return # Or re-raise the exception if main should handle it directly.

    if dialog_manager.is_active():
        active_dialog_provider_name = "Unknown"
        provider = dialog_manager.get_provider()
        if provider:
            active_dialog_provider_name = provider.get_provider_name()
        logger.info(f"Dialog provider '{active_dialog_provider_name}' is active. Standard STT/TTS initialization will be skipped.")
    else:
        # This block runs if DIALOG_PROVIDER was not set (is None or empty).
        logger.info("No active dialog provider. Proceeding with standard STT and TTS initialization.")
        initialize_tts()
        initialize_stt()

    logger.info("Speech systems initialization process complete.")
```

#### 📄 main.py

* Last Modified : `2025-05-29 18:53:41`

```python
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
    (or a dialog provider) and creates a speech loop where the user can interact.
    """
    try:
        initialize_speech_systems()
        run_speech_loop()
    except KeyboardInterrupt:
        print("\n\033[91mJarvis speech interface exiting due to user interruption (Ctrl+C).\033[0m")
        logger.info("Jarvis speech interface exited via KeyboardInterrupt in main.")
    except Exception as e:
        logger.error(f"An unhandled error occurred in the speech interface main: {e}", exc_info=True)
        print(f"\033[91mFatal Error in Speech Interface: {e}. Check logs.\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### 📄 speech_loop.py

* Last Modified : `2025-05-29 19:07:10`

```python
# speech_interface/speech_loop.py
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
            # Fall through to standard loop for robustness, though this indicates an issue.

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
```

---

## 📁 system/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/__init__.py

```

#### 📄 automation.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/automation.py
# Desktop automation
class Automation:
    def __init__(self):
        pass

    def automate_task(self, task_description):
        pass

```

#### 📄 media_controller.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/media_controller.py
# Media playback control
class MediaController:
    def __init__(self):
        pass

    def control_media(self, action):
        pass

```

#### 📄 power_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/power_manager.py
# Battery optimization
class PowerManager:
    def __init__(self):
        pass

    def optimize_power(self):
        pass

```

#### 📄 resource_monitor.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/resource_monitor.py
# System resource monitoring
class ResourceMonitor:
    def __init__(self):
        pass

    def get_resource_usage(self):
        pass

```

#### 📄 screenshot.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/screenshot.py
# Screen capture
class Screenshot:
    def __init__(self):
        pass

    def capture_screenshot(self):
        pass

```

#### 📄 update_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/system/update_manager.py
# Windows update management
class UpdateManager:
    def __init__(self):
        pass

    def manage_updates(self):
        pass

```

---

## 📁 tasks/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/__init__.py

```

#### 📄 calendar_sync.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/calendar_sync.py
# Calendar integration
class CalendarSync:
    def __init__(self):
        pass

    def sync_calendar(self):
        pass

```

#### 📄 financial_tracker.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/financial_tracker.py
# Expense tracking
class FinancialTracker:
    def __init__(self):
        pass

    def track_expense(self, amount, category):
        pass

```

#### 📄 note_sync.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/note_sync.py
# Note synchronization
class NoteSync:
    def __init__(self):
        pass

    def sync_notes(self):
        pass

```

#### 📄 reminder.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/reminder.py
# Reminders
class Reminder:
    def __init__(self):
        pass

    def set_reminder(self, time, message):
        pass

```

#### 📄 task_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/task_manager.py
# Task management
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append(task_description)

    def list_tasks(self):
        return self.tasks

```

#### 📄 timer.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/tasks/timer.py
# Timers and alarms
class Timer:
    def __init__(self):
        pass

    def set_timer(self, duration):
        pass

```

---

## 📁 ui/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/__init__.py

```

#### 📄 chat_interface.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/chat_interface.py
# Chat UI component
import tkinter as tk

class ChatInterface(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

```

#### 📄 main_window.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/main_window.py
# Main GUI window
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis UI")

```

#### 📄 startup_sequence.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/startup_sequence.py
# Boot animation
class StartupSequence:
    def __init__(self):
        pass

    def run_animation(self):
        pass

```

#### 📄 system_tray.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/system_tray.py
# System tray integration
class SystemTray:
    def __init__(self):
        pass

    def setup_tray_icon(self):
        pass

```

#### 📄 theme_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/ui/theme_manager.py
# UI themes
class ThemeManager:
    def __init__(self):
        pass

    def load_theme(self, theme_name):
        pass

```

---

## 📁 utils/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/utils/__init__.py

```

#### 📄 async_tools.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/utils/async_tools.py
# Async utilities
import asyncio

async def run_async_task(task):
    await asyncio.create_task(task)

```

#### 📄 helpers.py

* Last Modified : `2025-05-15 17:33:20`

```python
import os
import pygame
from core.logger import get_logger

logger = get_logger(__name__)

def play_audio(file_path: str) -> None:
    """
    Play an audio file using pygame.
    
    Args:
        file_path (str): Path to the audio file to play.
        
    Raises:
        FileNotFoundError: If the audio file doesn't exist.
        Exception: If there's an error playing the audio.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Clean up pygame resources
        pygame.mixer.quit()
    except Exception as e:
        logger.error(f"Error playing audio: {e}")
        raise Exception(f"Failed to play audio: {e}")

```

#### 📄 security.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/utils/security.py
# Security functions
import hashlib

def hash_string(text):
    return hashlib.sha256(text.encode()).hexdigest()

```

#### 📄 threading_utils.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/utils/threading_utils.py
# Threading utilities
import threading

def run_in_thread(func, args=()):
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread

```

---

## 📁 voice/

#### 📄 __init__.py

* Last Modified : `2025-03-23 17:04:16`

```python
# jarvis/voice/__init__.py

```

#### 📄 authentication.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/voice/authentication.py
# Voice authentication
class VoiceAuthenticator:
    def __init__(self):
        pass

    def authenticate_voice(self, audio):
        pass

```

### 📁 dialog/

##### 📄 __init__.py

* Last Modified : `2025-05-29 19:02:49`

```python
# jarvis/voice/dialog/__init__.py

from .manager import dialog_manager

__all__ = ["dialog_manager"]
```

##### 📄 base.py

* Last Modified : `2025-05-29 18:52:20`

```python
# jarvis/voice/dialog/base.py

from abc import ABC, abstractmethod
from typing import Optional

class BaseDialogProvider(ABC):
    PROVIDER_NAME = "base_dialog"

    def __init__(self, **kwargs):
        """
        Initialize the base dialog provider.
        kwargs can be used for provider-specific configurations passed from the manager.
        """
        pass

    @abstractmethod
    async def run_session(self) -> None:
        """
        Start and manage the interactive dialog session.
        This method should handle the entire lifecycle of the conversation,
        including audio input/output and interaction with the dialog model.
        """
        pass

    def get_provider_name(self) -> str:
        """
        Get the name of this dialog provider.
        
        Returns:
            str: Provider name.
        """
        return self.PROVIDER_NAME
```

#### 📁 manager/

###### 📄 __init__.py

* Last Modified : `2025-05-29 19:02:41`

```python
from .dialog_manager import dialog_manager

__all__ = ["dialog_manager"]

```

###### 📄 dialog_manager.py

* Last Modified : `2025-05-29 19:02:33`

```python
from typing import Optional
from core.logger import get_logger
from voice.dialog.base import BaseDialogProvider
from .provider_registry import ProviderRegistry

logger = get_logger(__name__)

class DialogProviderManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DialogProviderManager, cls).__new__(cls)
            cls._instance._active_provider: Optional[BaseDialogProvider] = None
            cls._instance._initialized: bool = False
        return cls._instance

    def initialize(self, provider_name: Optional[str] = None, **kwargs) -> None:
        if self._initialized and self._active_provider and \
           provider_name == self._active_provider.get_provider_name():
            logger.info(f"Dialog provider '{provider_name}' already initialized and active.")
            return
        
        if not provider_name:
            logger.info("No dialog provider specified for initialization. Dialog system will be inactive.")
            self._active_provider = None
            self._initialized = True
            return

        if provider_name not in ProviderRegistry.get_provider_names():
            available = ", ".join(ProviderRegistry.get_provider_names())
            logger.error(f"Invalid dialog provider '{provider_name}'. Available providers: {available}")
            raise ValueError(f"Invalid dialog provider '{provider_name}'. Available providers: {available}")
        
        logger.info(f"Initializing Dialog provider: {provider_name}")
        try:
            provider_class = ProviderRegistry.get_provider_class(provider_name)
            self._active_provider = provider_class(**kwargs)
            self._initialized = True
            logger.info(f"Dialog provider '{provider_name}' initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize dialog provider '{provider_name}': {e}", exc_info=True)
            self._active_provider = None
            self._initialized = True
            raise

    def get_provider(self) -> Optional[BaseDialogProvider]:
        if not self._initialized:
            logger.warning("DialogProviderManager accessed before explicit initialization call.")
        return self._active_provider

    def is_active(self) -> bool:
        return self._initialized and self._active_provider is not None

dialog_manager = DialogProviderManager()

```

###### 📄 provider_registry.py

* Last Modified : `2025-05-29 19:02:17`

```python
from typing import Dict, Type
from voice.dialog.base import BaseDialogProvider
from voice.dialog.providers.gemini_live.provider import GeminiLiveProvider

class ProviderRegistry:
    PROVIDERS: Dict[str, Type[BaseDialogProvider]] = {
        "gemini_live": GeminiLiveProvider,
    }
    
    @classmethod
    def get_provider_class(cls, provider_name: str) -> Type[BaseDialogProvider]:
        return cls.PROVIDERS.get(provider_name)
        
    @classmethod
    def get_available_providers(cls) -> Dict[str, Type[BaseDialogProvider]]:
        return cls.PROVIDERS.copy()
        
    @classmethod
    def get_provider_names(cls) -> list:
        return list(cls.PROVIDERS.keys())

```

---

#### 📁 providers/

###### 📄 __init__.py

* Last Modified : `2025-05-29 18:42:38`

```python
# jarvis/voice/dialog/providers/__init__.py

from .gemini_live import GeminiLiveProvider

__all__ = [
    "GeminiLiveProvider"
]
```

##### 📁 gemini_live/

####### 📄 __init__.py

* Last Modified : `2025-05-29 18:42:48`

```python
# jarvis/voice/dialog/providers/gemini_live/__init__.py

from .provider import GeminiLiveProvider

__all__ = ["GeminiLiveProvider"]
```

####### 📄 client_config.py

* Last Modified : `2025-05-29 18:52:44`

```python
# jarvis/voice/dialog/providers/gemini_live/client_config.py

import os
from google import genai
from google.genai import types
from core.config import AppConfig
from core.logger import get_logger

logger = get_logger(__name__)

# Constants from live.py
# FORMAT, CHANNELS, etc. are used by pyaudio, so they will be imported
# in session_handler.py where pyaudio is directly used.
# However, to keep them logically grouped if other parts of client_config needed them:
import pyaudio # For constants if needed here, though better in session_handler
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024


def get_gemini_client(api_key: str):
    """Initializes and returns a Gemini API client."""
    if not api_key:
        msg = "GEMINI_API_KEY is not provided for Gemini client initialization."
        logger.error(msg)
        raise ValueError(msg)
    
    return genai.Client(
        http_options={"api_version": "v1beta"}, # As per live.py
        api_key=api_key,
    )

def get_live_connect_config(system_instruction_text: str) -> types.LiveConnectConfig:
    """Constructs and returns the LiveConnectConfig for Gemini."""
    
    if not system_instruction_text:
        logger.warning("No system instruction provided for Gemini Live session. Using a generic default.")
        system_instruction_text = "You are a helpful AI assistant."

    return types.LiveConnectConfig(
        response_modalities=[
            "AUDIO",
        ],
        media_resolution="MEDIA_RESOLUTION_MEDIUM",
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Zephyr")
            )
        ),
        context_window_compression=types.ContextWindowCompressionConfig(
            trigger_tokens=25600,
            sliding_window=types.SlidingWindow(target_tokens=12800),
        ),
        system_instruction=types.Content(
            parts=[types.Part.from_text(text=system_instruction_text)],
            role="user" # As per live.py
        ),
        # session_resumption=types.SessionResumptionConfig(
        #     handle="HANDLE HERE" # Kept commented as in live.py
        # )
    )
```

###### 📁 core/

######## 📄 __init__.py

* Last Modified : `2025-05-29 19:36:09`

```python
from .session import GeminiLiveSession

```

######## 📄 audio.py

* Last Modified : `2025-05-29 19:34:48`

```python
import asyncio
import pyaudio
from core.logger import get_logger

# Audio constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

logger = get_logger(__name__)

class AudioHandler:
    def __init__(self, pya=None):
        self.pya = pya
        self.audio_stream = None
        
    async def listen_audio(self, out_queue):
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot listen to audio.")
            return

        try:
            mic_info = self.pya.get_default_input_device_info()
            self.audio_stream = await asyncio.to_thread(
                self.pya.open,
                format=FORMAT,
                channels=CHANNELS,
                rate=SEND_SAMPLE_RATE,
                input=True,
                input_device_index=mic_info["index"],
                frames_per_buffer=CHUNK_SIZE,
            )
        except Exception as e:
            logger.error(f"Failed to open audio stream for listening: {e}", exc_info=True)
            return

        logger.info(f"Listen audio task started.")
        try:
            while True:
                read_kwargs = {}
                if __debug__:
                    read_kwargs["exception_on_overflow"] = False
                
                data = await asyncio.to_thread(self.audio_stream.read, CHUNK_SIZE, **read_kwargs)
                await out_queue.put({"data": data, "mime_type": "audio/pcm"})
        except asyncio.CancelledError:
            logger.info("Listen audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in listen_audio: {e}", exc_info=True)
        finally:
            if self.audio_stream and self.audio_stream.is_active():
                try:
                    self.audio_stream.stop_stream()
                    self.audio_stream.close()
                except Exception as e_close:
                    logger.error(f"Error closing listen_audio stream: {e_close}")
            self.audio_stream = None
            logger.info("Listen audio task finished.")

    async def receive_audio(self, session, audio_in_queue):
        logger.info("Receive audio task started.")
        try:
            while True:
                if not session:
                    logger.warning("Session not active in receive_audio. Waiting.")
                    await asyncio.sleep(0.1)
                    continue
                
                turn = session.receive()
                async for response in turn:
                    if data := response.data:
                        audio_in_queue.put_nowait(data)
                        continue
                    if text := response.text:
                        print(text, end="", flush=True)
        except asyncio.CancelledError:
            logger.info("Receive audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in receive_audio: {e}", exc_info=True)
        finally:
            logger.info("Receive audio task finished.")

    async def play_audio(self, audio_in_queue):
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot play audio.")
            return

        stream = None
        try:
            stream = await asyncio.to_thread(
                self.pya.open,
                format=FORMAT,
                channels=CHANNELS,
                rate=RECEIVE_SAMPLE_RATE,
                output=True,
            )
        except Exception as e:
            logger.error(f"Failed to open audio stream for playing: {e}", exc_info=True)
            return

        logger.info("Play audio task started.")
        try:
            while True:
                bytestream = await audio_in_queue.get()
                await asyncio.to_thread(stream.write, bytestream)
                audio_in_queue.task_done()
        except asyncio.CancelledError:
            logger.info("Play audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in play_audio: {e}", exc_info=True)
        finally:
            if stream and stream.is_active():
                try:
                    stream.stop_stream()
                    stream.close()
                except Exception as e_close:
                    logger.error(f"Error closing play_audio stream: {e_close}")
            logger.info("Play audio task finished.")
            
    async def close_audio_resources(self):
        if self.audio_stream:
            try:
                if self.audio_stream.is_active():
                    self.audio_stream.stop_stream()
                self.audio_stream.close()
                logger.info("GeminiLiveSession microphone audio_stream closed.")
            except Exception as e:
                logger.error(f"Error closing microphone audio_stream in GeminiLiveSession: {e}", exc_info=True)
            finally:
                self.audio_stream = None

```

######## 📄 communication.py

* Last Modified : `2025-05-29 19:35:21`

```python
import asyncio
from core.logger import get_logger

logger = get_logger(__name__)

class CommunicationHandler:
    def __init__(self):
        pass
        
    async def send_realtime(self, out_queue, session):
        logger.info("Send realtime (audio/video) task started.")
        try:
            while True:
                msg = await out_queue.get()
                if session:
                    await session.send(input=msg)
                else:
                    logger.warning("Session not active in send_realtime, cannot send message. Waiting.")
                    await asyncio.sleep(0.1) 
        except asyncio.CancelledError:
            logger.info("Send realtime task cancelled.")
        except Exception as e:
            logger.error(f"Error in send_realtime: {e}", exc_info=True)
        finally:
            logger.info("Send realtime task finished.")

```

######## 📄 resources.py

* Last Modified : `2025-05-29 19:35:30`

```python
import asyncio
from core.logger import get_logger

logger = get_logger(__name__)

class ResourceManager:
    def __init__(self):
        pass
        
    async def close_resources(self, pya):
        if pya:
            try:
                pya.terminate()
                logger.info("GeminiLiveSession PyAudio instance terminated.")
            except Exception as e:
                logger.error(f"Error terminating PyAudio in GeminiLiveSession: {e}", exc_info=True)
            finally:
                pya = None
        logger.info("GeminiLiveSession resources closed.")

```

######## 📄 session.py

* Last Modified : `2025-05-29 19:36:01`

```python
import asyncio
import pyaudio
from core.logger import get_logger
from .audio import AudioHandler
from .video import VideoHandler
from .communication import CommunicationHandler
from .resources import ResourceManager

logger = get_logger(__name__)

class GeminiLiveSession:
    def __init__(self, client, connect_config, model_name: str, video_mode: str = "none"):
        self.client = client
        self.connect_config = connect_config
        self.model_name = model_name
        self.video_mode = video_mode

        self.audio_in_queue = None
        self.out_queue = None
        self.session = None
        self.other_tasks_list = []
        
        try:
            self.pya = pyaudio.PyAudio()
            logger.info("PyAudio instance created for GeminiLiveSession.")
        except Exception as e:
            logger.error(f"Failed to initialize PyAudio in GeminiLiveSession: {e}")
            self.pya = None
            raise
            
        self.audio_handler = AudioHandler(self.pya)
        self.video_handler = VideoHandler()
        self.comm_handler = CommunicationHandler()
        self.resource_manager = ResourceManager()

    async def run(self):
        logger.info(f"GeminiLiveSession run started with video_mode: {self.video_mode}")
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot run GeminiLiveSession.")
            return
            
        self.other_tasks_list = []
        try:
            async with self.client.aio.live.connect(model=self.model_name, config=self.connect_config) as session:
                self.session = session
                logger.info(f"Gemini Live session connected.")
                
                self.audio_in_queue = asyncio.Queue()
                self.out_queue = asyncio.Queue(maxsize=5)
                
                self.other_tasks_list.append(asyncio.create_task(
                    self.comm_handler.send_realtime(self.out_queue, self.session), 
                    name="GeminiSendRealtime"))
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.listen_audio(self.out_queue), 
                    name="GeminiListenAudio"))
                
                if self.video_mode == "camera":
                    self.other_tasks_list.append(asyncio.create_task(
                        self.video_handler.get_frames(self.out_queue, self.video_mode), 
                        name="GeminiGetFrames"))
                elif self.video_mode == "screen":
                    self.other_tasks_list.append(asyncio.create_task(
                        self.video_handler.get_screen(self.out_queue, self.video_mode), 
                        name="GeminiGetScreen"))
                
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.receive_audio(self.session, self.audio_in_queue), 
                    name="GeminiReceiveAudio"))
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.play_audio(self.audio_in_queue), 
                    name="GeminiPlayAudio"))
                
                if self.other_tasks_list:
                    await asyncio.gather(*self.other_tasks_list, return_exceptions=True)
                else:
                    logger.warning("No tasks were created in GeminiLiveSession run method.")

                logger.info("GeminiLiveSession: asyncio.gather completed for tasks.")

        except asyncio.CancelledError:
            logger.info("GeminiLiveSession run method was cancelled.")
        except Exception as e:
            logger.error(f"Exception in GeminiLiveSession run's main block: {e}", exc_info=True)
        finally:
            logger.info("GeminiLiveSession run method entering finally block for cleanup.")
            
            active_tasks_to_cancel = [t for t in self.other_tasks_list if t and not t.done()]
            if active_tasks_to_cancel:
                logger.info(f"Cancelling {len(active_tasks_to_cancel)} active tasks...")
                for task in active_tasks_to_cancel:
                    task.cancel()
                await asyncio.gather(*active_tasks_to_cancel, return_exceptions=True)
                logger.info("Finished cancelling tasks.")
            else:
                logger.info("No active tasks to cancel in finally block, or tasks already completed.")

            await self.close_resources()
            logger.info("GeminiLiveSession run method finished cleanup in finally block.")

    async def close_resources(self):
        logger.info("GeminiLiveSession closing resources...")
        await self.audio_handler.close_audio_resources()
        await self.resource_manager.close_resources(self.pya)
        self.pya = None
        logger.info("GeminiLiveSession resources closed.")

    def __del__(self):
        if self.pya:
            logger.warning("GeminiLiveSession __del__ called. Attempting to terminate PyAudio if not already done.")
            try:
                self.pya.terminate()
            except Exception:
                pass

```

######## 📄 video.py

* Last Modified : `2025-05-29 19:35:09`

```python
import asyncio
import base64
import io
import cv2
import PIL.Image
import mss
from core.logger import get_logger

logger = get_logger(__name__)

class VideoHandler:
    def __init__(self):
        pass
        
    def _get_frame(self, cap):
        ret, frame = cap.read()
        if not ret:
            return None
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(frame_rgb)
        img.thumbnail([1024, 1024])

        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)

        mime_type = "image/jpeg"
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_frames(self, out_queue, video_mode):
        if not video_mode == "camera":
            logger.debug("Camera mode not active, get_frames will not run.")
            return

        cap = await asyncio.to_thread(cv2.VideoCapture, 0)
        if not cap.isOpened():
            logger.error("Failed to open camera for get_frames.")
            return

        logger.info("Camera frames task started.")
        try:
            while True:
                frame = await asyncio.to_thread(self._get_frame, cap)
                if frame is None:
                    logger.info("No frame from camera, exiting get_frames loop.")
                    break
                await asyncio.sleep(1.0)
                await out_queue.put(frame)
        except asyncio.CancelledError:
            logger.info("get_frames task cancelled.")
        finally:
            if cap.isOpened():
                cap.release()
            logger.info("Camera frames task finished.")

    def _get_screen(self):
        sct = mss.mss()
        monitor = sct.monitors[0]
        i = sct.grab(monitor)
        mime_type = "image/jpeg"
        png_bytes = mss.tools.to_png(i.rgb, i.size)
        img = PIL.Image.open(io.BytesIO(png_bytes))
        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)
        jpeg_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(jpeg_bytes).decode()}

    async def get_screen(self, out_queue, video_mode):
        if not video_mode == "screen":
            logger.debug("Screen mode not active, get_screen will not run.")
            return

        logger.info("Screen capture task started.")
        try:
            while True:
                frame = await asyncio.to_thread(self._get_screen)
                if frame is None:
                    logger.warning("No frame from screen capture, exiting get_screen loop.")
                    break
                await asyncio.sleep(1.0)
                await out_queue.put(frame)
        except asyncio.CancelledError:
            logger.info("get_screen task cancelled.")
        finally:
            logger.info("Screen capture task finished.")

```

---

####### 📄 provider.py

* Last Modified : `2025-05-29 19:37:34`

```python
# jarvis/voice/dialog/providers/gemini_live/provider.py

import asyncio
from core.config import AppConfig
from core.logger import get_logger
from voice.dialog.base import BaseDialogProvider
from .session_handler import GeminiLiveSession
from .client_config import get_gemini_client, get_live_connect_config

logger = get_logger(__name__)

class GeminiLiveProvider(BaseDialogProvider):
    PROVIDER_NAME = "gemini_live"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("Initializing GeminiLiveProvider...")
        
        self.api_key = AppConfig.GEMINI_API_KEY
        self.model_name = AppConfig.GEMINI_LIVE_MODEL_NAME
        self.system_instruction = AppConfig.GEMINI_LIVE_SYSTEM_INSTRUCTION
        self.video_mode = AppConfig.GEMINI_LIVE_VIDEO_MODE

        if not self.api_key:
            msg = "GEMINI_API_KEY is not set in AppConfig. GeminiLiveProvider cannot be initialized."
            logger.error(msg)
            raise ValueError(msg)
        
        if not self.model_name:
            # AppConfig provides a default, so this should ideally not be empty.
            # This check is for robustness if AppConfig default was somehow bypassed or set to empty.
            msg = "GEMINI_LIVE_MODEL_NAME is not set or empty in AppConfig. Cannot initialize GeminiLiveProvider."
            logger.error(msg)
            raise ValueError(msg)

        try:
            self.client = get_gemini_client(self.api_key)
            self.connect_config = get_live_connect_config(self.system_instruction)
            
            self.session_handler = GeminiLiveSession(
                client=self.client,
                connect_config=self.connect_config,
                model_name=self.model_name,
                video_mode=self.video_mode
            )
            logger.info("GeminiLiveProvider initialized successfully with session handler.")
        except Exception as e:
            logger.error(f"Error during GeminiLiveProvider initialization: {e}", exc_info=True)
            raise

    async def run_session(self) -> None:
        logger.info(f"Starting Gemini Live session with provider: {self.PROVIDER_NAME}")
        try:
            await self.session_handler.run()
        except asyncio.CancelledError:
            logger.info(f"Gemini Live session (provider {self.PROVIDER_NAME}) was cancelled.")
        except Exception as e:
            logger.error(f"Error during Gemini Live session (provider {self.PROVIDER_NAME}): {e}", exc_info=True)
            raise # Re-throw to signal failure to the caller (speech_loop)
        finally:
            logger.info(f"Gemini Live session (provider {self.PROVIDER_NAME}) finished or was interrupted.")
            # Ensure session_handler's resources are cleaned up if its run() didn't complete finally block.
            # session_handler.run() already has a comprehensive finally block.
            # Calling close_resources again here might be redundant but safe if designed idempotently.
            if hasattr(self.session_handler, 'close_resources') and self.session_handler.pya is not None:
                 logger.debug("Provider ensuring session_handler resources are closed from its own finally block.")
                 await self.session_handler.close_resources()
```

####### 📄 session_handler.py

* Last Modified : `2025-05-29 19:36:29`

```python
from .core import GeminiLiveSession

```

---

---

---

#### 📄 engine.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/voice/engine.py
# Voice synthesis core
class VoiceEngine:
    def __init__(self):
        pass

    def synthesize_speech(self, text):
        pass

```

### 📁 hotword/

---

### 📁 recognition/

##### 📄 __init__.py

* Last Modified : `2025-03-15 00:09:25`

```python
# Initialize the recognition package
from .active_provider import recognition_manager, listen

__all__ = ['recognition_manager', 'listen']
```

##### 📄 active_provider.py

* Last Modified : `2025-05-29 18:53:55`

```python
from typing import Optional, Dict, Type
from core.logger import get_logger
from voice.recognition.base import BaseRecognitionProvider

from voice.recognition.providers.devsdocode_stt import SeleniumSTTProvider
from voice.recognition.providers.vosk_stt import VoskSTTProvider

logger = get_logger(__name__)

class RecognitionProviderManager:
    """
    Manages the active Speech Recognition provider.
    
    This class serves as a singleton that maintains the currently active
    recognition provider and allows switching between different providers.
    """
    
    PROVIDERS: Dict[str, Type[BaseRecognitionProvider]] = {
        "selenium_stt": SeleniumSTTProvider,
        "vosk": VoskSTTProvider,
    }
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RecognitionProviderManager, cls).__new__(cls)
            cls._instance._active_provider: Optional[BaseRecognitionProvider] = None
            cls._instance._initialized: bool = False
        return cls._instance
    
    def initialize(self, provider_name: str = "selenium_stt", **kwargs) -> None:
        """
        Initialize the recognition provider manager with a default provider.
        
        Args:
            provider_name (str): Name of the provider to use.
            **kwargs: Additional arguments to pass to the provider.
        
        Raises:
            ValueError: If the provider name is invalid.
        """
        if self._initialized:
            current_provider_name = self._active_provider.PROVIDER_NAME if self._active_provider else 'None'
            logger.info(f"RecognitionProviderManager already initialized (current STT provider: {current_provider_name}). Call to initialize with '{provider_name}' skipped.")
            return
            
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
        
        logger.info(f"Initializing Speech Recognition with provider: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def get_provider(self) -> Optional[BaseRecognitionProvider]:
        """
        Get the currently active recognition provider.
        
        Returns:
            Optional[BaseRecognitionProvider]: The active provider instance, or None if not initialized
                                              or no provider is active.
        """
        if not self._initialized:
            logger.warning("STT RecognitionProviderManager get_provider called before initialization.")
        return self._active_provider
    
    def set_provider(self, provider_name: str, **kwargs) -> None:
        """
        Change the active recognition provider.
        
        Args:
            provider_name (str): Name of the provider to use.
            **kwargs: Additional arguments to pass to the provider.
            
        Raises:
            ValueError: If the provider name is invalid.
        """
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
            
        logger.info(f"Switching Speech Recognition provider to: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def list_providers(self) -> Dict[str, str]:
        """
        Get a list of all available recognition providers.
        
        Returns:
            Dict[str, str]: Dictionary of provider names and their class names.
        """
        return {name: provider.__name__ for name, provider in self.PROVIDERS.items()}
    
    def listen(self, prints: bool = False) -> Optional[str]:
        """
        Listen for speech using the active provider.
        
        Args:
            prints (bool): Whether to print the transcribed text.
            
        Returns:
            Optional[str]: The transcribed text, or None if recognition failed or no provider.
        """
        provider = self.get_provider()
        if not provider:
            logger.error("Cannot listen: No active STT recognition provider.")
            return None
        return provider.listen(prints)

recognition_manager = RecognitionProviderManager()

def listen(prints: bool = False) -> Optional[str]:
    """
    Listen for speech using the active recognition provider.
    """
    return recognition_manager.listen(prints)
```

##### 📄 base.py

* Last Modified : `2025-03-15 00:09:25`

```python
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseRecognitionProvider(ABC):
    """
    Base class for all Speech Recognition providers.
    
    All speech recognition providers must implement this interface to ensure
    compatibility with the voice system.
    """
    
    PROVIDER_NAME = "base"
    
    def __init__(self):
        """Initialize the speech recognition provider."""
        pass
    
    @abstractmethod
    def listen(self, prints: bool = False) -> Optional[str]:
        """
        Listen for speech and return the transcribed text.
        
        Args:
            prints (bool): Whether to print the transcribed text.
            
        Returns:
            Optional[str]: The transcribed text, or None if recognition failed.
        """
        pass
    
    @abstractmethod
    def get_available_languages(self) -> Dict[str, Any]:
        """
        Get a list of available languages for this provider.
        
        Returns:
            Dict[str, Any]: Dictionary mapping language codes to their details.
        """
        pass
    
    def get_provider_name(self) -> str:
        """
        Get the name of this speech recognition provider.
        
        Returns:
            str: Provider name.
        """
        return self.PROVIDER_NAME
```

#### 📁 providers/

###### 📄 __init__.py

* Last Modified : `2025-03-23 17:23:24`

```python
from .devsdocode_stt import SeleniumSTTProvider
from .vosk_stt import VoskSTTProvider

__all__ = ['SeleniumSTTProvider', 'VoskSTTProvider']
```

###### 📄 devsdocode_stt.py

* Last Modified : `2025-05-29 07:10:47`

```python
from voice.recognition.providers.selenium_stt.provider import SeleniumSTTProvider

if __name__ == "__main__":
    from voice.recognition.providers.selenium_stt.main import *
```

##### 📁 selenium_stt/

####### 📄 driver_manager.py

* Last Modified : `2025-05-29 07:06:57`

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

from core.logger import get_logger

logger = get_logger(__name__)

class DriverManager:
    def __init__(self, wait_time: int = 10):
        self.wait_time = wait_time
        self.driver = None
        self.wait = None
        self.setup_driver()
    
    def setup_driver(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            try:
                self.driver.quit()
            except Exception:
                logger.warning("Error quitting previous driver instance.")
            finally:
                self.driver = None
        
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, self.wait_time)
            logger.info("Chrome WebDriver initialized/re-initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Chrome WebDriver: {e}")
            self.driver = None
            self.wait = None
            raise
    
    def try_stop_js_recognition(self):
        if not hasattr(self, 'driver') or not self.driver:
            return
        try:
            self.driver.execute_script("""
                if (window.currentRecognitionInstance && typeof window.currentRecognitionInstance.stop === 'function') {
                    try { window.currentRecognitionInstance.stop(); } catch (e) { /* ignore */ }
                }
            """)
        except Exception:
            logger.warning("Failed to execute script to stop JS recognition.")
            pass
    
    def cleanup(self):
        if hasattr(self, 'driver') and self.driver:
            self.try_stop_js_recognition()
            try:
                self.driver.quit()
                logger.info("Chrome WebDriver closed successfully")
            except Exception as e:
                logger.error(f"Error closing Chrome WebDriver: {e}")
            finally:
                self.driver = None

```

####### 📄 language_handler.py

* Last Modified : `2025-05-29 07:07:10`

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.logger import get_logger

logger = get_logger(__name__)

class LanguageHandler:
    def __init__(self, provider):
        self.provider = provider
    
    def select_language(self) -> None:
        if not self.provider.driver_manager.driver:
            return
        self.provider.driver_manager.driver.execute_script(
            f"""
            var select = document.getElementById('language_select');
            select.value = '{self.provider.language}';
            var event = new Event('change');
            select.dispatchEvent(event);
            """
        )

    def verify_language_selection(self) -> bool:
        if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
            return False
        try:
            language_select = self.provider.driver_manager.wait.until(
                EC.presence_of_element_located((By.ID, "language_select"))
            )
            self.provider.driver_manager.wait.until(
                lambda driver: driver.find_element(
                    By.CSS_SELECTOR, 
                    f"#language_select option[value='{self.provider.language}']"
                ).is_selected()
            )
            selected_option = language_select.find_element(By.CSS_SELECTOR, "option:checked")
            selected_language_value = selected_option.get_attribute("value")
            return selected_language_value == self.provider.language
        except Exception:
            return False

```

####### 📄 main.py

* Last Modified : `2025-05-29 07:08:21`

```python
import os
import time
from typing import Optional

from core.logger import get_logger
from voice.recognition.providers.selenium_stt.provider import SeleniumSTTProvider

logger = get_logger(__name__)

if __name__ == "__main__":
    provider = None
    try:
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_file_name = "index.html"
        html_file_path = os.path.join(script_dir, "assets", html_file_name)

        if not os.path.exists(html_file_path):
            logger.error(f"[FATAL ERROR] {html_file_name} not found at: {html_file_path}")
            logger.error(f"Please ensure '{html_file_name}' is in the '{os.path.join(script_dir, 'assets')}' directory.")
            exit(1)
        
        target_website_path = html_file_path
        
        logger.info(f"[INFO] Using speech recognition source: {target_website_path}")

        provider = SeleniumSTTProvider(
            website_path=target_website_path, 
            language="en-US", 
            quiet_timeout_seconds=7.0 
        )
        
        print("Made By ❤️ @DevsDoCode (SeleniumSTTProvider Test)")
        
        consecutive_error_count = 0
        max_consecutive_errors = 3

        while True: 
            if not provider or not provider.driver_manager.driver:
                logger.error("[ERROR] Speech listener or its WebDriver is not properly initialized. Attempting to re-initialize.")
                try:
                    provider = SeleniumSTTProvider(
                        website_path=target_website_path, 
                        language="en-US", 
                        quiet_timeout_seconds=7.0
                    )
                    logger.info("Re-initialized provider successfully.")
                    consecutive_error_count = 0
                except Exception as e:
                    logger.error(f"Failed to re-initialize provider: {e}")
                    consecutive_error_count +=1
                    if consecutive_error_count >= max_consecutive_errors:
                        logger.error("Max consecutive initialization errors reached. Exiting.")
                        break
                    time.sleep(2)
                    continue
            
            print("\nReady to listen...") 
            speech = provider.listen(prints=True)

            if speech is None:
                print("A critical error occurred during listen. Listener might try to recover.")
                consecutive_error_count += 1
                if consecutive_error_count >= max_consecutive_errors:
                    logger.error("Max consecutive listening errors reached. Exiting.")
                    break
                time.sleep(1)
                continue

            consecutive_error_count = 0

            if speech == "":
                print("No speech detected in this attempt or quiet timeout.") 
            else:
                print(f"Final text processed by main test: {speech}") 
                if "exit listener" in speech.lower():
                     print("Exit command received. Shutting down listener test.")
                     break
            
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Shutting down listener test...")
    except Exception as e:
        logger.error(f"[FATAL ERROR] An unexpected error occurred in the main application loop: {e}", exc_info=True)
    finally:
        print("Cleaning up resources...")
        if provider:
            pass 
        print("Listener test application finished.")

```

####### 📄 provider.py

* Last Modified : `2025-05-29 07:06:39`

```python
import os
from typing import Optional, Dict, Any

from core.logger import get_logger
from voice.recognition.base import BaseRecognitionProvider
from voice.recognition.providers.selenium_stt.driver_manager import DriverManager
from voice.recognition.providers.selenium_stt.recognition import RecognitionHandler

logger = get_logger(__name__)

class SeleniumSTTProvider(BaseRecognitionProvider):
    PROVIDER_NAME = "selenium_stt"

    LANGUAGE_OPTIONS = {
        "en-US": "English (United States)",
        "en-IN": "English (India)",
        "hi-IN": "Hindi (India)",
    }

    def __init__(self, language: str = "en-US", wait_time: int = 10, quiet_timeout_seconds: float = 7.0, website_path: Optional[str] = None):
        super().__init__()
        self.language = language
        self.wait_time = wait_time
        self.quiet_timeout_seconds = quiet_timeout_seconds

        default_local_html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "index.html")
        if website_path is None:
            self.raw_website_path = default_local_html_path
        else:
            self.raw_website_path = website_path
        
        self.driver_manager = DriverManager(wait_time)
        self.recognition_handler = RecognitionHandler(self)

    def listen(self, prints: bool = False) -> Optional[str]:
        result = self.recognition_handler.main()

        if result is None:
            logger.error("Speech recognition failed critically. WebDriver might be re-initialized on next call.")
            return None
        
        if result == "":
            return ""

        if prints:
            print(f"\033[92mYOU SAID: {result}\033[0m\n", flush=True)
        
        return result

    def get_available_languages(self) -> Dict[str, Any]:
        return self.LANGUAGE_OPTIONS

    def __del__(self):
        if hasattr(self, 'driver_manager'):
            logger.info("Closing SeleniumSTTProvider resources...")
            self.driver_manager.cleanup()

```

####### 📄 recognition.py

* Last Modified : `2025-05-29 07:07:45`

```python
import os
import time
from pathlib import Path
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from core.logger import get_logger
from voice.recognition.providers.selenium_stt.language_handler import LanguageHandler
from voice.recognition.providers.selenium_stt.utils import stream_text

logger = get_logger(__name__)

class RecognitionHandler:
    def __init__(self, provider):
        self.provider = provider
        self.language_handler = LanguageHandler(provider)
    
    def get_text(self) -> str:
        if not self.provider.driver_manager.driver:
            return ""
        try:
            return self.provider.driver_manager.driver.find_element(By.ID, "convert_text").text
        except Exception:
            return ""
    
    def main(self) -> Optional[str]:
        if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
            try:
                self.provider.driver_manager.setup_driver()
            except Exception as e:
                logger.error(f"Failed to setup driver in main: {e}")
                return None
            if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
                logger.error("WebDriver not available for listening cycle after setup attempt.")
                return None

        try:
            url_to_load: str
            if "://" in self.provider.raw_website_path:
                url_to_load = self.provider.raw_website_path
            else:
                abs_path = os.path.abspath(self.provider.raw_website_path)
                if not os.path.exists(abs_path):
                    logger.error(f"HTML file not found: {abs_path}")
                    return None
                url_to_load = Path(abs_path).as_uri()
            
            current_url = ""
            try:
                current_url = self.provider.driver_manager.driver.current_url
            except WebDriverException: 
                logger.warning("WebDriver connection lost, attempting to re-initialize.")
                self.provider.driver_manager.setup_driver() 
                if not self.provider.driver_manager.driver: 
                    logger.error("Failed to re-initialize WebDriver.")
                    return None
                current_url = "" 

            if current_url != url_to_load:
                self.provider.driver_manager.driver.get(url_to_load)
            else: 
                try:
                    text_area = self.provider.driver_manager.driver.find_element(By.ID, "convert_text")
                    if text_area:
                        text_area.clear()
                    self.provider.driver_manager.driver.execute_script("document.getElementById('is_recording').innerHTML = 'Recording: False';")
                except Exception:
                    logger.debug("Could not clear text area or reset recording status on existing page.")
                    pass 

            self.provider.driver_manager.wait.until(EC.presence_of_element_located((By.ID, "language_select")))
            self.provider.driver_manager.wait.until(EC.element_to_be_clickable((By.ID, "language_select")))
            self.provider.driver_manager.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#language_select option[value='en-US']"))) 
            self.language_handler.select_language()

            if not self.language_handler.verify_language_selection():
                logger.error(f"Failed to select language: {self.provider.language}. Please check language code and HTML options.")
                return None

            self.provider.driver_manager.driver.find_element(By.ID, "click_to_record").click()
            try:
                self.provider.driver_manager.wait.until(EC.text_to_be_present_in_element((By.ID, "is_recording"), "Recording: True"))
            except TimeoutException:
                logger.warning("Recording did not start in time.")
                self.provider.driver_manager.try_stop_js_recognition()
                return "" 

            print("\033[94m\rListening...", end='', flush=True)
            time_of_last_speech_or_start = time.time()
            last_processed_text = ""

            while True:
                is_recording_status_text = ""
                try:
                    is_recording_element = self.provider.driver_manager.driver.find_element(By.ID, "is_recording")
                    is_recording_status_text = is_recording_element.text if is_recording_element else "Recording: False"
                except WebDriverException: 
                    logger.error("WebDriver connection lost during recording.")
                    self.provider.driver_manager.driver = None 
                    return None 
                except Exception: 
                    logger.debug("Could not get recording status, assuming recording stopped.")
                    break 

                if not is_recording_status_text.startswith("Recording: True"):
                    break 

                current_text_from_page = self.get_text()
                if current_text_from_page and current_text_from_page != last_processed_text:
                    stream_text(current_text_from_page)
                    last_processed_text = current_text_from_page
                    time_of_last_speech_or_start = time.time()
                else:
                    if not last_processed_text and (time.time() - time_of_last_speech_or_start) > self.provider.quiet_timeout_seconds:
                        print("\r" + " " * 70 + "\r", end="", flush=True) 
                        print("Quiet timeout: No speech detected in this attempt.", flush=True)
                        self.provider.driver_manager.try_stop_js_recognition()
                        return "" 
                time.sleep(0.1) 
            
            self.provider.driver_manager.try_stop_js_recognition() 
            final_text = self.get_text()

            clear_length = 70
            if last_processed_text:
                clear_length = len(last_processed_text) + 30
            print("\r" + " " * clear_length + "\r", end="", flush=True)
            
            return final_text

        except WebDriverException as e:
            logger.error(f"WebDriverException in listening cycle: {e}. Attempting to re-initialize on next call.")
            self.provider.driver_manager.driver = None 
            return None
        except Exception as e:
            logger.error(f"Unexpected error in listening cycle: {e}")
            if hasattr(self.provider.driver_manager, 'driver') and self.provider.driver_manager.driver:
                self.provider.driver_manager.try_stop_js_recognition()
            return None

```

####### 📄 utils.py

* Last Modified : `2025-05-29 07:07:53`

```python
def stream_text(content: str) -> None:
    print("\033[96m\rUser Speaking: \033[93m" + f" {content}", end='', flush=True)

```

---

###### 📄 vosk_stt.py

* Last Modified : `2025-05-29 07:43:41`

```python
import os
import pyaudio
from typing import Optional, Dict, Any, Generator
from vosk import Model, KaldiRecognizer
import ast
from core.logger import get_logger
from voice.recognition.base import BaseRecognitionProvider

logger = get_logger(__name__)

class ModelNotFoundError(Exception):
    """Exception raised when a Vosk model is not found."""
    pass

class VoskSTTProvider(BaseRecognitionProvider):
    """
    Speech-to-Text provider using Vosk for offline speech recognition.
    
    This provider uses the Vosk library to provide offline speech recognition
    capabilities. It supports multiple languages through downloadable models.
    """

    PROVIDER_NAME = "vosk"
    
    # Default model mappings
    DEFAULT_MODEL_MAPPINGS = {
        "english-small": "voice/voices/assets/models/vosk/vosk-model-small-en-us-0.15",
    }
    
    def __init__(self, model_name=None, model_path=None, custom_mappings=None):
        """
        Initialize the Vosk STT provider.
        
        Args:
            model_name (str, optional): Name of the model to use from the mapping.
            model_path (str, optional): Direct path to a model directory.
            custom_mappings (dict, optional): Custom model name to path mappings.
            
        Raises:
            ValueError: If both model_name and model_path are provided.
            ModelNotFoundError: If the model is not found at the specified path.
        """
        super().__init__()
        self.model_mappings = self.DEFAULT_MODEL_MAPPINGS.copy()
        
        # Add custom mappings if provided
        if custom_mappings and isinstance(custom_mappings, dict):
            self.model_mappings.update(custom_mappings)
            
        # Validate and set model path
        self.model_path = self._resolve_model_path(model_name, model_path)
        
        # Initialize Vosk model
        try:
            self.model = Model(self.model_path)
            self.recognizer = KaldiRecognizer(self.model, 16000)
            logger.info(f"Vosk model initialized from: {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to initialize Vosk model: {e}")
            raise
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        self.stream = None
        
    def _resolve_model_path(self, model_name, model_path):
        """
        Resolve the model path from either a model name or direct path.
        
        Args:
            model_name (str, optional): Name of the model to use from the mapping.
            model_path (str, optional): Direct path to a model directory.
            
        Returns:
            str: The resolved model path.
            
        Raises:
            ValueError: If both model_name and model_path are provided or if model_name is unknown.
            ModelNotFoundError: If the model is not found at the specified path.
        """
        resolved_path = None
        
        # Check if both parameters are provided
        if model_name and model_path:
            raise ValueError("Provide either model_name OR model_path, not both. You might have used the wrong parameter.")
            
        # Resolve from model name
        if model_name:
            if model_name not in self.model_mappings:
                raise ValueError(f"Unknown model name: '{model_name}'. Available models: {', '.join(self.model_mappings.keys())}")
            resolved_path = self.model_mappings[model_name]
            
        # Use direct path
        elif model_path:
            resolved_path = model_path
            
        # Default to english-small if nothing specified
        else:
            resolved_path = self.model_mappings["english-small"]
            
        # Check if model exists
        if not os.path.exists(resolved_path):
            raise ModelNotFoundError(
                f"Vosk model not found at path: {resolved_path}\n"
                f"Please download the appropriate model and place it in the correct directory."
            )
            
        return resolved_path
    
    def _start_stream(self):
        """Start the audio stream if not already started."""
        if self.stream is None or not self.stream.is_active():
            try:
                self.stream = self.audio.open(
                    format=pyaudio.paInt16, 
                    channels=1, 
                    rate=16000, 
                    input=True, 
                    frames_per_buffer=8192
                )
                logger.debug("Vosk audio stream started.")
            except Exception as e:
                logger.error(f"Failed to open Vosk audio stream: {e}")
                self.stream = None
                raise
    
    def _stop_listening_stream(self):
        """Stop the audio stream and release the microphone resource gently."""
        if self.stream and self.stream.is_active():
            try:
                self.stream.stop_stream()
                self.stream.close()
                logger.debug("Vosk audio stream stopped and closed.")
            except Exception as e:
                logger.error(f"Error stopping/closing Vosk audio stream: {e}")
        self.stream = None

    
    def _speech_to_text_generator(self, prints: bool = True) -> Generator[str, None, None]:
        """
        Generate transcribed text from speech.
        
        Args:
            prints (bool): Whether to print the transcription results.
            
        Yields:
            str: The transcribed text in lowercase.
        """
        self._start_stream()
        
        while True:
            data = self.stream.read(8192)
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                result_dict = ast.literal_eval(result)
                if 'text' in result_dict and result_dict['text']:
                    if prints: 
                        print("\rTranscript: " + result_dict['text'])
                    yield result_dict['text'].lower()
            else:
                if prints: 
                    partial = self.recognizer.PartialResult()
                    partial_text = partial.split('"')[-2] if '"' in partial else ""
                    print("\rSpeaking: " + partial_text, end='', flush=True)
    
    def listen(self, prints: bool = False) -> Optional[str]:
        """
        Listen for speech and return the transcribed text.
        
        Args:
            prints (bool): Whether to print the transcribed text.
            
        Returns:
            Optional[str]: The transcribed text. Returns an empty string "" for silence 
                           or no speech detected, and None if a recognition error occurred.
        """
        recognized_text = None
        try:
            for text_segment in self._speech_to_text_generator(prints):
                if text_segment:
                    recognized_text = text_segment
                    break
            
            if recognized_text is None:
                 recognized_text = ""

            return recognized_text
        except Exception as e:
            logger.error(f"Error during Vosk speech recognition: {e}")
            return None
        finally:
            self._stop_listening_stream()
    
    def get_available_languages(self) -> Dict[str, Any]:
        """
        Get a list of available languages for this provider.
        
        Returns:
            Dict[str, Any]: Dictionary mapping language codes to their details.
        """
        return {name: path for name, path in self.model_mappings.items()}
    
    def __del__(self):
        """Clean up resources when the provider is destroyed."""
        if hasattr(self, 'stream') and self.stream:
            try:
                self.stream.stop_stream()
                self.stream.close()
            except Exception as e:
                logger.error(f"Error closing audio stream: {e}")
                
        if hasattr(self, 'audio'):
            try:
                self.audio.terminate()
                logger.info("PyAudio terminated successfully")
            except Exception as e:
                logger.error(f"Error terminating PyAudio: {e}")

```

---

---

### 📁 text_to_speech/

##### 📄 active_provider.py

* Last Modified : `2025-05-29 18:54:01`

```python
from typing import Optional, Dict, Type
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

from voice.text_to_speech.providers.deepgram import DeepgramTTSProvider
from voice.text_to_speech.providers.hearling import HearlingTTSProvider
from voice.text_to_speech.providers.speechify import SpeechifyTTSProvider
from voice.text_to_speech.providers.tiktok_tts import TikTokTTSProvider
from voice.text_to_speech.providers.edge_tts import EdgeTTSProvider

logger = get_logger(__name__)

class TTSProviderManager:
    """
    Manages the active Text-to-Speech provider.
    """
    
    PROVIDERS: Dict[str, Type[BaseTTSProvider]] = {
        "deepgram": DeepgramTTSProvider,
        "hearling": HearlingTTSProvider,
        "speechify": SpeechifyTTSProvider,
        "tiktok": TikTokTTSProvider,
        "edge_tts": EdgeTTSProvider,
    }
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TTSProviderManager, cls).__new__(cls)
            cls._instance._active_provider: Optional[BaseTTSProvider] = None
            cls._instance._initialized: bool = False
        return cls._instance
    
    def initialize(self, provider_name: str = "deepgram", **kwargs) -> None:
        """
        Initialize the TTS provider manager with a default provider.
        """
        if self._initialized:
            current_provider_name = self._active_provider.PROVIDER_NAME if self._active_provider else 'None'
            logger.info(f"TTSProviderManager already initialized (current TTS provider: {current_provider_name}). Call to initialize with '{provider_name}' skipped.")
            return
            
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
        
        logger.info(f"Initializing TTS with provider: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def get_provider(self) -> Optional[BaseTTSProvider]:
        """
        Get the currently active TTS provider.
        """
        if not self._initialized:
            logger.warning("TTS TTSProviderManager get_provider called before initialization.")
        return self._active_provider
    
    def set_provider(self, provider_name: str, **kwargs) -> None:
        """
        Change the active TTS provider.
        """
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
            
        logger.info(f"Switching TTS provider to: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def list_providers(self) -> Dict[str, str]:
        """
        Get a list of all available TTS providers.
        """
        return {name: provider.__name__ for name, provider in self.PROVIDERS.items()}
    
    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech using the active provider.
        """
        provider = self.get_provider()
        if not provider:
            logger.error("Cannot speak: No active TTS provider.")
            return
        provider.speak(text, voice)
    
    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> Optional[str]:
        """
        Generate speech using the active provider.
        """
        provider = self.get_provider()
        if not provider:
            logger.error("Cannot generate_speech: No active TTS provider.")
            return None
        return provider.generate_speech(text, voice, output_path)

tts_manager = TTSProviderManager()

def speak(text: str, voice: Optional[str] = None) -> None:
    """
    Speak text using the active TTS provider.
    """
    tts_manager.speak(text, voice)

def generate_speech(text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> Optional[str]:
    """
    Generate speech using the active TTS provider.
    """
    return tts_manager.generate_speech(text, voice, output_path)
```

##### 📄 base.py

* Last Modified : `2025-03-23 15:21:34`

```python
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseTTSProvider(ABC):
    """
    Base class for all Text-to-Speech providers.
    
    All TTS providers must implement this interface to ensure
    compatibility with the voice system.
    """
    
    PROVIDER_NAME = "base"
    
    def __init__(self):
        """Initialize the TTS provider."""
        pass
    
    @abstractmethod
    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Convert text to speech and return the path to the audio file.
        
        Args:
            text (str): The text to convert to speech.
            voice (Optional[str]): The voice to use for speech generation.
            output_path (Optional[str]): Path to save the audio file.
        
        Returns:
            str: Path to the generated audio file.
        """
        pass
    
    @abstractmethod
    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it immediately.
        
        Args:
            text (str): The text to speak.
            voice (Optional[str]): The voice to use for speech generation.
        """
        pass
    
    @abstractmethod
    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get a list of available voices for this provider.
        
        Returns:
            Dict[str, Any]: Dictionary mapping voice IDs to their details.
        """
        pass
    
    def get_provider_name(self) -> str:
        """
        Get the name of this TTS provider.
        
        Returns:
            str: Provider name.
        """
        return self.PROVIDER_NAME
```

#### 📁 providers/

###### 📄 deepgram.py

* Last Modified : `2025-03-23 15:21:34`

```python
import os
import base64
import requests
from typing import Optional

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

logger = get_logger(__name__)

class DeepgramTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider using Deepgram's API.
    
    This provider allows converting text to natural-sounding speech using
    Deepgram's various voice models.
    """
    
    PROVIDER_NAME = "deepgram"
    
    # Available voice models
    VOICE_MODELS = {
        "aura_asteria": "aura-asteria-en",
        "aura_arcas": "aura-arcas-en",
        "aura_luna": "aura-luna-en", 
        "aura_zeus": "aura-zeus-en"
    }
    
    def __init__(self, default_voice: str = "aura_arcas"):
        """
        Initialize the Deepgram TTS provider.
        
        Args:
            default_voice (str): The default voice model to use.
                                 Must be one of the keys in VOICE_MODELS.
        """
        super().__init__()
        self.api_url = "https://deepgram.com/api/ttsAudioGeneration"
        
        if default_voice not in self.VOICE_MODELS:
            logger.warning(f"Invalid voice model '{default_voice}'. Using default 'aura_arcas' instead.")
            default_voice = "aura_arcas"
            
        self.default_voice = default_voice
        self.temp_audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                           "../../../../data/cache/temp_audio.mp3")
        
        # Ensure cache directory exists
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        
        logger.info(f"Initialized Deepgram TTS provider with default voice: {self.VOICE_MODELS[default_voice]}")
    
    def _get_headers(self) -> dict:
        """
        Generate the headers required for the Deepgram API request.
        
        Returns:
            dict: Headers for the API request.
        """
        return {
            "authority": "deepgram.com",
            "method": "POST",
            "path": "/api/ttsAudioGeneration",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://deepgram.com",
            "referer": "https://deepgram.com/",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "dnt": "1"
        }
    
    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Convert text to speech using Deepgram's API.
        
        Args:
            text (str): The text to convert to speech.
            voice (str, optional): Voice model to use (one of the keys in VOICE_MODELS).
                                  If None, uses the default voice.
            output_path (str, optional): Path to save the audio file.
                                        If None, uses a temporary file.
        
        Returns:
            str: Path to the generated audio file.
            
        Raises:
            Exception: If the API request fails.
        """
        # Use default voice if none specified
        voice_key = voice if voice in self.VOICE_MODELS else self.default_voice
        voice_model = self.VOICE_MODELS[voice_key]
        
        # Determine output file path
        file_path = output_path if output_path else self.temp_audio_path
        
        # Clean up any existing file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logger.warning(f"Failed to remove existing audio file: {e}")
        
        # Prepare the request
        headers = self._get_headers()
        payload = {"text": text, "model": voice_model}
        
        try:
            logger.debug(f"Sending request to Deepgram TTS API with voice model: {voice_model}")
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            # Save the audio file
            with open(file_path, 'wb') as audio_file:
                audio_file.write(base64.b64decode(response.json()['data']))
            
            logger.debug(f"Successfully generated speech, saved to: {file_path}")
            return file_path
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to generate speech with Deepgram: {e}")
            raise Exception(f"Deepgram TTS API request failed: {e}")
    
    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text (str): The text to speak.
            voice (str, optional): Voice model to use.
                                  If None, uses the default voice.
        """
        try:
            # Generate speech
            audio_path = self.generate_speech(text, voice)
            
            # Import here to avoid circular imports
            from utils.helpers import play_audio
            
            # Play the audio
            logger.debug(f"Playing audio: {audio_path}")
            play_audio(audio_path)
            
            # Clean up the temporary file
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
                
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")
            
    def list_available_voices(self) -> dict:
        """
        Return a dictionary of available voice models.
        
        Returns:
            dict: Available voice models.
        """
        return self.VOICE_MODELS

```

###### 📄 edge_tts.py

* Last Modified : `2025-03-23 15:21:34`

```python
import os
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from typing import Optional, Dict, Any
from utils.helpers import play_audio

logger = get_logger(__name__)

class EdgeTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider that uses the Edge TTS command-line tool.
    
    This provider runs the edge-tts system command with the appropriate parameters.
    Available voices include (but are not limited to):
      • en-US-JennyNeural
      • en-SG-LunaNeural
      • en-AU-NatashaNeural
      • en-CA-ClaraNeural
      • en-CA-LiamNeural
    """
    PROVIDER_NAME = "edge_tts"

    VOICE_OPTIONS = {
        "en-US-JennyNeural": "en-US-JennyNeural",
        "en-SG-LunaNeural": "en-SG-LunaNeural",
        "en-AU-NatashaNeural": "en-AU-NatashaNeural",
        "en-CA-ClaraNeural": "en-CA-ClaraNeural",
        "en-CA-LiamNeural": "en-CA-LiamNeural",
    }

    def __init__(self, default_voice: str = "en-US-JennyNeural"):
        """
        Initialize the EdgeTTSProvider.
        
        Args:
            default_voice (str): The default voice to use.
        """
        super().__init__()
        if default_voice not in self.VOICE_OPTIONS:
            logger.warning(f"Default voice '{default_voice}' not available; reverting to 'en-US-JennyNeural'.")
            default_voice = "en-US-JennyNeural"
        self.default_voice = default_voice
        
        # Create cache directory with absolute path
        self.cache_dir = os.path.abspath(os.path.join("data", "cache"))
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Create paths for audio and subtitle files
        self.subtitle_file = os.path.join(self.cache_dir, "subtitles.srt")

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Generate speech using the edge-tts command.
        
        Args:
            text (str): The text to synthesize.
            voice (Optional[str]): The voice to use.
            output_path (Optional[str]): The file path to save the generated audio.
            
        Returns:
            str: The path to the generated audio file.
        """
        voice = voice if (voice and voice in self.VOICE_OPTIONS) else self.default_voice
        
        # Create output file in cache directory
        output_file = os.path.join(self.cache_dir, f"{voice}.mp3") if not output_path else output_path
        
        # Create a simple command just like the sample code
        command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "{output_file}" --write-subtitles "{self.subtitle_file}"'
        
        logger.debug(f"Executing command: {command}")
        os.system(command)
        return output_file

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Generate and immediately play synthesized speech.
        
        Args:
            text (str): The text to speak.
            voice (Optional[str]): The voice to use.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            # Use the play_audio helper function
            play_audio(audio_path)
            
            # Cleanup: remove the subtitle file and audio file after playing
            if os.path.exists(self.subtitle_file):
                os.remove(self.subtitle_file)
            if os.path.exists(audio_path):
                os.remove(audio_path)
        except Exception as e:
            logger.error(f"Failed in EdgeTTSProvider speak: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get a dictionary of available voices.
        
        Returns:
            dict: Mapping of available voice names.
        """
        return self.VOICE_OPTIONS

```

###### 📄 hearling.py

* Last Modified : `2025-03-23 15:21:34`

```python
import aiohttp
import asyncio
import aiofiles
import os
import random
import threading
from typing import Optional, List

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from utils.helpers import play_audio

logger = get_logger(__name__)


class HearlingTTSProvider(BaseTTSProvider):
    PROVIDER_NAME = "hearling"

    # New voice list for Hearling
    AVAILABLE_VOICES: List[str] = [
        'hi-IN-Standard-A', 'hi-IN-Standard-B', 'hi-IN-Standard-C',
        'hi-IN-Standard-D', 'hi-IN-Standard-E', 'hi-IN-Standard-F',
        'hi-IN-Wavenet-A', 'hi-IN-Wavenet-B', 'hi-IN-Wavenet-C',
        'hi-IN-Wavenet-D', 'hi-IN-Wavenet-E', 'hi-IN-Wavenet-F'
    ]

    def __init__(self, email_prefix: str = "devsdocode", max_pool_size: int = 5):
        super().__init__()
        self.email_prefix = email_prefix
        self.url_accounts = "https://api.hearling.com/accounts"
        self.url_clips = "https://api.hearling.com/clips"
        self.token_pool = []
        self.max_pool_size = max_pool_size
        self.is_closing = False

        # Create a temporary audio file path under data/cache
        self.temp_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../../../../data/cache/temp_audio.mp3"
        )
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)

        # Create a new event loop running in its own thread.
        self.loop = asyncio.new_event_loop()
        self.loop_thread = threading.Thread(target=self._run_loop, args=(self.loop,), daemon=True)
        self.loop_thread.start()
        # Ensure the provider is initialized
        future = asyncio.run_coroutine_threadsafe(self.initialize(), self.loop)
        try:
            future.result()  # Block until initialization completes.
        except Exception as e:
            logger.error(f"Initialization error in Hearling provider: {e}")
        logger.info("Initialized Hearling TTS provider")

    def _run_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        """Utility function: run the provided loop forever in a dedicated thread."""
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def initialize(self) -> None:
        """Initialize the async session and prefill the token pool."""
        self.session = aiohttp.ClientSession()
        await self.refill_token_pool()

    async def cleanup(self) -> None:
        """Cleanup asynchronous resources and stop the dedicated event loop."""
        self.is_closing = True
        if self.session and not self.session.closed:
            await self.session.close()
        # Stop the loop and wait for the thread to finish.
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.loop_thread.join()

    async def refill_token_pool(self) -> None:
        """Asynchronously prefill the token pool with account tokens."""
        if self.is_closing:
            return
        try:
            while len(self.token_pool) < self.max_pool_size:
                if self.is_closing:
                    break
                token = await self.create_account()
                if token:
                    self.token_pool.append(token)
        except Exception as e:
            logger.error(f"Token pool refill error: {e}")

    async def create_account(self) -> Optional[str]:
        """Create a new account to retrieve a token."""
        if self.session is None or self.session.closed:
            return None
        email = f"{self.email_prefix}{random.randint(10000, 99999)}@gmail.com"
        payload = {"email": email, "password": "DevsDoCode"}
        async with self.session.post(self.url_accounts, json=payload) as response:
            response.raise_for_status()
            data = await response.json()
            return data.get('token')

    async def get_token(self) -> Optional[str]:
        """
        Retrieve a token from the pool. If the pool is empty,
        refill it and then get a token.
        """
        if not self.token_pool:
            await self.refill_token_pool()
        return self.token_pool.pop() if self.token_pool else None

    async def download_audio(self, url: str, filename: str) -> None:
        """Download an audio file from the URL asynchronously."""
        async with self.session.get(url) as response:
            async with aiofiles.open(filename, 'wb') as f:
                await f.write(await response.read())

    async def _async_generate_speech(self, text: str, voice: Optional[str], output_path: str) -> None:
        """The asynchronous implementation of speech generation via Hearling API."""
        try:
            token = await self.get_token()
            if not token:
                raise Exception("Failed to get token")
            headers = {"Authorization": f"Bearer {token}"}

            # Choose the provided voice if valid; otherwise, use the first voice.
            selected_voice = voice if (voice in self.AVAILABLE_VOICES) else self.AVAILABLE_VOICES[0]
            payload = {"text": text, "voice": selected_voice}

            async with self.session.post(self.url_clips, headers=headers, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                audio_url = data['clip']['location']

            await self.download_audio(audio_url, output_path)

            # Refill token pool asynchronously.
            if not self.is_closing:
                asyncio.run_coroutine_threadsafe(self.refill_token_pool(), self.loop)
        except Exception as e:
            logger.error(f"Error generating speech: {e}")
            raise

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        A synchronous wrapper that triggers asynchronous speech generation.
        Returns the path to the generated audio file.
        """
        file_path = output_path if output_path else self.temp_audio_path
        future = asyncio.run_coroutine_threadsafe(
            self._async_generate_speech(text, voice, file_path), self.loop
        )
        try:
            future.result()  # Block until the coroutine completes.
        except Exception as e:
            logger.error(f"Error in generate_speech: {e}")
            raise
        return file_path

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play the generated audio.
        After playback, cleans up the temporary audio file.
        
        This method handles the async operations internally, providing a 
        synchronous interface to match other providers.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            play_audio(audio_path)
            # Don't remove the file here as play_audio now handles cleanup
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")

    def list_available_voices(self) -> List[str]:
        """Return the list of available voices."""
        return self.AVAILABLE_VOICES

    def __del__(self):
        """
        Attempt to clean up async resources when the object is deleted.
        Note that errors during __del__ are logged.
        """
        try:
            if hasattr(self, 'loop') and self.loop.is_running():
                asyncio.run_coroutine_threadsafe(self.cleanup(), self.loop).result()
        except Exception as e:
            logger.error(f"Error during cleanup in __del__: {e}")

```

###### 📄 speechify.py

* Last Modified : `2025-03-23 15:21:34`

```python
import os
import requests
import base64
from typing import Optional, Dict, Any

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from utils.helpers import play_audio

logger = get_logger(__name__)

class SpeechifyTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider using Speechify's API.
    
    This provider offers various celebrity and character voices.
    """
    
    PROVIDER_NAME = "speechify"
    
    # Available voice models
    VOICE_MODELS = {
        "mrbeast": "mrbeast",
        "jamie": "jamie",
        "snoop": "snoop",
        "henry": "henry",
        "gwyneth": "gwyneth",
        "cliff": "cliff",
        "narrator": "narrator"
    }
    
    def __init__(self, default_voice: str = "mrbeast"):
        """
        Initialize the Speechify TTS provider.
        
        Args:
            default_voice (str): Default voice to use
        """
        super().__init__()
        self.api_url = "https://audio.api.speechify.com/generateAudioFiles"
        self.default_voice = default_voice
        self.temp_audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                           "../../../../data/cache/temp_audio.mp3")
        
        # Ensure cache directory exists
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        
        logger.info(f"Initialized Speechify TTS provider with default voice: {default_voice}")

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Generate speech using Speechify's API.
        
        Args:
            text (str): Text to convert to speech
            voice (Optional[str]): Voice model to use
            output_path (Optional[str]): Path to save audio file
            
        Returns:
            str: Path to generated audio file
        """
        voice_name = voice if voice in self.VOICE_MODELS else self.default_voice
        file_path = output_path if output_path else self.temp_audio_path
        
        # Clean up existing file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logger.warning(f"Failed to remove existing audio file: {e}")
        
        # Prepare request
        payload = {
            "audioFormat": "mp3",
            "paragraphChunks": [text],
            "voiceParams": {
                "name": voice_name,
                "engine": "speechify",
                "languageCode": "en-US"
            }
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            
            # Save audio file
            audio_data = base64.b64decode(response.json()['audioStream'])
            with open(file_path, 'wb') as audio_file:
                audio_file.write(audio_data)
            
            return file_path
            
        except Exception as e:
            logger.error(f"Failed to generate speech with Speechify: {e}")
            raise

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text (str): Text to speak
            voice (Optional[str]): Voice to use
        """
        try:
            audio_path = self.generate_speech(text, voice)
            play_audio(audio_path)
            
            # Cleanup
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
                
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get available voice models.
        
        Returns:
            Dict[str, Any]: Available voice models
        """
        return self.VOICE_MODELS
```

###### 📄 tiktok_tts.py

* Last Modified : `2025-03-23 15:21:34`

```python
import os
import json
import base64
import requests
from typing import Optional, Dict, Any
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

logger = get_logger(__name__)

class TikTokTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider that aggregates two API endpoints.
    Internally it uses either the "Gesserit" or the "WeilByte" endpoints.
    
    Available voices (for both variants):
      • en_au_001
      • en_male_narration
      • en_male_funny
      • en_male_cody
      • en_female_emotional
      • en_us_rocket
      • en_female_f08_salut_damour

    To select the underlying API, provide variant="gesserit" or variant="weilbyte" when initializing.
    """
    PROVIDER_NAME = "tiktok"

    VOICE_OPTIONS = (
        "en_au_001",
        "en_male_narration",
        "en_male_funny",
        "en_male_cody",
        "en_female_emotional",
        "en_us_rocket",
        "en_female_f08_salut_damour",
    )

    API_ENDPOINTS = {
        "gesserit": "https://gesserit.co/api/tiktok-tts",
        "weilbyte": "https://tiktok-tts.weilnet.workers.dev/api/generation",
    }

    REQUEST_DATA_KEYS = {
        "gesserit": "base64",
        "weilbyte": "data",
    }

    def __init__(self, variant: str = "gesserit", default_voice: str = "en_us_rocket"):
        """
        Initialize the tiktok API TTS provider.
        
        Args:
            variant (str): Which underlying API variant to use ("gesserit" or "weilbyte").
            default_voice (str): The default voice to use.
        """
        super().__init__()
        if variant not in self.API_ENDPOINTS:
            raise ValueError("Invalid variant. Must be either 'gesserit' or 'weilbyte'.")
        self.variant = variant
        self.voice_options = self.VOICE_OPTIONS
        if default_voice not in self.voice_options:
            raise ValueError(f"Invalid default voice. Must be one of: {', '.join(self.voice_options)}")
        self.default_voice = default_voice
        self.api_endpoint = self.API_ENDPOINTS[variant]
        self.request_data_key = self.REQUEST_DATA_KEYS[variant]
        self.temp_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../../../../data/cache/temp_audio.mp3"
        )
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        logger.info(f"Initialized tiktokAPITTSProvider using variant '{variant}' with default voice: {default_voice}")

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Convert text to speech using the selected API.
        
        Args:
            text (str): Text to synthesize.
            voice (Optional[str]): Voice to use; if not provided or invalid, uses the default.
            output_path (Optional[str]): Where to save the generated audio.
            
        Returns:
            str: Path to the generated audio file.
        """
        # Use default voice if none provided or if the voice is not valid.
        voice = voice if (voice and voice in self.voice_options) else self.default_voice
        file_path = output_path if output_path else self.temp_audio_path

        # Clean up an existing file if needed.
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                logger.warning(f"Couldn't remove existing temporary file: {e}")

        headers = {"Content-Type": "application/json"}
        payload = {"text": text, "voice": voice}

        try:
            response = requests.post(self.api_endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Request to {self.api_endpoint} failed: {e}")
            raise

        try:
            audio_data = base64.b64decode(response.json()[self.request_data_key])
            with open(file_path, "wb") as f:
                f.write(audio_data)
        except Exception as e:
            logger.error(f"Error saving audio data: {e}")
            raise

        return file_path

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it immediately.
        
        Args:
            text (str): Text to speak.
            voice (Optional[str]): Voice to be used.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            # Using our centralized play_audio helper.
            from utils.helpers import play_audio
            play_audio(audio_path)
            # Clean up the temp file
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
        except Exception as e:
            logger.error(f"Failed to speak text in tiktokAPITTSProvider: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get a dictionary of available voices.
        
        Returns:
            dict: Mapping of voice IDs to voice names.
        """
        return {voice: voice for voice in self.voice_options}
```

---

---

### 📁 voices/

##### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/voice/voices/__init__.py

```

---

#### 📄 wake_word.py

* Last Modified : `2025-05-29 07:48:07`

```python
import pvporcupine
import pyaudio
import struct
from core.logger import get_logger
from core.config import AppConfig

class WakeWordDetector:
    def __init__(self, access_key, keywords=None, keyword_paths=None, sensitivities=None):
        self.logger = get_logger(__name__)
        self.access_key = access_key
        self.keywords = keywords
        self.keyword_paths = keyword_paths
        self.sensitivities = sensitivities

        if not self.access_key:
            self.logger.error("PICOVOICE_API_KEY is not provided. Wake word detection will fail.")
            raise ValueError("PICOVOICE_API_KEY is required for WakeWordDetector.")

        self.porcupine = None
        self.audio_stream = None
        try:
            self.pa = pyaudio.PyAudio()
            self.logger.info("PyAudio initialized for WakeWordDetector.")
        except Exception as e:
            self.logger.error(f"Failed to initialize PyAudio: {e}")
            self.pa = None
            raise
        self.logger.info("WakeWordDetector initialized.")

    def start_detector(self):
        if self.porcupine is not None:
            self.logger.warning("Detector already started.")
            return

        try:
            self.porcupine = pvporcupine.create(
                access_key=self.access_key,
                keywords=self.keywords,
                keyword_paths=self.keyword_paths,
                sensitivities=self.sensitivities
            )
            if not self.pa:
                self.logger.error("PyAudio instance not available. Cannot start detector.")
                raise RuntimeError("PyAudio not initialized. Cannot start Porcupine.")
            self.audio_stream = self.pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length
            )
            self.logger.info("Porcupine wake word detector started successfully.")
            self.logger.info(f"Listening for: {self.keywords}")
        except pvporcupine.PorcupineError as e:
            self.logger.error(f"Failed to initialize Porcupine: {e}")
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred while starting detector: {e}")
            self.stop_detector()
            raise

    def listen_for_wake_word(self):
        if self.porcupine is None or self.audio_stream is None:
            self.logger.error("Detector not started. Call start_detector() first.")
            raise RuntimeError("Wake word detector is not properly started.")

        try:
            while True:
                pcm = self.audio_stream.read(self.porcupine.frame_length, exception_on_overflow=False)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                result = self.porcupine.process(pcm)

                if result >= 0:
                    self.logger.info(f"Wake word '{self.keywords[result]}' detected.")
                    return True
        except Exception as e:
            self.logger.error(f"Error during wake word listening: {e}")
            return False

    def stop_detector(self):
        if self.audio_stream is not None:
            try:
                if self.audio_stream.is_active():
                    self.audio_stream.stop_stream()
                self.audio_stream.close()
            except Exception as e:
                self.logger.error(f"Error closing audio stream: {e}")
            finally:
                self.audio_stream = None

        if self.porcupine is not None:
            try:
                self.porcupine.delete()
            except Exception as e:
                self.logger.error(f"Error deleting Porcupine instance: {e}")
            finally:
                self.porcupine = None
        self.logger.info("Wake word detector stopped and resources released.")

    def __del__(self):
        self.logger.debug("WakeWordDetector being deleted, ensuring all resources are released.")
        if self.audio_stream is not None:
            try:
                if self.audio_stream.is_active():
                    self.audio_stream.stop_stream()
                self.audio_stream.close()
            except Exception as e:
                self.logger.error(f"Error closing audio stream during __del__: {e}")
            finally:
                self.audio_stream = None

        if self.porcupine is not None:
            try:
                self.porcupine.delete()
            except Exception as e:
                self.logger.error(f"Error deleting Porcupine instance during __del__: {e}")
            finally:
                self.porcupine = None
        
        if self.pa is not None:
            try:
                self.pa.terminate()
                self.logger.info("PyAudio instance terminated in WakeWordDetector.__del__.")
            except Exception as e:
                self.logger.error(f"Error terminating PyAudio during __del__: {e}")
            finally:
                self.pa = None
        
        self.logger.info("Wake word detector fully stopped and resources released from __del__.")


```

---

## 📁 web/

#### 📄 __init__.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/web/__init__.py

```

#### 📄 api_manager.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/web/api_manager.py
# API integrations
class APIManager:
    def __init__(self):
        pass

    def call_api(self, api_name, parameters):
        pass

```

#### 📄 browser.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/web/browser.py
# Browser automation
class BrowserAutomator:
    def __init__(self):
        pass

    def automate_browser_task(self, task_description):
        pass

```

#### 📄 scraper.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/web/scraper.py
# Web scraping
class WebScraper:
    def __init__(self):
        pass

    def scrape_website(self, url):
        pass

```

#### 📄 task_scheduler.py

* Last Modified : `2025-03-23 15:21:34`

```python
# jarvis/web/task_scheduler.py
# Web task scheduling
class WebTaskScheduler:
    def __init__(self):
        pass

    def schedule_web_task(self, task_description, time):
        pass

```

---

