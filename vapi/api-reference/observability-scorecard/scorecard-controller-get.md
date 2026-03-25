# Get Scorecard API Reference

## Endpoint

**Method:** GET
**URL:** `https://api.vapi.ai/observability/scorecard/{id}`

## Description

Retrieves a scorecard by its unique identifier. Scorecards are used to evaluate call quality based on structured output metrics.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the scorecard |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API key retrieved from your Dashboard |

## Response Schema

### Scorecard Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique scorecard identifier |
| `orgId` | string | Organization identifier that owns the scorecard |
| `createdAt` | date-time (ISO 8601) | Creation timestamp |
| `updatedAt` | date-time (ISO 8601) | Last update timestamp |
| `name` | string | User-friendly scorecard name |
| `description` | string | Scorecard details for reference |
| `metrics` | array | Collection of evaluation metrics |
| `assistantIds` | array | List of assistant IDs this scorecard is linked to |

### Metric Object

| Field | Type | Description |
|-------|------|-------------|
| `structuredOutputId` | string | References the structured output (number or boolean type only) |
| `conditions` | array | Evaluation rules with comparators, values, and point values |

## Example Usage

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.observability_scorecard.scorecard_controller_get(
    id="scorecard_123"
)
```

## Success Response (200)

```json
{
  "id": "scorecard_123",
  "orgId": "org_456",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:45:00Z",
  "name": "Call Quality Scorecard",
  "description": "Evaluates customer satisfaction metrics",
  "metrics": [
    {
      "structuredOutputId": "output_789",
      "conditions": []
    }
  ],
  "assistantIds": ["assistant_001", "assistant_002"]
}
```
