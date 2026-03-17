# LinkedIn URL to Domain

## Overview
This endpoint converts a company's LinkedIn URL into its associated email domain. It returns a success status with the domain or indicates if no domain was found.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/linkedin-to-domain` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company_linkedin_url` | string | The LinkedIn company profile URL |

**Example:**
```json
{
  "company_linkedin_url": "https://www.linkedin.com/company/blitz-api"
}
```

## Response

### Success (200 OK)
```json
{
  "found": true,
  "email_domain": "blitz-agency.com"
}
```

### Not Found
Returns `found: false` when no domain is located.

## Error Responses

| Status | Description |
|--------|-------------|
| **401 Unauthorized** | Missing API key, please provide a valid API key in the 'x-api-key' header |
| **402 Payment Required** | Insufficient credits balance |
| **500 Server Error** | Internal processing failures with timestamp |

## Pricing
- Free trial: 1,000 credits available
- Paid plans ($399+/month): Unlimited endpoint access
