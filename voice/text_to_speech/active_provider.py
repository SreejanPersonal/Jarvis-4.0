from typing import Optional, Dict
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

# Import all providers
from voice.text_to_speech.providers.deepgram import DeepgramTTSProvider
from voice.text_to_speech.providers.hearling import HearlingTTSProvider
from voice.text_to_speech.providers.speechify import SpeechifyTTSProvider
from voice.text_to_speech.providers.tiktok_tts import TikTokTTSProvider
from voice.text_to_speech.providers.edge_tts import EdgeTTSProvider

logger = get_logger(__name__)

class TTSProviderManager:
    """
    Manages the active Text-to-Speech provider.
    
    This class serves as a singleton that maintains the currently active
    TTS provider and allows switching between different providers.
    """
    
    # Available providers
    PROVIDERS = {
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
            cls._instance._active_provider = None
            cls._instance._initialized = False
        return cls._instance
    
    def initialize(self, provider_name: str = "deepgram", **kwargs) -> None:
        """
        Initialize the TTS provider manager with a default provider.
        
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
        
        logger.info(f"Initializing TTS with provider: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
        self._initialized = True
    
    def get_provider(self) -> BaseTTSProvider:
        """
        Get the currently active TTS provider.
        
        Returns:
            BaseTTSProvider: The active provider instance.
            
        Raises:
            RuntimeError: If the provider manager hasn't been initialized.
        """
        if not self._initialized:
            self.initialize()
            
        return self._active_provider
    
    def set_provider(self, provider_name: str, **kwargs) -> None:
        """
        Change the active TTS provider.
        
        Args:
            provider_name (str): Name of the provider to use.
            **kwargs: Additional arguments to pass to the provider.
            
        Raises:
            ValueError: If the provider name is invalid.
        """
        if provider_name not in self.PROVIDERS:
            available = ", ".join(self.PROVIDERS.keys())
            raise ValueError(f"Invalid provider '{provider_name}'. Available providers: {available}")
            
        logger.info(f"Switching TTS provider to: {provider_name}")
        self._active_provider = self.PROVIDERS[provider_name](**kwargs)
    
    def list_providers(self) -> Dict[str, str]:
        """
        Get a list of all available TTS providers.
        
        Returns:
            Dict[str, str]: Dictionary of provider names and their class names.
        """
        return {name: provider.__name__ for name, provider in self.PROVIDERS.items()}
    
    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech using the active provider.
        
        Args:
            text (str): The text to speak.
            voice (Optional[str]): The voice to use.
        """
        provider = self.get_provider()
        provider.speak(text, voice)
    
    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Generate speech using the active provider.
        
        Args:
            text (str): The text to convert to speech.
            voice (Optional[str]): The voice to use.
            output_path (Optional[str]): Path to save the audio file.
            
        Returns:
            str: Path to the generated audio file.
        """
        provider = self.get_provider()
        return provider.generate_speech(text, voice, output_path)

# Create a singleton instance
tts_manager = TTSProviderManager()

# Convenience functions that use the active provider
def speak(text: str, voice: Optional[str] = None) -> None:
    """
    Speak text using the active TTS provider.
    
    Args:
        text (str): The text to speak.
        voice (Optional[str]): The voice to use.
    """
    tts_manager.speak(text, voice)

def generate_speech(text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
    """
    Generate speech using the active TTS provider.
    
    Args:
        text (str): The text to convert to speech.
        voice (Optional[str]): The voice to use.
        output_path (Optional[str]): Path to save the audio file.
        
    Returns:
        str: Path to the generated audio file.
    """
    return tts_manager.generate_speech(text, voice, output_path)