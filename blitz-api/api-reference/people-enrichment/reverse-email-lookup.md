# Reverse Email Lookup

## Overview
The **Reverse Email Lookup** endpoint identifies professionals and retrieves their full profile using a verified work email address.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/enrichment/email-to-person` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `email` | string | Professional work email address |

**Example:**
```json
{
  "email": "antoine@blitz-agency.com"
}
```

## Response (200 OK)

Returns a person object with:

### Core Information
- `first_name`, `last_name`, `full_name`, `nickname`, `civility_title`
- `headline`: Professional summary
- `about_me`: Bio excerpt
- `linkedin_url`: LinkedIn profile link
- `connections_count`: Network size
- `profile_picture_url`: Photo URL

### Location Data
- `city`, `state_code`, `country_code`, `continent`

### Professional History
`experiences[]` array containing:
- `job_title`, `job_description`
- `company_linkedin_url`, `company_linkedin_id`
- `job_start_date`, `job_end_date`, `job_is_current`
- `job_location` details

### Additional Arrays
- `education[]`
- `skills[]`
- `certifications[]`

## Error Responses

| Status | Description |
|--------|-------------|
| **401** | Missing API key, please provide a valid API key in the 'x-api-key' header |
| **402** | Insufficient credits balance |
| **500** | Internal server error with timestamp |

## Pricing
Paid plans ($399+/month) offer unlimited requests; free trials include 1,000 credits.
