from googletrans import Translator
from gtts import gTTS

translator = Translator()

text = input("Enter English text: ")

result = translator.translate(text, dest="ta")
tamil_text = result.text

print("Tamil:", tamil_text)

tts = gTTS(tamil_text, lang='ta')
tts.save("output.mp3")

print("Audio saved as output.mp3")