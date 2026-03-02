# Use-Case Dossier: AEM Headless Content Delivery

**Generated:** 2026-03-01
**Owner:** Carolyn (Enterprise Architect)
**Status:** Draft — pending guardrail review

---

## Summary

Enterprise requires a scalable, channel-agnostic content delivery architecture using Adobe Experience Manager (AEM) as the content repository. Structured content must be delivered via API (GraphQL/REST) to multiple downstream consumers — web, mobile, kiosks, and emerging channels — without coupling content management to presentation layer.

---

## Top 3 Recommended Architectures

### 1. Pure Headless AEM (Content Fragments + GraphQL + CDN)

AEM serves as a headless CMS: Content Fragment Models define schema, Content Fragments hold structured content, and persisted GraphQL queries deliver JSON to any frontend via CDN.

| | |
|---|---|
| **Best for** | Multi-channel delivery, SPAs, mobile apps, IoT |
| **Pros** | Maximum channel flexibility; CDN-cacheable with persisted queries; single content source; GraphQL enables precise field selection |
| **Cons** | No WYSIWYG preview without additional tooling (Universal Editor); requires mature frontend team; higher initial implementation complexity |
| **Key components** | AEM as a Cloud Service, Content Fragment Models, GraphQL API, AEM Dispatcher, CDN (Fastly/Akamai) |

### 2. Hybrid Headful/Headless AEM

Marketing-owned pages remain headful (AEM Sites WYSIWYG with page components). Structured, reusable content — products, articles, app content — is authored as Content Fragments and delivered headlessly via GraphQL to non-web channels.

| | |
|---|---|
| **Best for** | Enterprises with both a marketing web presence and API-driven app/channel consumers |
| **Pros** | Fastest time-to-value for marketing; single platform for all content; editorial experience preserved; lower risk migration path |
| **Cons** | Governance complexity (clear ownership boundaries required); risk of content duplication between page content and fragments; two authoring paradigms to manage |
| **Key components** | AEM Sites + Content Fragments, AEM GraphQL API, Dispatcher, CDN |

### 3. AEM Headless + Edge Delivery Services (EDS)

AEM Content Fragments feed structured/API channels; document-based pages (Google Docs or SharePoint) are published via Adobe Edge Delivery Services for sub-second performance. Both content streams originate from AEM's content model.

| | |
|---|---|
| **Best for** | Organizations prioritizing Core Web Vitals, editorial simplicity, and CDN-native delivery at scale |
| **Pros** | Best-in-class delivery performance; document authoring lowers content team training burden; CDN-native by design |
| **Cons** | Newer pattern — less enterprise tooling maturity; separate authoring paradigm requires organizational change management; EDS roadmap dependency |
| **Key components** | AEM as a Cloud Service, Content Fragments, GraphQL API, AEM Edge Delivery Services, CDN |

---

## Guardrail Hits

> Source: `content/guardrails/sample.json` — AEM-specific limits

| Guardrail | Detail | Action Required |
|-----------|--------|-----------------|
| **Publish throughput** | Varies — CDN/Dispatcher dependent | Confirm expected peak RPS for content delivery endpoints; validate CDN tier |
| **Author instance limit** | Varies by contract (Cloud Service vs on-prem) | Verify AEM as a Cloud Service entitlement; confirm if upgrading from AEM 6.x |
| **Licensing gap risk** | AEM headless requires AEM as a Cloud Service (not AEM 6.x on-prem) | Verify current SKU with procurement/Panorama before architecture commitment |
| **Data residency risk** | If content delivery is global, CDN region coverage must be confirmed | Identify required delivery regions; confirm CDN PoP coverage matches |

---

## Clarifying Questions

- What downstream channels will consume headless content? (web SPA, native mobile, kiosk, voice assistant, IoT?)
- What is the expected peak requests per second (RPS) to content delivery endpoints?
- Is the current AEM deployment AEM as a Cloud Service or AEM on-premises (6.x)?
- Do content authors require WYSIWYG preview of headless content before publish?
- Are there data residency or compliance requirements (e.g., GDPR, HIPAA) for content or personalization data?
- How many Content Fragment Models and active content authors are expected?
- Is commerce platform integration required (e.g., Magento, Salesforce Commerce Cloud)?
- What frontend framework(s) will consume the GraphQL API? (React, Vue, native mobile SDK?)

---

## References

- [AEM Headless Introduction — Experience League](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/introduction)
- [Headful and Headless in AEM](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/headful-headless)
- [Content Fragments + GraphQL (Assets)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/content-fragments/content-fragments-graphql)
- [Content Delivery with GraphQL (Sites)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-delivery-with-graphql)
- [AEM Content Architect Journey](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/headless/architect/introduction)
- [AEM Headless Developer Journey](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/journeys/developer/overview)

---

*Generated by KITT — Knight Rider Intelligent Technology Team*
