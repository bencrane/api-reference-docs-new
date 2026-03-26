# Retrieve All Sends

Fetches a comprehensive list of all sends initiated throughout an organization.

**Endpoint:** `GET /api/v3/send`

## Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Page number for results (starts at 1) |
| `per_page` | integer | Sends per page, maximum of 100 |

## Response Fields

### Top-Level Response

| Field | Type | Description |
|-------|------|-------------|
| `current_page` | integer | The page number being returned |
| `per_page` | integer | Results per page |
| `total_count` | integer | Total sends across all pages |
| `sends` | array | Collection of send objects |

### Send Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique send identifier |
| `send_gid` | string | Global identifier for send |
| `type` | string | Category (see below) |
| `subtype` | string | Specific variant (see below) |
| `currency` | string | ISO 4217 format |
| `current_total_cost` | string | Cost at request time; may change before final status |
| `status` | string | Current state (see below) |
| `created_at` | string | ISO 8601 timestamp |
| `touch` | object | Campaign details (`id`, `name`) |
| `recipient` | object | Recipient info (`name`, `email`, `company_name`) |
| `sender` | object | Originating user (`id`, `name`, `email`, `team_id`, `team_name`) |
| `sent_via` | string | Platform origin (e.g., "Sendoso.com", "Salesforce Trigger") |
| `status_updates` | array | Status change history with timestamps |

### Send Types

- Amazon
- Handwritten Notes
- Inventoried Sends
- Sendoso Choice
- Sendoso Direct
- eGifts International
- eGifts USA

### Send Subtypes

Bundles, Coffee, Wine, Custom, Donate to Charity, Experiences, various eGift Cards by country, etc.

### Send Statuses

- Address Confirmation - Cancelled
- Bounced and Credited
- Cancelled
- Clicked
- Collecting recipient info
- Confirming Address
- Delivered
- Expired and Credited
- Failed
- Opened
- Packed
- Paused
- Processing
- Refunded
- Sent
- Shipped
- Undeliverable
- Used
- pending

## Example Response

```json
{
  "current_page": 1,
  "per_page": 10,
  "total_count": 892,
  "sends": [
    {
      "id": 1,
      "send_gid": "Z2lkOi8vc2VuZG9zby9TZW5kLzQ0",
      "type": "eGifts USA",
      "subtype": "eGift Cards USA",
      "currency": "USD",
      "current_total_cost": "2.0",
      "status": "Expired",
      "created_at": "2022-09-12T12:08:27-07:00",
      "touch": {
        "id": 12,
        "name": "eGift Cards USA"
      },
      "recipient": {
        "name": "John Doe",
        "email": "johndoe@acme.com",
        "company_name": "Acme"
      },
      "sender": {
        "id": 123,
        "name": "Marc Fernandez",
        "email": "marc.fernandez@sendoso.com",
        "team_id": 123,
        "team_name": "Marketing Ops"
      },
      "sent_via": "Sendoso.com",
      "status_updates": [
        {"status": "Sent", "occurred_at": "2022-09-12T12:08:27-07:00"},
        {"status": "Opened", "occurred_at": "2022-09-12T12:08:58-07:00"},
        {"status": "Clicked", "occurred_at": "2022-09-12T12:08:58-07:00"},
        {"status": "Expired", "occurred_at": "2022-12-11T00:00:02-08:00"}
      ]
    }
  ]
}
```
