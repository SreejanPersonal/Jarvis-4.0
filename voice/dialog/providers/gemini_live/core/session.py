import asyncio
import pyaudio
from core.logger import get_logger
from .audio import AudioHandler
from .video import VideoHandler
from .communication import CommunicationHandler
from .resources import ResourceManager

logger = get_logger(__name__)

class GeminiLiveSession:
    def __init__(self, client, connect_config, model_name: str, video_mode: str = "none"):
        self.client = client
        self.connect_config = connect_config
        self.model_name = model_name
        self.video_mode = video_mode

        self.audio_in_queue = None
        self.out_queue = None
        self.session = None
        self.other_tasks_list = []
        
        try:
            self.pya = pyaudio.PyAudio()
            logger.info("PyAudio instance created for GeminiLiveSession.")
        except Exception as e:
            logger.error(f"Failed to initialize PyAudio in GeminiLiveSession: {e}")
            self.pya = None
            raise
            
        self.audio_handler = AudioHandler(self.pya)
        self.video_handler = VideoHandler()
        self.comm_handler = CommunicationHandler()
        self.resource_manager = ResourceManager()

    async def run(self):
        logger.info(f"GeminiLiveSession run started with video_mode: {self.video_mode}")
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot run GeminiLiveSession.")
            return
            
        self.other_tasks_list = []
        try:
            async with self.client.aio.live.connect(model=self.model_name, config=self.connect_config) as session:
                self.session = session
                logger.info(f"Gemini Live session connected.")
                
                self.audio_in_queue = asyncio.Queue()
                self.out_queue = asyncio.Queue(maxsize=5)
                
                self.other_tasks_list.append(asyncio.create_task(
                    self.comm_handler.send_realtime(self.out_queue, self.session), 
                    name="GeminiSendRealtime"))
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.listen_audio(self.out_queue), 
                    name="GeminiListenAudio"))
                
                if self.video_mode == "camera":
                    self.other_tasks_list.append(asyncio.create_task(
                        self.video_handler.get_frames(self.out_queue, self.video_mode), 
                        name="GeminiGetFrames"))
                elif self.video_mode == "screen":
                    self.other_tasks_list.append(asyncio.create_task(
                        self.video_handler.get_screen(self.out_queue, self.video_mode), 
                        name="GeminiGetScreen"))
                
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.receive_audio(self.session, self.audio_in_queue), 
                    name="GeminiReceiveAudio"))
                self.other_tasks_list.append(asyncio.create_task(
                    self.audio_handler.play_audio(self.audio_in_queue), 
                    name="GeminiPlayAudio"))
                
                if self.other_tasks_list:
                    await asyncio.gather(*self.other_tasks_list, return_exceptions=True)
                else:
                    logger.warning("No tasks were created in GeminiLiveSession run method.")

                logger.info("GeminiLiveSession: asyncio.gather completed for tasks.")

        except asyncio.CancelledError:
            logger.info("GeminiLiveSession run method was cancelled.")
        except Exception as e:
            logger.error(f"Exception in GeminiLiveSession run's main block: {e}", exc_info=True)
        finally:
            logger.info("GeminiLiveSession run method entering finally block for cleanup.")
            
            active_tasks_to_cancel = [t for t in self.other_tasks_list if t and not t.done()]
            if active_tasks_to_cancel:
                logger.info(f"Cancelling {len(active_tasks_to_cancel)} active tasks...")
                for task in active_tasks_to_cancel:
                    task.cancel()
                await asyncio.gather(*active_tasks_to_cancel, return_exceptions=True)
                logger.info("Finished cancelling tasks.")
            else:
                logger.info("No active tasks to cancel in finally block, or tasks already completed.")

            await self.close_resources()
            logger.info("GeminiLiveSession run method finished cleanup in finally block.")

    async def close_resources(self):
        logger.info("GeminiLiveSession closing resources...")
        await self.audio_handler.close_audio_resources()
        await self.resource_manager.close_resources(self.pya)
        self.pya = None
        logger.info("GeminiLiveSession resources closed.")

    def __del__(self):
        if self.pya:
            logger.warning("GeminiLiveSession __del__ called. Attempting to terminate PyAudio if not already done.")
            try:
                self.pya.terminate()
            except Exception:
                pass
