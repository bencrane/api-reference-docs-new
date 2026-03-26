# Send a Recommendation

Automatically selects and delivers a recommendation to a specified recipient.

**Endpoint:** `POST /api/v3/smartsend/recommendations/send`

**Required scope:** `smartsend`

## Request Parameters

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `recipient_email` | string | The recipient's email address |
| `recipient_first_name` | string | Recipient's given name |
| `recipient_last_name` | string | Recipient's surname |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `price_lte_usd` | integer | Maximum product price in USD |
| `ship_to_country_code` | string | Country restriction for product delivery |
| `message` | string | Accompanying note with the product |
| `gift_exchange_enabled` | boolean | Enables recipients to swap gifts for comparable marketplace items |
| `meeting_url` | string | Associated meeting link |
| `require_approval` | boolean | Holds send for manager approval via send tracker |

## Response Structure

### Products Array

| Field | Type | Description |
|-------|------|-------------|
| `variant_id` | string | The delivered product's variant identifier |

### Send Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the send transaction |
