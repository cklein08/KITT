---
description: Run use-case matching - search wiki, validate, rank matches
---

# /match - Run Use-Case Matching

Search for similar use cases, validate against the canonical schema, and return ranked matches with supporting links.

## Instructions

### 1. Get User Input
Ask the user what use case they want to match, or use the current context (e.g., a use-case description they've shared, or text from a recent document).

If no context exists, prompt: "Describe the use case you'd like to match, or paste the relevant text."

### 2. Search Adobe Wiki (Primary)
**Use EasyMCP Adobe Wiki Confluence first:**
- Call `search_wiki_content` with a CQL or text query based on the use-case description
- Search for: use-case docs, product guardrails, RFPs, architecture docs
- Limit results (e.g., 10–20) for relevance

### 3. Fetch and Validate
For top results:
- Call `get_wiki_content` with the page URL to fetch full content
- Optionally use `extract_assets` with `asset_types: ["lucidchart"]` if diagrams are needed
- Validate content against the canonical schema (`content/canonical-schema.json`) where applicable

### 4. Rank and Present
- Rank matches by relevance (semantic similarity, schema alignment, recency)
- Present top 3–5 matches in a table:
  | Use Case | Source | Relevance | Link |
  |----------|--------|-----------|------|
- Include brief notes on why each match is relevant

### 5. Update State
Append matches to `state/matched-use-cases.md` with links and timestamps.

### 6. Offer Next Steps
- "Would you like a 1-page dossier for the top match?" → suggest `/dossier`
- "Should I run a guardrail check?" → suggest `/check`
