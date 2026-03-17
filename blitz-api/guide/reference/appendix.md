# Reference & Standards

## Endpoint Overview

The BlitzAPI v2 API uses base URL: `https://api.blitz-api.ai`

Most endpoints use POST requests, except `/v2/account/key-info` which uses GET.

### Search Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/search/waterfall-icp-keyword` | POST | Waterfall ICP keyword discovery |
| `/v2/search/employee-finder` | POST | Employee finder with filters |
| `/v2/search/companies` | POST | Company search |

### Enrichment Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/enrichment/email` | POST | Email from LinkedIn profile |
| `/v2/enrichment/phone` | POST | Phone from LinkedIn profile (US only) |
| `/v2/enrichment/email-to-person` | POST | Person profile from email |
| `/v2/enrichment/phone-to-person` | POST | Person profile from phone |
| `/v2/enrichment/company` | POST | Company enrichment |
| `/v2/enrichment/domain-to-linkedin` | POST | Domain to LinkedIn URL |
| `/v2/enrichment/linkedin-to-domain` | POST | LinkedIn URL to domain |

### Utility Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/utilities/email/validate` | POST | Email validation |
| `/v2/utilities/current-date` | POST | Timezone date retrieval |
| `/v2/account/key-info` | GET | API key health check |

> **Note:** All search functionality requires a Company LinkedIn URL as input (not a domain).

## Geographic Standards

BlitzAPI utilizes ISO 3166-1 alpha-2 country codes consistent with LinkedIn.

### Common Country Codes
| Code | Country |
|------|---------|
| US | United States |
| GB | United Kingdom |
| FR | France |
| CA | Canada |
| DE | Germany |
| AU | Australia |
| IN | India |
| BR | Brazil |
| SG | Singapore |

The system accepts `"WORLD"` for unrestricted global searches.

## Email Data Philosophy

The API distinguishes itself through verified identity matching rather than pattern generation.

> **Principle:** "We only return an email if we have a concrete record of it linked to that specific individual."

### Data Freshness
- Database records undergo revalidation every 30 days minimum
- Bounced addresses removed immediately
- No pattern-based email guessing

## Performance Requirements

| Metric | Value |
|--------|-------|
| Concurrency | 5 concurrent requests per second (all plans) |
| Recommended Timeouts | 10-20 seconds depending on operation |
| Rate Limit Response | 429 errors require 60+ second delays before retry |

## Error Handling

| Status | Meaning | Remediation |
|--------|---------|-------------|
| 401 Unauthorized | Missing or invalid API key | Check `x-api-key` header |
| 402 Payment Required | Insufficient credits/wrong plan | Upgrade plan or wait for reset |
| 422 Unprocessable Entity | Invalid input | Check request body format |
| 429 Too Many Requests | Rate limit exceeded | Wait 60+ seconds, implement backoff |
| 500 Internal Server Error | Server-side issue | Retry with exponential backoff |
