# LeadTags

## POST CreateTags

**Endpoint:** `https://api.heyreach.io/api/public/lead_tags/CreateTags`

Create one or multiple tags for your workspace. You can assign these tags to leads.

Available colors: `Blue`, `Green`, `Purple`, `Pink`, `Red`, `Cyan`, `Yellow`, `Orange`.

### Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Public API Key |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

### Body (raw JSON)

```json
{
  "tags": [
    {
      "displayName": "string",
      "color": "Blue|Green|Purple|Pink|Red|Cyan|Yellow|Orange"
    }
  ]
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/lead_tags/CreateTags' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "tags": [
    {
      "displayName": "string",
      "color": "Green"
    }
  ]
}'
```

### Example Response

```json
[
  {
    "displayName": "string",
    "color": "Purple"
  },
  {
    "displayName": "stri",
    "color": "Purple"
  }
]
```