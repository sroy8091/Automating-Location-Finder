import webbrowser,sys,os
import pyperclip
from gtts import gTTS

text = "Locating " + " ".join(sys.argv[1:])
tts = gTTS(text= text, lang="en")
tts.save("mapit.mp3")
os.system("mpg321 mapit.mp3")

if len(sys.argv)>1:
	address = " ".join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)