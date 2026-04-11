# Usage API [Starter]

Returns your API usage for the current month and historical breakdown.

## Endpoint

```
GET https://api.discolike.com/v1/usage
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| month_to_date_requests | Integer | Requests this month |
| month_to_date_records | Integer | Records returned this month |
| month_to_date_spend | Float | Spend this month |
| usage_summary | Object | Monthly breakdown by YYYY-MM |

### Monthly Summary Object

| Field | Type | Description |
|-------|------|-------------|
| access_id | String | API key identifier |
| description | String | API key description |
| requests | Integer | Request count |
| total_records | Integer | Records returned |
| monthly_spend | Float | Total spend |

## Example Request

```shell
curl "https://api.discolike.com/v1/usage" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "month_to_date_requests": 92,
  "month_to_date_records": 24936,
  "month_to_date_spend": 59.07,
  "usage_summary": {
    "2025-01": {
      "access_id": "API_KEY",
      "description": "[API] ACME Corp Integration",
      "requests": 92,
      "total_records": 24936,
      "monthly_spend": 59.07
    },
    "2024-12": {
      "requests": 403,
      "total_records": 98624,
      "monthly_spend": 237.55
    }
  }
}
```
