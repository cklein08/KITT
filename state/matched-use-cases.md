# Matched Use Cases

<!-- KITT stores use-case matches and supporting links here -->

Last updated: 2026-03-01

## Recent Matches

### 2026-03-01 — Headless Content Delivery with AEM

| # | Use Case | Source | Relevance | Link |
|---|----------|--------|-----------|------|
| 1 | AEM Headless: Content Fragments + GraphQL API for Multi-Channel Delivery | Adobe Experience League | High | [Link](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/introduction) |
| 2 | Hybrid Headful/Headless AEM Architecture | Adobe Experience League | High | [Link](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/headful-headless) |
| 3 | Persisted Queries + Dispatcher/CDN Caching for Production Headless | Adobe Experience League | High | [Link](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-fragments/content-fragments-graphql) |
| 4 | AEM Headless + Commerce Integration (Magento / Salesforce CC) | EnFuse Solutions | Medium | [Link](https://www.enfuse-solutions.com/headless-aem-decoupling-content-and-delivery-for-microservices-architectures/) |
| 5 | AEM Content Architect Journey: Content Fragment Modeling | Adobe Experience League | Medium | [Link](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/headless/architect/introduction) |

**Notes:**
- Primary pattern: Content Fragment Models → Content Fragments → GraphQL API → JSON → any frontend
- Enterprise standard (2025-2026): Hybrid architecture — headful for marketing pages, headless for data-rich/custom experiences
- Production requirement: Use persisted queries (HTTP GET) + CDN caching — do not expose raw GraphQL to clients
- Schema gaps to fill before dossier: `customerProfile.vertical`, `dataVolumes`, `licensingEntitlements`

## Stored Links

- [AEM Headless Introduction (Experience League)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/introduction)
- [Headful and Headless in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/headful-headless)
- [Content Fragments + GraphQL (Assets)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-fragments/content-fragments-graphql)
- [Content Delivery with GraphQL (Sites)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-delivery-with-graphql)
- [AEM Content Architect Journey](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/headless/architect/introduction)
- [AEM Headless Developer Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/journeys/developer/overview)
- [Headless AEM for Microservices (EnFuse)](https://www.enfuse-solutions.com/headless-aem-decoupling-content-and-delivery-for-microservices-architectures/)

---

*This file is updated by KITT when use-case matching is run.*
