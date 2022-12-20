from gtts import gTTS
from PyPDF2 import PdfReader

# For testing purposes, we need to hear the voice and play the mp3 file
import os

# TODO: use a try-except block

# Initializing the PdfReader module
text = ""
reader = PdfReader("./pdf_files/test.pdf") # TODO: dynamically capture the file name
number_of_pages = len(reader.pages)

# Extracting the text for each page
print("Initiating text extraction...")
for page_num in range(number_of_pages):
	page = reader.pages[page_num]
	raw_text = page.extract_text()
	text += raw_text.strip().replace("\n", " ")
	print(f"Finished extracting page { page_num + 1 } of { number_of_pages } pages.")

# Initializing the Google Text-to-Speech module
print("Converting...")
tts = gTTS(text, lang="en")
tts.save("./mp3_files/test.mp3") # Apply the TODO here too
print("We now have an mp3 file!")

# Plays the mp3 file
os.system("afplay ./mp3_files/test.mp3")