# Employee Finder Concepts

## Overview
The Employee Finder endpoint (`POST /v2/search/employee-finder`) enables searching for employees at specific companies using structured filters like job level, department, geography, and seniority. It returns paginated results across all matching employees rather than prioritizing a single contact.

## Key Use Cases
- Mapping entire departments
- Building multi-threaded outreach lists
- Exporting team rosters for hiring intelligence
- Accessing paginated results from large organizations

## Request Parameters

### Required

| Parameter | Description |
|-----------|-------------|
| `company_linkedin_url` | The target company's LinkedIn URL |

### Optional Filters

| Parameter | Description |
|-----------|-------------|
| `country_code` | ISO 2-letter codes (defaults to worldwide) |
| `continent` | Continental filtering |
| `sales_region` | Regional filtering |
| `job_level` | Seniority levels (VP, Director, etc.) |
| `job_function` | Departments (Sales, Marketing, Engineering) |
| `min_connections_count` | LinkedIn connection threshold (0-500) |
| `max_results` | Results per page (1-50, default 50) |
| `page` | Pagination starting at 1 |

**Critical:** All filter values are case-sensitive enums requiring exact matches from the [Field Normalization](../reference/field-normalization.md) reference.

## Response Structure

Top-level fields include:
- Company URL
- Result count
- Current page
- Total pages
- Results array

Each person object contains:
- Name components
- LinkedIn headline
- Location data
- Work experience history
- Education
- Skills
- Certifications

## Code Examples

### cURL
```bash
curl -X POST 'https://api.blitz-api.ai/v2/search/employee-finder' \
  -H 'x-api-key: YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "company_linkedin_url": "https://www.linkedin.com/company/openai",
    "job_level": ["VP", "Director"],
    "job_function": ["Sales & Business Development"],
    "sales_region": ["NORAM"],
    "max_results": 10,
    "page": 1
  }'
```

### Node.js
```javascript
const axios = require('axios');

async function findEmployees() {
  const response = await axios.post(
    'https://api.blitz-api.ai/v2/search/employee-finder',
    {
      company_linkedin_url: 'https://www.linkedin.com/company/openai',
      job_level: ['VP', 'Director'],
      max_results: 10,
      page: 1
    },
    {
      headers: { 'x-api-key': 'YOUR_API_KEY' }
    }
  );

  response.data.results.forEach(person => {
    console.log(`${person.full_name}: ${person.linkedin_url}`);
  });
}
```

### Python
```python
import requests

response = requests.post(
    'https://api.blitz-api.ai/v2/search/employee-finder',
    json={
        'company_linkedin_url': 'https://www.linkedin.com/company/openai',
        'job_level': ['VP', 'Director'],
        'max_results': 10,
        'page': 1
    },
    headers={'x-api-key': 'YOUR_API_KEY'}
)

for person in response.json()['results']:
    print(f"{person['full_name']}: {person['linkedin_url']}")
```

## Pagination Pattern
Iterate from page 1 until reaching `total_pages`, incrementing the page parameter with each request while maintaining filter consistency.

## Enrichment Integration
Chain Employee Finder results with enrichment endpoints:
- `/v2/enrichment/email` - Get verified emails
- `/v2/enrichment/phone` - Get phone numbers (US only)
