# List Project Usage Fields
Source: https://developers.deepgram.com/reference/manage/usage/list

## Endpoint

GET https://api.deepgram.com/v1/projects/:project_id/usage/fields

## Description

Lists the features, models, tags, languages, and processing method used for requests in the specified project

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
| start | string (date) | Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| end | string (date) | Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |

## Response

A list of fields for a specific project

| Field | Type | Description |
|-------|------|-------------|
| tags | list of strings | List of tags associated with the project |
| models | list of objects | List of models available for the project |
| processing_methods | list of strings | Processing methods supported by the API |
| features | list of strings | API features available to the project |

**models** object properties:
- **name** (string)
- **language** (string)
- **version** (string)
- **model_id** (string)

### Example Response (200 Retrieved)

```json
{
  "tags": [
    "tag=dev",
    "tag=production"
  ],
  "models": [
    {
      "name": "2-medical-nova",
      "language": "en-MY",
      "version": "2024-05-31.13574",
      "model_id": "1234567890-12345-67890"
    }
  ],
  "processing_methods": [
    "sync",
    "streaming"
  ],
  "features": [
    "alternatives",
    "detect_entities",
    "detect_language"
  ]
}
```

## Errors

- 400 Bad Request Error

## Example Code

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/usage/fields"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```
