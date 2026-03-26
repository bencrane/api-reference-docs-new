# Send eGift via Email

Delivers eGifts directly to recipients through email via the Sendoso platform.

**Endpoint:** `POST /api/v3/send`

## Request Body

The request requires a `send` object containing:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `touch_id` | integer | Yes | Campaign identifier within Sendoso |
| `name` | string | No | Recipient's full name |
| `email` | string | Yes | Recipient's email address |
| `custom_message` | string | No | Message content for the eGift email body |
| `via` | string | Yes | Must be set to `single_email_address` |
| `via_from` | string | Yes | The name of the application making the send request |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `success` | boolean | Yes | Indicates request success |
| `message` | string | Yes | Response message text |
| `tracking_code` | string | Yes | Unique identifier for tracking the send |
| `tracking_url` | string | Yes | URL for tracking the specific send |

## Example Request

```json
{
  "send": {
    "touch_id": 123456,
    "name": "John Smith",
    "email": "developers@sendoso.com",
    "custom_message": "Hi John, I wanted to personally invite you to...",
    "via": "single_email_address",
    "via_from": "YOUR APPLICATION NAME"
  }
}
```

## Example Responses

### 200 - Success

```json
{
  "success": true,
  "message": "EGifts send Successfully",
  "tracking_code": "df934732d35e597e87ca47990a6ada5c61f890fe",
  "tracking_url": "https://app.sendoso.com/track/df934732d35e597e87ca47990a6ada5c61f890d6"
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
  "description": "The access token is invalid",
  "expired": false
}
```

### 404 - Not Found

```json
{
  "success": false,
  "message": "Touch not found"
}
```
