"""
OpenRouter API Key Check
=========================
Verifies that OPENROUTER_API_KEY is set, valid, and using a free model.

Run from inside trip_notes/ with .venv active:
    python tests/check_openrouter.py

Called automatically by tests/check_api_setup.py.
API key must be in CISC395/.env (one level above trip_notes/).
"""

import os
import sys
import time

try:
    from dotenv import load_dotenv, find_dotenv
except ImportError:
    print("\u2717  python-dotenv not installed.")
    print("   From CISC395/:  pip install python-dotenv")
    sys.exit(1)

try:
    from openai import OpenAI
    import openai
except ImportError:
    print("\u2717  openai not installed.")
    print("   From CISC395/:  pip install openai")
    sys.exit(1)

# find_dotenv() searches upward from CWD (trip_notes/) and finds CISC395/.env
load_dotenv(find_dotenv())

print("=== OpenRouter API Key Check ===")
print()

key = os.getenv("OPENROUTER_API_KEY")
if not key:
    print("\u2717  OPENROUTER_API_KEY not found.")
    print("   Add to CISC395/.env:")
    print("       OPENROUTER_API_KEY=sk-or-v1-your-key-here")
    print("   Get a free key at: https://openrouter.ai")
    sys.exit(1)

if not key.startswith("sk-or-"):
    print(f"\u26a0  Key format looks unexpected: {key[:12]}...")
    print("   OpenRouter keys usually start with 'sk-or-'")
    print("   Continuing anyway...")
else:
    print(f"\u2713  Key found: {key[:16]}...")

MODEL = "openrouter/free"

client = OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1",
)

print(f"   Model: {MODEL}")
print("   Sending test request...")
print()

try:
    start = time.time()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Reply with exactly three words: API test successful"}
        ],
        max_tokens=20,
        extra_body={"reasoning": {"enabled": True}},
    )
    elapsed = time.time() - start
    msg = response.choices[0].message
    content = msg.content
    actual_model = response.model

    # With reasoning enabled, content may be None — check reasoning_details too
    if content:
        text = content.strip()
    elif hasattr(msg, "reasoning_details") and msg.reasoning_details:
        text = "(reasoning response — content in reasoning_details)"
    else:
        text = "(empty response — key works but model returned nothing)"

    print(f"\u2713  Response ({elapsed:.1f}s): {text}")
    print(f"\u2713  Model confirmed: {actual_model}")
    print()
    print("Your OpenRouter API key is working. Ready for Lab 08.")

except openai.AuthenticationError:
    print("\u2717  Authentication failed.")
    print("   Your API key is invalid or expired.")
    print("   Get a new key at: https://openrouter.ai")
    sys.exit(1)

except openai.RateLimitError:
    print("\u2717  Rate limit hit.")
    print("   Wait 1 minute and try again, or use: python tests/check_gemini.py")
    sys.exit(1)

except openai.APIConnectionError as e:
    print(f"\u2717  Connection error: {e}")
    print("   Check your internet connection.")
    sys.exit(1)

except Exception as e:
    print(f"\u2717  Unexpected error: {e}")
    sys.exit(1)
