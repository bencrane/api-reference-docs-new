# Delete a Project Key
Source: https://developers.deepgram.com/reference/manage/keys/delete

## Endpoint

**DELETE** `https://api.deepgram.com/v1/projects/:project_id/keys/:key_id`

## Description

Deletes an API key for a specific project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |
| key_id | string | Required | The key ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/keys/key_id"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Deleted

API key deleted.

```json
{
  "message": "API key successfully deleted for project 8f14e45f-ceea-4d3a-9f2b-1a2b3c4d5e6f"
}
```

### Response Fields

- **message** (string) - Confirmation message

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
