# Preview Insight API Reference

## Endpoint

**POST** `https://api.vapi.ai/reporting/insight/preview`

## Description

Generates a preview of an insight by executing queries and applying formulas to transform the data before visualization.

## Authentication

**Header Parameter:**
- `Authorization` (required): API key from the [Dashboard](dashboard.vapi.ai)

## Request Body

The request accepts one of four insight types via discriminator `type`:

### Bar Insight
```yaml
type: bar
name: string (optional)
queries: array (required)
  - JSONQueryOnCallTableWithStringTypeColumn
  - JSONQueryOnCallTableWithNumberTypeColumn
  - JSONQueryOnCallTableWithStructuredOutputColumn
  - JSONQueryOnEventsTable
formulas: array (optional)
  - InsightFormula
metadata: BarInsightMetadata (optional)
timeRange: InsightTimeRangeWithStep (optional)
groupBy: string (optional) # assistantId, workflowId, squadId, phoneNumberId, type, endedReason, customerNumber, campaignId, artifact.structuredOutputs[OutputID]
```

### Pie Insight
```yaml
type: pie
name: string (optional)
queries: array (required)
formulas: array (optional)
timeRange: InsightTimeRange (optional)
groupBy: string (optional)
```

### Line Insight
```yaml
type: line
name: string (optional)
queries: array (required)
formulas: array (optional)
metadata: LineInsightMetadata (optional)
timeRange: InsightTimeRangeWithStep (optional)
groupBy: string (optional)
```

### Text Insight
```yaml
type: text
name: string (optional)
queries: array (required) # Single query or multiple with formula
formula: object (optional)
timeRange: InsightTimeRange (optional)
```

## Query Types

### Call Table Queries

**String Type Column Query:**
```yaml
type: vapiql-json
table: call
column: id | artifact.structuredOutputs[OutputID]
operation: count
filters: array (optional)
name: string (optional)
```

**Number Type Column Query:**
```yaml
type: vapiql-json
table: call
column: cost | duration | averageModelLatency | averageVoiceLatency | averageTranscriberLatency | averageTurnLatency | averageEndpointingLatency | artifact.structuredOutputs[OutputID]
operation: average | sum | min | max
filters: array (optional)
name: string (optional)
```

**Structured Output Column Query:**
```yaml
type: vapiql-json
table: call
column: artifact.structuredOutputs[OutputID]
operation: average | count | sum | min | max
filters: array (optional)
name: string (optional)
```

### Events Table Query

```yaml
type: vapiql-json
table: events
on: string (required) # call.started, call.ended, assistant.voice.requestSucceeded, etc.
operation: count | percentage
filters: array (optional)
name: string (optional)
```

## Time Range Configuration

```yaml
start: string (optional) # ISO 8601 or relative (-7d, -2h, etc.)
end: string (optional) # ISO 8601 or relative
timezone: string (optional) # Defaults to UTC
step: minute | hour | day | week | month | quarter | year (optional, bar/line only)
```

## Formulas

Mathematical expressions using MathJS syntax:
```yaml
name: string
formula: string # e.g., "{{query_name}} / {{['other query']}} * 100"
```

## Filters

Supported filter types:
- **String filters:** `=`, `!=`, `contains`, `not_contains`
- **String array filters:** `in`, `not_in`, `is_empty`, `is_not_empty`
- **Number filters:** `=`, `!=`, `>`, `<`, `>=`, `<=`
- **Number array filters:** `in`, `not_in`
- **Date filters:** `=`, `!=`, `>`, `<`, `>=`, `<=`
- **Structured output filters:** varies by data type

## Response

```yaml
200 OK
{
  "id": string,
  "insightId": string,
  "orgId": string,
  "createdAt": string (ISO 8601),
  "updatedAt": string (ISO 8601)
}
```

## Example Request

```json
{
  "type": "bar",
  "name": "Call Volume by Assistant",
  "queries": [
    {
      "type": "vapiql-json",
      "table": "call",
      "column": "id",
      "operation": "count",
      "name": "Total Calls"
    }
  ],
  "timeRange": {
    "step": "day",
    "start": "-7d",
    "end": "now"
  },
  "groupBy": "assistantId"
}
```

## SDK Usage

```python
from vapi import Vapi, JsonQueryOnCallTableWithStringTypeColumn

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.insight.insight_controller_preview(
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
