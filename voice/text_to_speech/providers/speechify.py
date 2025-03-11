import os
import requests
import base64
from typing import Optional, Dict, Any

from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from utils.helpers import play_audio

logger = get_logger(__name__)

class SpeechifyTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider using Speechify's API.
    
    This provider offers various celebrity and character voices.
    """
    
    PROVIDER_NAME = "speechify"
    
    # Available voice models
    VOICE_MODELS = {
        "mrbeast": "mrbeast",
        "jamie": "jamie",
        "snoop": "snoop",
        "henry": "henry",
        "gwyneth": "gwyneth",
        "cliff": "cliff",
        "narrator": "narrator"
    }
    
    def __init__(self, default_voice: str = "mrbeast"):
        """
        Initialize the Speechify TTS provider.
        
        Args:
            default_voice (str): Default voice to use
        """
        super().__init__()
        self.api_url = "https://audio.api.speechify.com/generateAudioFiles"
        self.default_voice = default_voice
        self.temp_audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                           "../../../../data/cache/temp_audio.mp3")
        
        # Ensure cache directory exists
        os.makedirs(os.path.dirname(self.temp_audio_path), exist_ok=True)
        
        logger.info(f"Initialized Speechify TTS provider with default voice: {default_voice}")

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Generate speech using Speechify's API.
        
        Args:
            text (str): Text to convert to speech
            voice (Optional[str]): Voice model to use
            output_path (Optional[str]): Path to save audio file
            
        Returns:
            str: Path to generated audio file
        """
        voice_name = voice if voice in self.VOICE_MODELS else self.default_voice
        file_path = output_path if output_path else self.temp_audio_path
        
        # Clean up existing file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            logger.warning(f"Failed to remove existing audio file: {e}")
        
        # Prepare request
        payload = {
            "audioFormat": "mp3",
            "paragraphChunks": [text],
            "voiceParams": {
                "name": voice_name,
                "engine": "speechify",
                "languageCode": "en-US"
            }
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            
            # Save audio file
            audio_data = base64.b64decode(response.json()['audioStream'])
            with open(file_path, 'wb') as audio_file:
                audio_file.write(audio_data)
            
            return file_path
            
        except Exception as e:
            logger.error(f"Failed to generate speech with Speechify: {e}")
            raise

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text (str): Text to speak
            voice (Optional[str]): Voice to use
        """
        try:
            audio_path = self.generate_speech(text, voice)
            play_audio(audio_path)
            
            # Cleanup
            if os.path.exists(audio_path) and audio_path == self.temp_audio_path:
                os.remove(audio_path)
                
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get available voice models.
        
        Returns:
            Dict[str, Any]: Available voice models
        """
        return self.VOICE_MODELS