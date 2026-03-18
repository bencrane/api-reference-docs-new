# Hypertide - Get DNS Records

### `GET /domains/{domain}/dns-records`

**Get DNS records for a domain**

Gets custom DNS records for a domain.

#### Parameters

| Name | Type | In | Required | Description |
|---|---|---|---|---|
| `domain` | string | path | Yes | Domain name (e.g. `example.com`) |

#### Responses

| Code | Description |
|---|---|
| `200` | DNS records retrieved successfully |
| `401` | API key required |
| `403` | Permission denied |

**`200` - DNS records retrieved successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "records": [
    {
      "type": "A",
      "name": "subdomain",
      "content": "192.168.1.1",
      "ttl": 3600
    }
  ]
}
```
