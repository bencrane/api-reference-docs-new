# Update Structured Output API Reference

## Endpoint

**Method:** PATCH
**URL:** `https://api.vapi.ai/structured-output/{id}`
**Content-Type:** `application/json`

## Description

This endpoint allows you to update an existing structured output configuration. Structured outputs enable extraction of data from conversations using either AI-based extraction or regex pattern matching.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the structured output to update |

### Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schemaOverride` | string | Yes | Schema override parameter for the update |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Request Body

The request body uses the `UpdateStructuredOutputDTO` schema with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | enum | Output type: `ai` (LLM-based extraction, default) or `regex` (pattern-based) |
| `regex` | string | Regex pattern for transcript matching (regex type only) |
| `model` | object | LLM configuration (OpenAI, Anthropic, Google, or custom provider) |
| `compliancePlan` | object | Compliance configuration for sensitive data handling |
| `name` | string | Human-readable name for the structured output |
| `description` | string | Context about extracted data and usage |
| `assistantIds` | array | Assistant IDs linked to this output |
| `workflowIds` | array | Workflow IDs linked to this output |
| `schema` | object | JSON Schema defining extraction structure |

## Response

**Status Code:** 200 OK

The response returns a `StructuredOutput` object containing:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `orgId` | string | Organization identifier |
| `createdAt` | string (date-time) | ISO 8601 creation timestamp |
| `updatedAt` | string (date-time) | ISO 8601 last update timestamp |
| `type` | enum | Output type (`ai` or `regex`) |
| `name` | string | Structured output name |
| `description` | string | Purpose and usage context |
| `schema` | object | JSON Schema definition |
| `model` | object | Model configuration used |
| `assistantIds` | array | Linked assistant identifiers |
| `workflowIds` | array | Linked workflow identifiers |

## Example Usage

### Python SDK

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.structured_outputs.structured_output_controller_update(
    id="output-123",
    schema_override="schemaOverride",
)
```

### Request Example

```json
PATCH /structured-output/output-123?schemaOverride=value
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

{
  "type": "ai",
  "name": "Customer Information",
  "description": "Extracts customer details from conversations",
  "schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "Customer full name"
      },
      "email": {
        "type": "string",
        "format": "email",
        "description": "Customer email address"
      }
    },
    "required": ["name", "email"]
  }
}
```

### Response Example

```json
{
  "id": "output-123",
  "orgId": "org-456",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-20T14:45:30Z",
  "type": "ai",
  "name": "Customer Information",
  "description": "Extracts customer details from conversations",
  "schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "Customer full name"
      },
      "email": {
        "type": "string",
        "format": "email",
        "description": "Customer email address"
      }
    },
    "required": ["name", "email"]
  },
  "assistantIds": ["asst-789"],
  "workflowIds": []
}
```

## Notes

- If no model is specified, GPT-4.1 is used by default
- Liquid templating is supported in custom system/user prompts
- For regex type, both raw patterns and regex literal format are supported using RE2 syntax
- Compliance overrides should only be enabled when no sensitive data will be stored
