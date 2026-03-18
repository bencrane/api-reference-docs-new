# Hypertide - Get Pending Orders

### `GET /orders/pending`

**Get pending (unpaid) orders**

Fetches unpaid orders from Airtable that were created via the HT API. Results are filtered to only show orders belonging to the authenticated API client.

#### Parameters

No parameters.

#### Responses

| Code | Description |
|---|---|
| `200` | Pending orders retrieved successfully |
| `401` | API key required |
| `403` | Permission denied |

**`200` - Pending orders retrieved successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "count": 3,
  "orders": [
    {
      "id": "recXXXXXXXXXXXXXX",
      "domain": "example.com",
      "status": "Todo",
      "paymentStatus": "Unpaid",
      "forwardingDomain": "forward.example.com",
      "sendingTool": "Smartlead.ai",
      "organizationName": "Client Inc.",
      "createdAt": "2024-01-01"
    }
  ],
  "requestId": "string"
}
```
