import asyncio
from core.logger import get_logger

logger = get_logger(__name__)

class ResourceManager:
    def __init__(self):
        pass
        
    async def close_resources(self, pya):
        if pya:
            try:
                pya.terminate()
                logger.info("GeminiLiveSession PyAudio instance terminated.")
            except Exception as e:
                logger.error(f"Error terminating PyAudio in GeminiLiveSession: {e}", exc_info=True)
            finally:
                pya = None
        logger.info("GeminiLiveSession resources closed.")
