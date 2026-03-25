# Get Insight API Reference

## Endpoint

**GET** `https://api.vapi.ai/reporting/insight/{id}`

## Description

Retrieves a specific insight configuration by its unique identifier. The response returns the insight's complete structure, including queries, formulas, and visualization metadata.

## Parameters

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the insight to retrieve |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from [Dashboard](dashboard.vapi.ai)." |

## Response

### Success Response (200)

The response is a discriminated union that returns one of four insight types:

#### Bar Insight
```json
{
  "type": "bar",
  "name": "string",
  "formulas": [
    {
      "name": "string",
      "formula": "string"
    }
  ],
  "metadata": {
    "xAxisLabel": "string",
    "yAxisLabel": "string",
    "yAxisMin": 0,
    "yAxisMax": 0,
    "name": "string"
  },
  "timeRange": {
    "step": "day",
    "start": "ISO8601",
    "end": "ISO8601",
    "timezone": "UTC"
  },
  "groupBy": "assistantId",
  "queries": [],
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

#### Pie Insight
```json
{
  "type": "pie",
  "name": "string",
  "formulas": [],
  "timeRange": {
    "start": "ISO8601",
    "end": "ISO8601",
    "timezone": "UTC"
  },
  "groupBy": "assistantId",
  "queries": [],
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

#### Line Insight
```json
{
  "type": "line",
  "name": "string",
  "formulas": [],
  "metadata": {
    "xAxisLabel": "string",
    "yAxisLabel": "string",
    "yAxisMin": 0,
    "yAxisMax": 0,
    "name": "string"
  },
  "timeRange": {
    "step": "day",
    "start": "ISO8601",
    "end": "ISO8601",
    "timezone": "UTC"
  },
  "groupBy": "assistantId",
  "queries": [],
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

#### Text Insight
```json
{
  "type": "text",
  "name": "string",
  "formula": {},
  "timeRange": {
    "start": "ISO8601",
    "end": "ISO8601",
    "timezone": "UTC"
  },
  "queries": [],
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

### Shared Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Insight type: `bar`, `pie`, `line`, or `text` |
| `name` | string | Display name for the insight |
| `id` | string | Unique insight identifier |
| `orgId` | string | Organization identifier |
| `createdAt` | datetime | ISO 8601 creation timestamp |
| `updatedAt` | datetime | ISO 8601 last update timestamp |
| `queries` | array | Data queries powering the insight |
| `formulas` | array | Mathematical expressions for data transformation |
| `timeRange` | object | Time range configuration with optional step aggregation |
| `groupBy` | string | Column to group results by |
| `metadata` | object | Visualization settings (bar/line only) |

## Query Types

Insights support queries on two tables:

### Call Table Queries
- String columns: `id`, `artifact.structuredOutputs[OutputID]`
- Number columns: `cost`, `duration`, `averageModelLatency`, etc.
- Operations: `count`, `average`, `sum`, `min`, `max`

### Events Table Queries
- Event types: call lifecycle, assistant operations, transcriber events, etc.
- Operations: `count`, `percentage`
- Supports filtering on event-specific fields

## Time Range Configuration

- `step`: Aggregation interval (`minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`)
- `start`: ISO 8601 date or relative format (e.g., `-7d`)
- `end`: ISO 8601 date or relative format (default: now)
- `timezone`: IANA timezone string (default: UTC)

## Code Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.insight.insight_controller_find_one(id="insight_123")
print(response)
```
