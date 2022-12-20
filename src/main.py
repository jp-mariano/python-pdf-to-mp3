from gtts import gTTS

# For testing purposes, we need to hear the voice and play the mp3 file
import os

tts = gTTS("Hello, this is my normal way of speaking!", lang="en")
tts.save("./mp3_files/test.mp3")

# Plays the mp3 file
os.system("afplay ./mp3_files/test.mp3")
