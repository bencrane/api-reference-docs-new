# Get a Project Model
Source: https://developers.deepgram.com/reference/manage/projects/models/get

API Reference > Manage > Projects > Get a Project Model

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/models/:model_id`

## Example Request

### Python

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/models/model_id"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Example Response

**200 Retrieved**

```json
{
  "name": "general",
  "canonical_name": "enhanced-general",
  "architecture": "polaris",
  "languages": [
    "en",
    "en-us"
  ],
  "version": "2022-05-18.1",
  "uuid": "c7226e9e-ae1c-4057-ae2a-a71a6b0dc588",
  "batch": true,
  "streaming": true,
  "formatted_output": false
}
```

## Description

Returns metadata for a specific model.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The unique identifier of the project |
| model_id | string | Required | The unique identifier of the model |

## Response

A model object that can be either STT or TTS.

- **STT object** (9 properties)
- **TTS object** (7 properties)

## Errors

- **400** - Bad Request Error
