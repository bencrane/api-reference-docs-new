# Get All Users

Retrieves a paginated list of all active users in your organization.

**Endpoint:** `GET /api/v3/users`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | The page number of the results you want to retrieve (the first page is 1) |
| `per_page` | integer | The number of users to be returned per page (max is 100) |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `current_page` | integer | Yes | The current page being returned |
| `per_page` | integer | Yes | The number of results being returned per page |
| `total_users` | integer | Yes | The total number of users |
| `users` | array | Yes | List of user objects |

### User Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | The user's identifier |
| `first_name` | string | Yes | The user's first name |
| `last_name` | string | Yes | The user's last name |
| `email` | string | Yes | The user's email |
| `team_group_id` | number | Yes | The user's team group id |

## Example Response

```json
{
  "current_page": 1,
  "per_page": 5,
  "total_users": 20,
  "users": [
    {
      "id": 12345,
      "first_name": "Sendoso",
      "last_name": "Devs",
      "email": "developers@sendoso.com",
      "team_group_id": 6789
    }
  ]
}
```
