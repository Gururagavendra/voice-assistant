from gtts import gTTS
import os
import subprocess

def speak(text):
    """Converts text to speech and plays it."""
    if not text:
        print("No text provided for speech.")
        return
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
       # Ensure playback completes before continuing
    subprocess.run(["mpg321", "speech.mp3"], check=True)
    cleanup()

# Sample usage
def command_feedback(command_success):
    if command_success:
        speak("Command executed successfully.")
    else:
        speak("I did not understand the command. Could you please clarify? Or this functionality may not be available yet.")
    cleanup()
    
def cleanup():
    """Deletes the speech file after it has been played."""
    os.remove("speech.mp3")
    print("Speech file deleted.")


# speak("Hello, I am Jarvis. How can I help")