# Company Enrichment

## Overview
The Company Enrichment endpoint retrieves comprehensive company profiles from LinkedIn URLs.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/company` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company_linkedin_url` | string | LinkedIn company profile URL |

**Example:**
```json
{
  "company_linkedin_url": "https://www.linkedin.com/company/blitz-api"
}
```

## Response Data

Successful responses (200 status) include:
- LinkedIn URL and ID
- Company name and description
- Industry classification
- Company type and size
- Employee count on LinkedIn
- Headquarters location (city, country code, country name)
- Website domain and full URL
- Followers count
- Founded year
- Specialties

## Error Responses

| Status | Description |
|--------|-------------|
| **401** | Invalid API key, please provide a valid API key in the 'x-api-key' header |
| **404** | Not Found |
| **429** | Rate limit exceeded, please try again later |

## Pricing
All endpoints are unlimited on paid plans ($399+/mo). Free trial accounts receive 1,000 credits.
