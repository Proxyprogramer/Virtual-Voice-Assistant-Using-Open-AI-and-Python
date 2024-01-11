# Commands in Hindi or English => English

# 1. Listen
# 2. Translate
# 3. Connect

import speech_recognition as sr
from googletrans import Translator

# Listen Function (Multi-Language)
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
    return query


# Translation
def TranslationOnHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line, dest='en')
    data = result.text
    print(f"You: {data}.")
    return data


# Connect
def MicExecution():
    query = Listen()
    data = TranslationOnHinToEng(query)
    return data

MicExecution()