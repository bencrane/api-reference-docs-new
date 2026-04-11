# Count API [Starter]

Get a count of companies matching your search criteria before running a full Discover query.

---

## Endpoint

```
GET https://api.discolike.com/v1/count
```

---

## Parameters

### Search Filters

| Parameter | Description |
|-----------|-------------|
| phrase_match | Exact text to search (up to 20 phrases) |
| negate_phrase_match | Exact text to exclude |
| tech_stack | Vendor domains to include (Team) |
| negate_tech_stack | Vendor domains to exclude (Team) |

### Location Filters

| Parameter | Description |
|-----------|-------------|
| country | ISO-3166-1 alpha-2 country codes (e.g., US, GB, DE) |
| negate_country | Countries to exclude |
| state | US state codes (single country only) |
| negate_state | States to exclude |

### Company Filters

| Parameter | Description |
|-----------|-------------|
| min_digital_footprint | Minimum score (0-800, default: 50) |
| max_digital_footprint | Maximum score (0-800, default: 800) |
| start_date | Company start date (YYYY-MM-DD or range) |
| category | Industry filter (see BizData) |
| negate_category | Industries to exclude |

### Other Filters

| Parameter | Description |
|-----------|-------------|
| social | Required social presence: facebook, linkedin, twitter, instagram, etc. |
| negate_social | Social profiles to exclude |
| language | ISO-639-2 language codes |
| negate_language | Languages to exclude |
| redirect | Include redirecting domains (0 or 1, default: 0) |

---

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| count | Integer | Number of matching profiles |

---

## Example Request

```bash
curl "https://api.discolike.com/v1/count?phrase_match=enterprise+software&country=US" \
  -H "x-discolike-key: API_KEY"
```

---

## Example Response

```json
{
  "count": 1542
}
```
