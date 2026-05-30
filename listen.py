import webbrowser
import datetime 
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("\n[STATUS]: Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )

        print("[STATUS]: Recognizing...")

        try:

            text = recognizer.recognize_google(audio)

            print(f"\n[YOU]: {text}")

            return text.lower()

        except sr.UnknownValueError:

            print("\n[JARVIS]: Could not understand audio.")
            return ""

        except sr.RequestError:

            print("\n[JARVIS]: Internet connection issue.")
            return ""

# FUNCTION CALL
listen()