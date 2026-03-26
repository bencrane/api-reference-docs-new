# Get All Team Group Users

Retrieves the list of users for a specific team.

**Endpoint:** `GET /api/v3/groups/{team_group_id}/members`

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `team_group_id` | integer | Yes | The team group identifier |

## Response Fields

Returns an array of user objects:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | User's unique identifier |
| `first_name` | string | User's first name |
| `last_name` | string | User's last name |
| `email` | string | User's email address |
| `balance` | string | User's personal account balance |
| `sandbox` | boolean | Indicates sandbox user status |
| `team_group_id` | integer | User's team group identifier |
| `team_id` | integer | The team's organization id |
| `key` | string | The user invitation identifier that was used by this user to sign up |

## Example Responses

### 200 - OK

```json
[
  {
    "id": 12345,
    "balance": "578.0",
    "first_name": "Sendoso",
    "last_name": "Devs",
    "email": "developers@sendoso.com",
    "team_group_id": 6789,
    "team_id": 4321,
    "sandbox": false,
    "key": "b7afc3c89f84e56d4731f8d6c2c0c543"
  },
  {
    "id": 987,
    "balance": "500.0",
    "first_name": "Sendoso",
    "last_name": "Devs 2",
    "email": "developers2@sendoso.com",
    "team_group_id": 6789,
    "team_id": 4321,
    "sandbox": false,
    "key": "3cd39d35349da5ec6a67a248c661asw4"
  }
]
```

### 404 - Not Found

```json
{
  "message": "Group not found!"
}
```
