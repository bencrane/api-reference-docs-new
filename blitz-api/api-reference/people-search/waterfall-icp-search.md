# Waterfall ICP Search

## Overview
This endpoint identifies optimal decision-makers at target companies using a prioritized cascade hierarchy that attempts each tier sequentially until reaching `max_results`.

## Key Characteristics

| Feature | Value |
|---------|-------|
| **Response Structure** | Person data nested in `results[].person` (differs from Employee Finder) |
| **Metrics** | `icp` indicates cascade tier (1=highest priority); `ranking` shows overall relevance (1=most relevant) |
| **Performance** | Sub-600ms latency |
| **Rate Limit** | 5 requests/second across all plans |
| **Max Results** | 25 contacts per query |

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/search/waterfall-icp-keyword` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |

## Request Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company_linkedin_url` | string | Full LinkedIn company URL (URI format) |
| `cascade` | array | Ordered array of search tiers (minimum 1 item, maximum 8) |

### Cascade Tier Options

Each tier includes:

| Field | Type | Description |
|-------|------|-------------|
| `include_title` | array | Job titles to match (supports partial matching) |
| `exclude_title` | array | Keywords that disqualify candidates |
| `location` | array | LinkedIn country codes or "WORLD" for global scope |
| `include_headline_search` | boolean | Extend search into LinkedIn headline text |

### Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `max_results` | number | Default 1, maximum 25 |

## Example Request

```json
{
  "company_linkedin_url": "https://www.linkedin.com/company/openai",
  "cascade": [
    {
      "include_title": ["CMO", "Chief Marketing Officer"],
      "exclude_title": ["assistant", "intern"],
      "location": ["WORLD"],
      "include_headline_search": false
    },
    {
      "include_title": ["VP Marketing", "Head of Marketing"],
      "exclude_title": ["assistant"],
      "location": ["US", "GB"],
      "include_headline_search": true
    }
  ],
  "max_results": 5
}
```

## Response Fields

Each result includes:
- `icp`: Which tier matched (1 = highest priority)
- `ranking`: Overall company relevance position
- `what_matched`: Filter criteria that triggered the match
- `person`: Full profile data including:
  - Names, headline, location (city/state/country/continent)
  - LinkedIn URL, connection count, profile picture
  - Experiences (with job details and dates)
  - Education, skills, and certifications

## Error Responses

| Status | Description |
|--------|-------------|
| **200** | Success |
| **402** | Insufficient credits |
| **422** | Invalid input/missing fields |
| **500** | Server error |

## Pricing
Unlimited on paid plans ($399+/mo); free trials receive 1,000 credits.
