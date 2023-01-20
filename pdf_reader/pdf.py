import PyPDF2
import pyttsx3
import camelot

file_name = input("Enter the PDF file name: ")

pdf_file = open(file_name, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

engine = pyttsx3.init()

for page in range(len(pdf_reader.pages)):
    page_content = pdf_reader.pages[page].extract_text()
    engine.say(page_content)
engine.runAndWait()
pdf_file.close()
