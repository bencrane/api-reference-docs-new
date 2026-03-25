# List Project Member Scopes
Source: https://developers.deepgram.com/reference/manage/members/scopes/list

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/members/:member_id/scopes`

## Description

Retrieves a list of scopes for a specific member.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |
| member_id | string | Required | The member ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/members/member_id/scopes"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of scopes for a specific member.

```json
{
  "scopes": [
    "transcription:read",
    "transcription:write",
    "analytics:read",
    "account:manage"
  ]
}
```

### Response Fields

- **scopes** (list of strings) - The API scopes of the member

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
