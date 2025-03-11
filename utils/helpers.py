import os
from playsound import playsound
from core.logger import get_logger

logger = get_logger(__name__)

def play_audio(file_path: str) -> None:
    """
    Play an audio file.
    
    Args:
        file_path (str): Path to the audio file to play.
        
    Raises:
        FileNotFoundError: If the audio file doesn't exist.
        Exception: If there's an error playing the audio.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    try:
        playsound(file_path)
    except Exception as e:
        logger.error(f"Error playing audio: {e}")
        raise Exception(f"Failed to play audio: {e}")