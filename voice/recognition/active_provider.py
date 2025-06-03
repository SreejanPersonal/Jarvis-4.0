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