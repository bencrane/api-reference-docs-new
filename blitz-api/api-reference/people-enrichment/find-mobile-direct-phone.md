# Find Mobile & Direct Phone

## Overview
The endpoint retrieves direct mobile phone numbers from LinkedIn profile URLs.

**Important Limitations:**
- Geographic restriction to **US contacts only**
- Requires specific paid plan tier ($599/mo minimum)

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/phone` |
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
```json
{
  "found": true,
  "phone": "+1234567890"
}
```

## Error Responses

| Status | Description |
|--------|-------------|
| **401** | Missing API key, please provide a valid API key in the 'x-api-key' header |
| **402** | Insufficient credits balance |
| **500** | Server error with timestamp |

## Pricing
- Paid plans ($399+/mo) offer unlimited endpoint access
- Free trials provide 1,000 credits
- Phone enrichment requires Unlimited Phone Numbers plan ($599/mo)

**API Key Acquisition:** Available at https://app.blitz-api.ai
