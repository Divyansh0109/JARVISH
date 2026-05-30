# JARVIS MARK-I

An Iron-Man inspired AI desktop assistant built using Python.

---

# 🚀 Day 2 — Voice Recognition & Command System

Day 2 focused on making Jarvis interactive.
The goal was to allow Jarvis to listen to voice commands,
understand speech, and perform actions automatically.

---

# ✅ Features Implemented

- Voice recognition system
- Microphone input
- Speech-to-text conversion
- AI voice responses
- Website automation
- Time assistant
- Command processing
- Error handling

---

# 🛠 Technologies Used

- Python 3.11
- speech_recognition
- edge_tts
- pygame
- asyncio
- webbrowser
- datetime
- os

---

# 📂 Project Structure

```bash
JARVIS-MARK1/
│
├── main.py
├── assistant/
├── ui/
├── assets/
├── sounds/
├── animations/
└── README.md
```

---

# ⚙️ Installation

## Install Dependencies

```bash
pip install SpeechRecognition
pip install edge-tts
pip install pygame
pip install pyaudio
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 🧠 How It Works

```text
YOU SPEAK
   ↓
Microphone records audio
   ↓
Google Speech Recognition converts speech → text
   ↓
Python checks commands
   ↓
Jarvis decides action
   ↓
edge_tts generates AI voice
   ↓
pygame plays audio
   ↓
Jarvis responds
```

---

# 📜 Day 2 Main Code

```python
import speech_recognition as sr
import asyncio
import edge_tts
import pygame
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

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        print("[STATUS]: Recognizing...")

        text = recognizer.recognize_google(audio)

        print(f"\n[YOU]: {text}")

        return text.lower()


print("=" * 50)
print("      JARVIS MARK-II")
print("=" * 50)

asyncio.run(
    speak("System online. How can I help you?")
)

command = listen()

if "youtube" in command:

    asyncio.run(
        speak("Opening YouTube")
    )

    webbrowser.open("https://youtube.com")

elif "google" in command:

    asyncio.run(
        speak("Opening Google")
    )

    webbrowser.open("https://google.com")

elif "time" in command:

    time = datetime.datetime.now().strftime("%I:%M %p")

    asyncio.run(
        speak(f"The current time is {time}")
    )

else:

    asyncio.run(
        speak("Command not recognized")
    )
```

---

# 📚 Concepts Learned

- Speech Recognition
- Microphone Input Handling
- Async Programming
- AI Voice Generation
- Audio Playback Systems
- Conditional Statements
- Website Automation
- Time Handling
- Error Handling
- Command Processing

---

# 🔍 Modules Explanation

## speech_recognition
Converts voice into text using Google's speech recognition system.

## edge_tts
Generates realistic AI voice using Microsoft Neural Voices.

## pygame
Plays generated audio files.

## asyncio
Handles asynchronous programming.

## webbrowser
Automatically opens websites.

## datetime
Retrieves current system time.

## os
Handles file operations like deleting MP3 files.

---

# 🧩 System Architecture

```text
INPUT SYSTEM
↓
Microphone Input

PROCESSING SYSTEM
↓
Speech Recognition

DECISION SYSTEM
↓
if / elif Command Logic

OUTPUT SYSTEM
↓
AI Voice Output

ACTION SYSTEM
↓
Website Automation
```

---

# 🎯 Day 2 Goal Achieved

✅ Jarvis can now:
- listen
- understand speech
- execute commands
- respond using AI voice

---

# 🔥 Future Plans

- Open applications
- Spotify control
- Weather system
- Wake-word detection
- GUI / Hologram UI
- ChatGPT integration
- System monitoring
- AI memory system

---

# 👨‍💻 Developer

Built by Divyansh Sen 🚀
