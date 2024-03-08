import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use pocketsphinx for offline speech recognition
        command = recognizer.recognize_sphinx(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None

def process_command(command):
    if command == "open browser":
        # Code to open the browser
        print("Opening browser...")
    elif command == "open notepad":
        # Code to open Notepad
        print("Opening Notepad...")
    else:
        print("Command not recognized.")

# Main loop
while True:
    command = listen_for_command()
    if command:
        process_command(command)
