# PublicLink API [Enterprise]

Find related domains by shared public contact information (social links, phone numbers, emails).

## Endpoint

```
GET https://api.discolike.com/v1/publiclink
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to discover linkage for |
| source | Linkage source: `email`, `social`, or `phone` |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| domain | String | Normalized query domain |
| linked_domain | String | Related domain found |
| link_values | Array | Shared contact values establishing the link |
| record_date | Date | Date the record was compiled |

## Example Request

```
curl "https://api.discolike.com/v1/publiclink?domain=acmehotels.com&source=email" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
[
  {
    "domain": "acmehotels.com",
    "linked_domain": "acmeresorts.com",
    "link_values": ["privacy@acmehotels.com", "dpo@acmehotels.com"],
    "record_date": "2024-07-17"
  },
  {
    "domain": "acmehotels.com",
    "linked_domain": "acmehotels.co.uk",
    "link_values": ["privacy@acmehotels.com"],
    "record_date": "2024-07-17"
  }
]
```
