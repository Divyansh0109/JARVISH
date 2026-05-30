# JARVIS MARK-I

## 🚀 Day 3 — Automation & App Control

### Overview

Day 3 focused on transforming Jarvis from a voice assistant into an automation assistant.

Previously, Jarvis could listen and speak. Now it can perform real actions on the computer such as opening applications, searching Google, and playing YouTube videos based on voice commands.

---

## ✅ Features Implemented

### Application Launcher

Jarvis can open desktop applications using voice commands.

Examples:

- Open Chrome
- Open VS Code
- Open Spotify

Implemented using:

```python
import subprocess
```

Example:

```python
subprocess.Popen(["chrome.exe"])
```

---

### Google Search Automation

Example Command:

```text
Search artificial intelligence
```

Implemented using:

```python
pywhatkit.search(search_query)
```

---

### YouTube Automation

Example Command:

```text
Play industry baby
```

Implemented using:

```python
pywhatkit.playonyt(song)
```

---

## 🛠 Technologies Used

- Python 3.11
- speech_recognition
- edge_tts
- pygame
- asyncio
- subprocess
- pywhatkit
- webbrowser
- os

---

## 🧠 Concepts Learned

- Automation
- Dynamic Commands
- String Manipulation
- Application Control
- Browser Automation
- Command Processing

---

## 📂 Workflow

```text
USER SPEAKS
      ↓
Microphone Input
      ↓
Speech Recognition
      ↓
Text Command
      ↓
Decision Engine
      ↓
Automation Layer
      ↓
Windows / Browser Action
      ↓
Voice Response
```

---

## 📈 Project Evolution

### Day 1
Text → Voice

### Day 2
Voice → Text → Voice

### Day 3
Voice → Text → Decision → Action → Voice

---

## 🎯 Day 3 Goal Achieved

Jarvis can now:

- Listen to commands
- Understand speech
- Open applications
- Search Google
- Play YouTube videos
- Respond with AI voice

---

## 👨‍💻 Developer

Built by Divyansh Sen

Project: JARVIS MARK-I
