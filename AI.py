import google.generativeai as genai

# Connect the Gemini client with the API key used by Jarvis.
genai.configure(
    api_key="AQ.Ab8RN6J71pzZ1-8TSUD4iPsI6TgN8eeRcD18APP-ugdGGaKxjw"
)

# Gemini Flash is quick enough for short voice-assistant replies.
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# These instructions keep Jarvis's answers brief and easy to speak aloud.
SYSTEM_PROMPT = """
You are Jarvis Mark-I.

Created by Divyansh Sen.

You are a voice assistant.

Keep responses short and natural.

Avoid markdown.
"""


def ask_ai(question):
    """Send a question to Gemini and return Jarvis's response."""

    try:
        # Add the user's question after Jarvis's permanent instructions.
        response = model.generate_content(
            SYSTEM_PROMPT +
            "\n\nUser: " +
            question
        )

        # Return plain text so the caller can print and speak it.
        return response.text

    except Exception as e:
        # Log the real error for debugging, but give the user a simple reply.
        print(f"[AI ERROR]: {e}")

        return (
            "Sorry, I cannot connect "
            "to my AI brain."
        )
