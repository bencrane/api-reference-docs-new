# Subsidiaries API [Enterprise]

Find parent-subsidiary relationships between domains. Uses data from our Subsidiaries Linkage Dataset.

## Endpoint

```
GET https://api.discolike.com/v1/subsidiaries
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Query domain |
| match | Match type: `source`, `linked`, `parent`, `child`, or `recursive`. The `recursive` option retrieves all child subsidiaries for all parent domains of the query domain. |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| source_domain | String | Normalized source domain |
| source_fqdn | String | Full source URL |
| source_score | Integer | Source domain score (1-800) |
| linked_domain | String | Normalized linked domain |
| linked_fqdn | String | Full linked URL |
| linked_score | Integer | Linked domain score (1-800) |
| record_date | Date | Date the record was compiled |
| parent_domain | String | Domain with highest score |
| child_domain | String | Subsidiary domain |

## Example Request

```
curl "https://api.discolike.com/v1/subsidiaries?domain=acmemail.com&match=child" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
[
  {
    "source_domain": "acmecorp.com",
    "source_fqdn": "mail.acmecorp.com",
    "source_score": 855,
    "linked_domain": "acmemail.com",
    "linked_fqdn": "acmemail.com",
    "linked_score": 84,
    "record_date": "2025-03-10",
    "parent_domain": "acmecorp.com",
    "child_domain": "acmemail.com"
  }
]
```
