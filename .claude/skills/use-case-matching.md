---
name: use-case-matching
description: Search Adobe Wiki for use-case docs, validate against canonical schema, rank and return matches with supporting links
---

# Use-Case Matching Skill

## What This Skill Does

Searches for similar use cases in Adobe Wiki Confluence, validates content against the canonical schema, and returns ranked matches with supporting links. Used when the user wants to find similar use cases, match a new use case to existing ones, or discover reference documentation.

## When to Use

Claude Code will invoke this skill when:
- User asks to "find similar use cases," "match this use case," or "search for use-case docs"
- User provides a use-case description and wants to find related documentation
- User runs `/match` command
- User asks "what use cases are similar to X?" or "find me references for this architecture"

## How It Works

1. **Input** - Use-case description (from user message, pasted text, or file). If missing, ask the user.

2. **Search** - Call EasyMCP Adobe Wiki Confluence tools:
   - `search_wiki_content` with CQL or text query based on the use-case description
   - Search for: use-case docs, product guardrails, RFPs, architecture docs
   - Limit to 10–20 results for relevance

3. **Fetch** - For top results, call `get_wiki_content` with page URL. Optionally use `extract_assets` with `asset_types: ["lucidchart"]` for diagrams.

4. **Validate** - Compare content to `content/canonical-schema.json`. Note schema alignment and completeness.

5. **Rank** - Rank by relevance (semantic fit, schema alignment, recency). Return top 3–5.

6. **Output** - Present table of matches with links. Update `state/matched-use-cases.md`.

## Example

```
User: "Find use cases similar to real-time personalization for logged-in users"
Claude: [invokes use-case-matching, searches wiki, fetches top pages, ranks, presents table]
Result: "I've located 3 similar use cases. [Table with links]. Would you like a dossier for the top match?"
```

## Notes

- **Primary source:** EasyMCP Adobe Wiki Confluence. Must be configured in `.cursor/mcp.json`.
- **TODO:** Vector DB semantic search (Phase 2) for improved ranking when embeddings are available.
- If Adobe Wiki is unavailable, fall back to local `content/use-case-examples/` and web search.
