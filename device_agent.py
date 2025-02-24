import subprocess
import webbrowser
import pyautogui
import time

def open_chrome():
    """Opens Google Chrome"""
    try:
        subprocess.run(["google-chrome"], check=True)  # Linux
    except FileNotFoundError:
        try:
            subprocess.run(["chrome"], check=True)  # Windows
        except FileNotFoundError:
            print("Chrome not found!")

def open_youtube():
    """Opens YouTube in the default browser"""
    webbrowser.open("https://www.youtube.com")

def play_song(song_name):
    """Searches for a song on YouTube"""
    search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    webbrowser.open(search_url)

def open_app(app_name):
    """Opens an application based on the OS"""
    try:
        subprocess.run([app_name], check=True)
    except FileNotFoundError:
        print(f"Application '{app_name}' not found!")

def execute_command(command):
    """Processes text commands and calls appropriate functions"""
    command = command.lower()
    
    if "open chrome" in command:
        open_chrome()
        return 1
    elif "open youtube" in command:
        open_youtube()
        return 1
    elif "play song" in command:
        song_name = command.replace("play song", "").strip()
        play_song(song_name)
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_app(app_name)
    else:
        return 0

# Simulating input from LLM
if __name__ == "__main__":
    while True:
        command = input("Enter command: ")  # Simulating LLM output
        if command.lower() == "exit":
            break
        execute_command(command)
