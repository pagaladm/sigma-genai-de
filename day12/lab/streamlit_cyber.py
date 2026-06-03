import streamlit as st
import subprocess
from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Sigma Command Center",
    page_icon="🚨",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main-header{
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:#ff4b4b;
}

.sub-header{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.kpi-card{
    background-color:#111827;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #374151;
}

.agent-box{
    background:#1f2937;
    padding:15px;
    border-radius:12px;
    border-left:5px solid #10b981;
    margin-bottom:10px;
}

.success-box{
    background:#0f5132;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-header">🚨 SIGMA COMMAND CENTER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-header">AI Powered Multi-Agent Incident Response Platform</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🤖 Agents Active", "4")

with c2:
    st.metric("📚 Knowledge Docs", "24")

with c3:
    st.metric("🚨 Incident Type", "Schema Drift")

with c4:
    st.metric("✅ System Status", "Recovered")

st.divider()

# --------------------------------------------------
# MAIN LAYOUT
# --------------------------------------------------
left, right = st.columns([2, 1])

# --------------------------------------------------
# LEFT SIDE
# --------------------------------------------------
with left:

    st.subheader("🎯 Incident Overview")

    st.info("""
    **Current Incident**
    
    A schema drift was detected in the Sigma transaction pipeline.
    
    Column renamed:
    
    `merchant_name ➜ merchant_nm`
    
    Recovery workflow executed successfully.
    """)

    st.subheader("📈 Agent Execution Timeline")

    st.progress(100, text="🔍 Forensics Agent Completed")

    st.progress(100, text="💰 Impact Agent Completed")

    st.progress(100, text="🔧 Recovery Agent Completed")

    st.progress(100, text="📄 Report Agent Completed")

# --------------------------------------------------
# RIGHT SIDE
# --------------------------------------------------
with right:

    st.subheader("🤖 Agent Status")

    st.success("🟢 Supervisor Agent")

    st.success("🟢 Forensics Agent")

    st.success("🟢 Impact Agent")

    st.success("🟢 Recovery Agent")

    st.success("🟢 Report Agent")

    st.subheader("🕒 Last Investigation")

    st.code(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.divider()

# --------------------------------------------------
# RUN BUTTON
# --------------------------------------------------
st.subheader("🚀 Investigation Control")

if st.button("Run Investigation", use_container_width=True):

    with st.spinner("Supervisor Agent coordinating investigation..."):

        result = subprocess.run(
            ["python3", "agents/supervisor_agent.py"],
            capture_output=True,
            text=True
        )

    st.success("Investigation Completed")

    st.subheader("Supervisor Output")

    if result.stdout:
        st.code(result.stdout)

    if result.stderr:
        st.error(result.stderr)

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    [
        "🔍 Forensics",
        "💰 Impact Analysis",
        "📚 Knowledge Base"
    ]
)

# --------------------------------------------------
# FORENSICS TAB
# --------------------------------------------------
with tab1:

    st.error("""
    ### Root Cause Analysis

    Schema Drift Detected

    merchant_name
         ↓
    merchant_nm

    Impact:
    Downstream ETL Failure
    """)

    report_path = Path("reports/incident_report.md")

    if report_path.exists():

        st.subheader("Latest Incident Report")

        with open(report_path) as f:
            st.markdown(f.read())

# --------------------------------------------------
# IMPACT TAB
# --------------------------------------------------
with tab2:

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "QuickMart Threshold",
            "₹50,000",
            "Exceeded"
        )

    with col2:
        st.metric(
            "FuelPlus Threshold",
            "₹1,00,000",
            "Exceeded"
        )

    st.warning("""
    ### Potential SLA Breach

    - QuickMart impacted
    - FuelPlus impacted
    - Escalation triggered
    """)

# --------------------------------------------------
# KNOWLEDGE BASE TAB
# --------------------------------------------------
with tab3:

    kb_files = [
        "knowledge_base/data_contracts/sigma_transactions_v1.md",
        "knowledge_base/runbooks/kinesis_replay_runbook.md",
        "knowledge_base/past_incidents/incident_001.md",
        "knowledge_base/sla_contracts/quickmart_sla.md"
    ]

    for file in kb_files:

        if Path(file).exists():

            with st.expander(f"📄 {Path(file).name}"):

                with open(file) as f:
                    st.markdown(f.read()[:3000])