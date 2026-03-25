# List Project Keys
Source: https://developers.deepgram.com/reference/manage/keys/list

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/keys`

## Description

Retrieves all API keys associated with the specified project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | enum | Optional | Only return keys with a specific status. Allowed values: `active`, `expired` |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/keys"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of API keys.

```json
{
  "api_keys": [
    {
      "member": {
        "member_id": "1000-2000-3000-4000",
        "email": "john@test.com"
      },
      "api_key": {
        "api_key_id": "1234567890abcdef1234567890abcdef",
        "comment": "A comment",
        "scopes": [
          "admin"
        ],
        "created": "2021-01-01T00:00:00Z"
      }
    }
  ]
}
```

### Response Fields

- **api_keys** (list of objects)
  - **member** (object)
    - **member_id** (string)
    - **email** (string)
  - **api_key** (object)
    - **api_key_id** (string)
    - **comment** (string)
    - **scopes** (array of strings)
    - **created** (string, datetime)

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
