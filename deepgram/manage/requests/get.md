# Get a Project Request
Source: https://developers.deepgram.com/reference/manage/requests/get

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/requests/:request_id

## Description

Retrieves a specific request for a specific project

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |
| request_id | string | Required | |

## Response

A specific request for a specific project

| Field | Type | Description |
|-------|------|-------------|
| request | object | A single request |

**request** object properties:
- **request_id** (string)
- **project_uuid** (string)
- **created** (string)
- **path** (string)
- **api_key_id** (string)
- **response** (object)
- **code** (integer)
- **deployment** (string)
- **callback** (string)

### Example Response (200 Retrieved)

```json
{
  "request": {
    "request_id": "a3f47c9e-8b2d-4f1a-9c3e-2d5b7f6a1e4c",
    "project_uuid": "d9f8e7a6-1234-4b56-8c9d-0e1f2a3b4c5d",
    "created": "2024-01-15T09:30:00Z",
    "path": "/v1/projects/d9f8e7a6-1234-4b56-8c9d-0e1f2a3b4c5d/requests/a3f47c9e-8b2d-4f1a-9c3e-2d5b7f6a1e4c",
    "api_key_id": "key_7f8e9d6c5b4a3e2f1d0c",
    "response": {},
    "code": 200,
    "deployment": "us-west-2",
    "callback": "https://myapp.example.com/callbacks/deepgram"
  }
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/requests/request_id"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```
