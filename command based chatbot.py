import subprocess
import webbrowser
# Define a dictionary to map commands to actions
command_actions = {
    
    "open google":"open_google()",
    "open browser": "open_browser()",
    "open calculator": "open_calculator()",
    "shutdown computer": "shutdown_computer()",
    # Add more commands and corresponding actions as needed
}

# Function to perform action corresponding to "open browser" command
# def open_browser():
#     print("Opening browser...")  # You can replace this with actual code to open a browser
# Function to perform action corresponding to "open browser" command


def open_browser():
    url = "https://www.chrome.com"  # Change the URL to the desired website
    webbrowser.open(url)
    print("Browser opened successfully.")

def open_google():
    url = "https://www.google.com"  # URL for Google's search page
    webbrowser.open(url)
    print("Google opened successfully.")

# Function to perform action corresponding to "open calculator" command
# def open_calculator():
#     print("Opening calculator...")  # You can replace this with actual code to open a calculator
def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        print("Calculator opened successfully.")
    except FileNotFoundError:
        print("Calculator application not found.")
# Function to perform action corresponding to "shutdown computer" command

# import os
# def shutdown_computer():
#     print("Shutting down computer...")
#     os.system("shutdown /s /t 1")

# if __name__ == "__main__":
#     shutdown_computer()


    
# Main function to handle user input and perform actions
def main():
    print("Welcome! Type a command to perform an action (e.g., 'open browser', 'shutdown computer').")
    while True:
        command = input("Enter a command: ").lower()
        if command == "exit":
            print("Exiting...")
            break
        elif command in command_actions:
            eval(command_actions[command])  # Execute the corresponding action
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
