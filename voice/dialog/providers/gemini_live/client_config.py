import pyaudio
from google import genai
from google.genai import types
from core.logger import get_logger

logger = get_logger(__name__)

FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024


def get_gemini_client(api_key: str):
    """Initializes and returns a Gemini API client."""
    if not api_key:
        msg = "GEMINI_API_KEY is not provided for Gemini client initialization."
        logger.error(msg)
        raise ValueError(msg)
    
    return genai.Client(
        http_options={"api_version": "v1beta"},
        api_key=api_key,
    )

def get_live_connect_config(system_instruction_text: str) -> types.LiveConnectConfig:
    """Constructs and returns the LiveConnectConfig for Gemini."""
    
    if not system_instruction_text:
        logger.warning("No system instruction provided for Gemini Live session. Using a generic default.")
        system_instruction_text = "You are a helpful AI assistant."

    return types.LiveConnectConfig(
        response_modalities=[
            "AUDIO",
        ],
        media_resolution="MEDIA_RESOLUTION_MEDIUM",
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Zephyr")
            )
        ),
        context_window_compression=types.ContextWindowCompressionConfig(
            trigger_tokens=25600,
            sliding_window=types.SlidingWindow(target_tokens=12800),
        ),
        system_instruction=types.Content(
            parts=[types.Part.from_text(text=system_instruction_text)],
            role="user"
        ),
        # session_resumption=types.SessionResumptionConfig(
        #     handle="HANDLE HERE"
        # )
    )