# Create Analytics Queries

## Endpoint

**POST** `https://api.vapi.ai/analytics`

## Description

This endpoint allows you to submit analytics queries to retrieve aggregated data about calls and subscriptions. You can specify which table to query, how to group results, what time range to analyze, and which aggregation operations to perform.

## Authentication

**Header Parameter:**
- `Authorization` (required): Your API Key from the Vapi Dashboard

## Request Body

The request uses `application/json` content type with the following structure:

**Root Schema:** `AnalyticsQueryDTO`
- `queries` (required): Array of `AnalyticsQuery` objects

### AnalyticsQuery Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `table` | enum | Yes | Target table: `call` or `subscription` |
| `name` | string | Yes | Query identifier for the response |
| `operations` | array | Yes | Array of `AnalyticsOperation` objects |
| `groupBy` | enum | No | Group by column (type, assistantId, endedReason, analysis.successEvaluation, status) |
| `groupByVariableValue` | array | No | Variable value keys to group by |
| `timeRange` | object | No | Time range specifications |

### AnalyticsOperation Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `operation` | enum | Yes | Aggregation type: sum, avg, count, min, max, history |
| `column` | enum | Yes | Target column (cost, duration, concurrency, etc.) |
| `alias` | string | No | Custom name for the result column |

### TimeRange Object

| Field | Type | Description |
|-------|------|-------------|
| `start` | ISO 8601 datetime | Start date (defaults to 7 days ago) |
| `end` | ISO 8601 datetime | End date (defaults to now) |
| `step` | enum | Time aggregation step (second, minute, hour, day, week, month, quarter, year, decade, century, millennium) |
| `timezone` | string | Timezone for results (defaults to UTC) |

## Response

**Status Code:** 200

**Content Type:** `application/json`

**Schema:** Array of `AnalyticsQueryResult` objects

### AnalyticsQueryResult Object

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Query identifier matching request |
| `timeRange` | object | Applied time range configuration |
| `result` | array | Result set with grouped data and aggregated metrics |

## Example Request

```json
{
  "queries": [
    {
      "table": "call",
      "name": "Total Call Duration",
      "operations": [
        {
          "operation": "sum",
          "column": "duration"
        }
      ]
    }
  ]
}
```

## Example Response

```json
[
  {
    "name": "Total Call Duration",
    "timeRange": {
      "start": "2024-01-01T00:00:00Z",
      "end": "2024-01-08T00:00:00Z",
      "timezone": "UTC"
    },
    "result": [
      {
        "date": "2024-01-01",
        "sumDuration": 3600
      },
      {
        "date": "2024-01-02",
        "sumDuration": 4200
      }
    ]
  }
]
```

## SDK Example (Python)

```python
from vapi import Vapi, AnalyticsQuery, AnalyticsOperation

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.analytics.get(
    queries=[
        AnalyticsQuery(
            table="call",
            name="Total Call Duration",
            operations=[
                AnalyticsOperation(
                    operation="sum",
                    column="duration",
                )
            ],
        )
    ],
)
```
