import subprocess
import webbrowser
import speech_recognition as sr

# Define a dictionary to map commands to actions
command_actions = {
    "open facebook": "open_faceboook()",
    "open twitter": "open_twitter()",
    "open yahoo": "open_yahoo()",
    "open youtube": "open_youtube()",
    "open google": "open_google()",
    "open browser": "open_browser()",
    "open calculator": "open_calculator()",
    "shutdown computer": "shutdown_computer()"
    # Add more commands and corresponding actions as needed
}
def open_facebook():
    url = "https://www.facebook.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("facebook opened successfully.")

def open_twitter():
    url = "https://www.twitter.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Twitter opened successfully.")


def open_yahoo():
    url = "https://www.yahoo.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("yahoo opened successfully.")

def open_youtube():
    url = "https://www.youtube.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Youtube opened successfully.")



# Function to perform action corresponding to "open browser" command
def open_browser():
    url = "https://www.chrome.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Browser opened successfully.")

# Function to perform action corresponding to "open google" command
def open_google():
    url = "https://www.google.com"  # URL for Google's search page
    webbrowser.open(url)
    print("Google opened successfully.")

# Function to perform action corresponding to "open calculator" command
def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        print("Calculator opened successfully.")
    except FileNotFoundError:
        print("Calculator application not found.")

# Function to perform action corresponding to "shutdown computer" command
def shutdown_computer():
    print("Shutting down computer...")
    subprocess.Popen(["shutdown", "/s", "/t", "1"])

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Main function to handle user input and perform actions
def main():
    print("Welcome! Speak a command to perform an action : ")
    while True:
        command = recognize_speech()
        if command == "exit":
            print("Exiting...")
            break
        elif command in command_actions:
            eval(command_actions[command])  # Execute the correspo
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
