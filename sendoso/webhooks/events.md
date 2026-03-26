# Events

Webhook event types are triggered during the send lifecycle. All events reflect statuses visible in the send tracker. Users can subscribe to any combination of these events through their webhooks portal.

## Available Event Types

The platform supports 31 distinct event types:

### Processing States

| Event | Description |
|-------|-------------|
| `send.initiated` | Send creation in progress |
| `send.order_received` | Order received and processing |
| `send.fulfilling` | Processing by Sendoso |
| `send.amazon_fulfilling` | Amazon processing |
| `send.pending_approval` | Awaiting sender approval |
| `send.pending_sendoso_approval` | Awaiting Sendoso Admin approval |
| `send.confirming_address` | Awaiting recipient address confirmation |

### Delivery States

| Event | Description |
|-------|-------------|
| `send.sent` | eGift sent to recipient |
| `send.shipped` | In transit to recipient |
| `send.amazon_shipped` | Shipped from Amazon |
| `send.delivered` | Delivered to recipient |

### Engagement States

| Event | Description |
|-------|-------------|
| `send.clicked` | eGift viewed by recipient |
| `send.opened` | eGift opened by recipient |
| `send.redeemed` | eGift redeemed by recipient |

### Error/Failure States

| Event | Description |
|-------|-------------|
| `send.blocked` | Redemption request blocked |
| `send.bounced` | Cannot be redeemed; refund issued |
| `send.canceled` | Canceled by sender |
| `send.confirmation_canceled` | Address confirmation canceled |
| `send.email_blacklist` | Redemption blacklisted |
| `send.expired` | Redemption link expired |
| `send.failed` | Send failed |
| `send.fulfillment_issue` | Fulfillment-side issue |
| `send.insufficient_funds` | Insufficient account funds |
| `send.invalid_email_format` | Invalid recipient email |
| `send.out_of_stock` | Product unavailable |
| `send.refunded` | Send refunded |
| `send.suspicious_email` | Email flagged as suspicious |
| `send.undeliverable` | Cannot be delivered |

## Webhook Payload Schema

All events use a standardized JSON structure:

```json
{
  "send_gid": "<string>",
  "status_changed_at": "<string>"
}
```

### Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `send_gid` | string | The gid of the send |
| `status_changed_at` | string | The time at which the send's status was changed in ISO 8601 format |
