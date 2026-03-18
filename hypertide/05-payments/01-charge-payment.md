# Hypertide - Charge Payment

## Payments

Payment processing

---

### `POST /payments/charge`

**Charge customer's saved card**

Charges a customer's saved card for an order without requiring UI.

**Auto-detected values** (all derived from Airtable records):

- `email` — Auto-detected from Client Email field in records (optional to provide)
- `orderType` — Determined from User Count field (52 = Azure, 3 = Google)
- `purchaseDomains` — Determined from Payment Status (contains `"UserDomain"` = false)

**Coupon Support:**

- Optionally pass a Stripe coupon code or promotion code to apply a discount

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "recordIds": [
    "rec123",
    "rec456"
  ],
  "couponCode": "DISCOUNT20",
  "description": "Monthly subscription charge"
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | Payment processed successfully |
| `400` | Validation failed, invalid coupon, or records already paid |
| `401` | API key required |
| `403` | Permission denied or unauthorized records |

**`400` - Validation failed, invalid coupon, or records already paid**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "MISSING_RECORD_IDS",
  "message": "string",
  "details": {
    "alreadyPaidRecords": [
      {
        "recordId": "string",
        "domain": "string",
        "paymentStatus": "string"
      }
    ]
  }
}
```

**`403` - Permission denied or unauthorized records**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "UNAUTHORIZED_RECORDS",
  "message": "string"
}
```
