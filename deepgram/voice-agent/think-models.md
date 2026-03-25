# Think Models
Source: https://developers.deepgram.com/reference/voice-agent/think-models

Retrieves the available think models that can be used for AI agent processing

## Endpoint

**GET** `https://api.deepgram.com/v1/agent/settings/think/models`

### Example Request

```python
import requests

url = "https://api.deepgram.com/v1/agent/settings/think/models"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

### Example Response (200 Retrieved)

```json
{
  "models": [
    {
      "id": "gpt-4o",
      "name": "GPT-4o - Optimized",
      "provider": "OpenAI"
    }
  ]
}
```

## Response

List of available think models

| Field | Type | Description |
|-------|------|-------------|
| models | list of objects | Available think model configurations |

Models object variants: 5

## Errors

| Status | Description |
|--------|-------------|
| 400 | Bad Request Error |
