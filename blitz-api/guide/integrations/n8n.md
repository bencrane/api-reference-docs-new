# n8n Integration

## Overview
This guide explains how to automate BlitzAPI enrichment workflows using n8n's HTTP Request node for tasks like waterfall search, enrichment, and CRM synchronization.

## Setup Instructions

### Credential Creation

1. Navigate to **Credentials > New**
2. Select **"Header Auth"**
3. Name it `x-api-key`
4. Enter your BlitzAPI key

### Node Configuration

The HTTP Request node requires:
- **Method:** POST
- **URL:** `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword`
- **Credential Type:** Generic Credential Type with Header Auth selection
- **Body Content Type:** JSON with expression mapping

## Critical Rate Limiting Guidance

> **Warning:** n8n executes workflows extremely fast. Processing bulk items without throttling will trigger API limits at 5 requests per second, causing 429 errors.

### Throttling Solution

Implement a "Split In Batches" pattern:

1. **Batch size:** 1 (maximum 5)
2. Connect to HTTP Request node
3. Add **200-millisecond wait delay** between requests
4. Configure loop-back for sequential processing

## Waterfall Search Templates

### Sales Leader
Cascades from CRO/VP Sales to Director-level roles in US/GB:

```json
{
  "company_linkedin_url": "={{ $json.company_linkedin_url }}",
  "cascade": [
    {
      "include_title": ["CRO", "VP Sales", "Chief Revenue Officer"],
      "exclude_title": ["assistant", "intern"],
      "location": ["US", "GB"],
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

### Marketing Decision Maker
CMO priority with VP/Head of Marketing fallback globally:

```json
{
  "company_linkedin_url": "={{ $json.company_linkedin_url }}",
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
      "location": ["WORLD"],
      "include_headline_search": true
    }
  ],
  "max_results": 1
}
```

### Founder/SMB
Owner/Founder focus in France/Germany with CEO fallback:

```json
{
  "company_linkedin_url": "={{ $json.company_linkedin_url }}",
  "cascade": [
    {
      "include_title": ["Owner", "Founder", "Co-Founder"],
      "exclude_title": [],
      "location": ["FR", "DE"],
      "include_headline_search": false
    },
    {
      "include_title": ["CEO", "Managing Director"],
      "exclude_title": [],
      "location": ["FR", "DE"],
      "include_headline_search": true
    }
  ],
  "max_results": 1
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| JSON validation errors | Check for proper escaping and bracket matching |
| Array formatting problems | Ensure arrays use square brackets `[]` |
| Credential name mismatches | Header name must be exactly `x-api-key` |
| 429 Rate Limit errors | Implement batch processing with delays |
