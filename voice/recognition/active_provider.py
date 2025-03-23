from typing import Optional, Dict
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
    
    # Available providers
    PROVIDERS = {
        "selenium_stt": SeleniumSTTProvider,
        "vosk": VoskSTTProvider,
    }
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RecognitionProviderManager, cls).__new__(cls)
            cls._instance._active_provider = None
            cls._instance._initialized = False
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
            return
            
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
        
        logger.info(f"Initializing Speech Recognition with provider: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def get_provider(self) -> BaseRecognitionProvider:
        """
        Get the currently active recognition provider.
        
        Returns:
            BaseRecognitionProvider: The active provider instance.
            
        Raises:
            RuntimeError: If the provider manager hasn't been initialized.
        """
        if not self._initialized:
            self.initialize()
            
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
            Optional[str]: The transcribed text, or None if recognition failed.
        """
        provider = self.get_provider()
        return provider.listen(prints)

# Create a singleton instance
recognition_manager = RecognitionProviderManager()

# Convenience functions that use the active provider
def listen(prints: bool = False) -> Optional[str]:
    """
    Listen for speech using the active recognition provider.
    
    Args:
        prints (bool): Whether to print the transcribed text.
        
    Returns:
        Optional[str]: The transcribed text, or None if recognition failed.
    """
    return recognition_manager.listen(prints)
