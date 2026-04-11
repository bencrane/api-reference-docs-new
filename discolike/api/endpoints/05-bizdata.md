# BizData API [Starter]

Returns firmographic data for a domain — company name, industry, employee count, location, languages, and social profiles. Subdomains are automatically normalized to root domain. Use alongside [Score](../score/) for lead prioritization and [Growth](../growth/) for quarter-over-quarter changes.

## Endpoint

```
GET https://api.discolike.com/v1/bizdata
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to look up |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| domain | String | Normalized domain (unique identifier) |
| name | String | Company name from certificate or website |
| status | Object | Operating status: `active` or `closed` with confidence score |
| score | Integer | Digital footprint score (1-800) reflecting company size |
| start_date | Date | First certificate date (company start estimate) |
| end_date | Date | Last certificate date if closed, null if active |
| address | Object | HQ address (street, city, state, zip, country) |
| phones | Array | Phone numbers from website |
| public_emails | Array | Contact emails from website |
| social_urls | Array | Social media profile URLs |
| description | String | Company description from website |
| keywords | Object | NLP-generated keywords with confidence scores |
| industry_groups | Object | Top 2 industry classifications with scores |
| employees | String | Employee count range (e.g., `1-10`, `51-200`, `1001-5000`, `10001+`) |
| redirect_domain | String | Final domain if redirects exist |
| update_date | Date | Last record update |

## Example Request

```bash
curl "https://api.discolike.com/v1/bizdata?domain=acmecorp.com" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "domain": "acmecorp.com",
  "name": "Acme Corporation",
  "status": {
    "status": "active",
    "confidence": 1
  },
  "score": 650,
  "start_date": "2010-03-15",
  "end_date": null,
  "address": {
    "street": "123 Main Street",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94105",
    "country": "US"
  },
  "phones": ["+15555550100"],
  "public_emails": ["info@acmecorp.com"],
  "social_urls": [
    "https://twitter.com/acmecorp",
    "https://www.linkedin.com/company/acme-corporation"
  ],
  "description": "Leading provider of enterprise software solutions.",
  "keywords": {
    "enterprise software": 0.70,
    "cloud solutions": 0.65,
    "business automation": 0.61
  },
  "industry_groups": {
    "SOFTWARE": 0.95,
    "IT_SERVICES": 0.01
  },
  "employees": "201-500",
  "update_date": "2024-01-15"
}
```
