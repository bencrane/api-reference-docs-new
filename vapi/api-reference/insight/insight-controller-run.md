# Run Insight API Reference

## Endpoint

**POST** `https://api.vapi.ai/reporting/insight/{id}/run`

## Description

Executes an insight report and returns a run response with metadata about the execution.

## Parameters

### Path Parameters
- **id** (required, string): The identifier of the insight to execute

### Header Parameters
- **Authorization** (required, string): API key obtained from the [Dashboard](dashboard.vapi.ai)
- **Content-Type**: `application/json`

## Request Body

The request accepts an `InsightRunDTO` object with the following optional properties:

### formatPlan
- **format** (string, enum): Output data structure
  - `raw`: Database results with evaluated formulas (default)
  - `recharts`: Pre-formatted for recharts.js chart rendering

### timeRangeOverride
Customizes the time range for the query:
- **start**: ISO 8601 date-time or relative format (e.g., "-7d", "-2w")
  - Default: 7 days ago
  - Units: d, h, w, m, y
- **end**: ISO 8601 date-time or relative format
  - Default: now
  - Units: d, h, w, m, y
- **step**: Aggregation interval (minute, hour, day, week, month, quarter, year)
  - Default: day
  - Ignored for Pie and Text Insights
- **timezone**: Timezone for query execution (default: UTC)

## Response

**Status: 200 OK**

```json
{
  "id": "string",
  "insightId": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.insight.insight_controller_run(id="insight_123")
```
