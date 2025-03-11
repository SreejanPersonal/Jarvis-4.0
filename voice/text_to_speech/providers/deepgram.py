import os
import base64
import requests
from typing import Optional

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider

logger = get_logger(__name__)

class DeepgramTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider using Deepgram's API.
    
    This provider allows converting text to natural-sounding speech using
    Deepgram's various voice models.
    """
    
    PROVIDER_NAME = "deepgram"
    
    # Available voice models
    VOICE_MODELS = {
        "aura_asteria": "aura-asteria-en",
        "aura_arcas": "aura-arcas-en",
        "aura_luna": "aura-luna-en", 
        "aura_zeus": "aura-zeus-en"
    }
    
    def __init__(self, default_voice: str = "aura_arcas"):
        """
        Initialize the Deepgram TTS provider.
        
        Args:
            default_voice (str): The default voice model to use.
                                 Must be one of the keys in VOICE_MODELS.
        """
        super().__init__()
        self.api_url = "https://deepgram.com/api/ttsAudioGeneration"
        
        if default_voice not in self.VOICE_MODELS:
            logger.warning(f"Invalid voice model '{default_voice}'. Using default 'aura_arcas' instead.")
            default_voice = "aura_arcas"
            
        self.default_voice = default_voice
        self.temp_audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                           "../../../../data/cache/temp_audio.mp3")
        
        # Ensure cache directory exists
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        
        logger.info(f"Initialized Deepgram TTS provider with default voice: {self.VOICE_MODELS[default_voice]}")
    
    def _get_headers(self) -> dict:
        """
        Generate the headers required for the Deepgram API request.
        
        Returns:
            dict: Headers for the API request.
        """
        return {
            "authority": "deepgram.com",
            "method": "POST",
            "path": "/api/ttsAudioGeneration",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://deepgram.com",
            "referer": "https://deepgram.com/",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "dnt": "1"
        }
    
    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Convert text to speech using Deepgram's API.
        
        Args:
            text (str): The text to convert to speech.
            voice (str, optional): Voice model to use (one of the keys in VOICE_MODELS).
                                  If None, uses the default voice.
            output_path (str, optional): Path to save the audio file.
                                        If None, uses a temporary file.
        
        Returns:
            str: Path to the generated audio file.
            
        Raises:
            Exception: If the API request fails.
        """
        # Use default voice if none specified
        voice_key = voice if voice in self.VOICE_MODELS else self.default_voice
        voice_model = self.VOICE_MODELS[voice_key]
        
        # Determine output file path
        file_path = output_path if output_path else self.temp_audio_path
        
        # Clean up any existing file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logger.warning(f"Failed to remove existing audio file: {e}")
        
        # Prepare the request
        headers = self._get_headers()
        payload = {"text": text, "model": voice_model}
        
        try:
            logger.debug(f"Sending request to Deepgram TTS API with voice model: {voice_model}")
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            # Save the audio file
            with open(file_path, 'wb') as audio_file:
                audio_file.write(base64.b64decode(response.json()['data']))
            
            logger.debug(f"Successfully generated speech, saved to: {file_path}")
            return file_path
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to generate speech with Deepgram: {e}")
            raise Exception(f"Deepgram TTS API request failed: {e}")
    
    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text (str): The text to speak.
            voice (str, optional): Voice model to use.
                                  If None, uses the default voice.
        """
        try:
            # Generate speech
            audio_path = self.generate_speech(text, voice)
            
            # Import here to avoid circular imports
            from utils.helpers import play_audio
            
            # Play the audio
            logger.debug(f"Playing audio: {audio_path}")
            play_audio(audio_path)
            
            # Clean up the temporary file
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
                
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")
            
    def list_available_voices(self) -> dict:
        """
        Return a dictionary of available voice models.
        
        Returns:
            dict: Available voice models.
        """
        return self.VOICE_MODELS
