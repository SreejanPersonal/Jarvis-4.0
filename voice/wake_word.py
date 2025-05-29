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

