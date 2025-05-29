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
