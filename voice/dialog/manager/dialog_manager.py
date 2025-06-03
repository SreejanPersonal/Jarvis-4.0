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
