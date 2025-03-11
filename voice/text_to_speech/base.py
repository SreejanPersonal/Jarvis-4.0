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