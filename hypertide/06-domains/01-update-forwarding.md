# Hypertide - Update Forwarding

## Domains

Domain and DNS management

---

### `POST /domains/update-forwarding`

**Update forwarding configuration**

Updates forwarding domain or email for specified domains.

**Behavior based on order status:**

- **Orders in progress:** Update is saved and will be applied automatically when the order completes
- **Completed orders:** Update is applied immediately

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "domains": [
    "domain1.com",
    "domain2.com"
  ],
  "forwardingDomain": "forward.example.com",
  "forwardingEmail": "contact@example.com"
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | Forwarding update processed |
| `400` | Validation failed |
| `401` | API key required |
| `403` | Permission denied — domains don't belong to your account |
| `404` | No matching domains found |

**`200` - Forwarding update processed**

**Media type:** `application/json`

```json
{
  "success": true,
  "message": "Successfully processed 3 domain(s)",
  "queued": {
    "count": 0,
    "message": "These domains are still being set up. Forwarding will be applied automatically when the order completes.",
    "domains": [
      "string"
    ]
  },
  "updated": {
    "count": 0,
    "message": "Forwarding updated successfully",
    "domains": [
      "string"
    ]
  },
  "failed": {
    "count": 0,
    "domains": [
      {
        "domain": "string",
        "reason": "string"
      }
    ]
  }
}
```
