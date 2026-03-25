# Create a Project Key
Source: https://developers.deepgram.com/reference/manage/keys/create

## Endpoint

**POST** `https://api.deepgram.com/v1/projects/:project_id/keys`

## Description

Creates a new API key with specified settings for the project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Request Body

API key settings (required).

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/keys"

payload = { "expiration_date": "2026-01-01T00:00:00Z" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Successful

API key created successfully.

```json
{
  "api_key_id": "1234567890abcdef1234567890abcdef",
  "key": "1234567890abcdef1234567890abcdef",
  "comment": "a comment",
  "scopes": [
    "member"
  ],
  "tags": [
    "tag-1"
  ],
  "expiration_date": "2024-05-01T00:00:00.000000Z"
}
```

### Response Fields

- **api_key_id** (string) - The unique identifier of the API key
- **key** (string) - The API key
- **comment** (string) - A comment for the API key
- **scopes** (list of strings) - The scopes for the API key
- **tags** (list of strings) - The tags for the API key
- **expiration_date** (string, date-time) - The expiration date of the API key

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
