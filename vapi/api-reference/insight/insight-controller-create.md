# Create Insight API Reference

## Endpoint

**POST** `https://api.vapi.ai/reporting/insight`

## Description

Creates a new insight for data visualization and analysis. Insights can be displayed as bar charts, pie charts, line graphs, or text values based on queries from call and event data.

## Authentication

**Header Parameter:**
- `Authorization` (required): Your API Key from the [Dashboard](dashboard.vapi.ai)

## Request Body

The request accepts four insight type variants, distinguished by the `type` discriminator field:

### Bar Chart Insight

```json
{
  "type": "bar",
  "name": "string",
  "queries": [
    {
      "type": "vapiql-json",
      "table": "call",
      "column": "string",
      "operation": "string",
      "name": "string",
      "filters": []
    }
  ],
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
    "yAxisMax": 100,
    "name": "string"
  },
  "timeRange": {
    "step": "day",
    "start": "string",
    "end": "string",
    "timezone": "UTC"
  },
  "groupBy": "assistantId"
}
```

### Pie Chart Insight

```json
{
  "type": "pie",
  "name": "string",
  "queries": [],
  "formulas": [],
  "timeRange": {
    "start": "string",
    "end": "string",
    "timezone": "UTC"
  },
  "groupBy": "assistantId"
}
```

### Line Chart Insight

```json
{
  "type": "line",
  "name": "string",
  "queries": [],
  "formulas": [],
  "metadata": {
    "xAxisLabel": "string",
    "yAxisLabel": "string",
    "yAxisMin": 0,
    "yAxisMax": 100,
    "name": "string"
  },
  "timeRange": {
    "step": "day",
    "start": "string",
    "end": "string",
    "timezone": "UTC"
  },
  "groupBy": "assistantId"
}
```

### Text Insight

```json
{
  "type": "text",
  "name": "string",
  "queries": [],
  "formula": {},
  "timeRange": {
    "start": "string",
    "end": "string",
    "timezone": "UTC"
  }
}
```

## Schema Details

### Query Types

**Call Table Queries (String Type Column):**
- Operates on the `call` table
- Column: `id` or `artifact.structuredOutputs[OutputID]`
- Operation: `count`

**Call Table Queries (Number Type Column):**
- Column: `cost`, `duration`, `averageModelLatency`, `averageVoiceLatency`, `averageTranscriberLatency`, `averageTurnLatency`, `averageEndpointingLatency`, or `artifact.structuredOutputs[OutputID]`
- Operations: `average`, `sum`, `min`, `max`

**Events Table Queries:**
- Table: `events`
- Events: `call.started`, `call.ended`, `call.inProgress`, `assistant.voice.requestStarted`, `assistant.model.tokenReceived`, `pipeline.userSpeechStarted`, and many others
- Operations: `count`, `percentage`

### Filters

Filters are applied based on column type:

**String Filters:**
- Operators: `=`, `!=`, `contains`, `not_contains`
- Columns: `assistantId`, `workflowId`, `squadId`, `phoneNumberId`, `type`, `customerNumber`, `status`, `endedReason`, `forwardedPhoneNumber`, `campaignId`

**Number Filters:**
- Operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Columns: `duration`, `cost`, `averageModelLatency`, `averageVoiceLatency`, `averageTranscriberLatency`, `averageTurnLatency`, `averageEndpointingLatency`

**Date Filters:**
- Operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Columns: `startedAt`, `endedAt`
- Values: ISO 8601 date-time strings

### Time Range

- `start`: ISO 8601 date-time or relative format (e.g., "-7d", "-2w"). Default: 7 days ago
- `end`: ISO 8601 date-time or relative format. Default: now
- `step` (bar/line only): `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`. Default: `day`
- `timezone`: IANA timezone string. Default: `UTC`

Relative time units: `d` (days), `h` (hours), `w` (weeks), `m` (months), `y` (years)

### Formulas

Mathematical expressions using MathJS syntax. Reference query names with "{{query_name}}" or "{{['query name']}}" format. Must contain at least one query reference. Supported operations: `+`, `-`, `*`, `/`, `%`, and any MathJS function.

### Group By Options

`assistantId`, `workflowId`, `squadId`, `phoneNumberId`, `type`, `endedReason`, `customerNumber`, `campaignId`, `artifact.structuredOutputs[OutputID]`

## Response

**Status Code:** 201 Created

```json
{
  "type": "bar",
  "name": "string",
  "queries": [],
  "formulas": [],
  "metadata": {
    "xAxisLabel": "string",
    "yAxisLabel": "string",
    "yAxisMin": 0,
    "yAxisMax": 100,
    "name": "string"
  },
  "timeRange": {
    "step": "day",
    "start": "string",
    "end": "string",
    "timezone": "UTC"
  },
  "groupBy": "assistantId",
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

### Response Fields

- `id`: Unique identifier for the insight
- `orgId`: Organization identifier
- `createdAt`: ISO 8601 creation timestamp
- `updatedAt`: ISO 8601 last updated timestamp

## Python SDK Example

```python
from vapi import Vapi, JsonQueryOnCallTableWithStringTypeColumn

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.insight.insight_controller_create(
    request={
        "type": "bar",
        "queries": [
            JsonQueryOnCallTableWithStringTypeColumn(
                type="vapiql-json",
                table="call",
                column="id",
                operation="count",
            )
        ]
    },
)
```
