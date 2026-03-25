# Create a Project Invite
Source: https://developers.deepgram.com/reference/manage/invites/create

## Endpoint

POST https://api.deepgram.com/v1/projects/:project_id/invites

## Description

Generates an invite for a specific project

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |

## Request Body

Email to invite to the project

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Required | The email address of the invitee |
| scope | string | Required | The scope of the invitee |

### Example Request

```json
{
    "email": "jane.doe@example.com",
    "scope": "read:transcripts write:projects"
}
```

## Response

The invite was successfully generated

| Field | Type | Description |
|-------|------|-------------|
| message | string | Confirmation message |

### Example Response (200 Successful)

```json
{
  "message": "Invite successfully generated and sent to jane.doe@example.com"
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/invites"

payload = {
    "email": "jane.doe@example.com",
    "scope": "read:transcripts write:projects"
}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```
