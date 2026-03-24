"""
Lab 7 Starter Template — API Programming Foundations
CISC 395 - Applied Generative AI and LLM Applications

Instructions:
1. Copy this file to Lab07/main.py
2. Make sure your .env file has: OPENROUTER_API_KEY=sk-or-v1-...
3. Run: python main.py
"""

from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import openai

# Load API key from .env file
load_dotenv()

# ── Configuration ─────────────────────────────────────────────────────────────

MODEL = "meta-llama/llama-3.3-70b-instruct:free"

# Alternative free models (change MODEL string to switch):
# "google/gemini-2.0-flash-exp:free"      ← Google Gemini
# "qwen/qwen3-coder-480b-a22b:free"       ← Best for code

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# ── Helper Function ────────────────────────────────────────────────────────────

def ask(messages, temperature=0.7, max_tokens=500):
    """
    Send a list of messages to the API and return the response text.

    Args:
        messages: list of dicts with "role" and "content" keys
        temperature: float 0.0-2.0 (lower = more consistent, higher = more creative)
        max_tokens: maximum number of tokens in the response

    Returns:
        str: the AI's response text, or an error message
    """
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    except openai.AuthenticationError:
        return "Error: Bad API key — check your .env file"
    except openai.RateLimitError:
        return "Error: Rate limit reached — wait a moment and retry"
    except openai.APIConnectionError:
        return "Error: Connection failed — check your internet connection"


# ── Your Code Below ───────────────────────────────────────────────────────────
# Delete or modify the example below and add your own code for each exercise.

if __name__ == "__main__":

    # Quick test to verify your setup works
    reply = ask(
        messages=[{"role": "user", "content": "Say 'Setup successful!' and nothing else."}],
        temperature=0.0,
        max_tokens=20,
    )
    print("Setup check:", reply)
    print()

    # ── Exercise 1: Replace with your code ──
    # ── Exercise 2: Replace with your code ──
    # ── Exercise 3: Replace with your code ──
    # ── Exercise 4: Replace with your code ──
