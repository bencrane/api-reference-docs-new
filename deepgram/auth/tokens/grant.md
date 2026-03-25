# Token-Based Authentication
Source: https://developers.deepgram.com/reference/auth/tokens/grant

## Endpoint

**POST** `https://api.deepgram.com/v1/auth/grant`

## Description

Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint will not work with the Manage APIs.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Request Body

Time to live settings.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ttl_seconds | double | Optional | Time to live in seconds for the token. Defaults to 30 seconds. Range: 1-3600 |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/auth/grant"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Successful

Grant response.

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U",
  "expires_in": 30
}
```

### Response Fields

- **access_token** (string) - JSON Web Token (JWT)
- **expires_in** (double) - Time in seconds until the JWT expires

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
