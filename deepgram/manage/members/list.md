# List Project Members
Source: https://developers.deepgram.com/reference/manage/members/list

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/members`

## Description

Retrieves a list of members for a given project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/members"

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

A list of members for a given project.

```json
{
  "members": [
    {
      "member_id": "a3f47c9e-8b2d-4f1a-9c3e-2d5b7f6a1e4c",
      "email": "jane.doe@example.com"
    }
  ]
}
```

### Response Fields

- **members** (list of objects)
  - **member_id** (string) - The unique identifier of the member
  - **email** (string) - The member's email address

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
