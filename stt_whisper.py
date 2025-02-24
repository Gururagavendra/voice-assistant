import whisper
import pyaudio
import wave
import numpy as np
import os
import time
import tempfile

# Load Whisper model
model = whisper.load_model("small")  # Use "small" or "medium" for better accuracy

# Initialize pyaudio for real-time recording
p = pyaudio.PyAudio()
RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1

# # Directory to store temporary files
# TEMP_DIR = "tmp"

filename="audio.wav"

def transcribe_audio(filename):
    """Converts recorded audio to text using Whisper"""
    # print("Transcribing audio...")
    # print( model.transcribe(filename))
    result = model.transcribe(filename)
    return result["text"]

def remove_audio_file(filename):
    """Removes the specified audio file"""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")



def listen():
    """Records audio after wake word detection and transcribes it."""
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    print("Listening for command...")
    frames = []
    silent_threshold = 2  # seconds of silence before stopping

    last_speech_time = time.time()

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Check for silence (if no speech for a threshold time)
        if np.abs(audio_data).mean() < 100:  # Silence threshold
            if time.time() - last_speech_time > silent_threshold:
                print("No more speech detected.")
                break
        else:
            last_speech_time = time.time()

    print("Finished recording.")
    stream.stop_stream()
    stream.close()

    # Save the audio
    audio_filename = "audio.wav"
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return audio_filename

def listen_for_command():
   
    # Start recording and transcribing command after wake word
    audio_filename = listen()
    command = transcribe_audio(audio_filename)   

    remove_audio_file(filename)  # Remove any existing audio file

    if command:
        print("You said:", command)
        return command
    else:
        print("No command detected.")
        return None
    
### individual module testing ###
if __name__ == "__main__":
    print("Speak a command after 'Hey Jarvis'...")
    text = listen_for_command()
    print("Recognized:", text)
