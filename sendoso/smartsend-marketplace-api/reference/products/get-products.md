# Get Marketplace Products

Retrieves a paginated catalog of all marketplace products.

**Endpoint:** `GET /api/v3/marketplace/products`

**Required scope:** `marketplace`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `after` | string | Cursor for pagination from previous response |
| `price_gte_usd` | integer | Minimum product price in USD |
| `price_lte_usd` | integer | Maximum product price in USD |
| `ship_to_country_codes[]` | array | Country codes for shipping destinations |
| `category_ids[]` | array | Category identifiers to filter results |
| `text_search` | string | Text-based product filtering |

## Response Structure

### Pagination Object

| Field | Type | Description |
|-------|------|-------------|
| `after` | string | Cursor for fetching subsequent pages |
| `next_page.url` | string | Direct URL to next page |

### Categories Array

| Field | Type | Description |
|-------|------|-------------|
| `group_name` | string | Category group identifier |
| `children` | array | Nested category entries |
| `children[].id` | string | Category identifier for filtering |
| `children[].name` | string | Category display name |

### Products Array

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique product identifier |
| `name` | string | Product title |
| `description` | string | Product details |
| `variants` | array | Available product options |

### Variant Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Variant identifier |
| `estimated_total_price.currency` | string | Price currency code |
| `estimated_total_price.price_per_unit` | string | Unit cost |
| `images` | array | Product imagery |

### Image Object

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Standard image URL |
| `cdn_main.url` | string | Optimized CDN image |
| `cdn_thumbnail.url` | string | Thumbnail CDN version |
