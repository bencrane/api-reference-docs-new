# Delete a Project
Source: https://developers.deepgram.com/reference/manage/projects/delete

API Reference > Manage > Projects > Delete a Project

## Endpoint

**DELETE** `https://api.deepgram.com/v1/projects/:project_id`

## Example Request

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id"

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
  "message": "Project 'VoiceAnalytics2024' has been successfully deleted."
}
```

## Description

Deletes the specified project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The unique identifier of the project |

## Response

A project.

| Property | Type | Description |
|----------|------|-------------|
| message | string | Confirmation message |

## Errors

- **400** - Bad Request Error
