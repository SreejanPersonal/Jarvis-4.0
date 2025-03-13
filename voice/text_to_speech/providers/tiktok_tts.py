import os
import json
import base64
import requests
from typing import Optional, Dict, Any
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

logger = get_logger(__name__)

class TikTokTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider that aggregates two API endpoints.
    Internally it uses either the "Gesserit" or the "WeilByte" endpoints.
    
    Available voices (for both variants):
      • en_au_001
      • en_male_narration
      • en_male_funny
      • en_male_cody
      • en_female_emotional
      • en_us_rocket
      • en_female_f08_salut_damour

    To select the underlying API, provide variant="gesserit" or variant="weilbyte" when initializing.
    """
    PROVIDER_NAME = "tiktok"

    VOICE_OPTIONS = (
        "en_au_001",
        "en_male_narration",
        "en_male_funny",
        "en_male_cody",
        "en_female_emotional",
        "en_us_rocket",
        "en_female_f08_salut_damour",
    )

    API_ENDPOINTS = {
        "gesserit": "https://gesserit.co/api/tiktok-tts",
        "weilbyte": "https://tiktok-tts.weilnet.workers.dev/api/generation",
    }

    REQUEST_DATA_KEYS = {
        "gesserit": "base64",
        "weilbyte": "data",
    }

    def __init__(self, variant: str = "gesserit", default_voice: str = "en_us_rocket"):
        """
        Initialize the tiktok API TTS provider.
        
        Args:
            variant (str): Which underlying API variant to use ("gesserit" or "weilbyte").
            default_voice (str): The default voice to use.
        """
        super().__init__()
        if variant not in self.API_ENDPOINTS:
            raise ValueError("Invalid variant. Must be either 'gesserit' or 'weilbyte'.")
        self.variant = variant
        self.voice_options = self.VOICE_OPTIONS
        if default_voice not in self.voice_options:
            raise ValueError(f"Invalid default voice. Must be one of: {', '.join(self.voice_options)}")
        self.default_voice = default_voice
        self.api_endpoint = self.API_ENDPOINTS[variant]
        self.request_data_key = self.REQUEST_DATA_KEYS[variant]
        self.temp_audio_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../../../../data/cache/temp_audio.mp3"
        )
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        logger.info(f"Initialized tiktokAPITTSProvider using variant '{variant}' with default voice: {default_voice}")

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Convert text to speech using the selected API.
        
        Args:
            text (str): Text to synthesize.
            voice (Optional[str]): Voice to use; if not provided or invalid, uses the default.
            output_path (Optional[str]): Where to save the generated audio.
            
        Returns:
            str: Path to the generated audio file.
        """
        # Use default voice if none provided or if the voice is not valid.
        voice = voice if (voice and voice in self.voice_options) else self.default_voice
        file_path = output_path if output_path else self.temp_audio_path

        # Clean up an existing file if needed.
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                logger.warning(f"Couldn't remove existing temporary file: {e}")

        headers = {"Content-Type": "application/json"}
        payload = {"text": text, "voice": voice}

        try:
            response = requests.post(self.api_endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Request to {self.api_endpoint} failed: {e}")
            raise

        try:
            audio_data = base64.b64decode(response.json()[self.request_data_key])
            with open(file_path, "wb") as f:
                f.write(audio_data)
        except Exception as e:
            logger.error(f"Error saving audio data: {e}")
            raise

        return file_path

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it immediately.
        
        Args:
            text (str): Text to speak.
            voice (Optional[str]): Voice to be used.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            # Using our centralized play_audio helper.
            from utils.helpers import play_audio
            play_audio(audio_path)
            # Clean up the temp file
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
        except Exception as e:
            logger.error(f"Failed to speak text in tiktokAPITTSProvider: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get a dictionary of available voices.
        
        Returns:
            dict: Mapping of voice IDs to voice names.
        """
        return {voice: voice for voice in self.voice_options}