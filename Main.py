from Body.Speak import Speak
import speech_recognition as sr
import os
from Jarvis import MainExe

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()


    if "activate" in query:
        print("")
        print("Friday Activated!    ")
        Speak("Friday Activated!")
        print("")
        MainExe()
    
    else:
        pass

while True:
    WakeupDetected()