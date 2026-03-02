---
name: dossier-generation
description: Generate 1-page dossier with top-3 architectures, guardrail hits, and clarifying questions
---

# Dossier Generation Skill

## What This Skill Does

Creates a 1-page dossier summarizing a use case with top-3 recommended architectures, guardrail hits, clarifying questions, and references. Output is Markdown saved to `state/synthesized-docs/`. Optionally supports pending-review workflow for architect sign-off.

## When to Use

Claude Code will invoke this skill when:
- User asks to "generate a dossier," "create a 1-pager," or "summarize this use case"
- User runs `/dossier` command
- User wants a synthesized document for an RFP, stakeholder review, or internal reference
- After use-case matching, when user wants a formal deliverable

## How It Works

1. **Input** - Use-case details (from `/match` results, pasted description, or file). If no context, ask or suggest running `/match` first.

2. **Synthesize** - Create structured content:
   - **Summary** - Problem + desired outcome (1–2 sentences)
   - **Top 3 architectures** - Brief pros/cons for each
   - **Guardrail hits** - From `content/guardrails/` or `/check` output
   - **Clarifying questions** - From canonical template
   - **References** - Links to matched use cases, wiki pages

3. **Format** - Markdown, ~500–800 words (1 page). Structure per `content/canonical-template.md`.

4. **Save** - Write to `state/synthesized-docs/{YYYY-MM-DD}-{slug}.md`. Optionally copy to `state/synthesized-docs/pending-review/` for architect review.

5. **Output** - Present dossier to user. Offer next steps: guardrail check, RFP draft, slide summary.

## Example

```
User: "Generate a dossier for the real-time personalization use case"
Claude: [invokes dossier-generation, synthesizes from matched use cases, writes to synthesized-docs]
Result: "Dossier saved to state/synthesized-docs/2026-03-01-realtime-personalization.md. [Shows content]. Would you like an RFP draft or guardrail check?"
```

## Notes

- **MVP:** Markdown output only. PPT/Lucid export: Phase 2.
- **References:** Use links from `state/matched-use-cases.md` when available.
- **Guardrails:** Run `/check` first if guardrail hits are unknown, or use cached results.
