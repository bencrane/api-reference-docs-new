# Delete Structured Output

## Endpoint

**DELETE** `https://api.vapi.ai/structured-output/{id}`

## Description

Removes a structured output configuration from the system.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the structured output to delete |

### Header Parameters

| Name | Type | Required | Description |
|----------|--------|----------|----------------------------------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### 200 OK

Returns the deleted structured output object.

**Content-Type:** `application/json`

### Response Schema

The response follows the `StructuredOutput` schema with these key properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier for the structured output |
| `orgId` | string | Organization ID the output belongs to |
| `name` | string | Name of the structured output |
| `type` | string | Type: `ai` or `regex` |
| `schema` | JsonSchema | JSON Schema definition for output |
| `createdAt` | string (date-time) | Creation timestamp (ISO 8601) |
| `updatedAt` | string (date-time) | Last update timestamp (ISO 8601) |
| `model` | object | Model configuration for extraction |
| `regex` | string | Regex pattern (if type is `regex`) |
| `description` | string | Description of what gets extracted |
| `assistantIds` | array | Associated assistant IDs |
| `workflowIds` | array | Associated workflow IDs |
| `compliancePlan` | object | Compliance overrides |

## Example Request

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

client.structured_outputs.structured_output_controller_remove(
    id="structured-output-id-here"
)
```
