# Create Scorecard API Reference

## Endpoint

**Method:** POST
**URL:** `https://api.vapi.ai/observability/scorecard`
**Content-Type:** `application/json`

## Description

Creates a new scorecard for evaluating assistant performance based on structured output metrics and conditions.

## Parameters

### Headers

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Authorization | string | Yes | "Retrieve your API Key from Dashboard" |

## Request Schema

The request body follows the `CreateScorecardDTO` schema:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | No | User-facing scorecard identifier, not used for evaluation |
| description | string | No | User-facing scorecard explanation, not used for evaluation |
| metrics | array | **Yes** | Metrics containing structured output IDs and evaluation conditions |
| assistantIds | array | No | Assistant IDs this scorecard links to for call evaluation |

### Metrics Structure

Each metric object requires:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| structuredOutputId | string | **Yes** | "unique identifier for the structured output that will be used to evaluate the scorecard" |
| conditions | array | **Yes** | "conditions that will be used to evaluate the scorecard" with comparators, values, and points |

## Response Schema

The `Scorecard` object returns:

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique scorecard identifier |
| orgId | string | Organization identifier |
| createdAt | string | ISO 8601 timestamp of creation |
| updatedAt | string | ISO 8601 timestamp of last modification |
| name | string | Scorecard name |
| description | string | Scorecard description |
| metrics | array | Configured metrics array |
| assistantIds | array | Linked assistant IDs |

## Example Request

```python
from vapi import Vapi, ScorecardMetric

client = Vapi(token="YOUR_TOKEN_HERE")

client.observability_scorecard.scorecard_controller_create(
    metrics=[
        ScorecardMetric(
            structured_output_id="call_duration_seconds",
            conditions=[{}],
        )
    ],
)
```

## Response Status

**201 Created** - Returns the newly created Scorecard object with all assigned fields populated.
