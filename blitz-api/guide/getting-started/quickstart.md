# Quickstart Guide

## Overview
This guide demonstrates how to retrieve verified professional emails from LinkedIn profiles in under two minutes.

## Core Endpoint

| Property | Value |
|----------|-------|
| **Service** | `POST /v2/enrichment/email` |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | API key via `x-api-key` header |

## Step 1: Get Your API Key

1. Visit [https://app.blitz-api.ai](https://app.blitz-api.ai)
2. Create an account or sign in
3. Copy your API key from the dashboard

## Step 2: Make Your First Request

### cURL
```bash
curl -X POST 'https://api.blitz-api.ai/v2/enrichment/email' \
  -H 'x-api-key: YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "person_linkedin_url": "https://www.linkedin.com/in/example-person"
  }'
```

### Python
```python
import requests

response = requests.post(
    'https://api.blitz-api.ai/v2/enrichment/email',
    json={
        'person_linkedin_url': 'https://www.linkedin.com/in/example-person'
    },
    headers={
        'x-api-key': 'YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
)

print(response.json())
```

### Node.js
```javascript
const axios = require('axios');

const response = await axios.post(
  'https://api.blitz-api.ai/v2/enrichment/email',
  {
    person_linkedin_url: 'https://www.linkedin.com/in/example-person'
  },
  {
    headers: {
      'x-api-key': 'YOUR_API_KEY',
      'Content-Type': 'application/json'
    }
  }
);

console.log(response.data);
```

## Response Data

The API returns a JSON object with these key fields:

| Field | Type | Description |
|-------|------|-------------|
| `found` | boolean | Indicates successful email discovery |
| `email` | string | Primary verified work email |
| `all_emails` | array | Collection of verified addresses |
| `job_order_in_profile` | integer | Position in person's job history |
| `company_linkedin_url` | string | Associated company LinkedIn URL |
| `email_domain` | string | Email address domain |

### Example Response
```json
{
  "found": true,
  "email": "john@acme-corp.com",
  "all_emails": [
    {
      "email": "john@acme-corp.com",
      "job_order_in_profile": 1,
      "company_linkedin_url": "https://www.linkedin.com/company/acme-corp",
      "email_domain": "acme-corp.com"
    }
  ]
}
```

## Key Features
- All paid plans include **unlimited** requests — included in your flat monthly subscription
- Email addresses are validated through SMTP handshake verification
- Typically returns one email per profile

## Next Steps

- [Waterfall Search](../concepts/waterfall-logic.md) - Find contacts by job title/company
- [Employee Finder](../concepts/employee-finder.md) - Search all employees at a company
- [Code Examples](./code-examples.md) - Production-ready implementations
