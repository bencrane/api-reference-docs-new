# Contacts API [Starter]

## Overview

The Contacts API enables searching for business contacts/personas using vector search, with support for similarity matching, filtering, and name-based lookup.

## Subscription Level

| Feature | Required Plan |
|---------|---------------|
| Base search | STARTER |
| `inclusion_query_id` | STARTER |
| `exclusion_query_id` | PRO |

## Search Contacts

### Endpoint

```
GET https://api.discolike.com/v1/contacts
```

### Search Parameters

| Parameter | Description |
|-----------|-------------|
| persona_id | Use one or more persona IDs as the basis for similarity matching. Up to 10 IDs can be provided. |
| icp_text | Natural language description of your ideal contact profile for semantic matching. |
| negate_icp_text | Natural language description of contacts to exclude from results. |
| domain | Limit results to contacts at specific domains. Up to 100 domains can be provided. |
| inclusion_query_id | Include results from saved queries. Works with domain lists (scopes to companies) and contact lists (scopes to specific contacts). Requires Starter plan or higher. |
| exclusion_query_id | Exclude results from saved queries. Works with domain lists (excludes companies) and contact lists (excludes specific contacts). Requires Pro plan or higher. |

### Persona Filters

| Parameter | Description |
|-----------|-------------|
| seniority | Filter by seniority level. Acceptable values: `executive`, `vp`, `director`, `manager`, `senior_ic`, `mid_level`, `entry_level` |
| negate_seniority | Exclude contacts with specified seniority levels. |
| department | Filter by department. Examples: `Sales`, `Marketing`, `Engineering`, `Finance`, `HR` |
| negate_department | Exclude contacts in specified departments. |
| skills | Filter by skills. Multiple skills can be provided. |
| name | Filter by contact name (partial match supported). |
| title | Filter by job title (partial match supported). |
| summary | Filter by profile summary text (semantic search). Up to 20 phrases, space-separated. |
| negate_summary | Exclude contacts matching this summary description. Up to 20 phrases, space-separated. |
| person_country | Filter by contact's country using ISO-3166-1 alpha-2 codes. |
| person_state | Filter by contact's state/region. |

### Contact Data Filters

| Parameter | Description |
|-----------|-------------|
| has_email | Set to `true` to only include contacts with email addresses. |
| email_validated | Set to `true` to only include contacts with validated email addresses. |
| has_phone | Set to `true` to only include contacts with phone numbers. |
| has_linkedin | Set to `true` to only include contacts with LinkedIn profiles. |
| min_connections | Minimum LinkedIn connections required. |

### Company Filters

| Parameter | Description |
|-----------|-------------|
| filter_industry | Filter by company industry. See BizData Dataset for values. |
| negate_filter_industry | Exclude contacts at companies in specified industries. |
| filter_country | Filter by company country using ISO-3166-1 alpha-2 codes. |
| negate_filter_country | Exclude contacts at companies in specified countries. |
| filter_state | Filter by company state/region. |
| negate_filter_state | Exclude contacts at companies in specified states. |
| employees | Filter by company size. Format: `1-10`, `11-50`, `51-200`, `201-500`, `501-1000`, `1001-5000`, `5001-10000`, `10001+` |
| revenue_range | Filter by company revenue range. Values: `<1M`, `1-10M`, `10-100M`, `100M-1B`, `>1B`, `N/A` |

### Pagination & Output

| Parameter | Description |
|-----------|-------------|
| max_records | Maximum records to return, range 1-500 (optional, defaults to 100). |
| offset | Number of records to skip for pagination (optional, defaults to 0). |
| results_by_company | Limit results per company, range 0-10. When set, offset is ignored (optional, defaults to 0). |
| include_search_contacts | Set to `true` to include input persona_ids in results (optional, defaults to false). |
| consensus | Number of top results to use for building search vector, range 1-20 (optional, defaults to 1). |

### Example Request

```bash
curl "https://api.discolike.com/v1/contacts?icp_text=VP%20of%20Sales%20at%20SaaS%20companies&seniority=vp&filter_industry=TECHNOLOGY&max_records=50" \
  -H "x-discolike-key: API_KEY"
```

**Using domain and contact lists together:**

```bash
curl "https://api.discolike.com/v1/contacts?inclusion_query_id=DOMAIN_LIST_ID&exclusion_query_id=CONTACT_LIST_ID&seniority=vp&filter_industry=TECHNOLOGY" \
  -H "x-discolike-key: API_KEY"
```

In this example, `inclusion_query_id` references a domain list (scoping to specific companies), while `exclusion_query_id` references a contact list (excluding previously found contacts). The system automatically detects the list type and applies the correct filter.

### Example Response

```json
[
  {
    "persona_id": 12345678,
    "domain": "example.com",
    "name": "Jane Doe",
    "title": "VP of Sales",
    "department": "Sales",
    "seniority": "vp",
    "skills": ["sales leadership", "enterprise sales", "saas"],
    "phone": "+15555550123",
    "email": "jane.doe@example.com",
    "email_validated": true,
    "social_urls": [
      "https://linkedin.com/in/janedoe",
      "https://x.com/janedoe"
    ],
    "connections": 500,
    "country": "US",
    "state": "CA",
    "industry": ["TECHNOLOGY"],
    "employees": "51-200",
    "revenue_range": "10-100M",
    "similarity": 87
  }
]
```

Search for contacts using three modes:

1. **Similarity mode**: When `persona_id` or `icp_text` is provided - uses vector search with cosine similarity scores (0-100 scale)
2. **Domain mode**: When only `domain` is provided - returns all contacts at specified domains matching filters
3. **Filter mode**: When no search input is provided - returns contacts matching company and persona filters

## Count Contacts

### Endpoint

```
GET https://api.discolike.com/v1/contacts/count
```

Accepts the same filter parameters as the Search Contacts endpoint (persona filters, contact data filters, and company filters).

### Example Request

```bash
curl "https://api.discolike.com/v1/contacts/count?seniority=vp&filter_industry=TECHNOLOGY&filter_country=US" \
  -H "x-discolike-key: API_KEY"
```

### Example Response

```json
{
  "count": 15432
}
```

## Lookup Contact

### Endpoint

```
GET https://api.discolike.com/v1/contacts/lookup
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| persona_id | The persona ID to look up (provide this OR linkedin). |
| linkedin | LinkedIn URL or username to look up (provide this OR persona_id). |

### Example Request

```bash
curl "https://api.discolike.com/v1/contacts/lookup?persona_id=12345678" \
  -H "x-discolike-key: API_KEY"
```

Or lookup by LinkedIn URL/username:

```bash
curl "https://api.discolike.com/v1/contacts/lookup?linkedin=https://www.linkedin.com/in/janedoe" \
  -H "x-discolike-key: API_KEY"
```

### Example Response

```json
{
  "persona_id": 12345678,
  "name": "Jane Doe",
  "title": "VP of Sales",
  "domain": "example.com",
  "company_name": "Example Corp",
  "summary": "Experienced sales leader with 15+ years in enterprise software..."
}
```
