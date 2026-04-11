# Redirects API [Team]

Discover redirect relationships between domains. Uses data from DiscoLike's Redirect Domains Dataset.

## Endpoint

```
GET https://api.discolike.com/v1/redirects
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | The domain to query |
| match | Direction of redirect relationship: `source` or `linked` |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| source_domain | String | Normalized source domain |
| source_fqdn | String | Full source URL |
| linked_domain | String | Normalized destination domain |
| linked_fqdn | String | Full destination URL |
| record_date | Date | Compilation date of the record |

## Example Request

```bash
curl "https://api.discolike.com/v1/redirects?domain=acmeoldsite.com&match=source" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
[
  {
    "source_domain": "acmeoldsite.com",
    "source_fqdn": "acmeoldsite.com",
    "linked_domain": "acmecorp.com",
    "linked_fqdn": "acmecorp.com",
    "record_date": "2024-07-02"
  }
]
```
