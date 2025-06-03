import asyncio
from core.logger import get_logger

logger = get_logger(__name__)

class CommunicationHandler:
    def __init__(self):
        pass
        
    async def send_realtime(self, out_queue, session):
        logger.info("Send realtime (audio/video) task started.")
        try:
            while True:
                msg = await out_queue.get()
                if session:
                    await session.send(input=msg)
                else:
                    logger.warning("Session not active in send_realtime, cannot send message. Waiting.")
                    await asyncio.sleep(0.1) 
        except asyncio.CancelledError:
            logger.info("Send realtime task cancelled.")
        except Exception as e:
            logger.error(f"Error in send_realtime: {e}", exc_info=True)
        finally:
            logger.info("Send realtime task finished.")
