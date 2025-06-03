import pvporcupine
import pyaudio
import struct

access_key = "NCfIRXMaIPkBpxb+x+VLvd0p8ppkxIoiFC7YoTNKHJDTxP4C/uSOaQ=="

porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])

pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

try:
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)
        if result >= 0:
            print("Detected jarvis")
            break
finally:
    audio_stream.stop_stream()
    audio_stream.close()
    pa.terminate()
    porcupine.delete()