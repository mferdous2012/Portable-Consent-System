# scripts/batch_test.py

import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm_engine.local_extract import extract_consent_info_local

# Sample batch of clauses for testing
clauses = [
    "Under GDPR Article 7, the data subject shall have the right to withdraw their consent at any time.",
    "According to CCPA, businesses must disclose the purposes for which personal data is collected.",
    "Users must be informed of their right to access the data a company stores about them, as required by PIPEDA.",
    "HIPAA mandates that patients must authorize any sharing of their health information with third parties.",
    "The individual may revoke previously given consent for data processing by notifying the controller in writing."
]

results = []
print("\n📦 Batch Testing Consent Clause Extraction with Local LLM\n")

for i, clause in enumerate(clauses, 1):
    print(f"Clause {i}:")
    print(f"{clause}\n")
    result = extract_consent_info_local(clause)
    print("🧠 Extracted Info:")
    print(result)
    print("\n" + "-"*60 + "\n")
    results.append({"clause": clause, "extraction": result})

# Save results to a JSON file
output_path = os.path.join(os.path.dirname(__file__), "..", "results", "batch_extraction_results.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ Results saved to: {output_path}")
