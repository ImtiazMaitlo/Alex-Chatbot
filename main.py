import subprocess
import webbrowser
import speech_recognition as sr

# Define a dictionary to map commands to actions
command_actions = {
    "open facebook": "open_facebook()",
    "open twitter": "open_twitter()",
    "open yahoo": "open_yahoo()",
    "open youtube": "open_youtube()",
    "open google": "open_google()",
    "open browser": "open_browser()",
    "open calculator": "open_calculator()",
    "shutdown computer": "shutdown_computer()",
    "open notepad": "open_notepad()",
    "open file explorer": "open_file_explorer()",
    "open command prompt": "open_command_prompt()",
    "open control panel": "open_control_panel()",
    "open task manager": "open_task_manager()",
    "open word": "open_word()",
    "open excel": "open_excel()",
    "open powerpoint": "open_powerpoint()",
    "restart computer": "restart_computer()",
    "open desktop": "open_desktop()",
    "open cmd": "open_cmd()",
    "open popup menu": "open_popup_menu()",
    "open calendar": "open_calendar()",
    "open chatgpt": "open_chatgpt()"
    # Add more commands and corresponding actions as needed
}

def open_facebook():
    url = "https://www.facebook.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Facebook opened successfully.")

def open_twitter():
    url = "https://www.twitter.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Twitter opened successfully.")

def open_yahoo():
    url = "https://www.yahoo.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Yahoo opened successfully.")

def open_youtube():
    url = "https://www.youtube.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Youtube opened successfully.")

def open_google():
    url = "https://www.google.com"  # URL for Google's search page
    webbrowser.open(url)
    print("Google opened successfully.")

def open_browser():
    url = "https://www.chrome.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Browser opened successfully.")

def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        print("Calculator opened successfully.")
    except FileNotFoundError:
        print("Calculator application not found.")

def shutdown_computer():
    print("Shutting down computer...")
    subprocess.Popen(["shutdown", "/s", "/t", "1"])

def open_notepad():
    try:
        subprocess.Popen("notepad.exe")
        print("Notepad opened successfully.")
    except FileNotFoundError:
        print("Notepad application not found.")

def open_file_explorer():
    try:
        subprocess.Popen("explorer.exe")
        print("File Explorer opened successfully.")
    except FileNotFoundError:
        print("File Explorer application not found.")

def open_command_prompt():
    try:
        subprocess.Popen("cmd.exe")
        print("Command Prompt opened successfully.")
    except FileNotFoundError:
        print("Command Prompt application not found.")

def open_control_panel():
    try:
        subprocess.Popen("control.exe")
        print("Control Panel opened successfully.")
    except FileNotFoundError:
        print("Control Panel application not found.")

def open_task_manager():
    try:
        subprocess.Popen("taskmgr.exe")
        print("Task Manager opened successfully.")
    except FileNotFoundError:
        print("Task Manager application not found.")

def open_word():
    try:
        subprocess.Popen("winword.exe")
        print("Microsoft Word opened successfully.")
    except FileNotFoundError:
        print("Microsoft Word application not found.")

def open_excel():
    try:
        subprocess.Popen("excel.exe")
        print("Microsoft Excel opened successfully.")
    except FileNotFoundError:
        print("Microsoft Excel application not found.")

def open_powerpoint():
    try:
        subprocess.Popen("powerpnt.exe")
        print("Microsoft PowerPoint opened successfully.")
    except FileNotFoundError:
        print("Microsoft PowerPoint application not found.")

def restart_computer():
    print("Restarting computer...")
    subprocess.Popen(["shutdown", "/r", "/t", "1"])

def open_desktop():
    try:
        subprocess.Popen("explorer.exe /root,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
        print("Desktop opened successfully.")
    except FileNotFoundError:
        print("Desktop application not found.")

def open_cmd():
    try:
        subprocess.Popen("cmd.exe")
        print("Command Prompt opened successfully.")
    except FileNotFoundError:
        print("Command Prompt application not found.")

def open_popup_menu():
    try:
        subprocess.Popen("explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}")
        print("Popup menu opened successfully.")
    except FileNotFoundError:
        print("Popup menu application not found.")

def open_calendar():
    try:
        subprocess.Popen("outlookcal:")
        print("Calendar opened successfully.")
    except FileNotFoundError:
        print("Calendar application not found.")

def open_chatgpt():
    url = "https://chat.openai.com/"  # Change the URL to the desired website
    webbrowser.open(url)
    print("ChatGPT opened successfully.")

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
            eval(command_actions[command])  # Execute the corresponding action
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
