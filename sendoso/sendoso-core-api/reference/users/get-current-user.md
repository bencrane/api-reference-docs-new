# Get Current User

Retrieves information about the currently authenticated user.

**Endpoint:** `GET /api/v3/me`

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | Yes | The user's identifier |
| `first_name` | string | Yes | The user's first name |
| `last_name` | string | Yes | The user's last name |
| `email` | string | Yes | The user's email address |
| `role` | string | Yes | The user's role |
| `balance` | string | Yes | The user's personal balance |
| `team_balance` | integer | Yes | The sum of all users' balances |

## Example Response

```json
{
  "id": 123456,
  "first_name": "Sendoso",
  "last_name": "Devs",
  "email": "developers@sendoso.com",
  "balance": "500.0",
  "team_balance": 1543,
  "role": "manager"
}
```
