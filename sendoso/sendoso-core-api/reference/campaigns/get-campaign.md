# Get Campaign

Retrieves comprehensive details about a specific campaign.

**Endpoint:** `GET /api/v3/touches/{touch_id}`

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `touch_id` | integer | Yes | The unique identifier for the campaign |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `success` | boolean | Yes | Indicates request completion; returns `true` for successful 200 responses |
| `touch` | object | Yes | The campaign object |

### Campaign Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | Yes | Campaign identifier |
| `name` | string | Yes | Campaign name |
| `start_date` | string | Yes | Campaign launch date (ISO 8601 format) |
| `end_date` | string | No | Campaign conclusion date (ISO 8601 format) |
| `description` | string | Yes | Campaign details |
| `created_at` | string | Yes | Creation timestamp (ISO 8601 format) |
| `user_id` | integer | Yes | Creator's user identifier |
| `gift_id` | integer | Yes | Associated gift identifier |
| `starting_egift_price` | number | No | Minimum eGift amount (eGift campaigns only) |
| `ending_egift_price` | number | No | Maximum eGift amount (eGift campaigns only) |
| `status` | string | Yes | Always "Active" for this endpoint |
| `is_default_price` | boolean | Yes | Whether eGift amount is fixed or configurable |
| `delivery_type` | string | Yes | "mail" (physical) or "email" (eGift) |
| `hubspot_key` | string | Yes | HubSpot integration identifier |
| `ship_to_countries` | array | Yes | Supported destinations (ISO 3166-1 alpha-2) |
| `currency` | string | Yes | Gift currency (ISO 4217 format) |

## Example Responses

### 200 Success

```json
{
  "success": true,
  "touch": {
    "id": 123456,
    "name": "Sendoso Gift",
    "start_date": "2023-10-25T00:00:00.000-07:00",
    "end_date": null,
    "description": "",
    "created_at": "2023-10-25T05:21:59.000-07:00",
    "user_id": 78901,
    "gift_id": 39,
    "starting_egift_price": null,
    "ending_egift_price": null,
    "status": "Active",
    "is_default_price": true,
    "delivery_type": "mail",
    "hubspot_key": null,
    "ship_to_countries": ["US", "ES", "CA"],
    "currency": "USD"
  }
}
```

### 404 Not Found

```json
{
  "message": "Touch not found!"
}
```
