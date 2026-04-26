import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
original = "வணக்கம். நான் பாவனா!"
speech = gTTS(original, lang='ta')
speech.save("sample.mp3")
r = sr.Recognizer()
audio_mp3 = AudioSegment.from_mp3("sample.mp3")
audio_mp3.export("sample.wav", format="wav")
with sr.AudioFile("sample.wav") as source:
    audio = r.record(source)
recognized = r.recognize_google(audio, language='ta')
print("Original:", original)
print("Recognized:", recognized)
o = original.split()
rtext = recognized.split()
errors = 0
for w in o:
    if w not in rtext:
        errors += 1
print("Number of Errors:", errors)
