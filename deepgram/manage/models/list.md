# List All Available Models
Source: https://developers.deepgram.com/reference/manage/models/list

API Reference > Manage > Models > List All Available Models

## Endpoint

**GET** `https://api.deepgram.com/v1/models`

## Example Request

### Python

```python
import requests

url = "https://api.deepgram.com/v1/models"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Example Response

**200 Retrieved**

```json
{
  "stt": [
    {
      "name": "nova-3",
      "canonical_name": "nova-3",
      "architecture": "base",
      "languages": [
        "en",
        "en-us"
      ],
      "version": "2021-11-10.1",
      "uuid": "6b28e919-8427-4f32-9847-492e2efd7daf",
      "batch": true,
      "streaming": true,
      "formatted_output": true
    }
  ],
  "tts": [
    {
      "name": "zeus",
      "canonical_name": "aura-2-zeus-en",
      "architecture": "aura-2",
      "languages": [
        "en",
        "en-US"
      ],
      "version": "2025-04-07.0",
      "uuid": "2baf189d-91ac-481d-b6d1-750888667b31",
      "metadata": {
        "accent": "American",
        "age": "Adult",
        "color": "#C58DFF",
        "image": "https://static.deepgram.com/examples/avatars/zeus.jpg",
        "sample": "https://static.deepgram.com/examples/Aura-2-zeus.wav",
        "tags": [
          "masculine",
          "deep",
          "trustworthy",
          "smooth"
        ],
        "use_cases": [
          "IVR"
        ]
      }
    }
  ]
}
```

## Description

Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| include_outdated | boolean | Optional | Returns non-latest versions of models |

## Response

A list of models.

| Property | Type | Description |
|----------|------|-------------|
| stt | list of objects | Speech-to-text models (9 properties) |
| tts | list of objects | Text-to-speech models (7 properties) |

## Errors

- **400** - Bad Request Error
