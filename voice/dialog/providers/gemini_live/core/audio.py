import asyncio
import pyaudio
from core.logger import get_logger

FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

logger = get_logger(__name__)

class AudioHandler:
    def __init__(self, pya=None):
        self.pya = pya
        self.audio_stream = None
        
    async def listen_audio(self, out_queue):
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot listen to audio.")
            return

        try:
            mic_info = self.pya.get_default_input_device_info()
            self.audio_stream = await asyncio.to_thread(
                self.pya.open,
                format=FORMAT,
                channels=CHANNELS,
                rate=SEND_SAMPLE_RATE,
                input=True,
                input_device_index=mic_info["index"],
                frames_per_buffer=CHUNK_SIZE,
            )
        except Exception as e:
            logger.error(f"Failed to open audio stream for listening: {e}", exc_info=True)
            return

        logger.info(f"Listen audio task started.")
        try:
            while True:
                read_kwargs = {}
                if __debug__:
                    read_kwargs["exception_on_overflow"] = False
                
                data = await asyncio.to_thread(self.audio_stream.read, CHUNK_SIZE, **read_kwargs)
                await out_queue.put({"data": data, "mime_type": "audio/pcm"})
        except asyncio.CancelledError:
            logger.info("Listen audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in listen_audio: {e}", exc_info=True)
        finally:
            if self.audio_stream and self.audio_stream.is_active():
                try:
                    self.audio_stream.stop_stream()
                    self.audio_stream.close()
                except Exception as e_close:
                    logger.error(f"Error closing listen_audio stream: {e_close}")
            self.audio_stream = None
            logger.info("Listen audio task finished.")

    async def receive_audio(self, session, audio_in_queue):
        logger.info("Receive audio task started.")
        try:
            while True:
                if not session:
                    logger.warning("Session not active in receive_audio. Waiting.")
                    await asyncio.sleep(0.1)
                    continue
                
                turn = session.receive()
                async for response in turn:
                    if data := response.data:
                        audio_in_queue.put_nowait(data)
                        continue
                    if text := response.text:
                        print(text, end="", flush=True)
        except asyncio.CancelledError:
            logger.info("Receive audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in receive_audio: {e}", exc_info=True)
        finally:
            logger.info("Receive audio task finished.")

    async def play_audio(self, audio_in_queue):
        if not self.pya:
            logger.error("PyAudio not initialized. Cannot play audio.")
            return

        stream = None
        try:
            stream = await asyncio.to_thread(
                self.pya.open,
                format=FORMAT,
                channels=CHANNELS,
                rate=RECEIVE_SAMPLE_RATE,
                output=True,
            )
        except Exception as e:
            logger.error(f"Failed to open audio stream for playing: {e}", exc_info=True)
            return

        logger.info("Play audio task started.")
        try:
            while True:
                bytestream = await audio_in_queue.get()
                await asyncio.to_thread(stream.write, bytestream)
                audio_in_queue.task_done()
        except asyncio.CancelledError:
            logger.info("Play audio task cancelled.")
        except Exception as e:
            logger.error(f"Error in play_audio: {e}", exc_info=True)
        finally:
            if stream and stream.is_active():
                try:
                    stream.stop_stream()
                    stream.close()
                except Exception as e_close:
                    logger.error(f"Error closing play_audio stream: {e_close}")
            logger.info("Play audio task finished.")
            
    async def close_audio_resources(self):
        if self.audio_stream:
            try:
                if self.audio_stream.is_active():
                    self.audio_stream.stop_stream()
                self.audio_stream.close()
                logger.info("GeminiLiveSession microphone audio_stream closed.")
            except Exception as e:
                logger.error(f"Error closing microphone audio_stream in GeminiLiveSession: {e}", exc_info=True)
            finally:
                self.audio_stream = None
