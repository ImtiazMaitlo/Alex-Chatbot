from gtts import gTTS
# from gtts import gTTS: This line imports the gTTS class from the gtts module. gTTS stands for Google Text-to-Speech. 
# This class allows us to generate speech from text using Google's Text-to-Speech API.
import os
# import os: This line imports the os module, which provides a way to interact with the operating system.
# We'll use it to save the generated audio file and play it.

def text_to_speech(text):
    # def text_to_speech(text): This line defines a function named text_to_speech that takes a single argument text,
    # which represents the text we want to convert to speech.
    tts = gTTS(text=text, lang='en')
    # tts = gTTS(text=text, lang='en'): This line creates a gTTS object by passing the text we want to convert (text) and 
    # the language (lang) as arguments. Here, we specify 'en' for English.
    tts.save("output.mp3")
    # tts.save("output.mp3"): This line saves the generated speech as an MP3 file named "output.mp3" in the current directory. 
    # The save() method of the gTTS object is used to save the speech to a file.
    os.system("start output.mp3")  # For Windows, opens the MP3 file with the default audio player
    # os.system("start output.mp3"): This line executes a system command to open the generated MP3 file using the default audio player. 
    # For Windows, the command start output.mp3 opens the file in the default media player.

if __name__ == "__main__":
    while True:
        
         print("To Exit from program writr exit")
         input_text = input("Enter the text to convert to English pronunciation : ")
         if input_text.lower() == "exit":
            bye_message = "Bye bye, friend!"
            print(bye_message)  # Print the goodbye message
            text_to_speech(bye_message)  # Convert and play the goodbye message
            break
         
         
    # input_text = input("Enter the text to convert to English pronunciation: "): This line prompts the user to enter the text they want to convert to English pronunciation.
    # The input text is stored in the variable input_text.
         text_to_speech(input_text)
    # text_to_speech(input_text): This line calls the text_to_speech function, passing the user's input text as an argument. 
    # The function will then convert the text to speech and play it.


