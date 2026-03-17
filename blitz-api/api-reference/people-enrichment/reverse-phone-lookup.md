# Reverse Phone Lookup

## Overview
The Reverse Phone Lookup endpoint identifies professionals and retrieves their complete profile using a verified phone number.

**Note:** This feature is **US numbers only**.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/phone-to-person` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `phone` | string | Phone number (format: '+1234567890') |

**Example:**
```json
{
  "phone": "+1234567890"
}
```

## Response (200 OK)

Returns a JSON object containing:

| Field | Type | Description |
|-------|------|-------------|
| `found` | boolean | Whether the phone matches a professional profile |
| `person` | object | Profile data (see below) |

### Person Object
- Name fields (`first_name`, `last_name`, `full_name`, `nickname`)
- Professional headline and biography
- Location (`city`, `state_code`, `country_code`, `continent`)
- LinkedIn URL and connection count
- Profile picture URL
- Work experiences with job details and timeline
- Education, skills, and certifications arrays

## Error Responses

| Status | Description |
|--------|-------------|
| **401 Unauthorized** | Missing API key, please provide a valid API key |
| **402 Payment Required** | Insufficient credits balance |
| **500 Server Error** | Controlled error with timestamp |

## Pricing
- Unlimited requests on paid plans ($399+/month)
- Free trial accounts receive 1,000 credits
