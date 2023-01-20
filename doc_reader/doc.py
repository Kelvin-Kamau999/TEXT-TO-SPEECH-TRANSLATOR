import docx
import pyttsx3

file_name = input("Enter the docx file name: ")

doc = docx.Document(file_name)
engine = pyttsx3.init()

for para in doc.paragraphs:
    engine.say(para.text)
engine.runAndWait()
