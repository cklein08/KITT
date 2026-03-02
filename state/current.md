# Current State

Last updated: 2026-03-01

## Active Priorities

1. Headless content delivery use cases for Adobe Experience Manager (AEM)
   - Dossier drafted: `state/synthesized-docs/2026-03-01-aem-headless-content-delivery.md`
   - Status: Pending customer entitlement and licensing confirmation before presenting

## Open Threads

- **[BLOCKER]** Confirm AEM as a Cloud Service entitlement with customer (blocks all headless architectures)
- **[BLOCKER]** Confirm licensed SKU includes Content Fragments + GraphQL delivery (Panorama check)
- Capture expected peak RPS to validate CDN tier
- Identify delivery regions; confirm CDN PoP coverage and data residency requirements
- Customer conversation: ask 4 clarifying questions (platform, SKU, RPS, delivery regions)

## Recent Context

- KITT setup completed on 2026-03-01
- Integrations configured: EasyMCP Adobe Wiki Confluence, KITT voice (TTS)
- /match (2026-03-01): 5 AEM headless matches found; stored in matched-use-cases.md
- /dossier (2026-03-01): 3-architecture dossier generated; Pure Headless primary, Hybrid lowest-risk
- /check (2026-03-01): 2 blockers, 1 security hard-requirement (persisted queries only in prod), 1 data residency gap
- Persisted queries mandated as production non-negotiable; raw GraphQL blocked at design phase

---

*This file is updated by KITT at the end of each session.*
