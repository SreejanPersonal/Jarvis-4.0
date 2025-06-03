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
