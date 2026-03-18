# Hypertide - Add DNS Record

### `POST /domains/{domain}/dns-records`

**Add a DNS record**

Adds a custom DNS record for a domain.

**Allowed record types:** `A`, `TXT`, `CNAME`

> **Note:** DKIM CNAME records (containing `._domainkey`, `dkim`, `selector1`, `selector2`) cannot be added via API.

#### Parameters

| Name | Type | In | Required | Description |
|---|---|---|---|---|
| `domain` | string | path | Yes | Domain name (e.g. `example.com`) |

#### Request Body

**Media type:** `application/json`

```json
{
  "type": "A",
  "hostname": "mail",
  "content": "192.168.1.1",
  "ttl": 3600
}
```

#### Responses

| Code | Description |
|---|---|
| `201` | DNS record created successfully |
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
