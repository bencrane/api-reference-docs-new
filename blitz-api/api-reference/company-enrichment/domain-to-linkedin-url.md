# Domain to LinkedIn URL

## Overview
This endpoint converts a website domain into a corresponding Company LinkedIn URL, serving as the foundational step when working with domain-only source data.

## Key Purpose
The API enables users to resolve domains to LinkedIn company URLs, which are required inputs for downstream features like Waterfall ICP, Employee Finder, and Company Enrichment services.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/domain-to-linkedin` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `domain` | string | Website domain in URL format |

**Example:**
```json
{
  "domain": "https://www.blitz-agency.com"
}
```

## Response

### Success (200 OK)
Returns JSON with boolean `found` status and `company_linkedin_url` string when a match is located.

```json
{
  "found": true,
  "company_linkedin_url": "https://www.linkedin.com/company/blitz-api"
}
```

## Error Responses

| Status | Description |
|--------|-------------|
| **402 Payment Required** | Insufficient credits balance |
| **422 Unprocessable Entity** | Input validation failures (e.g., missing domain field) |
| **500 Internal Server Error** | Server-side processing issues with timestamp |

## Pricing & Credits
Free trial accounts receive 1,000 credits. Paid plans ($399+/month) offer unlimited endpoint access.
