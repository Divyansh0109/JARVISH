

import speech_recognition as sr      # Speech to text
import asyncio                       # Async support for edge_tts
import edge_tts                      # AI voice generation
import pygame                        # Audio playback
#import pywhatkit                     # Google search & YouTube automation
import os                            # OS operations
import webbrowser                    # Open websites
import datetime                      # Current date & time
import psutil                        # System monitoring
import requests                       # API requests    
import json                           # JSON handling
from AI import ask_ai          # AI response generation 

# Create speech recognizer object
recognizer = sr.Recognizer()
WAKE_WORD = ["jarvis","hey jarvis","daddy's home","hey buddy"]  # Wake word to activate assistant

# TEXT TO SPEECH FUNCTION


async def speak(text):
    

    # Show Jarvis response in terminal
    print(f"\n[JARVIS]: {text}")

    # Generate AI voice
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-GuyNeural"
    )

    # Save generated voice as mp3
    await communicate.save("voice.mp3")

    # Initialize audio engine
    pygame.mixer.init()

    # Load generated audio
    pygame.mixer.music.load("voice.mp3")

    # Play audio
    pygame.mixer.music.play()

    # Wait until audio finishes
    while pygame.mixer.music.get_busy():
        continue

    # Stop audio engine
    pygame.mixer.quit()

    # Delete temporary audio file
    os.remove("voice.mp3")

def wait_for_wake_word():

    while True:

        text = listen()

        if not text:
            continue

        for word in WAKE_WORD:

            if word in text:

                command = text.replace(
                    word,
                    ""
                ).strip()

                return command
# SPEECH RECOGNITION FUNCTION


def listen():

    with sr.Microphone() as source:

        print("\n[STATUS]: Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            return ""

        print("[STATUS]: Recognizing...")

        try:

            text = recognizer.recognize_google(audio)

            print(f"\n[YOU]: {text}")

            return text.lower()

        except:

            return ""

def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    
    except:
        return {}   

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)


# STARTUP SCREEN


print("=" * 50)
print("         JARVIS ACTIVATED")
print("=" * 50)

# Startup greeting
asyncio.run(
    speak("System online. How can I help you?")
)

# ASSISTANT STATE


# True = Jarvis listens
# False = Jarvis sleeps
jarvis_awake = True

# MAIN LOOP

while True:

    print(
        "\n[STATUS]: Waiting for wake word..."
    )

    command = wait_for_wake_word()

    # User only said wake word
    if command == "":

        asyncio.run(
            speak(
                "Yes Divyansh?"
            )
        )

        command = listen()

    if command == "":
        continue

     
    # EXIT COMMAND
     
    if "exit" in command:

        asyncio.run(
            speak("Goodbye Divyansh")
        )

        break

    # SLEEP MODE
    
    elif "go to sleep" in command:

        jarvis_awake = False

        asyncio.run(
            speak("Entering sleep mode")
        )

        continue

     
    # WAKE MODE
     
    elif "wake up" in command:

        jarvis_awake = True

        asyncio.run(
            speak("I am awake now")
        )

        continue

    # If sleeping, ignore all commands
    if not jarvis_awake:
        continue

    # BATTERY STATUS
    
    elif "battery" in command:

     battery = psutil.sensors_battery()
     percent = battery.percent
     asyncio.run(
        speak(
            f"Your battery is at {percent} percent"
        ))
     
    # OPEN YOUTUBE
    
    elif "youtube" in command:

        asyncio.run(
            speak("Opening YouTube")
        )

        webbrowser.open("https://youtube.com")
 
    # PLAY SONG ON YOUTUBE
     
    elif "play" in command:

        song = command.replace(
            "play",
            ""
        ).strip()

        asyncio.run(
            speak(f"Playing {song}")
        )

        pywhatkit.playonyt(song)

    # GOOGLE SEARCH
     
    elif "search" in command:

        search_query = command.replace(
            "search",
            ""
        ).strip()

        asyncio.run(
            speak(f"Searching for {search_query}")
        )

        pywhatkit.search(search_query)

     # OPEN VS CODE
     
    elif "vs code" in command:

        asyncio.run(
            speak("Opening Visual Studio Code")
        )

        os.startfile(
            r"C:\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        )

    #remember information
    elif "remember" in command:

        data = command.replace(
        "remember",
        ""
        ).strip()

        if " is " in data:

            key, value = data.split( " is ", 1)
            memory = load_memory()
            memory[key] = value
            save_memory(memory)
            asyncio.run(
            speak( f"I will remember that {key} is {value}"))
    
    #recall information
    elif "what is" in command:
        key = command.replace("what is my","" ).strip()
        memory = load_memory()

        if key in memory:

            asyncio.run(
                speak(f"Your {key} is {memory[key]}") )

        else:
            print("\n[STATUS]: Asking AI...")
            answer = ask_ai(command)
            asyncio.run(
                speak(answer) )

    # OPEN GOOGLE
     
    elif "google" in command:

        asyncio.run(
            speak("Opening Google")
        )

        webbrowser.open("https://google.com")

     
    # OPEN INSTAGRAM
     
    elif "insta" in command:

        asyncio.run(
            speak("Opening Instagram")
        )

        webbrowser.open("https://instagram.com")

     
    # CURRENT TIME
     
    elif "time" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        asyncio.run(
            speak(
                f"The current time is {current_time}"
            )
        )

      # GREETING
     
    elif "hello" in command:

        asyncio.run(
            speak("Hello Divyansh")
        )
    
    #system status

    elif "system status" in command:

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        battery = psutil.sensors_battery()

        battery_percent = battery.percent

        asyncio.run(
         speak(
            f"""
            CPU usage is {cpu} percent.
            RAM usage is {ram} percent.
            Battery is {battery_percent} percent.
            """
        )
    )

    #Wheather information
    elif "weather in" in command:

        city = command.replace(
        "weather in",
        ""
            ).strip()

        response = requests.get(
        f"https://wttr.in/{city}?format=3"
        )

        weather = response.text

        asyncio.run(
        speak(weather)
        )  
    
    # IP ADDRESS

    elif "ip address" in command:
        try:
            response = requests.get(
            "https://api.ipify.org?format=json"
             )
            ip = response.json()["ip"]

            asyncio.run(
            speak(f"Your IP address is {ip}")
         )

        except:

            asyncio.run(
                     speak(
                "Unable to fetch IP address"
                 )
             )
            

    # UNKNOWN COMMAND
    else:
        print("\n[STATUS]: Thinking...")
        answer = ask_ai(command)
        print(f"\n[AI]: {answer}")
        asyncio.run(speak(answer))

