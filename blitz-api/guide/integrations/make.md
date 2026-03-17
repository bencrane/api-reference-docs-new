# Make (Integromat) Integration

## Overview
This guide explains how to integrate BlitzAPI with Make's HTTP module to connect with thousands of apps like Airtable, HubSpot, and Google Sheets using REST principles.

## Core Setup

### Step 1: HTTP Module Setup
Use the "Make a request" module with POST method to your BlitzAPI endpoint:
- **URL:** `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword`

### Step 2: Authentication
Add custom headers instead of username/password fields:
- `x-api-key`: YOUR_BLITZ_API_KEY
- `Content-Type`: application/json (optional but recommended)

### Step 3: Body Configuration
Use Raw mode with JSON content type.

> **Note:** For nested objects like our Waterfall Cascade, you must use Raw mode.

## Rate Limiting Solution

Make can trigger 500 requests simultaneously from spreadsheet rows. To avoid 429 errors:

1. Insert a **Sleep module** (Tools > Sleep) after the HTTP request
2. Set delay to **1 second**
3. This keeps operations under the 5 requests/second limit

## JSON Recipe Examples

### Scenario A: Sales Leader
Searches for CRO/VP Sales, falling back to Sales Director with US/GB location filters:

```json
{
  "company_linkedin_url": "{{company_linkedin_url}}",
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

### Scenario B: Marketing Decision Maker
Prioritizes CMO globally, with VP/Head of Marketing fallback:

```json
{
  "company_linkedin_url": "{{company_linkedin_url}}",
  "cascade": [
    {
      "include_title": ["CMO", "Chief Marketing Officer"],
      "exclude_title": ["assistant", "intern"],
      "location": ["WORLD"],
      "include_headline_search": false
    },
    {
      "include_title": ["VP Marketing", "Head of Marketing"],
      "exclude_title": ["assistant", "intern"],
      "location": ["WORLD"],
      "include_headline_search": true
    }
  ],
  "max_results": 1
}
```

### Scenario C: Email Enrichment
POST to email endpoint with person LinkedIn URL:

```json
{
  "person_linkedin_url": "{{person_linkedin_url}}"
}
```

**Endpoint:** `https://api.blitz-api.ai/v2/enrichment/email`

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **400 Bad Request** | Verify JSON syntax and quote marks remain intact when mapping variables |
| **Parse Errors** | Confirm Content-Type explicitly set to JSON |
| **Response Extraction** | Use JSON > Parse JSON module after HTTP request to convert response strings into usable mapped variables |
