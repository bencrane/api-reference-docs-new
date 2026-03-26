# Invite New User

Creates a new user invitation for a specific team group.

**Endpoint:** `POST /api/v3/users`

## Request Body

The request requires a `user` object containing:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `first_name` | string | Yes | The new user's first name |
| `last_name` | string | Yes | The new user's last name |
| `email` | string | Yes | The new user's email address |
| `role` | string | Yes | User role: `regular` or `manager` |
| `team_group_id` | integer | Yes | Team ID (retrieve via Get All Team Groups endpoint) |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Whether the invitation was created successfully |
| `message` | string | The response message |
| `receiver_email` | string | The invitation recipient's email |
| `team_group_id` | integer | The team group ID for the invitation |
| `user_role` | string | The assigned user role |
| `invitation_status` | string | Status: `pending`, `accepted`, or `expired` |
| `expires_at` | string | Expiration date/time in ISO 8601 format |

## Example Responses

### 201 - Created

```json
{
  "success": true,
  "message": "Invitation sent successfully",
  "receiver_email": "developers@sendoso.com",
  "team_group_id": 1234,
  "user_role": "manager",
  "invitation_status": "pending",
  "expires_at": "2023-11-11T12:18:55.000-08:00"
}
```

### 400 - Invalid Team Group

```json
{
  "success": false,
  "message": "Please enter a valid team group"
}
```

### 400 - Invalid Role

```json
{
  "success": false,
  "message": "Role can be one of these: manager,regular"
}
```
