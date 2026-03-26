# Send Physical Gift with Address Collection

Sends physical items when the recipient's address is unknown, utilizing address collection functionality.

**Endpoint:** `POST /api/v3/send`

## Request Body

The request requires a `send` object containing:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `touch_id` | integer | Yes | Campaign identifier within Sendoso |
| `name` | string | Yes | Recipient's full name |
| `email` | string | Yes | Recipient's email address |
| `custom_message` | string | No | Message for notecard in gift box |
| `no_address` | boolean | Yes | Must be `true` |
| `confirm_address` | boolean | Yes | Must be `true` |
| `address_confirmation_via` | string | Yes | Delivery method: `email` or `link` |
| `resume_with_unconfirmed_address` | boolean | Yes | Must be `false` for this endpoint |
| `expire_after_days` | integer | Yes | Form validity duration (2-7 days) |
| `hide_product_info` | boolean | Yes | Hides gift name/image from collection page |
| `address_confirmation_custom_message` | string | No | Custom message for address collection email |
| `via` | string | Yes | Must be `single_person_or_company` |
| `via_from` | string | Yes | Application name making the request |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Request success indicator |
| `message` | string | Response description |
| `tracking_code` | string | Unique send identifier |

## Example Request

```json
{
  "send": {
    "touch_id": 123456,
    "name": "John Smith",
    "email": "developers@sendoso.com",
    "custom_message": "Hi John, I wanted to personally invite you to...",
    "no_address": true,
    "confirm_address": true,
    "address_confirmation_via": "email",
    "resume_with_unconfirmed_address": false,
    "expire_after_days": 5,
    "hide_product_info": true,
    "address_confirmation_custom_message": "Please update your shipping address!",
    "via": "single_person_or_company",
    "via_from": "YOUR APPLICATION NAME"
  }
}
```

## Example Responses

### 200 - Success

```json
{
  "success": true,
  "message": "Gift send Successfully",
  "tracking_code": "116d64dc686937dd17b1865019cee71d295bcf38"
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
