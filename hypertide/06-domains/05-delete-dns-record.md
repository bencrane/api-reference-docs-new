# Hypertide - Delete DNS Record

### `DELETE /domains/{domain}/dns-records/{recordId}`

**Delete a DNS record**

Deletes a custom DNS record for a domain.

**Allowed record types:** `A`, `TXT`, `CNAME`

> **Note:** DKIM CNAME records cannot be deleted via API. Pass `type` and `hostname` as query parameters for validation.

#### Parameters

| Name | Type | In | Required | Description |
|---|---|---|---|---|
| `domain` | string | path | Yes | Domain name |
| `recordId` | string | path | Yes | DNS record ID |
| `type` | string | query | No | Record type for validation (recommended). Available values: `A`, `TXT`, `CNAME` |
| `hostname` | string | query | No | Record hostname for DKIM validation |

#### Responses

| Code | Description |
|---|---|
| `200` | DNS record deleted successfully |
| `400` | Invalid record type or DKIM record blocked |
| `401` | API key required |
| `403` | Permission denied |

**`400` - Invalid record type or DKIM record blocked**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "INVALID_RECORD_TYPE",
  "message": "string"
}
```
