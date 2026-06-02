import subprocess

print("=" * 60)
print("SIGMA INTELLIGENCE PLATFORM - SUPERVISOR")
print("=" * 60)

print("\n[1/4] Running Forensics Agent...")
subprocess.run(["python3", "agents/forensics_agent.py"])

print("\n[2/4] Running Impact Agent...")
subprocess.run(["python3", "agents/impact_agent.py"])

print("\n[3/4] Running Recovery Agent...")
subprocess.run(["python3", "agents/recovery_agent.py"])

print("\n[4/4] Running Incident Report Agent...")
subprocess.run(["python3", "agents/incident_report_agent.py"])

print("\n" + "=" * 60)
print("INCIDENT WORKFLOW COMPLETE")
print("Report: reports/incident_report.md")
print("=" * 60)