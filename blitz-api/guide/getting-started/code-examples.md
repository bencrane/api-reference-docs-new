# Code Examples & Best Practices

## Overview
The Blitz API v2 provides production-ready endpoints for B2B lead generation, enrichment, and validation.

**Base URL:** `https://api.blitz-api.ai`

## Core Endpoints

### Search & Discovery
- **Waterfall ICP Keyword Search**: Find decision-makers using prioritized cascades
- **Employee Finder**: Search by role, department, location with pagination
- **Company Search**: Filter by industry, size, keywords with cursor pagination

### Enrichment
- Email from LinkedIn profile
- Phone numbers (US only)
- Full person profiles from email/phone
- Company profiles from LinkedIn URL
- Domain-to-LinkedIn conversion
- LinkedIn-to-domain lookup

### Utilities
- Email validation via SMTP
- API key health checks
- Server timestamp retrieval

## Authentication

All requests require the `x-api-key` header.

> **Warning:** Never expose your API key in client-side code — always call from backend systems.

## Production-Ready Client Implementation

### Node.js/TypeScript

```typescript
import axios, { AxiosInstance } from 'axios';

class BlitzAPIClient {
  private client: AxiosInstance;
  private maxRetries = 3;

  constructor(apiKey: string) {
    this.client = axios.create({
      baseURL: 'https://api.blitz-api.ai',
      headers: {
        'x-api-key': apiKey,
        'Content-Type': 'application/json'
      },
      timeout: 15000
    });
  }

  async request<T>(method: string, endpoint: string, data?: any): Promise<T> {
    let lastError: Error;

    for (let attempt = 0; attempt < this.maxRetries; attempt++) {
      try {
        const response = await this.client.request({
          method,
          url: endpoint,
          data
        });
        return response.data;
      } catch (error: any) {
        lastError = error;

        if (error.response?.status === 429) {
          // Rate limited - wait and retry
          await this.sleep(Math.pow(2, attempt) * 1000);
          continue;
        }

        if (error.response?.status === 401) {
          throw new Error('Invalid API key');
        }

        if (error.response?.status === 402) {
          throw new Error('Insufficient credits');
        }

        throw error;
      }
    }

    throw lastError!;
  }

  private sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

### Python

```python
import requests
import time
from typing import Any, Dict, Optional

class BlitzAPIClient:
    def __init__(self, api_key: str):
        self.base_url = 'https://api.blitz-api.ai'
        self.headers = {
            'x-api-key': api_key,
            'Content-Type': 'application/json'
        }
        self.max_retries = 3
        self.timeout = 15

    def request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None
    ) -> Any:
        last_error = None

        for attempt in range(self.max_retries):
            try:
                response = requests.request(
                    method=method,
                    url=f"{self.base_url}{endpoint}",
                    json=data,
                    headers=self.headers,
                    timeout=self.timeout
                )

                if response.status_code == 429:
                    # Rate limited - exponential backoff
                    time.sleep(2 ** attempt)
                    continue

                if response.status_code == 401:
                    raise Exception('Invalid API key')

                if response.status_code == 402:
                    raise Exception('Insufficient credits')

                response.raise_for_status()
                return response.json()

            except requests.exceptions.RequestException as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise

        raise last_error
```

## Rate Limiting & Error Handling

### Rate Limits
- 5 requests per second across all plans
- 5 concurrent requests maximum

### Error Responses

| Status | Meaning | Action |
|--------|---------|--------|
| 401 | Invalid API key | Check key validity |
| 402 | Insufficient credits | Upgrade plan or wait for reset |
| 429 | Rate limit exceeded | Implement backoff, retry after delay |
| 500 | Server error | Retry with exponential backoff |

## Response Patterns

- Most endpoints return `found` (boolean) plus relevant data
- Search endpoints include pagination (either offset-based pages or cursor-based)
- Waterfall ICP returns results ranked by `icp` tier and `ranking` position

## Plan Requirements

| Endpoint Category | Required Plan |
|-------------------|---------------|
| Search endpoints | Unlimited Leads+ |
| Email enrichment | Unlimited Email+ |
| Phone enrichment | Unlimited Phone |
| Utilities | Any plan |
