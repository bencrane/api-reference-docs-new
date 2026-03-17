# Find Work Email

## Overview
The Find Work Email endpoint retrieves verified work email addresses from LinkedIn profile URLs. Access requires an "Unlimited Email" plan ($499/mo) or higher tier.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/email` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `person_linkedin_url` | string | LinkedIn profile URL |

**Example:**
```json
{
  "person_linkedin_url": "https://www.linkedin.com/in/antoine-blitz-5581b7373"
}
```

## Response

### Success (200 OK)
Returns an object containing:

| Field | Type | Description |
|-------|------|-------------|
| `found` | boolean | Indicates email availability |
| `email` | string | Primary verified work email address |
| `all_emails` | array | Associated emails with metadata |

Each email in `all_emails` includes:
- `job_order_in_profile`: Position in person's job history
- `company_linkedin_url`: Associated company LinkedIn URL
- `email_domain`: Email address domain

**Example:**
```json
{
  "found": true,
  "email": "antoine@blitz-agency.com",
  "all_emails": [
    {
      "email": "antoine@blitz-agency.com",
      "job_order_in_profile": 1,
      "company_linkedin_url": "https://www.linkedin.com/company/blitz-api",
      "email_domain": "blitz-agency.com"
    }
  ]
}
```

## Error Responses

| Status | Description |
|--------|-------------|
| **401 Unauthorized** | Missing or invalid API key in headers |
| **402 Payment Required** | Insufficient account credits |
| **500 Internal Server Error** | Server-side processing failure with timestamp |
