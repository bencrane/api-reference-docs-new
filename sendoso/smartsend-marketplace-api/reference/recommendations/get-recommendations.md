# Get Gift Recommendations

Retrieves personalized product recommendations for a specified recipient based on their email address.

**Endpoint:** `GET /api/v3/smartsend/recommendations`

**Required scope:** `smartsend`

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `recipient_email` | string | Yes | The email address of the gift recipient |
| `price_lte_usd` | integer | No | Maximum product price in USD |
| `ship_to_country_code` | string | No | Country code for shipping destination |

## Response Structure

Returns a `products` array containing recommended items.

### Product Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique product identifier |
| `name` | string | Product title |
| `description` | string | Product details |
| `interests` | array | Interest categories that prompted the recommendation |
| `variants` | array | Available product variants |

### Variant Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Variant identifier |
| `estimated_total_price` | object | Pricing information |
| `estimated_total_price.currency` | string | Currency code |
| `estimated_total_price.price_per_unit` | string | Unit cost |
| `images` | array | Product images |

### Image Object

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Standard image URL |
| `cdn_main` | object | CDN-hosted full-size image URL |
| `cdn_thumbnail` | object | CDN-hosted thumbnail URL |
