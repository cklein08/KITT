---
description: Generate 1-page dossier with top-3 architectures
---

# /dossier - Generate 1-Page Dossier

Create a 1-page dossier summarizing the use case with top-3 recommended architectures and clear guardrail hits.

## Instructions

### 1. Get Use-Case Context
Use the current use case from context (e.g., from `/match` results, a pasted description, or a file). If unclear, ask the user to provide the use-case details.

If no matches exist, consider running `/match` first to find similar use cases for reference.

### 2. Synthesize Content
- Summarize the use case (problem, desired outcome, key constraints)
- Propose **top 3 recommended architectures** with brief pros/cons
- Include **guardrail hits** from `content/guardrails/` (or run `/check` if not yet done)
- Add **clarifying questions** the agent should ask (from canonical template)
- Keep to **1 page** (approx. 500–800 words)

### 3. Output Format
Write the dossier in Markdown. Structure:
```markdown
# Use-Case Dossier: {Title}

## Summary
{1-2 sentences}

## Top 3 Recommended Architectures
1. **{Name}** – {brief description}, Pros: ..., Cons: ...
2. **{Name}** – ...
3. **{Name}** – ...

## Guardrail Hits
- {limit/risk 1}
- {limit/risk 2}

## Clarifying Questions
- {question 1}
- {question 2}

## References
- {link 1}
- {link 2}
```

### 4. Save to State
Save the dossier to `state/synthesized-docs/{YYYY-MM-DD}-{slug}.md` (e.g., `state/synthesized-docs/2026-03-01-realtime-personalization.md`).

Optionally copy to `state/synthesized-docs/pending-review/` if architect sign-off is required.

### 5. Confirm
Present the dossier to the user and confirm: "Dossier saved. Would you like me to run a guardrail check or generate an RFP draft?"
