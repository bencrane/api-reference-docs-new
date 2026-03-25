# Update Scorecard API Reference

## Endpoint
**Method:** PATCH
**URL:** `https://api.vapi.ai/observability/scorecard/{id}`
**Content-Type:** application/json

## Description
Updates an existing scorecard with new configuration details, metrics, or linked assistants.

## Parameters

### Path Parameters
- **id** (required, string): The unique identifier of the scorecard to update

### Headers
- **Authorization** (required, string): API key retrieved from the Vapi Dashboard

## Request Body Schema

The request body follows the `UpdateScorecardDTO` schema with these optional fields:

| Field | Type | Description |
|-------|------|-------------|
| name | string | User-facing name for the scorecard (non-evaluative) |
| description | string | User-facing description (non-evaluative) |
| metrics | array | Metrics containing conditions and point values for scoring |
| assistantIds | array | IDs of assistants linked to this scorecard |

### Metrics Structure
Each metric includes:
- **structuredOutputId** (required): Identifier for the structured output (number or boolean type only)
- **conditions** (required): Array of condition objects with comparators, values, and point values

## Response Schema

Returns a `Scorecard` object with:

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique scorecard identifier |
| orgId | string | Organization identifier |
| createdAt | string (ISO 8601) | Scorecard creation timestamp |
| updatedAt | string (ISO 8601) | Last modification timestamp |
| name | string | Scorecard name |
| description | string | Scorecard description |
| metrics | array | Configured metrics for evaluation |
| assistantIds | array | Linked assistant identifiers |

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.observability_scorecard.scorecard_controller_update(
    id="scorecard_12345"
)
```

## Example Response

```json
{
  "id": "scorecard_12345",
  "orgId": "org_789",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-16T14:22:00Z",
  "name": "Call Quality Scorecard",
  "description": "Evaluates call handling metrics",
  "metrics": [
    {
      "structuredOutputId": "output_456",
      "conditions": []
    }
  ],
  "assistantIds": ["assistant_001", "assistant_002"]
}
```
