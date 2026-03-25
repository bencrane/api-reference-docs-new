# Update Project Member Scopes
Source: https://developers.deepgram.com/reference/manage/members/scopes/update

## Endpoint

**PUT** `https://api.deepgram.com/v1/projects/:project_id/members/:member_id/scopes`

## Description

Updates the scopes for a specific member.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |
| member_id | string | Required | The member ID |

## Request Body

A scope to update.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| scope | string | Required | A scope to update |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/members/member_id/scopes"

payload = {"scope": "member"}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Updated

Updated the scopes for a specific member.

```json
{
  "message": "Member scopes updated successfully"
}
```

### Response Fields

- **message** (string) - Confirmation message

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
