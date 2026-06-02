import sys
sys.path.append(".")
from nova_client import ask_nova
import os

prompt = """
Create an incident report using these findings:

FORENSICS:
- Root Cause: Schema Drift
- merchant_name was renamed to merchant_nm

IMPACT:
- Records Affected: 100
- GMV Impact Analysis Completed

RECOVERY:
- Records Fixed: 100
- merchant_nm renamed back to merchant_name
- Recovery successful

Generate a report with:

1. Summary
2. Root Cause
3. Business Impact
4. Recovery Actions
5. Prevention Recommendations

Use markdown format.
"""

response = ask_nova(prompt)

report_text = response["output"]["message"]["content"][0]["text"]

os.makedirs("reports", exist_ok=True)

with open("reports/incident_report.md", "w") as f:
    f.write(report_text)

print("=== INCIDENT REPORT GENERATED ===")
print("Saved: reports/incident_report.md")