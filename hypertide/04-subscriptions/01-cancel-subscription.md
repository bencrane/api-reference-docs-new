# Hypertide - Cancel Subscription

## Subscriptions

Subscription management

---

### `POST /subscriptions/cancel`

**Cancel subscription or products**

Cancels subscription products or entire subscriptions.

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "subscriptionId": "sub_1234567890",
  "productIds": [
    "string"
  ],
  "domainRecordIds": [
    "string"
  ],
  "isPartialProductCancellation": false
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | Subscription cancelled successfully |
| `400` | Validation failed |
| `401` | API key required |
| `403` | Permission denied |
