> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> How to securely authenticate your requests with BlitzAPI.

BlitzAPI uses API Keys to authenticate requests. You can view and manage your API keys in the [BlitzAPI Dashboard](https://app.blitz-api.ai).

## The `x-api-key` Header

Authentication to the API is handled via an HTTP header. Include your API key in every request using the `x-api-key` header.

<Warning>
  **Security Warning**: Your API keys carry many privileges. **Do not** use your API keys in client-side code (browsers, mobile apps).

  Always route requests through your own backend server to keep your keys secret.
</Warning>

### Example Request

Here is how to set the header in various environments:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.blitz-api.ai/v2/account/key-info" \
   -H "x-api-key: YOUR_API_KEY"
  ```

  ```javascript JavaScript theme={null}
  const axios = require('axios');


  const client = axios.create({
   baseURL: 'https://api.blitz-api.ai',
   headers: {
     'x-api-key': 'YOUR_API_KEY',
     'Content-Type': 'application/json'
   }
  });
  ```

  ```python Python theme={null}
  import requests


  headers = {
     "x-api-key": "YOUR_API_KEY",
     "Content-Type": "application/json"
  }
  ```
</CodeGroup>

## Verifying your Key

To check if your key is active, use the `GET /v2/account/key-info` endpoint. This is a great way to "health check" your integration before running batch jobs.

**Response:**

```json  theme={null}
{
  "valid": true,
  "id": "key_abc123",
  "remaining_credits": 99.5,
  "next_reset_at": "2026-02-12T17:48:25.199Z",
  "max_requests_per_seconds": 5,
  "allowed_apis": [
    "/search/waterfall-icp-keyword",
    "/enrichment/email",
    "/enrichment/phone"
  ],
  "active_plans": [
    {
      "name": "Unlimited Leads",
      "status": "active",
      "started_at": "2026-01-12T17:48:25.200Z"
    }
  ]
}
```

**Response Fields:**

| Field                      | Type      | Description                                                                             |
| :------------------------- | :-------- | :-------------------------------------------------------------------------------------- |
| `valid`                    | `boolean` | `true` if the key is active and can make requests.                                      |
| `id`                       | `string`  | Internal identifier for your API key.                                                   |
| `remaining_credits`        | `number`  | Remaining usage allowance. Relevant for trial accounts only — paid plans are unlimited. |
| `next_reset_at`            | `string`  | ISO 8601 timestamp of when your allowance resets.                                       |
| `max_requests_per_seconds` | `integer` | Your plan's rate limit. Use this value to configure your rate limiter client-side.      |
| `allowed_apis`             | `array`   | List of endpoint paths your key is authorized to call.                                  |
| `active_plans`             | `array`   | Your active subscription(s) with name, status, and start date.                          |

## Errors

If authentication fails, the API will return a `401 Unauthorized` error.

| **Code** | **Meaning**          | **Solution**                                                                          |
| -------- | -------------------- | ------------------------------------------------------------------------------------- |
| `401`    | **Unauthorized**     | Missing or invalid API key. Check that the `x-api-key` header is present and correct. |
| `402`    | **Payment Required** | Your key is valid, but your account has reached its limit. Upgrade your plan.         |
| `404`    | **Not Found**        | The API Key provided does not exist in our system.                                    |


Built with [Mintlify](https://mintlify.com).