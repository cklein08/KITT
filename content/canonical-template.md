# Canonical Use-Case Template (Fillable)

Each field has a short instruction — keep entries concise and factual.

---

## 1. Use-case ID & Title

- **ID:** (auto-generated)
- **Title:** Short, descriptive (10 words max) e.g., "Real-time personalization for logged-in users"

## 2. Summary (1–2 sentences)

- High-level what and why. (Problem + desired outcome) e.g., "Serve personalized content to logged-in users within 200ms to increase CTR by 10%."

## 3. Business context & objectives

- Primary business driver(s) (growth, retention, cost reduction)
- Success metrics (KPIs & targets) e.g., "Increase CTR +10%, reduce manual segmentation by 80%."

## 4. Customer profile & constraints

- Vertical, company size, regions
- Relevant constraints: legal, compliance, data residency

## 5. Current state (if applicable)

- Existing architecture summary (products, integrations, on-prem/cloud)
- Data sources, volumes, frequency (events/day, peak RPS)

## 6. Desired state / scope

- Products expected (AEM, AEP, AJO, etc.)
- Functional scope (what must the solution do?)
- Non-functional requirements (latency, availability, throughput) e.g., "<200ms response, 99.95% availability, ingest 50M events/day"

## 7. Key technical details (structured)

- Data types (events, profiles, content) & retention
- Estimated ingest rate (avg/peak RPS)
- Expected profile count and segment sizes
- Integration endpoints (3rd-party systems, APIs)

## 8. Licensing & entitlements (known)

- Current licenses/tiers owned per product (versions where relevant)
- Gaps/unknowns to verify

## 9. Guardrails & hard limits to check

- Known product limits (e.g., AEP RPS, AJO throughput, API rate limits)
- Any contractual or SLA constraints

## 10. Risks & mitigation ideas

- Top 3 risks (technical, operational, security)
- Suggested mitigations or alternative approaches

## 11. Historical references & similar use-cases

- Links/IDs to 2–3 similar canonical use-cases or case studies
- Notes on differences

## 12. Implementation effort estimate (ballpark)

- Dev effort (low/med/high + estimated weeks)
- Infra or licensing changes required

## 13. Required clarifying questions (for intake)

- Auto-generated list of the most important follow-ups the agent should ask e.g., "Is anonymized PII allowed for profile stitching?"; "What is peak monthly concurrency?"

## 14. Desired outputs from the AI agent (checklist)

- 1-page dossier (Y/N)
- Top-3 recommended architectures (Y/N)
- RFP answer draft (Y/N)
- Slide summary (Y/N)
- Lucid diagram (Y/N)

## 15. Implementation notes & post-mortem (living fields)

- Implementation start/end dates
- Actual issues encountered (short bullets)
- Final outcomes vs targets (KPIs)

## 16. Provenance & attachments

- Source docs (links) — architecture diagrams, RFP text, product docs
- Meeting recordings/transcripts (links)

## 17. Owner & reviewers

- Use-case owner (name, email)
- SME reviewers (names/emails)
