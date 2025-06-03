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