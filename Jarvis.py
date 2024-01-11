from Body.Speak import Speak
from Body.Listen import Listen

def MainExe():

    while True:

        query = Listen().lower()

        if "hello" in query:
            Speak("Hi! I am Friday")

        elif "goodbye" in query:
            Speak("Bye Sir")
