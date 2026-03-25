# List Project Invites
Source: https://developers.deepgram.com/reference/manage/invites/list

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/invites

## Description

Generates a list of invites for a specific project

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |

## Response

A list of invites for a specific project

**invites** - list of objects

Properties:
- **email** (string) - The email address of the invitee
- **scope** (string) - The scope/permissions for the invite

### Example Response (200 Retrieved)

```json
{
  "invites": [
    {
      "email": "jane.doe@example.com",
      "scope": "read:transcriptions"
    }
  ]
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/invites"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```
