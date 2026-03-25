# Run Structured Output - API Reference

## Endpoint Details

**Method:** POST
**URL:** `https://api.vapi.ai/structured-output/run`
**Content-Type:** application/json

## Description

This endpoint executes structured output extraction on one or more call records. It allows you to run either a previously created structured output by ID or a transient structured output definition, updating call artifacts with the extracted data.

## Authentication

**Header Parameter:** `Authorization`
- **Required:** Yes
- **Description:** API Key from [Dashboard](dashboard.vapi.ai)
- **Schema:** string

## Request Body

The request accepts a `StructuredOutputRunDTO` object with the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previewEnabled` | boolean | No | If true, executes immediately and returns response without updating artifacts. Default: false |
| `structuredOutputId` | string | No | ID of existing structured output to run. Either this or `structuredOutput` must be provided |
| `structuredOutput` | CreateStructuredOutputDTO | No | Transient structured output definition. Either this or `structuredOutputId` must be provided |
| `callIds` | array[string] | **Yes** | Array of call IDs to process. Max 1 ID if preview is true; up to 100 if false |

### CreateStructuredOutputDTO Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | **Yes** | Name of the structured output |
| `schema` | JsonSchema | **Yes** | JSON Schema definition for extraction |
| `type` | string | No | Either 'ai' (default) or 'regex' |
| `regex` | string | No | Regex pattern (required when type is 'regex'). Supports raw patterns or regex literals with RE2 syntax |
| `model` | object | No | Model configuration (OpenAI, Anthropic, Google, or custom). Defaults to GPT-4.1 |
| `description` | string | No | Context about what data will be extracted |
| `compliancePlan` | object | No | Compliance overrides for storage configuration |
| `assistantIds` | array[string] | No | Assistant IDs to link this output to |
| `workflowIds` | array[string] | No | Workflow IDs to link this output to |

## Response Schema

Returns a `StructuredOutput` object with:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier for the structured output |
| `orgId` | string | Organization ID |
| `name` | string | Name of the structured output |
| `schema` | JsonSchema | JSON Schema definition |
| `type` | string | Type: 'ai' or 'regex' |
| `model` | object | Model configuration used |
| `regex` | string | Regex pattern (if applicable) |
| `description` | string | Description of extraction purpose |
| `createdAt` | string (ISO 8601) | Creation timestamp |
| `updatedAt` | string (ISO 8601) | Last update timestamp |
| `assistantIds` | array[string] | Linked assistant IDs |
| `workflowIds` | array[string] | Linked workflow IDs |
| `compliancePlan` | object | Compliance configuration |

## JSON Schema Types

The `JsonSchema` object supports:
- **Primitive types:** string, number, integer, boolean
- **Complex types:** array, object
- **Format options:** date-time, time, date, duration, email, hostname, ipv4, ipv6, uuid
- **Validation:** pattern (regex), required fields, enum values, nested properties

## Supported Models

**AI-based extraction:**
- OpenAI (gpt-4.1, gpt-4o, gpt-3.5-turbo, etc.)
- Anthropic (claude-3-opus, claude-3-5-sonnet, claude-opus-4, etc.)
- Anthropic Bedrock
- Google (gemini-2.5-pro, gemini-2.0-flash, etc.)
- Custom LLM providers

**Regex-based extraction:** Pattern matching without LLM processing

## Example Request

```bash
curl -X POST https://api.vapi.ai/structured-output/run \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "callIds": ["call_1234567890abcdef"],
    "structuredOutputId": "output_xyz123",
    "previewEnabled": false
  }'
```

## Example Request (Transient Output)

```bash
curl -X POST https://api.vapi.ai/structured-output/run \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "callIds": ["call_1234567890abcdef"],
    "structuredOutput": {
      "name": "Call Summary",
      "type": "ai",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" },
          "sentiment": { "type": "string", "enum": ["positive", "negative", "neutral"] }
        },
        "required": ["summary"]
      }
    }
  }'
```

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.structured_outputs.structured_output_controller_run(
    call_ids=["call_1234567890abcdef"]
)
```

## HTTP Status Codes

- **200 OK:** Successfully executed. Returns the `StructuredOutput` object
- **400 Bad Request:** Invalid parameters or missing required fields
- **401 Unauthorized:** Missing or invalid API key
- **404 Not Found:** Specified structured output ID not found

## Key Notes

- When using liquid templating in custom prompts, reference conversation history with `{{transcript}}` or `{{messages}}`
- Access structured output definition via `{{structuredOutput}}`, `{{structuredOutput.name}}`, `{{structuredOutput.schema}}`, etc.
- Preview mode returns immediately without persisting changes to call artifacts
- Maximum 100 call IDs per request (1 ID required for preview mode)
