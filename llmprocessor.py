from dotenv import load_dotenv
load_dotenv()  # Take environment variables from .env file
import os
from groq import Groq
from tts_py import command_feedback
from device_agent import execute_command

# Fetch the API key from the .env file
api_key = os.getenv("GROQ_API_KEY")

# Create a client instance with the API key
client = Groq(api_key=api_key)

status = None
conversation_history = []  # List to store conversation history

def query_llm(command):
    # Assistant-specific prompt for personal assistant interaction
    prompt = f"""
    You are a highly intelligent and interactive personal assistant, similar to Jarvis from Iron Man.
    Your role is to help optimize tasks, provide insightful discussions, and offer mental support.
    Please generate a valid response that can assist me in my tasks or engage in a meaningful discussion based on the following input.

    User's command: "{command}"
    """

    # Add the user's command to the conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Keep only the last 10 phrases in the conversation history
    # if len(conversation_history) > 10:
    #     conversation_history.pop(0)  # Remove the oldest message

    # Create a chat completion request with the assistant role and the conversation history
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama-3.3-70b-versatile",  # Model selection
        max_tokens=50,  # Limit the response to about 50 words (average 6 characters per word)
    )

    # Get and return the response content
    assistant_response = chat_completion.choices[0].message.content

    # Ensure the response is under 50 words (based on average word length)
    assistant_response = " ".join(assistant_response.split()[:50])

    # Add assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response

# Function to simulate the device agent executing the command
def execute_device_command(command):
    # Execute the command using the imported function
    status = execute_command(command)
    
    # Check the status and return appropriate message
    if status == 1:
        return "Success"
    else:
        return "Command not recognized by the device agent."

def provide_command_feedback(status):
    if status == 1:
        command_feedback(True)
    elif status == 0:
        command_feedback(False)
