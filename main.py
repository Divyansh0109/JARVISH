import speech_recognition as sr
import asyncio
import edge_tts
import pygame
import pywhatkit
import subprocess
import os
import webbrowser
import datetime

recognizer = sr.Recognizer()

# SPEAK FUNCTION
async def speak(text):

    print(f"\n[JARVIS]: {text}")

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-GuyNeural"
    )

    await communicate.save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    os.remove("voice.mp3")


# LISTEN FUNCTION
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

        except:

            return ""


# STARTUP
print("=" * 50)
print("      JARVIS MARK-II")
print("=" * 50)

asyncio.run(
    speak("System online. How can I help you?")
)
asyncio.run(
    speak("how are you doing today?")
)
# TAKE COMMAND
command = listen()


# COMMANDS
if "youtube" in command:

    asyncio.run(
        speak("Opening YouTube")
    )

    webbrowser.open("https://youtube.com")

elif "antigravity" in command:
    asyncio.run(
        speak("Opening Antigravity")
    )

    os.startfile(r"C:\Users\DELL\AppData\Local\Programs\Antigravity IDE\Antigravity IDE.exe")

elif "vs code" in command:
    asyncio.run(
        speak("Opening Visual Studio Code")
    )

    os.startfile(r"C:\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe")


elif "google" in command:

    asyncio.run(
        speak("Opening Google")
    )

    webbrowser.open("https://google.com")
elif "insta" in command:

    asyncio.run(
        speak("Opening Instagram")
    )

    webbrowser.open("https://instagram.com")

elif "time" in command:

    time = datetime.datetime.now().strftime("%I:%M %p")

    asyncio.run(
        speak(f"The current time is {time}")
    )


elif "hello" in command:

    asyncio.run(
        speak("Hello Divyansh")
    )


else:

    asyncio.run(
        speak("Command not recognized")
    )