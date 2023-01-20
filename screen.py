from comtypes import client

def yy():
    # Get the text from the screen
    jaws = client.CreateObject("FreedomScientific.JAWS")
    text = jaws.Text
    # Speak the text
    jaws.SpeakString(text)

yy()
