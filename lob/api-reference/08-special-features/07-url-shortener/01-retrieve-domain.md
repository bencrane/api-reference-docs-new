# Domains — Retrieve

Retrieve details for a single domain.

## AUTHORIZATIONS

`basicAuth`

## PATH PARAMETERS

| Parameter | Type | Required | Description |
|---|---|---|---|
| `domain_id` | string | Yes | Unique identifier for a domain. |

## Responses

### 200 — Returns domain related details.

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for a domain. |
| `domain` | string | The registered domain/hostname. |
| `error_redirect_link` | string | URL to redirect customers if a short link is broken or inactive. |
| `status` | string | Enum: `"configured"`, `"not_configured"`. The configuration status of the domain. |
| `created_at` | string | The date and time the domain was created. |
| `updated_at` | string | The date and time the domain was last updated. |

### default — Error

---

## Endpoint

`GET /domains/{domain_id}`

## Request Sample

```shell
curl -X GET "https://api.lob.com/v1/domains/{domain_id}" \
  -u <YOUR_LIVE_API_KEY>:
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "string",
  "domain": "string",
  "error_redirect_link": "string",
  "status": "configured",
  "created_at": "string",
  "updated_at": "string"
}
```