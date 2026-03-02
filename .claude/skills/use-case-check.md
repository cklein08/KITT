---
name: use-case-check
description: Validate use case against product guardrails, licensing limits, and known risks
---

# Use-Case Check Skill

## What This Skill Does

Validates a use case against product guardrails (AEP RPS, AJO throughput, API limits), licensing/entitlement constraints, and known risk patterns. Flags issues before implementation so the EA team can address them early.

## When to Use

Claude Code will invoke this skill when:
- User asks to "check guardrails," "validate this use case," or "run a risk check"
- User runs `/check` command
- User asks "will this work with our AEP limits?" or "what are the licensing gaps?"
- After use-case matching, when user wants to verify feasibility

## How It Works

1. **Input** - Use-case details (from `/match` results, pasted description, or file). If missing, ask the user.

2. **Load Guardrails** - Read `content/guardrails/` (e.g., `sample.json`, product-specific files). These define:
   - Product limits (RPS, throughput, API rate limits)
   - Licensing/entitlement requirements
   - Contractual or SLA constraints
   - Known risk patterns

3. **Compare** - For the use case, check:
   - Latency/throughput vs product limits
   - Profile/event volumes vs caps
   - Licensing tiers vs required entitlements
   - Integration endpoints vs rate limits
   - Risk patterns from guardrails

4. **Output** - Structured report:
   - **Guardrail hits** (with severity)
   - **Licensing gaps**
   - **Top 3 risks** with mitigations
   - **Clear to proceed?** (yes / with caveats / no)

5. **Update State** (optional) - Append to `state/current.md` if user wants to track.

## Example

```
User: "Check if this use case will work with our AEP setup"
Claude: [invokes use-case-check, loads guardrails, compares, presents report]
Result: "Guardrail check complete. 2 hits: (1) Peak RPS 2000 exceeds AEP limit of 1500; (2) Profile count requires Enterprise tier. Mitigations: [list]. Clear to proceed? With caveats."
```

## Notes

- **Requires:** `content/guardrails/` with product limits. Start with `sample.json`.
- **TODO:** Panorama integration for live entitlement lookup (future enhancement).
- If guardrails are incomplete, note "Partial check - verify X manually."
