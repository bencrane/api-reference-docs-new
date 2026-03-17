# Authentication

## Authentication Method
BlitzAPI uses API key-based authentication via the `x-api-key` HTTP header. Keys are managed through the [BlitzAPI Dashboard](https://app.blitz-api.ai).

## Header Implementation

The `x-api-key` header must be included in all requests.

### cURL
```bash
curl "https://api.blitz-api.ai/v2/account/key-info" \
  -H "x-api-key: YOUR_API_KEY"
```

### JavaScript
```javascript
const axios = require('axios');

const client = axios.create({
  baseURL: 'https://api.blitz-api.ai',
  headers: {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
  }
});

const response = await client.get('/v2/account/key-info');
```

### Python
```python
import requests

headers = {
    'x-api-key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.blitz-api.ai/v2/account/key-info',
    headers=headers
)
```

## Security Guidelines

> **Important:** Your API keys carry many privileges. **Do not** use your API keys in client-side code.

Instead, route all requests through your backend server.

## Key Verification Endpoint

Use `GET /v2/account/key-info` to validate your key's status.

### Response Fields

| Field | Description |
|-------|-------------|
| `valid` | Boolean indicating active status |
| `remaining_credits` | Usage allowance (trial accounts only) |
| `max_requests_per_seconds` | Rate limit for your plan |
| `allowed_apis` | Authorized endpoint paths |
| `active_plans` | Current subscriptions |

## Error Codes

| Status | Description |
|--------|-------------|
| **401 Unauthorized** | Missing or invalid key |
| **402 Payment Required** | Account limit reached |
| **404 Not Found** | Key doesn't exist in system |
