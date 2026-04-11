# Growth API [Starter]

Quarterly growth metrics derived from a company's digital footprint, tracking [Score](../score/) and subdomain changes over time. Use with [BizData](../bizdata/) for full firmographic context.

## Endpoint

```
GET https://api.discolike.com/v1/growth
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to analyze |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| domain | String | Normalized domain |
| score_YYYYQX | Integer | Digital footprint score for each quarter |
| score_growth_3m | Float | Score growth rate (last 3 months) |
| subdomains_YYYYQX | Integer | Subdomain count for each quarter |
| subdomain_growth_3m | Float | Subdomain growth rate (last 3 months) |

## Example Request

```bash
curl "https://api.discolike.com/v1/growth?domain=acmecorp.com" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "domain": "acmecorp.com",
  "score_2024Q1": 58,
  "score_2024Q2": 66,
  "score_2024Q3": 87,
  "score_growth_3m": 11.2,
  "subdomains_2024Q1": 5,
  "subdomains_2024Q2": 4,
  "subdomains_2024Q3": 3,
  "subdomain_growth_3m": -1.9
}
```
