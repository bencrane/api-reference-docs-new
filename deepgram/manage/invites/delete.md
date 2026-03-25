# Delete a Project Invite
Source: https://developers.deepgram.com/reference/manage/invites/delete

## Endpoint

DELETE https://api.deepgram.com/v1/projects/:project_id/invites/:email

## Description

Deletes an invite for a specific project

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |
| email | string | Required | |

## Response

The invite was successfully deleted

| Field | Type | Description |
|-------|------|-------------|
| message | string | Confirmation message |

### Example Response (200 Deleted)

```json
{
  "message": "Invite for user jane.doe@example.com successfully deleted from project 8f14e45f-ceea-4d3a-9f2b-1a2b3c4d5e6f"
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/invites/email"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```
