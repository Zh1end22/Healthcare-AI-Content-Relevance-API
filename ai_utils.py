# ai_utils.py
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

# 1) Your API key (from .env)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

# 2) Pick a valid model. Default to "gemini-1.5-flash", but override with GEMINI_MODEL
#    See https://ai.google.dev/api/generate-content → ListModels for other model IDs :contentReference[oaicite:1]{index=1}
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

async def query_gemini(prompt: str) -> str:
    """
    Send `prompt` to Gemini and return the generated text.
    """
    url = (
        f"https://generativelanguage.googleapis.com/v1beta"
        f"/models/{GEMINI_MODEL}:generateContent"
    )

    headers = {
        "Content-Type": "application/json",
        # You can also pass the key as ?key=... in the URL, but this header works too
        "x-goog-api-key": GEMINI_API_KEY,
    }

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

        # Extract the generated text from the response
        return data["candidates"][0]["content"]["parts"][0]["text"]
