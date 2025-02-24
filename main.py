from llmprocessor import execute_device_command, query_llm
from tts_py import command_feedback, speak
from stt_whisper import listen_for_command
from device_agent import execute_command
from wake_word import listen_for_wake_word

import torch

from realtime_stt import realtime_transcribe

if __name__ == "__main__":
    print("Starting Jarvis Assistant... 🚀")
    
    # Loop to keep the assistant running
    while True:
        # torch.cuda.empty_cache()

        # wait for wake word command and start listening
        if True:
        # if listen_for_wake_word():
            # speak("System Initiating, yes master how can i help you today")
            command = realtime_transcribe()
            print("Command: ", command)

            #command to llm
            if command:
                if command == "exit" or command == "Exit":
                    print("Exiting assistant...")
                    speak("Exiting assistant...")
                    break
                else:
                    print("Starting assistant")

                    # Pass input to llmprocessor

                    response = query_llm(command)
                    print(f"LLM Response: {response}")
                    # speak(response)

                    # # Send command to device agent
                    # execution_result = execute_device_command(response)
                    # print(f"Device Agent Execution: {execution_result}")
                    # speak(execution_result)
                    # # Wait for the next command
                    # print("\033[92mWaiting for the next command... 🎤\033[0m\n")
            else:
                print("\033[92mWaiting for input from user... 🎤\033[0m")
                
        else:
            print("Listening for wake word...")
            continue
        
