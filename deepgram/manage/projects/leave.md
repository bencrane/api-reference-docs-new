# Leave a Project
Source: https://developers.deepgram.com/reference/manage/projects/leave

API Reference > Manage > Projects > Leave a Project

## Endpoint

**DELETE** `https://api.deepgram.com/v1/projects/:project_id/leave`

## Example Request

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/leave"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

## Example Response

**200 Deleted**

```json
{
  "message": "Successfully removed user from project 8f14e45f-ceea-4d3a-9f2a-1a2b3c4d5e6f"
}
```

## Description

Removes the authenticated account from the specific project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The unique identifier of the project |

## Response

Successfully removed account from project.

| Property | Type | Description |
|----------|------|-------------|
| message | string | Confirmation message |

## Errors

- **400** - Bad Request Error
