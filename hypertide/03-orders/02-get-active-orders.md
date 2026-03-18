# Hypertide - Get Orders

### `GET /orders/active`

**Get active (paid) orders**

Fetches paid orders from Airtable that were created via the HT API. Results are filtered to only show orders belonging to the authenticated API client.

#### Parameters

No parameters.

#### Responses

| Code | Description |
|---|---|
| `200` | Active orders retrieved successfully |
| `401` | API key required |
| `403` | Permission denied |

**`200` - Active orders retrieved successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "count": 5,
  "orders": [
    {
      "id": "recXXXXXXXXXXXXXX",
      "domain": "example.com",
      "status": "In Progress",
      "paymentStatus": "Paid",
      "subscriptionId": "sub_1234567890",
      "forwardingDomain": "forward.example.com",
      "sendingTool": "Smartlead.ai",
      "organizationName": "Client Inc.",
      "createdAt": "2024-01-01"
    }
  ],
  "requestId": "string"
}
```
