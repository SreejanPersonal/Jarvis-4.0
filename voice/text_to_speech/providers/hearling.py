import aiohttp
import asyncio
import aiofiles
import os
import random
import threading
from typing import Optional, List

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from utils.helpers import play_audio

logger = get_logger(__name__)


class HearlingTTSProvider(BaseTTSProvider):
    PROVIDER_NAME = "hearling"

    # New voice list for Hearling
    AVAILABLE_VOICES: List[str] = [
        'hi-IN-Standard-A', 'hi-IN-Standard-B', 'hi-IN-Standard-C',
        'hi-IN-Standard-D', 'hi-IN-Standard-E', 'hi-IN-Standard-F',
        'hi-IN-Wavenet-A', 'hi-IN-Wavenet-B', 'hi-IN-Wavenet-C',
        'hi-IN-Wavenet-D', 'hi-IN-Wavenet-E', 'hi-IN-Wavenet-F'
    ]

    def __init__(self, email_prefix: str = "devsdocode", max_pool_size: int = 5):
        super().__init__()
        self.email_prefix = email_prefix
        self.url_accounts = "https://api.hearling.com/accounts"
        self.url_clips = "https://api.hearling.com/clips"
        self.token_pool = []
        self.max_pool_size = max_pool_size
        self.is_closing = False

        # Create a temporary audio file path under data/cache
        self.temp_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../../../../data/cache/temp_audio.mp3"
        )
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)

        # Create a new event loop running in its own thread.
        self.loop = asyncio.new_event_loop()
        self.loop_thread = threading.Thread(target=self._run_loop, args=(self.loop,), daemon=True)
        self.loop_thread.start()
        # Ensure the provider is initialized
        future = asyncio.run_coroutine_threadsafe(self.initialize(), self.loop)
        try:
            future.result()  # Block until initialization completes.
        except Exception as e:
            logger.error(f"Initialization error in Hearling provider: {e}")
        logger.info("Initialized Hearling TTS provider")

    def _run_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        """Utility function: run the provided loop forever in a dedicated thread."""
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def initialize(self) -> None:
        """Initialize the async session and prefill the token pool."""
        self.session = aiohttp.ClientSession()
        await self.refill_token_pool()

    async def cleanup(self) -> None:
        """Cleanup asynchronous resources and stop the dedicated event loop."""
        self.is_closing = True
        if self.session and not self.session.closed:
            await self.session.close()
        # Stop the loop and wait for the thread to finish.
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.loop_thread.join()

    async def refill_token_pool(self) -> None:
        """Asynchronously prefill the token pool with account tokens."""
        if self.is_closing:
            return
        try:
            while len(self.token_pool) < self.max_pool_size:
                if self.is_closing:
                    break
                token = await self.create_account()
                if token:
                    self.token_pool.append(token)
        except Exception as e:
            logger.error(f"Token pool refill error: {e}")

    async def create_account(self) -> Optional[str]:
        """Create a new account to retrieve a token."""
        if self.session is None or self.session.closed:
            return None
        email = f"{self.email_prefix}{random.randint(10000, 99999)}@gmail.com"
        payload = {"email": email, "password": "DevsDoCode"}
        async with self.session.post(self.url_accounts, json=payload) as response:
            response.raise_for_status()
            data = await response.json()
            return data.get('token')

    async def get_token(self) -> Optional[str]:
        """
        Retrieve a token from the pool. If the pool is empty,
        refill it and then get a token.
        """
        if not self.token_pool:
            await self.refill_token_pool()
        return self.token_pool.pop() if self.token_pool else None

    async def download_audio(self, url: str, filename: str) -> None:
        """Download an audio file from the URL asynchronously."""
        async with self.session.get(url) as response:
            async with aiofiles.open(filename, 'wb') as f:
                await f.write(await response.read())

    async def _async_generate_speech(self, text: str, voice: Optional[str], output_path: str) -> None:
        """The asynchronous implementation of speech generation via Hearling API."""
        try:
            token = await self.get_token()
            if not token:
                raise Exception("Failed to get token")
            headers = {"Authorization": f"Bearer {token}"}

            # Choose the provided voice if valid; otherwise, use the first voice.
            selected_voice = voice if (voice in self.AVAILABLE_VOICES) else self.AVAILABLE_VOICES[0]
            payload = {"text": text, "voice": selected_voice}

            async with self.session.post(self.url_clips, headers=headers, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                audio_url = data['clip']['location']

            await self.download_audio(audio_url, output_path)

            # Refill token pool asynchronously.
            if not self.is_closing:
                asyncio.run_coroutine_threadsafe(self.refill_token_pool(), self.loop)
        except Exception as e:
            logger.error(f"Error generating speech: {e}")
            raise

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        A synchronous wrapper that triggers asynchronous speech generation.
        Returns the path to the generated audio file.
        """
        file_path = output_path if output_path else self.temp_audio_path
        future = asyncio.run_coroutine_threadsafe(
            self._async_generate_speech(text, voice, file_path), self.loop
        )
        try:
            future.result()  # Block until the coroutine completes.
        except Exception as e:
            logger.error(f"Error in generate_speech: {e}")
            raise
        return file_path

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play the generated audio.
        After playback, cleans up the temporary audio file.
        
        This method handles the async operations internally, providing a 
        synchronous interface to match other providers.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            play_audio(audio_path)
            # Don't remove the file here as play_audio now handles cleanup
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")

    def list_available_voices(self) -> List[str]:
        """Return the list of available voices."""
        return self.AVAILABLE_VOICES

    def __del__(self):
        """
        Attempt to clean up async resources when the object is deleted.
        Note that errors during __del__ are logged.
        """
        try:
            if hasattr(self, 'loop') and self.loop.is_running():
                asyncio.run_coroutine_threadsafe(self.cleanup(), self.loop).result()
        except Exception as e:
            logger.error(f"Error during cleanup in __del__: {e}")
