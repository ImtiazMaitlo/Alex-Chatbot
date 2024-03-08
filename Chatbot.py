import speech_recognition as sr
import subprocess

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)

def process_command(command):
    if "open" in command:
        # Extract the application name from the command
        app_name = command.split("open")[1].strip()
        execute_command(f"start {app_name}.exe")  # Example: start notepad.exe
    elif "close" in command:
        # Extract the application name from the command
        app_name = command.split("close")[1].strip()
        execute_command(f"taskkill /F /IM {app_name}.exe")  # Example: taskkill /F /IM notepad.exe

def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        process_command(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Continuously listen for commands
while True:
    listen_for_commands()
