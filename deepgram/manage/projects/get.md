# Get a Project
Source: https://developers.deepgram.com/reference/manage/projects/get

API Reference > Manage > Projects > Get a Project

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id`

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

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

## Example Response

**200 Retrieved**

```json
{
  "project_id": "proj_9f8b7c6d5e4a3b2c1d0e",
  "mip_opt_out": false,
  "name": "Acme Corp Voice Analytics"
}
```

## Description

Retrieves information about the specified project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The unique identifier of the project |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | double | Optional | 1-1000. Defaults to 10. Number of results to return per page. Default 10. Range [1,1000] |
| page | double | Optional | Navigate and return the results to retrieve specific portions of information of the response |

## Response

A project.

| Property | Type | Description |
|----------|------|-------------|
| project_id | string | The unique identifier of the project |
| mip_opt_out | boolean | Model Improvement Program opt-out |
| name | string | The name of the project |

## Errors

- **400** - Bad Request Error
