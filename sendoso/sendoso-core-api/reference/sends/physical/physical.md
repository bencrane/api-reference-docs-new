# Send Physical Gift

Sends physical items to recipients when their address is already known.

**Endpoint:** `POST /api/v3/send`

## Request Body

The request requires a `send` object containing:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `touch_id` | integer | Yes | Campaign ID within Sendoso |
| `name` | string | Yes | Recipient's full name |
| `email` | string | Yes | Recipient's email address |
| `address` | string | Yes | Street address |
| `city` | string | Yes | City name |
| `state` | string | Yes | State/province |
| `zip` | string | Yes | Postal code |
| `country` | string | Yes | Country name |
| `mobile_no` | number | No* | Phone number (*required for non-US addresses) |
| `custom_message` | string | No | Message for notecard in gift box |
| `confirm_address` | boolean | Yes | Set to `false` when providing recipient address |
| `via` | string | Yes | Must be `single_person_or_company` |
| `via_from` | string | Yes | Application name making the request |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Request success status |
| `message` | string | Response message |
| `tracking_code` | string | Unique tracking identifier |

## Example Request

```json
{
  "send": {
    "touch_id": 123456,
    "name": "John Smith",
    "email": "developers@sendoso.com",
    "address": "639 Front St, Floor 3",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94111",
    "country": "USA",
    "mobile_no": 1234567890,
    "custom_message": "Hi John, I wanted to personally invite you to...",
    "confirm_address": false,
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
