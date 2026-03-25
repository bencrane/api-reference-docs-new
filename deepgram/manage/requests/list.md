# List Project Requests
Source: https://developers.deepgram.com/reference/manage/requests/list

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/requests

## Description

Generates a list of requests for a specific project

## Authentication

Authorization Token
Use Authorization: Token <API_KEY>
Example: Authorization: Token 12345abcdef

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | string (date-time) | Optional | Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM |
| end | string (date-time) | Optional | End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM |
| limit | double | Optional | Number of results to return per page. Default 10. Range [1,1000] |
| page | double | Optional | Navigate and return the results to retrieve specific portions of information of the response |
| accessor | string | Optional | Filter for requests where a specific accessor was used |
| request_id | string | Optional | Filter for a specific request id |
| deployment | enum | Optional | Filter for requests where a specific deployment was used. Allowed values: hosted, beta, self-hosted |
| endpoint | enum | Optional | Filter for requests where a specific endpoint was used. Allowed values: listen, read, speak, agent |
| method | enum | Optional | Filter for requests where a specific method was used. Allowed values: sync, async, streaming |
| status | enum | Optional | Filter for requests that succeeded (status code < 300) or failed (status code >=400). Allowed values: succeeded, failed |

## Response

A list of requests for a specific project

| Field | Type | Description |
|-------|------|-------------|
| page | double | The page number of the paginated response |
| limit | double | The number of results per page |
| requests | list of objects | See properties below |

**requests** object properties:
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
  "page": 1,
  "limit": 10,
  "requests": [
    {
      "request_id": "a3f1c9d2-4b7e-4f8a-9c3d-2e5b7f6a1d9e",
      "project_uuid": "d9f8a7b6-c5e4-4d3f-8a2b-1c0d9e8f7a6b",
      "created": "2024-01-15T09:30:00Z",
      "path": "/v1/listen",
      "api_key_id": "key_1234567890abcdef",
      "response": {},
      "code": 200,
      "deployment": "production",
      "callback": "https://example.com/callback"
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

url = "https://api.deepgram.com/v1/projects/project_id/requests"

querystring = {
    "accessor": "12345678-1234-1234-1234-123456789012",
    "request_id": "12345678-1234-1234-1234-123456789012",
    "deployment": "hosted",
    "endpoint": "listen",
    "method": "async",
    "status": "succeeded"
}

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```
