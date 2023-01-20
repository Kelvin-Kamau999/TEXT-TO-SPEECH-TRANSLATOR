import pyttsx3

file_name = input("Enter the file name: ")
with open(file_name, 'r') as file:
    content = file.read()

engine = pyttsx3.init()
engine.say(content)
engine.runAndWait()

