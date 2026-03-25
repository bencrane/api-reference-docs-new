# Get Structured Output API Reference

## Endpoint

**GET** `https://api.vapi.ai/structured-output/{id}`

## Description

Retrieves a structured output configuration by its unique identifier. This endpoint allows you to fetch details about how data extraction is configured for a specific structured output instance.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier for the structured output |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard (dashboard.vapi.ai)" |

## Response

### Success Response (200)

Returns a `StructuredOutput` object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier for the structured output |
| `orgId` | string | Organization ID that owns this structured output |
| `createdAt` | string (ISO 8601) | Creation timestamp |
| `updatedAt` | string (ISO 8601) | Last update timestamp |
| `name` | string | Name of the structured output |
| `description` | string | Description of what data gets extracted |
| `type` | enum | Either `ai` (LLM-based) or `regex` (pattern-based) |
| `schema` | JsonSchema | JSON Schema definition for extracted data |
| `model` | object | Model configuration (OpenAI, Anthropic, Google, etc.) |
| `regex` | string | Regex pattern (only for type: "regex") |
| `assistantIds` | array | Assistant IDs linked to this output |
| `workflowIds` | array | Workflow IDs linked to this output |
| `compliancePlan` | object | Compliance configuration overrides |

## Code Example

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN_HERE",
)

client.structured_outputs.structured_output_controller_find_one(
    id="id",
)
```
