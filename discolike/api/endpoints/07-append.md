# Append API [Starter+]

Enrich customer or prospect profiles by appending firmographic and domain data to a list of domains from a CSV or Excel file. Returns BizData profiles, Score values, and Growth metrics for each domain.

## Endpoint

```
POST https://api.discolike.com/v1/append
```

## Parameters

Request must use `Content-Type: multipart/form-data` with the file as `file` parameter. Maximum file size is 1MB (first 10,000 rows processed).

| Parameter | Description |
|-----------|-------------|
| dataset | Datasets to append: `bizdata` (Starter), `domain_status` / `redirects` / `growth` (Team) |
| domain_column | Column containing domains. Auto-detected if not provided |

## Response Fields

Field naming depends on the dataset combination:

| Scenario | Bizdata fields | Non-bizdata fields |
|----------|----------------|-------------------|
| `bizdata` only | No prefix (`name`, `score`) | N/A |
| `bizdata` + others | No prefix (`name`, `score`) | Prefixed (`redirects:redirect_count`) |
| Single non-bizdata | N/A | No prefix (`status_code`) |
| Multiple non-bizdata | N/A | Prefixed (`domain_status:status_code`, `growth:score_growth_3m`) |

`domain` is always available without prefix. Original input columns are prefixed with `input:`.

### Dataset-specific fields

| Dataset | Fields |
|---------|--------|
| `bizdata` | Standard BizData fields (`name`, `status`, `score`, `description`, etc.) |
| `redirects` | `redirect_sources` (array of domains redirecting to this domain, capped at 1,000), `redirect_count` (true total) |
| `domain_status` | `status_code`, `status_reason`, `record_date` |
| `growth` | Quarterly `score_*` and `subdomains_*` fields, `score_growth_3m`, `subdomain_growth_3m` |

Returns JSON by default. Add `&csv=true` for CSV output.

## Example Request

```bash
curl --form file='@domains.csv' \
  "https://api.discolike.com/v1/append?dataset=bizdata&dataset=redirects" \
  -H "x-discolike-key: API_KEY"
```

Input file:
```
domain
acmesoftware.com
```

## Example Response

```json
[
  {
    "domain": "acmesoftware.com",
    "name": "Acme Software Inc",
    "status": {
      "status": "active",
      "confidence": 1.0
    },
    "score": 250,
    "start_date": "2018-02-17",
    "address": {
      "state": "CA",
      "country": "US"
    },
    "phones": ["+15555550900"],
    "public_emails": ["info@acmesoftware.com"],
    "description": "Enterprise software company providing business intelligence and data analytics solutions.",
    "keywords": {
      "business intelligence": 0.63,
      "data analytics": 0.51
    },
    "industry_groups": {
      "SOFTWARE": 0.85
    },
    "redirects:redirect_sources": ["oldacme.com", "acme-software.com"],
    "redirects:redirect_count": 2
  }
]
```

**Note:** Bizdata fields (`name`, `score`, `description`, etc.) are never prefixed. Non-bizdata fields are prefixed with the dataset name when combined with bizdata or other datasets.
