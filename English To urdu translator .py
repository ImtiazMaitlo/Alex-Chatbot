from gtts import gTTS
from googletrans import Translator
import os

def translate_text_to_urdu(text):
    translator = Translator()
    translation = translator.translate(text, dest='ur')
    return translation.text

def text_to_speech(text):
    tts = gTTS(text=text, lang='ur')
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows, opens the MP3 file with the default audio player

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text to translate to Urdu and convert to voice: ")
        if input_text == "exit":
         break

        urdu_translation = translate_text_to_urdu(input_text)
        text_to_speech(urdu_translation)
