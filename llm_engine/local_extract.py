import re
import requests
import json
from llm_engine.prompts import consent_extraction_prompt

def extract_consent_info_local(input_clause: str, model="phi3") -> dict:
    prompt = consent_extraction_prompt.format(input_clause=input_clause)

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        raw = response.json()["response"].strip()

        # 🧽 Clean markdown block
        if raw.startswith("```json"):
            raw = raw.removeprefix("```json").removesuffix("```").strip()
        elif raw.startswith("```"):
            raw = raw.removeprefix("```").removesuffix("```").strip()

        # ❌ Remove inline comments (e.g., // some text)
        raw = re.sub(r"//.*", "", raw)

        return json.loads(raw)

    except json.JSONDecodeError:
        return {"error": "Invalid JSON after cleaning", "raw": raw}
    except Exception as e:
        return {"error": str(e)}
