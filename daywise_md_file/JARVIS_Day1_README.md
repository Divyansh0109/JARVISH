# JARVIS MARK-I

An Iron-Man inspired AI desktop assistant built using Python.

---

# 🚀 Day 1 — Foundation & Voice System

Day 1 focused on building the core foundation of the project.
The goal was to make Jarvis speak using realistic AI-generated voice
and create the initial project structure.

---

# ✅ Features Implemented

- AI-generated voice system
- Terminal-style startup UI
- Realistic speech using Microsoft Neural Voices
- Automatic MP3 generation and playback
- Temporary file cleanup
- Virtual environment setup
- Basic project architecture

---

# 🛠 Technologies Used

- Python 3.11
- edge_tts
- pygame
- asyncio
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

## Clone Repository

```bash
git clone <your-repo-link>
cd JARVIS-MARK1
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install edge-tts
pip install pygame
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 🧠 How It Works

```text
Text Input
   ↓
edge_tts generates AI voice
   ↓
voice.mp3 created
   ↓
pygame plays audio
   ↓
Temporary file deleted
```

---

# 📜 Day 1 Main Code

```python
import asyncio
import edge_tts
import pygame
import os

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


print("=" * 50)
print("      JARVIS MARK-I INITIALIZING")
print("=" * 50)

asyncio.run(
    speak(
        "System online. Hello Divyansh."
    )
)
```

---

# 📚 Concepts Learned

- Python virtual environments
- Async programming
- AI voice generation
- Audio playback systems
- File handling
- Python modules
- Functions
- Terminal UI design

---

# 🎯 Day 1 Goal Achieved

✅ Jarvis can speak using realistic AI-generated voice.

---

# 🔥 Future Plans

- Voice recognition
- Website automation
- Weather system
- Spotify integration
- GUI / Hologram UI
- Wake-word detection
- ChatGPT integration

---

# 👨‍💻 Developer

Built by Divyansh Sen 🚀
