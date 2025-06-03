import asyncio
import base64
import io
import cv2
import PIL.Image
import mss
from core.logger import get_logger

logger = get_logger(__name__)

class VideoHandler:
    def __init__(self):
        pass
        
    def _get_frame(self, cap):
        ret, frame = cap.read()
        if not ret:
            return None
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(frame_rgb)
        img.thumbnail([1024, 1024])

        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)

        mime_type = "image/jpeg"
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_frames(self, out_queue, video_mode):
        if not video_mode == "camera":
            logger.debug("Camera mode not active, get_frames will not run.")
            return

        cap = await asyncio.to_thread(cv2.VideoCapture, 0)
        if not cap.isOpened():
            logger.error("Failed to open camera for get_frames.")
            return

        logger.info("Camera frames task started.")
        try:
            while True:
                frame = await asyncio.to_thread(self._get_frame, cap)
                if frame is None:
                    logger.info("No frame from camera, exiting get_frames loop.")
                    break
                await asyncio.sleep(1.0)
                await out_queue.put(frame)
        except asyncio.CancelledError:
            logger.info("get_frames task cancelled.")
        finally:
            if cap.isOpened():
                cap.release()
            logger.info("Camera frames task finished.")

    def _get_screen(self):
        sct = mss.mss()
        monitor = sct.monitors[0]
        i = sct.grab(monitor)
        mime_type = "image/jpeg"
        png_bytes = mss.tools.to_png(i.rgb, i.size)
        img = PIL.Image.open(io.BytesIO(png_bytes))
        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)
        jpeg_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(jpeg_bytes).decode()}

    async def get_screen(self, out_queue, video_mode):
        if not video_mode == "screen":
            logger.debug("Screen mode not active, get_screen will not run.")
            return

        logger.info("Screen capture task started.")
        try:
            while True:
                frame = await asyncio.to_thread(self._get_screen)
                if frame is None:
                    logger.warning("No frame from screen capture, exiting get_screen loop.")
                    break
                await asyncio.sleep(1.0)
                await out_queue.put(frame)
        except asyncio.CancelledError:
            logger.info("get_screen task cancelled.")
        finally:
            logger.info("Screen capture task finished.")
