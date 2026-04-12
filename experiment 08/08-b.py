import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

sentences = ["AI is the future", "Python is easy", "Speech to text works"]
r = sr.Recognizer()

for s in sentences:
    gTTS(s).save("a.mp3")
    AudioSegment.from_mp3("a.mp3").export("a.wav", format="wav")
    with sr.AudioFile("a.wav") as src:
        text = r.recognize_google(r.record(src))
    acc = round(sum(w in text.lower() for w in s.lower().split()) / len(s.split()) * 100, 2)
    print(s, "|", text, "|", acc, "%")