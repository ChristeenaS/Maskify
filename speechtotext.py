import pyttsx3
#import pyaudio
import speech_recognition as sr
import os
import datetime

name=''
phno=''
r=sr.Recognizer()
c="is it correct?"
def say(command):
    speaker=pyttsx3.init()
    speaker.say(command)
    speaker.runAndWait()

def speak():
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0.1)
                audio2=r.listen(source)
                text=r.recognize_google(audio2)
                print(text)
                return text
        except sr.RequestError as e:
                print("cannot identify the voice:{0}".format(e))
        except sr.UnknownValueError:
                return "try again"

