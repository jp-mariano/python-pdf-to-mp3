from gtts import gTTS
from PyPDF2 import PdfReader

# For testing purposes, we need to hear the voice and play the mp3 file
# Also used to fetch the PDF file name
import os

try:
	# Input the PDF document's file path below (replace "test.pdf" with your own file)
	pdf_file_directory = "./pdf_files/test.pdf"
	file_name = os.path.basename(pdf_file_directory).split(".")[0]

	# Initializing the PdfReader module
	text = ""
	reader = PdfReader(pdf_file_directory)
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

	mp3_file_directory = f"./mp3_files/{ file_name }.mp3"
	tts.save(mp3_file_directory)
	print("We now have an mp3 file!")

	# Plays the mp3 file (uncomment when testing)
	# os.system(f"afplay { mp3_file_directory }")
except Exception as e:
	raise e