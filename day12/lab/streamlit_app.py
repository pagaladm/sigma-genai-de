import streamlit as st
import subprocess
from pathlib import Path

st.set_page_config(
    page_title="Sigma Intelligence Platform",
    page_icon="🔴",
    layout="wide"
)

st.title("🔴 Sigma Intelligence Platform")
st.markdown("### Multi-Agent Incident Response System")

st.markdown("---")

if st.button("🚨 Run Incident Investigation"):

    with st.spinner("Running Supervisor Agent..."):
        result = subprocess.run(
            ["python3", "agents/supervisor_agent.py"],
            capture_output=True,
            text=True
        )

    st.success("Investigation Complete")

    st.subheader("Supervisor Output")
    st.code(result.stdout)

st.markdown("---")

# Incident Report
report_file = Path("reports/incident_report.md")

if report_file.exists():
    st.subheader("📄 Incident Report")

    with open(report_file, "r") as f:
        report = f.read()

    st.markdown(report)

# Knowledge Base
st.markdown("---")
st.subheader("📚 Knowledge Base Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Data Contracts")

with col2:
    st.success("Runbooks")

with col3:
    st.success("Past Incidents")