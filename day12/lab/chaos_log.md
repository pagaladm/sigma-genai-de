# Chaos Log — Team Name: Sigma Intelligence Platform by diksha

## Day 12 | Wednesday 4 June 2026

---

## Pre-Exercise Answer (fill before Phase 1)

**Question:** Should the 9 tool functions be one Lambda or separate Lambdas? What breaks if they are one?

**Answer:**

The 9 tool functions should be separate Lambdas.

Benefits:

* Better scalability
* Easier debugging
* Independent permissions
* Lower blast radius during failures
* Easier maintenance

If all tools are placed inside one Lambda:

* A single failure affects all tools
* Debugging becomes difficult
* Deployments become riskier
* Permissions become overly broad

---

## Phase 2 — Manual Investigation

**Records in Kinesis (02:00–02:20 UTC):** 100 records sent

**Records in S3 (02:00–02:20 UTC):** 1 file, ~20 KB total

**Records in Snowflake (02:00–02:20):** 0 rows loaded

---

**Failure timestamp:** 02:12 UTC

**What changed at that timestamp:**

The incoming schema changed from:

merchant_name

to:

merchant_nm

**Root cause (your hypothesis):**

Schema drift caused downstream validation failures because the incoming records no longer matched the expected data contract.

**Why no alert fired:**

No schema validation alarm existed in the pipeline.

**Time taken to find this:** 30 minutes

---

**Signals you connected:**

* Data contract schema
* Generated transaction records
* Schema drift dataset
* Incident report output

**Signal you missed (fill this in Phase 3 after seeing the agent output):**

Past incident similarity stored in the knowledge base.

---

## Phase 3 — Comparison

**What I found (Phase 2 manual):**

* Time taken: 30 minutes
* Root cause found? Yes
* SLA breach identified? Partial
* Prevention created? No

**What the agent found (Phase 3):**

* Time taken: 30 seconds
* Root cause found? Yes
* SLA breach identified? Yes
* Prevention created? Yes (3 live alarms)

**What I missed that the agent caught:**

The agent matched the current incident with a previous incident stored in the knowledge base and used SLA contracts to determine notification requirements.

**Why the agent caught it:**

The agent used Retrieval Augmented Generation (RAG) with:

* Data Contracts
* SLA Contracts
* Runbooks
* Past Incidents

---

## Judgment Questions

**Forensics Agent:**
*The agent found the root cause by correlating Lambda version history with Snowflake query history. What is the one CloudWatch alarm that would have caught this at 02:12 instead of 09:03? Write it as a metric alarm definition.*

Answer:

Alarm Name: SchemaLoadFailureAlarm

Condition:

* Records arriving > 0
* Snowflake rows loaded = 0
* Duration > 5 minutes

Action:

* Trigger SNS notification
* Open incident ticket
* Notify on-call engineer

---

**Recovery Agent:**
*The recovery used transaction_id as the idempotency key. What happens if a legitimate duplicate transaction_id exists in the source data? How would you change the deduplication logic?*

Answer:

A legitimate duplicate transaction_id would be incorrectly skipped during recovery.

To avoid this, use a composite key:

transaction_id + transaction_date + customer_id

This uniquely identifies records while preventing accidental data loss.

---

**Hardening Agent:**
*The sigma-lambda-version-change alarm fires on any Lambda error spike after a version change. Your team deploys 20 Lambda functions per day in prod. Would you keep this alarm? If yes, how do you stop it from spamming? If no, what replaces it?*

Answer:

I would keep the alarm but reduce noise.

Improvements:

* Trigger only for production aliases
* Require sustained error rate for 5 minutes
* Combine deployment events with business metrics
* Suppress alerts during approved deployment windows

This reduces alert fatigue while maintaining protection.

---

## Your Honest Reflection

**Which part of the manual investigation took longest and why:**

Finding the root cause took the longest because I had to compare the expected schema with the incoming data and manually identify the field mismatch.

**What would have happened if this hit prod at 2 AM with no agents:**

The issue could have remained undetected for several hours, causing delayed reporting, SLA violations, and incorrect business metrics.

**One thing you would add to this platform that none of the 6 agents currently do:**

A predictive anomaly detection agent that learns historical pipeline behavior and warns about potential failures before they occur.
