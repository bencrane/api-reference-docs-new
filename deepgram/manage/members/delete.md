# Delete a Project Member
Source: https://developers.deepgram.com/reference/manage/members/delete

## Endpoint

**DELETE** `https://api.deepgram.com/v1/projects/:project_id/members/:member_id`

## Description

Removes a member from the project using their unique member ID.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |
| member_id | string | Required | The member ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/members/member_id"

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

Delete the specific member from the project.

```json
{
  "message": "Member with ID 7f3a9c2e-4d1b-4f8a-9c3e-2b7d5f6a8e9c has been successfully removed from project 3a1b2c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d."
}
```

### Response Fields

- **message** (string) - Confirmation message

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
