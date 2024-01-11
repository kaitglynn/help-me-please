```python
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

class VoiceChat:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        mixer.init()

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            return text
        except:
            print("Sorry, I didn't get that.")
            return ""

    def speak(self, text, lang="en"):
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")
        mixer.music.load("response.mp3")
        mixer.music.play()

    def change_voice(self, lang):
        self.lang = lang

voice_chat = VoiceChat()

def sendVoiceMessage():
    message = voice_chat.listen()
    if message != "":
        # send message to bot
        pass

def changeVoice():
    # change voice of bot
    voice_chat.change_voice("fr")
```
