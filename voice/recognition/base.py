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