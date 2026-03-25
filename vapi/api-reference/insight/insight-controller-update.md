# Update Insight API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/reporting/insight/{id}`

## Description

Updates an existing insight with new configuration, queries, formulas, and visualization settings.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the insight to update |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from Dashboard (bearer token format) |

## Request Body

The request body uses a discriminated union based on the `type` field. Four insight types are supported:

### Bar Insight

```json
{
  "type": "bar",
  "name": "string (optional)",
  "formulas": [
    {
      "name": "string",
      "formula": "string (MathJS expression with {{query_name}} references)"
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
    "step": "minute|hour|day|week|month|quarter|year",
    "start": "ISO 8601 or relative time (-{number}{unit})",
    "end": "ISO 8601 or relative time",
    "timezone": "string (default: UTC)"
  },
  "groupBy": "assistantId|workflowId|squadId|phoneNumberId|type|endedReason|customerNumber|campaignId|artifact.structuredOutputs[OutputID]",
  "queries": [
    {
      "type": "vapiql-json",
      "table": "call|events",
      "column": "string",
      "operation": "count|average|sum|min|max|percentage",
      "filters": [],
      "name": "string"
    }
  ]
}
```

### Pie Insight

```json
{
  "type": "pie",
  "name": "string (optional)",
  "formulas": [],
  "timeRange": {
    "start": "ISO 8601 or relative time",
    "end": "ISO 8601 or relative time",
    "timezone": "string"
  },
  "groupBy": "assistantId|workflowId|...",
  "queries": []
}
```

### Line Insight

```json
{
  "type": "line",
  "name": "string (optional)",
  "formulas": [],
  "metadata": {
    "xAxisLabel": "string",
    "yAxisLabel": "string",
    "yAxisMin": 0,
    "yAxisMax": 100,
    "name": "string"
  },
  "timeRange": {
    "step": "minute|hour|day|week|month|quarter|year",
    "start": "ISO 8601 or relative time",
    "end": "ISO 8601 or relative time",
    "timezone": "string"
  },
  "groupBy": "assistantId|workflowId|...",
  "queries": []
}
```

### Text Insight

```json
{
  "type": "text",
  "name": "string (optional)",
  "formula": {},
  "timeRange": {
    "start": "ISO 8601 or relative time",
    "end": "ISO 8601 or relative time",
    "timezone": "string"
  },
  "queries": []
}
```

## Query Types

### Call Table Query (String Column)

```json
{
  "type": "vapiql-json",
  "table": "call",
  "column": "id|artifact.structuredOutputs[OutputID]",
  "operation": "count",
  "name": "Query Name",
  "filters": []
}
```

### Call Table Query (Number Column)

```json
{
  "type": "vapiql-json",
  "table": "call",
  "column": "cost|duration|averageModelLatency|averageVoiceLatency|averageTranscriberLatency|averageTurnLatency|averageEndpointingLatency|artifact.structuredOutputs[OutputID]",
  "operation": "average|sum|min|max",
  "name": "Query Name",
  "filters": []
}
```

### Events Table Query

```json
{
  "type": "vapiql-json",
  "table": "events",
  "on": "call.started|call.ended|call.inProgress|...",
  "operation": "count|percentage",
  "name": "Query Name",
  "filters": []
}
```

## Filter Types

### String Column Filter

```json
{
  "column": "assistantId|workflowId|squadId|phoneNumberId|type|customerNumber|status|endedReason|forwardedPhoneNumber|campaignId",
  "operator": "=|!=|contains|not_contains",
  "value": "string"
}
```

### Number Column Filter

```json
{
  "column": "duration|cost|averageModelLatency|averageVoiceLatency|averageTranscriberLatency|averageTurnLatency|averageEndpointingLatency",
  "operator": "=|!=|>|<|>=|<=",
  "value": 0
}
```

### Date Column Filter

```json
{
  "column": "startedAt|endedAt",
  "operator": "=|!=|>|<|>=|<=",
  "value": "ISO 8601 date-time string"
}
```

## Response

**Status Code:** 200 OK

```json
{
  "type": "bar|pie|line|text",
  "name": "string",
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:35:00Z",
  "formulas": [],
  "metadata": {},
  "timeRange": {},
  "groupBy": "string",
  "queries": []
}
```

## Formula Syntax

Formulas use MathJS expressions with query references in LiquidJS format:

- `{{query_name}}` - For single-word query names
- `{{['query name']}}` - For multi-word query names

**Example:**
```
{{['Query 1']}} / {{['Query 2']}} * 100
({{Query1}} * 10) + {{Query2}}
```

Supported operations: `+`, `-`, `*`, `/`, `%`

## Time Range Defaults

- **Start:** 7 days ago
- **End:** Now
- **Timezone:** UTC
- **Step:** Day

## Example Request

```bash
curl -X PATCH https://api.vapi.ai/reporting/insight/insight-123 \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "bar",
    "name": "Call Duration Analysis",
    "timeRange": {
      "step": "day",
      "start": "-7d",
      "end": "now",
      "timezone": "UTC"
    },
    "groupBy": "assistantId",
    "queries": [
      {
        "type": "vapiql-json",
        "table": "call",
        "column": "duration",
        "operation": "average",
        "name": "Avg Duration",
        "filters": []
      }
    ]
  }'
```

## Example Response

```json
{
  "type": "bar",
  "name": "Call Duration Analysis",
  "id": "insight-123",
  "orgId": "org-456",
  "createdAt": "2024-01-10T08:00:00Z",
  "updatedAt": "2024-01-15T10:35:00Z",
  "timeRange": {
    "step": "day",
    "start": "-7d",
    "end": "now",
    "timezone": "UTC"
  },
  "groupBy": "assistantId",
  "queries": [
    {
      "type": "vapiql-json",
      "table": "call",
      "column": "duration",
      "operation": "average",
      "name": "Avg Duration",
      "filters": []
    }
  ]
}
```

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.insight.insight_controller_update(id="insight-123")
```
