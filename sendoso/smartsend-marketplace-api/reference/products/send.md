# Send a Product (Variant)

Sends a product variant to a recipient through the Sendoso platform.

**Endpoint:** `POST /api/v3/marketplace/products/send`

**Required scope:** `marketplace` or `smartsend`

## Request Parameters

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `variant_ids` | array | Catalog product variant identifiers from the marketplace. Only the first variant processes when multiple are provided. |
| `recipient_email` | string | Recipient's email address |
| `recipient_first_name` | string | Recipient's given name |
| `recipient_last_name` | string | Recipient's surname |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `sender_first_name` | string | Sender's given name |
| `sender_last_name` | string | Sender's surname |
| `sender_email` | string | Sender's email address |
| `sender_organization_name` | string | Organization associated with sender |
| `message` | string | Accompanying text with the product |
| `gift_exchange_enabled` | boolean | When true, recipients may swap for equivalent or lower-value marketplace items |
| `meeting_url` | string | Link to a meeting |
| `require_approval` | boolean | When true, the transaction awaits manager approval via send tracker |

## Response Structure

### Success Response

| Field | Type | Description |
|-------|------|-------------|
| `products` | array | Includes sent variant identifier |
| `send` | object | Includes transaction ID for the initiated send |
