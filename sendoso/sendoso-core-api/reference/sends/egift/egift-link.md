# Generate eGift Links

Creates unique eGift links for embedding in custom outreach communications to recipients. Each recipient will have a unique link generated that is associated to the email you passed in the request.

**Endpoint:** `POST /api/v3/send/generate_egift_links`

## Request Body

The request requires a `send` object containing:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `touch_id` | integer | Yes | Campaign identifier within Sendoso |
| `via` | string | Yes | Must be set to `"generate_egift_links"` |
| `via_from` | string | Yes | Application name making the request (should remain consistent) |
| `recipient_users` | array | Yes | List of recipient objects |

### Recipient Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string | Yes | Recipient's email address |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Request status |
| `message` | string | Response text |
| `egift_links` | array | Generated links |
| `expiration_days` | integer | Link validity period |

### eGift Link Object

| Field | Type | Description |
|-------|------|-------------|
| `egift_link` | string | Unique shareable URL per recipient |
| `recipient_email_or_phone_number` | string | Associated contact |

## Example Request

```json
{
  "send": {
    "touch_id": 123456,
    "via": "generate_egift_links",
    "via_from": "Your Application Name",
    "recipient_users": [
      {"email": "developers@sendoso.com"},
      {"email": "developers2@sendoso.com"}
    ]
  }
}
```

## Example Responses

### 200 - Success

```json
{
  "success": true,
  "message": "Success! Here are your 2 eGift Card links:",
  "egift_links": [
    {
      "egift_link": "https://sendo.so/g/NzOHQCUf9eqw0",
      "recipient_email_or_phone_number": "developers@sendoso.com"
    },
    {
      "egift_link": "https://sendo.so/g/9d91rKc7O3d4",
      "recipient_email_or_phone_number": "developers2@sendoso.com"
    }
  ],
  "expiration_days": 30
}
```

### 400 - Bad Request

```json
{
  "success": false,
  "message": "email can't be blank"
}
```

### 401 - Unauthorized

```json
{
  "success": false,
  "message": "The access token is invalid"
}
```

### 404 - Not Found

```json
{
  "success": false,
  "message": "Touch not found"
}
```
