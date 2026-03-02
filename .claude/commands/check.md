---
description: Run guardrail/risk check on use case
---

# /check - Run Guardrail/Risk Check

Validate a use case against product guardrails, licensing limits, and known risks. Flag issues before implementation.

## Instructions

### 1. Get Use-Case Context
Use the current use case from context (e.g., from `/match` results, a pasted description, or a file). If unclear, ask the user to provide the use-case details or point to a matched use case.

### 2. Load Guardrails
Read `content/guardrails/` (e.g., `sample.json` and any product-specific files). These define:
- Product limits (AEP RPS, AJO throughput, API rate limits)
- Licensing/entitlement constraints
- Known contractual or SLA constraints

### 3. Compare Use Case to Guardrails
For the use case, check:
- **Latency/throughput** – Does it exceed product limits?
- **Profile/event volumes** – Within known caps?
- **Licensing** – Does the customer have the required tiers?
- **Integration endpoints** – Any rate limits or constraints?
- **Risks** – Cross-reference with `content/guardrails/` risk patterns

### 4. Present Findings
Output a structured report:
- **Guardrail hits** – Where the use case exceeds or conflicts with limits (with severity)
- **Licensing gaps** – Missing entitlements to verify
- **Risks** – Top 3 risks with suggested mitigations
- **Clear to proceed?** – Summary: yes, with caveats, or no (with blockers)

### 5. Update State (optional)
If the user wants to track this check, append to `state/current.md` under "Open Threads" or "Recent Context."
