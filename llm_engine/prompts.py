# llm_engine/prompts.py

consent_extraction_prompt = """
You are a legal assistant trained to analyze privacy regulations such as GDPR, CCPA, PIPEDA, etc.
Your task is to extract structured semantic information from a given legal clause related to consent.

Given a clause, extract the following fields:

1. Jurisdiction: Identify the legal source (e.g., GDPR, CCPA, HIPAA, PIPEDA)
2. Clause Type: One of ["Consent Grant", "Consent Withdrawal", "Consent Update", 
                        "Purpose Limitation", "Data Sharing", "Access Request", "Revocation"]
3. Data Subject Role: Who is giving or controlling the consent (e.g., user, patient, consumer)
4. Data Controller Role: Who is receiving or processing the data (e.g., hospital, platform, organization)
5. Rights Mentioned: What rights does the clause describe for the data subject?
6. Obligations Mentioned: What obligations are imposed on the controller?
7. Time Limitation (if any): Duration for which consent is valid
8. Withdrawal Conditions (if any): How and when consent can be withdrawn
9. Summary: A 1-line plain English summary of the clause.

Return the response in the following JSON format:

{{
  "jurisdiction": "",
  "clause_type": "",
  "data_subject_role": "",
  "data_controller_role": "",
  "rights": [],
  "obligations": [],
  "time_limitation": "",
  "withdrawal_conditions": "",
  "summary": ""
}}

Clause:
\"\"\"{input_clause}\"\"\"
"""
