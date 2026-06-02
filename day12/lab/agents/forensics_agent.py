import sys
sys.path.append(".")
import json

with open("generated_data/clean_transactions.json") as f:
    clean = json.load(f)

with open("generated_data/schema_drift.json") as f:
    broken = json.load(f)

clean_fields = set(clean[0].keys())
broken_fields = set(broken[0].keys())

print("=== FORENSICS REPORT ===")

print("\nMissing Fields:")
print(clean_fields - broken_fields)

print("\nNew Fields:")
print(broken_fields - clean_fields)


from nova_client import ask_nova
from kb_reader import get_data_contract, get_past_incident

data_contract = get_data_contract()
past_incident = get_past_incident()

prompt = f"""
You are a Forensics Agent.

DATA CONTRACT:
{data_contract[:1000]}

PAST INCIDENT:
{past_incident[:1000]}

CURRENT INCIDENT

Expected fields:
{list(clean_fields)}

Actual fields:
{list(broken_fields)}

Analyze:

1. Root Cause
2. Evidence from Data Contract
3. Similarity with Past Incident
4. Business Impact
5. Recommended Fix

Keep answer concise.
"""

response = ask_nova(prompt)

print("\n=== NOVA FORENSICS ANALYSIS ===\n")

print(
    response["output"]["message"]["content"][0]["text"]
)