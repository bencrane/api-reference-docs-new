# Discover API [Starter]

## Overview

The Discover API enables companies to be found using domain lookalike matching, natural language ICP descriptions, phrase matching, or structured filters. Results return BizData profiles ranked by relevance.

## Endpoint

```
GET https://api.discolike.com/v1/discover
```

## Discovery Methods

| Method | Parameter | Description |
|--------|-----------|-------------|
| ICP Prompt | `icp_prompt` | Natural language ICP description that auto-extracts filters, generates ICP text, and suggests domains |
| Domain Lookalike | `domain` | Example domains (up to 10) for finding similar companies |
| ICP Text | `icp_text` | Natural language ideal customer description |
| Filters Only | structured filters | Location, industry, score, and other filters without search vector |

## Parameters

### Discovery Input (Starter)

- **domain** (string[]): Lookalike domains, maximum 10
- **negate_domain** (string[]): Domains to exclude, maximum 10
- **icp_text** (string): Natural language customer profile
- **negate_icp_text** (string): Concepts to exclude

### Phrase Matching (Starter)

- **phrase_match** (string[]): Exact text fragments, maximum 20
- **negate_phrase_match** (string[]): Fragments to exclude

### Location Filters (Starter)

- **country** (string[]): ISO-3166-1 alpha-2 codes
- **negate_country** (string[]): Countries to exclude
- **state** (string[]): State/province codes (single country)
- **negate_state** (string[]): States to exclude

### Company Filters (Starter)

- **min_digital_footprint** (integer): 0-800 minimum score (default: 50)
- **max_digital_footprint** (integer): 0-800 maximum score (default: 800)
- **start_date** (string): Format `YYYY-MM-DD` or range `YYYY-MM-DD,YYYY-MM-DD`
- **category** (string[]): Industry filters (TECHNOLOGY, HEALTHCARE, etc.)
- **negate_category** (string[]): Industries to exclude
- **employee_range** (string): Format `min,max` (e.g., `1,5000`)

### Social & Language Filters (Starter)

- **social** (string[]): Required social platforms (facebook, instagram, linkedin, twitter, x, youtube, tiktok, pinterest, threads, yelp, googleplay, applestore, amazon)
- **negate_social** (string[]): Platforms to exclude
- **language** (string[]): ISO-639 2-letter codes
- **negate_language** (string[]): Languages to exclude
- **redirect** (boolean): Include redirect domains (default: false)
- **exclude_leadgen** (boolean): Filter low-score profiles lacking contact info (default: true)

### Tech Stack Targeting (Team)

- **tech_stack** (string[]): Vendor domains, maximum 20
- **negate_tech_stack** (string[]): Vendor domains to exclude

### Subdomain Targeting (Company)

- **subdomain** (string[]): Specific subdomains, maximum 10
- **negate_subdomain** (string[]): Subdomains to exclude

### Query Inclusion (Starter)

- **inclusion_query_id** (string[]): Limit to saved query results

### Query Exclusion (Pro)

- **exclusion_query_id** (string[]): Exclude saved query results

### Result Controls (Starter)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| max_records | integer | 100 | Maximum records (5-10,000) |
| offset | integer | 0 | Records to skip for pagination |
| min_similarity | integer | 0 | Minimum similarity score (0-99) |
| consensus | integer | 1 | Top results for consensus (1-20) |
| variance | string | UNRESTRICTED | Diversity control: LOW, MID_LOW, MEDIUM, MID_HIGH, HIGH, UNRESTRICTED |
| include_search_domains | boolean | false | Include input domains in results |

### AI Features (Starter)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| enhanced | boolean | false | AI-powered result enhancement |
| retrieval | boolean | false | Enable page data retrieval |
| auto_icp_text | boolean | false | Auto-generate ICP text from domains |
| auto_phrase_match | boolean | false | Auto-generate phrase matches |
| icp_prompt | string | — | Natural language prompt that auto-extracts filters and runs discovery |

## Plan Requirements

| Feature | Minimum Plan |
|---------|--------------|
| Core discovery, filters, ICP text, phrase matching | Starter |
| Tech stack/vendor targeting | Team |
| Query exclusion & inclusion lists | Pro |
| Subdomain targeting | Company |

## Response Headers

| Header | Description |
|--------|-------------|
| X-Total-Count | Number of results returned |
| X-Applied-Filters | JSON object of filters used; when `icp_prompt` provided, shows extracted/merged filters useful for iterative workflows |

## Response Fields

Returns BizData profiles with additional discovery fields:

| Field | Type | Description |
|-------|------|-------------|
| similarity | float | Score (0-100) between result and query |
| vendors | string[] | Detected technology vendors |
| employees | string | Employee count range bucket |

Full profile schema available in BizData dataset documentation.

## Examples

### Domain Lookalike

```bash
curl "https://api.discolike.com/v1/discover?domain=stripe.com&country=US&min_digital_footprint=100&max_records=50" \
  -H "x-discolike-key: API_KEY"
```

### ICP Text Search

```bash
curl "https://api.discolike.com/v1/discover?icp_text=enterprise+SaaS+companies+in+financial+services&country=US&min_digital_footprint=200" \
  -H "x-discolike-key: API_KEY"
```

### ICP Prompt (One-Call Discovery)

```bash
curl "https://api.discolike.com/v1/discover?icp_prompt=SaaS+companies+in+financial+services+with+50-200+employees+in+the+US&min_digital_footprint=200" \
  -H "x-discolike-key: API_KEY"
```

### Phrase Match with Filters

```bash
curl "https://api.discolike.com/v1/discover?phrase_match=cloud+security&category=TECHNOLOGY&employee_range=51,5000" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
[
  {
    "domain": "acmesoftware.com",
    "name": "Acme Software",
    "similarity": 87.3,
    "status": {
      "status": "active",
      "confidence": 1
    },
    "score": 450,
    "start_date": "2015-03-20",
    "address": {
      "city": "San Francisco",
      "state": "CA",
      "country": "US"
    },
    "phones": ["+15555550200"],
    "public_emails": ["info@acmesoftware.com"],
    "social_urls": ["https://linkedin.com/company/acme-software"],
    "redirect_domain": null,
    "description": "Enterprise software solutions for modern businesses.",
    "keywords": {
      "enterprise software": 0.72,
      "cloud platform": 0.65
    },
    "industry_groups": {
      "SOFTWARE": 0.89
    },
    "employees": "201-500"
  }
]
```
