from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
translator = Translator()
r = sr.Recognizer()
text = input("Input Text: ")
translated = translator.translate(text, dest="ta").text
speech = gTTS(translated, lang='ta')
speech.save("audio.mp3")
audio_mp3 = AudioSegment.from_mp3("audio.mp3")
audio_mp3.export("audio.wav", format="wav")
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)
recognized = r.recognize_google(audio, language='ta')
acc = len(set(translated.split()) & set(recognized.split()))/len(translated.split())*100
f = open("results.txt","w")
f.write("Input Text: "+text+"\n")
f.write("Translated Text: "+translated+"\n")
f.write("Recognized Text: "+recognized+"\n")
f.write("Accuracy: "+str(round(acc,2)) + "%")
f.close()
print("Results saved in results.txt")
