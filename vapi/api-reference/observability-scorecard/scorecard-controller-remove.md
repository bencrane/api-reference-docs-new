# Delete Scorecard API Reference

## Endpoint

**Method:** DELETE
**URL:** `https://api.vapi.ai/observability/scorecard/{id}`

## Description

This endpoint removes a scorecard from the system. Upon successful deletion, the complete scorecard object is returned.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the scorecard to be deleted |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key retrieved from the Dashboard for authentication |

## Response

**Status Code:** 200 OK

**Response Schema:** Scorecard object with the following structure:

```yaml
{
  id: string,                    # Unique scorecard identifier
  orgId: string,                 # Organization identifier
  createdAt: string (ISO 8601),  # Creation timestamp
  updatedAt: string (ISO 8601),  # Last update timestamp
  name: string,                  # Scorecard name (user reference)
  description: string,           # Scorecard description (user reference)
  metrics: array,                # Array of ScorecardMetric objects
  assistantIds: array            # Assistant IDs linked to scorecard
}
```

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.observability_scorecard.scorecard_controller_remove(id="id")
```
