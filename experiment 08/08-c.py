from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
translator = Translator()
r = sr.Recognizer()
text = input("Enter English Text: ")
tamil = translator.translate(text, dest="ta").text
hindi = translator.translate(text, dest="hi").text
tts1 = gTTS(tamil, lang='ta')
tts1.save("tamil.mp3")
tts2 = gTTS(hindi, lang='hi')
tts2.save("hindi.mp3")
audio_tamil_mp3 = AudioSegment.from_mp3("tamil.mp3")
audio_tamil_mp3.export("tamil.wav", format="wav")
with sr.AudioFile("tamil.wav") as source:
    audio = r.record(source)
tamil_rec = r.recognize_google(audio, language='ta')
audio_hindi_mp3 = AudioSegment.from_mp3("hindi.mp3")
audio_hindi_mp3.export("hindi.wav", format="wav")
with sr.AudioFile("hindi.wav") as source:
    audio = r.record(source)
hindi_rec = r.recognize_google(audio, language='hi')
acc_ta = len(set(tamil.split()) & set(tamil_rec.split()))/len(tamil.split())*100
acc_hi = len(set(hindi.split()) & set(hindi_rec.split()))/len(hindi.split())*100
print("Tamil Accuracy:",round(acc_ta,2),"%")
print("Hindi Accuracy:",round(acc_hi,2),"%")
