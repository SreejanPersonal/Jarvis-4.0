from abc import ABC, abstractmethod
from typing import Optional

class BaseDialogProvider(ABC):
    PROVIDER_NAME = "base_dialog"

    def __init__(self, **kwargs):
        """
        Initialize the base dialog provider.
        kwargs can be used for provider-specific configurations passed from the manager.
        """
        pass

    @abstractmethod
    async def run_session(self) -> None:
        """
        Start and manage the interactive dialog session.
        This method should handle the entire lifecycle of the conversation,
        including audio input/output and interaction with the dialog model.
        """
        pass

    def get_provider_name(self) -> str:
        """
        Get the name of this dialog provider.
        
        Returns:
            str: Provider name.
        """
        return self.PROVIDER_NAME