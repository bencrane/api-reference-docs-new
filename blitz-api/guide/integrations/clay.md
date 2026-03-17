# Clay Integration

## Overview
This guide covers integrating BlitzAPI with Clay to enrich leads at scale without coding.

## Setup Methods

### Sculptor (Fastest)
1. Copy a cURL command from BlitzAPI's API Reference
2. Paste into Clay's HTTP API enrichment using the "Paste cURL" button
3. Clay's AI automatically maps parameters to your table columns

### Manual Setup

| Setting | Value |
|---------|-------|
| Method | POST |
| URL | `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword` |
| Headers | `content-type: application/json`, `x-api-key: YOUR_API_KEY` |

## Critical Rate Limiting Requirement

> **Important:** You **must** configure the rate limit settings in Clay. We allow 5 requests per second.

Configure these exact settings:

| Setting | Value |
|---------|-------|
| Max Requests | 5 |
| Time Period | 1000 ms |

Failure to implement this causes `429 Too Many Requests` errors.

## Popular Payloads

### Waterfall Search
Finds decision-makers using cascading title/location filters:

```json
{
  "company_linkedin_url": "{{Company LinkedIn URL}}",
  "cascade": [
    {
      "include_title": ["VP Sales", "CRO"],
      "exclude_title": ["assistant", "intern"],
      "location": ["US"],
      "include_headline_search": false
    },
    {
      "include_title": ["Sales Director", "Head of Sales"],
      "exclude_title": ["assistant"],
      "location": ["US", "GB"],
      "include_headline_search": true
    }
  ],
  "max_results": 1
}
```

### Enrich Email
Extracts verified emails from LinkedIn profile URLs:

```json
{
  "person_linkedin_url": "{{Person LinkedIn URL}}"
}
```

**Endpoint:** `https://api.blitz-api.ai/v2/enrichment/email`

## Output Mapping

After successful requests:
1. Hover over the results cell
2. Select "Add to Table"
3. Map fields like email, phone, and LinkedIn URL

The `icp` field indicates which cascade tier matched (tier ranking system).

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 429 errors | Configure rate limiting (5 req/sec) |
| Empty results | Check field normalization values |
| Invalid JSON | Verify curly braces and quotes |
