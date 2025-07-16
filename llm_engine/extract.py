# llm_engine/extract.py

import openai
from llm_engine.prompts import consent_extraction_prompt

# Set your OpenAI API key before calling this function
openai.api_key = "YOUR_API_KEY_HERE"

def extract_consent_info(input_clause: str, model: str = "gpt-3.5-turbo") -> dict:
    """Send a consent clause to the LLM and return structured extraction."""
    
    prompt = consent_extraction_prompt.format(input_clause=input_clause)

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a legal assistant extracting semantic consent data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800,
        )
        reply = response['choices'][0]['message']['content']
        return eval(reply) if reply.startswith("{") else {"error": "Invalid JSON format returned"}
    
    except Exception as e:
        return {"error": str(e)}
