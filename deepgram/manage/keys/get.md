# Get a Project Key
Source: https://developers.deepgram.com/reference/manage/keys/get

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/keys/:key_id`

## Description

Retrieves information about a specified API key.

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

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A specific API key.

```json
{
  "item": {
    "member": {
      "member_id": "1000-2000-3000-4000",
      "email": "john@test.com",
      "first_name": "John",
      "last_name": "Doe",
      "api_key": {
        "api_key_id": "1000-2000-3000-4000",
        "comment": "A comment",
        "scopes": [
          "admin"
        ],
        "tags": [
          "prod",
          "west-region"
        ],
        "expiration_date": "2021-01-01T00:00:00Z",
        "created": "2021-01-01T00:00:00Z"
      }
    }
  }
}
```

### Response Fields

- **item** (object)
  - **member** (object)
    - **member_id** (string)
    - **email** (string)
    - **first_name** (string)
    - **last_name** (string)
    - **api_key** (object)
      - **api_key_id** (string)
      - **comment** (string)
      - **scopes** (array of strings)
      - **tags** (array of strings)
      - **expiration_date** (string, datetime)
      - **created** (string, datetime)

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
