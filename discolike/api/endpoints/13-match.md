# Match API [Team]

Match a company name to domain profiles. Returns ranked candidates with confidence scores. For bulk matching, see [Match Bulk](../bulk-match/). To enrich matched domains with firmographic data, use [BizData](../bizdata/) or [Append](../append/).

## Endpoint

```
GET https://api.discolike.com/v1/match
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | Company name to match (required) |
| country | ISO-3166-1 alpha-2 country code |
| state | US state code |
| city | City name |
| zip_code | Zip code |
| phone | Phone in E.164 or local format |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| query | Object | Query parameters used |
| matches | Array | [BizData](../../../datasets/bizdata/) profiles with match_confidence |

Each match includes `match_confidence` (0-100) indicating how well it matches the query.

## Example Request

```bash
curl "https://api.discolike.com/v1/match?name=acme+software&country=US" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "query": {
    "name": "acme software",
    "country": "US"
  },
  "matches": [
    {
      "domain": "acmesoftware.com",
      "name": "Acme Software Inc",
      "match_confidence": 100,
      "score": 250,
      "address": {
        "state": "CA",
        "country": "US"
      }
    }
  ]
}
```

---

Previous: [LLM Providers](/v1/docs/api/endpoints/llm-providers/) | Next: [Match Bulk](/v1/docs/api/endpoints/bulk-match/)
