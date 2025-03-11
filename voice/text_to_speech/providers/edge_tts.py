import os
from playsound import playsound
from core.logger import get_logger
from voice.text_to_speech.base import BaseTTSProvider
from typing import Optional, Dict, Any

logger = get_logger(__name__)

class EdgeTTSProvider(BaseTTSProvider):
    """
    Text-to-Speech provider that uses the Edge TTS command-line tool.
    
    This provider runs the edge-tts system command with the appropriate parameters.
    Available voices include (but are not limited to):
      • en-US-JennyNeural
      • en-SG-LunaNeural
      • en-AU-NatashaNeural
      • en-CA-ClaraNeural
      • en-CA-LiamNeural
    """
    PROVIDER_NAME = "edge_tts"

    VOICE_OPTIONS = {
        "en-US-JennyNeural": "en-US-JennyNeural",
        "en-SG-LunaNeural": "en-SG-LunaNeural",
        "en-AU-NatashaNeural": "en-AU-NatashaNeural",
        "en-CA-ClaraNeural": "en-CA-ClaraNeural",
        "en-CA-LiamNeural": "en-CA-LiamNeural",
    }

    def __init__(self, default_voice: str = "en-CA-LiamNeural", subtitle_file: str = "ASSETS/Subtitles_File.srt"):
        """
        Initialize the EdgeTTSProvider.
        
        Args:
            default_voice (str): The default voice to use.
            subtitle_file (str): File to output subtitles.
        """
        super().__init__()
        if default_voice not in self.VOICE_OPTIONS:
            logger.warning(f"Default voice '{default_voice}' not available; reverting to 'en-CA-LiamNeural'.")
            default_voice = "en-CA-LiamNeural"
        self.default_voice = default_voice
        self.subtitle_file = subtitle_file
        # Build a temporary output path inside data/cache for consistency.
        self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../data/cache")
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_speech(self, text: str, voice: Optional[str] = None, output_path: Optional[str] = None) -> str:
        """
        Generate speech using the edge-tts command.
        
        Args:
            text (str): The text to synthesize.
            voice (Optional[str]): The voice to use.
            output_path (Optional[str]): The file path to save the generated audio.
            
        Returns:
            str: The path to the generated audio file.
        """
        voice = voice if (voice and voice in self.VOICE_OPTIONS) else self.default_voice
        output_file = (output_path if output_path else 
                       os.path.join(self.output_dir, f"{voice}.mp3"))
        # Build the command string (make sure to maintain the same order of parameters).
        command = (
            f"edge-tts --voice \"{voice}\" --text \"{text}\" "
            f"--write-media \"{output_file}\" --write-subtitles {self.subtitle_file}"
        )
        logger.debug(f"Executing command: {command}")
        os.system(command)
        return output_file

    def speak(self, text: str, voice: Optional[str] = None) -> None:
        """
        Generate and immediately play synthesized speech.
        
        Args:
            text (str): The text to speak.
            voice (Optional[str]): The voice to use.
        """
        try:
            audio_path = self.generate_speech(text, voice)
            from utils.helpers import play_audio
            play_audio(audio_path)
            # Cleanup: remove the generated subtitle file and audio.
            if os.path.exists(self.subtitle_file):
                os.remove(self.subtitle_file)
            if os.path.exists(audio_path):
                os.remove(audio_path)
        except Exception as e:
            logger.error(f"Failed in EdgeTTSProvider speak: {e}")

    def list_available_voices(self) -> Dict[str, Any]:
        """
        Get a dictionary of available voices.
        
        Returns:
            dict: Mapping of available voice names.
        """
        return self.VOICE_OPTIONS