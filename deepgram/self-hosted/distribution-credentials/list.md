# List Project Self-Hosted Distribution Credentials
Source: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/list

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/self-hosted/distribution/credentials`

## Description

Lists sets of distribution credentials for the specified project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/self-hosted/distribution/credentials"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of distribution credentials for a specific project.

```json
{
  "distribution_credentials": [
    {
      "member": {
        "member_id": "3376abcd-8e5e-49d3-92d4-876d3a4f0363",
        "email": "email@example.com"
      },
      "distribution_credentials": {
        "distribution_credentials_id": "8b36cfd0-472f-4a21-833f-2d6343c3a2f3",
        "provider": "quay",
        "scopes": [
          "self-hosted:product:api",
          "self-hosted:product:engine"
        ],
        "created": "2023-06-28T15:36:59.609841Z",
        "comment": "My Self-Hosted Distribution Credentials"
      }
    }
  ]
}
```

### Response Fields

- **distribution_credentials** (list of objects) - Array of distribution credentials with associated member information
  - **member** (object)
    - **member_id** (string)
    - **email** (string)
  - **distribution_credentials** (object)
    - **distribution_credentials_id** (string)
    - **provider** (string)
    - **scopes** (list of strings)
    - **created** (string, datetime)
    - **comment** (string)

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
