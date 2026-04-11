# Metrics API [Starter]

Aggregated domain metrics. Subdomains are normalized to root domain.

## Endpoint

```
GET https://api.discolike.com/v1/metrics
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to investigate |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| domain | String | Normalized domain name |
| date_from | DateTime | Earliest certificate validity in dataset |
| date_to | DateTime | Latest certificate validity in dataset |
| lookback_all | Integer | Total registration events since date_from |
| lookback_360 | Integer | Registration events in last 360 days |
| lookback_720 | Integer | Registration events in last 720 days |

## Example Request

```shell
curl "https://api.discolike.com/v1/metrics?domain=www.acmecorp.com" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "domain": "acmecorp.com",
  "date_from": "2018-03-15 10:30:00",
  "date_to": "2024-08-20 14:45:30",
  "lookback_all": 45,
  "lookback_360": 12,
  "lookback_720": 28
}
```
