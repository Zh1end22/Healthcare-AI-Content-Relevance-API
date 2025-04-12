# scoring.py
import re
import json
from ai_utils import query_gemini

# --- your client interests and themes ---
CLIENT_AREAS = [
    "workflow optimization",
    "physician experience",
    "clinical decision support",
    "data interoperability",
    "patient engagement"
]

THEMES = [
    "Workflow Optimization",
    "Physician Experience",
    "Clinical Decision Support",
    "Data Interoperability",
    "Patient Engagement",
    "Other"
]

def _build_prompt(article: str) -> str:
    return f"""
You are a healthcare AI analyst. Analyze the article below.

ARTICLE:
\"\"\"
{article}
\"\"\"

TASKS:
1. Score the article's relevance to healthcare AI (0-100).
2. Score its alignment with these client interest areas: {', '.join(CLIENT_AREAS)} (0-100).
3. Categorize it into one of these themes: {', '.join(THEMES)}.
4. Give a one‑paragraph rationale explaining why this would interest a healthcare AI client.

RESPOND IN JSON FORMAT ONLY, for example:
{{
  "relevance_score": 85,
  "alignment_score": 78,
  "theme": "Workflow Optimization",
  "rationale": "…"
}}
"""

async def analyze_article(article: str) -> dict:
    """
    1) Sends the article text to Gemini via query_gemini()
    2) Cleans out any ```json / ``` fences
    3) Parses to dict (with a fallback)
    """
    raw = await query_gemini(_build_prompt(article))

    # 1) Strip any leading/trailing code fences:
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip())  # remove leading ``` or ```json
    cleaned = re.sub(r"\s*```$", "", cleaned)               # remove trailing ```
    
    # 2) Try normal JSON parse
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        # 3) Fallback: grab from first { to last }
        start = cleaned.find("{")
        end   = cleaned.rfind("}")
        if start != -1 and end != -1:
            snippet = cleaned[start : end+1]
            try:
                return json.loads(snippet)
            except json.JSONDecodeError:
                pass

    # 4) If all else fails, return the raw for debugging
    return {
        "error": "Failed to parse Gemini response as JSON",
        "raw_response": raw
    }
