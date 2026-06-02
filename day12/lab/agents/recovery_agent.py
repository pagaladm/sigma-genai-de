import json

# Load broken data
with open("generated_data/schema_drift.json", "r") as f:
    broken_data = json.load(f)

recovered_data = []
fixed_count = 0

for record in broken_data:

    # Fix schema drift
    if "merchant_nm" in record:
        record["merchant_name"] = record.pop("merchant_nm")
        fixed_count += 1

    recovered_data.append(record)

# Save recovered data
with open("generated_data/recovered_data.json", "w") as f:
    json.dump(recovered_data, f, indent=2)

print("=== RECOVERY REPORT ===")
print(f"Records Processed: {len(broken_data)}")
print(f"Records Fixed: {fixed_count}")
print("Recovered File: generated_data/recovered_data.json")