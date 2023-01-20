import pyttsx3
import pyperclip

def tts_screen_reader():
    # Get the text from the clipboard
    text = pyperclip.paste()
    # Speak the text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

tts_screen_reader()
