import json
# Read SLA contracts
with open("knowledge_base/sla_contracts/quickmart_sla.md") as f:
    quickmart_sla = f.read()

with open("knowledge_base/sla_contracts/fuelplus_sla.md") as f:
    fuelplus_sla = f.read()
with open("generated_data/clean_transactions.json") as f:
    clean = json.load(f)

with open("generated_data/schema_drift.json") as f:
    broken = json.load(f)

clean_count = len(clean)
broken_count = len(broken)

clean_gmv = sum(r["amount"] for r in clean)
broken_gmv = sum(r["amount"] for r in broken)

print("=== IMPACT REPORT ===")
print(f"Expected Records: {clean_count}")
print(f"Actual Records: {broken_count}")

print(f"\nExpected GMV: ₹{clean_gmv:,.2f}")
print(f"Actual GMV: ₹{broken_gmv:,.2f}")

print(f"\nGMV Gap: ₹{clean_gmv - broken_gmv:,.2f}")

# SLA thresholds from knowledge base
QUICKMART_THRESHOLD = 50000
FUELPLUS_THRESHOLD = 100000

gmv_gap = abs(clean_gmv - broken_gmv)

print("\n=== SLA ANALYSIS ===")

if gmv_gap > QUICKMART_THRESHOLD:
    print("QuickMart SLA Breach: YES")
    print("Notification Required: Within 2 hours")
else:
    print("QuickMart SLA Breach: NO")

if gmv_gap > FUELPLUS_THRESHOLD:
    print("FuelPlus SLA Breach: YES")
    print("Notification Required: Within 4 hours")
else:
    print("FuelPlus SLA Breach: NO")