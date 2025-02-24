import pvporcupine
import pyaudio
import struct

# Replace with your Access Key
ACCESS_KEY = "JxkYTGfA5SlDn6RDOKwlRFoXc7DjkOalJFbjsNz11fwIQv9Cu0DMWw=="

# Choose a built-in wake word or a custom `.ppn` model
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keywords=['bumblebee']
)

# Setup PyAudio
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("Listening for the wake word...")

def listen_for_wake_word():
    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                return 1

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()

# listen_for_wake_word()
