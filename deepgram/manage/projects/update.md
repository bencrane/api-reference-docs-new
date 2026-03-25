# Update a Project
Source: https://developers.deepgram.com/reference/manage/projects/update

API Reference > Manage > Projects > Update a Project

## Endpoint

**PATCH** `https://api.deepgram.com/v1/projects/:project_id`

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

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

## Example Response

**200 Updated**

```json
{
  "message": "Successfully updated project info."
}
```

## Description

Updates the name or other properties of an existing project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The unique identifier of the project |

## Request Body

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| name | string | Optional | The name of the project |

## Response

A project.

| Property | Type | Description |
|----------|------|-------------|
| message | string | Confirmation message |

## Errors

- **400** - Bad Request Error
