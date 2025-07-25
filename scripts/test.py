import sys
import os

# Dynamically add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm_engine.local_extract import extract_consent_info_local

clause = """
Under GDPR Article 7, the data subject shall have the right to withdraw their consent at any time.
"""

print("🧪 Testing Local LLM (Phi-3 or Mistral via Ollama)...")
result = extract_consent_info_local(clause)
print(result)
