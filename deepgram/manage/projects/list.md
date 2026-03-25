# List Projects
Source: https://developers.deepgram.com/reference/manage/projects/list

API Reference > Manage > Projects > List Projects

## Endpoint

**GET** `https://api.deepgram.com/v1/projects`

## Example Request

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

## Example Response

**200 Retrieved**

```json
{
  "projects": [
    {
      "project_id": "proj_9f8a7b6c5d4e3f21",
      "name": "Customer Support Transcriptions"
    }
  ]
}
```

## Description

Retrieves basic information about the projects associated with the API key.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Response

A list of projects.

### Properties

- **projects** - list of objects (2 properties)

## Errors

- **400** - Bad Request Error
