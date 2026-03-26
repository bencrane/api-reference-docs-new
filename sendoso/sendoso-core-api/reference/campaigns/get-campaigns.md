# Get All Campaigns

Retrieves a list of active campaigns within an organization.

**Endpoint:** `GET /api/v3/touches`

## Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | The page number of the results you want to retrieve (the first page is 1) |
| `per_page` | integer | The number of campaigns to be returned per page (max is 100) |
| `delivery_type` | string | Optional filter: `mail` for physical items or `email` for eGift campaigns |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `current_page` | integer | Current page number |
| `per_page` | integer | Results per page |
| `total_posts` | integer | Total campaign count |
| `touches` | array | List of campaign objects |

### Campaign Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Campaign identifier |
| `name` | string | Campaign name |
| `start_date` | string | ISO 8601 format; gifts cannot be sent before this date |
| `end_date` | string | ISO 8601 format (optional); gifts cannot be sent after |
| `status` | string | Always `Active` for this endpoint |
| `delivery_type` | string | Either `mail` or `email` |
| `currency` | string | ISO 4217 format |
| `ship_to_countries` | array | ISO 3166-1 alpha-2 country codes |
| `is_default_price` | boolean | Whether eGift amount is fixed or range-based |

## Example Response

```json
{
  "current_page": 1,
  "per_page": 1,
  "total_posts": 5,
  "touches": [
    {
      "id": 123456,
      "name": "Sendoso Gift",
      "start_date": "2023-10-25T00:00:00.000-07:00",
      "end_date": null,
      "delivery_type": "mail",
      "currency": "USD",
      "ship_to_countries": ["US", "ES", "CA"]
    }
  ]
}
```
