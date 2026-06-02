import os

def read_kb_document(path):
    with open(path, "r") as f:
        return f.read()

def get_data_contract():
    return read_kb_document(
        "knowledge_base/data_contracts/sigma_transactions_v1.md"
    )

def get_runbook():
    return read_kb_document(
        "knowledge_base/runbooks/kinesis_replay_runbook.md"
    )

def get_past_incident():
    return read_kb_document(
        "knowledge_base/past_incidents/incident_001.md"
    )

if __name__ == "__main__":

    print("=== DATA CONTRACT ===")
    print(get_data_contract()[:300])

    print("\n=== RUNBOOK ===")
    print(get_runbook()[:300])

    print("\n=== PAST INCIDENT ===")
    print(get_past_incident()[:300])