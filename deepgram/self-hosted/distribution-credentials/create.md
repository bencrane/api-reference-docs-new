# Create a Project Self-Hosted Distribution Credential
Source: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/create

## Endpoint

**POST** `https://api.deepgram.com/v1/projects/:project_id/self-hosted/distribution/credentials`

## Description

Creates a set of distribution credentials for the specified project.

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
| scopes | list of enums | Optional | List of permission scopes for the credentials |
| provider | enum | Optional | The provider of the distribution service. Defaults to `quay`. Allowed values: `quay` |

## Request Body

The set of distribution credentials to create.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| comment | string | Optional | Optional comment about the credentials |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/self-hosted/distribution/credentials"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Successful

Single distribution credential.

```json
{
  "member": {
    "member_id": "c7b9b131-73f3-11d9-8665-0b00d2e44b83",
    "email": "email@example.com"
  },
  "distribution_credentials": {
    "distribution_credentials_id": "82c32c10-53b2-4d23-993f-864b3d44502a",
    "provider": "quay",
    "scopes": [
      "self-hosted:product:api",
      "self-hosted:product:engine"
    ],
    "created": "2023-06-28T15:36:59.609841Z",
    "comment": "My Self-Hosted Distribution Credentials"
  }
}
```

### Response Fields

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
