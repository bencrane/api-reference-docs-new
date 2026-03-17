# Company Search Concepts

## Overview
The Company Search endpoint (`POST /v2/search/companies`) enables users to find companies matching precise criteria for account-based marketing and prospecting workflows. The feature is included unlimited on paid plans.

## Key Functionality
The API accepts a POST request with optional filters combined using AND logic between fields and OR logic within fields. Responses are paginated and include up to 25 results per request.

## Request Parameters

### Main Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company` | object | Filter criteria container (required) |
| `max_results` | integer | Results per page; default 10, max 25 |
| `cursor` | string | Pagination token |

### Company Filter Fields

| Field | Description |
|-------|-------------|
| `keywords.include/exclude` | Array of inclusion/exclusion terms |
| `industry.include` | Normalized industry names (case-sensitive) |
| `hq.country_code` | 2-letter ISO country codes |
| `employee_range` | Employee count brackets like "51-200" |

## Response Structure
Results include company name, LinkedIn URL, website, industry, employee count, and headquarters details. Each response provides a cursor for fetching subsequent pages.

## Code Examples

### JavaScript
```javascript
const axios = require('axios');

const response = await axios.post(
  'https://api.blitz-api.ai/v2/search/companies',
  {
    company: {
      industry: { include: ['Computer Software'] },
      employee_range: ['51-200', '201-500'],
      hq: { country_code: ['FR', 'DE'] }
    },
    max_results: 25
  },
  {
    headers: {
      'x-api-key': 'YOUR_API_KEY',
      'Content-Type': 'application/json'
    }
  }
);
```

### Python
```python
import requests

response = requests.post(
    'https://api.blitz-api.ai/v2/search/companies',
    json={
        'company': {
            'industry': {'include': ['Computer Software']},
            'employee_range': ['51-200', '201-500'],
            'hq': {'country_code': ['FR', 'DE']}
        },
        'max_results': 25
    },
    headers={
        'x-api-key': 'YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
)
```

### cURL
```bash
curl -X POST 'https://api.blitz-api.ai/v2/search/companies' \
  -H 'x-api-key: YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "company": {
      "industry": {"include": ["Computer Software"]},
      "employee_range": ["51-200", "201-500"],
      "hq": {"country_code": ["FR", "DE"]}
    },
    "max_results": 25
  }'
```

## Implementation Guidance
The recommended workflow:
1. Use Company Search to build target lists
2. Extract LinkedIn URLs as enrichment keys
3. Pass these to downstream contact-finding tools for decision-maker identification and verification
