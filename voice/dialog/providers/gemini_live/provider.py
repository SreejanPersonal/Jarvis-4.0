import asyncio
from core.config import AppConfig
from core.logger import get_logger
from voice.dialog.base import BaseDialogProvider
from .session_handler import GeminiLiveSession
from .client_config import get_gemini_client, get_live_connect_config

logger = get_logger(__name__)

class GeminiLiveProvider(BaseDialogProvider):
    PROVIDER_NAME = "gemini_live"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("Initializing GeminiLiveProvider...")
        
        self.api_key = AppConfig.GEMINI_API_KEY
        self.model_name = AppConfig.GEMINI_LIVE_MODEL_NAME
        self.system_instruction = AppConfig.GEMINI_LIVE_SYSTEM_INSTRUCTION
        self.video_mode = AppConfig.GEMINI_LIVE_VIDEO_MODE

        if not self.api_key:
            msg = "GEMINI_API_KEY is not set in AppConfig. GeminiLiveProvider cannot be initialized."
            logger.error(msg)
            raise ValueError(msg)
        
        if not self.model_name:
            msg = "GEMINI_LIVE_MODEL_NAME is not set or empty in AppConfig. Cannot initialize GeminiLiveProvider."
            logger.error(msg)
            raise ValueError(msg)

        try:
            self.client = get_gemini_client(self.api_key)
            self.connect_config = get_live_connect_config(self.system_instruction)
            
            self.session_handler = GeminiLiveSession(
                client=self.client,
                connect_config=self.connect_config,
                model_name=self.model_name,
                video_mode=self.video_mode
            )
            logger.info("GeminiLiveProvider initialized successfully with session handler.")
        except Exception as e:
            logger.error(f"Error during GeminiLiveProvider initialization: {e}", exc_info=True)
            raise

    async def run_session(self) -> None:
        logger.info(f"Starting Gemini Live session with provider: {self.PROVIDER_NAME}")
        try:
            await self.session_handler.run()
        except asyncio.CancelledError:
            logger.info(f"Gemini Live session (provider {self.PROVIDER_NAME}) was cancelled.")
        except Exception as e:
            logger.error(f"Error during Gemini Live session (provider {self.PROVIDER_NAME}): {e}", exc_info=True)
            raise
        finally:
            logger.info(f"Gemini Live session (provider {self.PROVIDER_NAME}) finished or was interrupted.")
            # Ensure session_handler's resources are cleaned up if its run() didn't complete finally block.
            # session_handler.run() already has a comprehensive finally block.
            # Calling close_resources again here might be redundant but safe if designed idempotently.
            if hasattr(self.session_handler, 'close_resources') and self.session_handler.pya is not None:
                 logger.debug("Provider ensuring session_handler resources are closed from its own finally block.")
                 await self.session_handler.close_resources()