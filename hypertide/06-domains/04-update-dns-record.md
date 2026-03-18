# Hypertide - Update DNS Record

### `PUT /domains/{domain}/dns-records/{recordId}`

**Update a DNS record**

Updates a custom DNS record for a domain.

**Allowed record types:** `A`, `TXT`, `CNAME`

> **Note:** DKIM CNAME records cannot be modified via API.

#### Parameters

| Name | Type | In | Required | Description |
|---|---|---|---|---|
| `domain` | string | path | Yes | Domain name |
| `recordId` | string | path | Yes | DNS record ID |

#### Request Body

**Media type:** `application/json`

```json
{
  "type": "A",
  "content": "string",
  "ttl": 0
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | DNS record updated successfully |
| `400` | Validation failed (invalid record type or DKIM record blocked) |
| `401` | API key required |
| `403` | Permission denied |

**`400` - Validation failed**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "VALIDATION_FAILED",
  "message": "string"
}
```
