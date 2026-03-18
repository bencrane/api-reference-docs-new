# Hypertide - Update Usernames

## Users

User management

---

### `POST /users/update-username`

**Update usernames for domains**

Updates the user configuration for specified domains.

**Inbox count calculation:**

- For Entra/Azure domains (52 total): inboxes are split across provided users
- For Google domains (3 total): 3 inboxes per domain

**Example:** For an Entra domain with 2 users, each gets 26 inboxes (52 ÷ 2)

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "domains": [
    "domain1.com",
    "domain2.com"
  ],
  "users": [
    {
      "first_name": "John",
      "last_name": "Doe"
    },
    {
      "first_name": "Jane",
      "last_name": "Smith"
    }
  ]
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | Usernames updated successfully |
| `400` | Validation failed |
| `401` | API key required |
| `403` | Permission denied — domains don't belong to your account |
| `404` | No matching domains found |

**`200` - Usernames updated successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "message": "Successfully updated 2 domain(s)",
  "updated": {
    "count": 0,
    "domains": [
      "string"
    ]
  },
  "failed": {
    "count": 0,
    "domains": [
      {
        "domain": "string",
        "reason": "string"
      }
    ]
  }
}
```
