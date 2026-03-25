# Create Tool API Reference

## Endpoint

**POST** `https://api.vapi.ai/tool`

## Description

Creates a new tool that can be called during assistant interactions. Tools enable the assistant to execute external actions, make API requests, or trigger specific workflows based on conversation context.

## Authentication

**Header Parameter:**
- `Authorization` (required): API key retrieved from the Vapi Dashboard

**Content-Type:** `application/json`

## Request Body

The request accepts a comprehensive tool configuration object with the following main sections:

### Core Tool Definition
- **name** (string, required): Function name (a-z, A-Z, 0-9, underscores, dashes; max 64 characters)
- **description** (string): Purpose and usage guidance for the AI model
- **parameters** (OpenAIFunctionParameters): Input schema defining function arguments

### Server Configuration
Specifies where tool requests are sent:
- **url** (string): Destination endpoint
- **method** (string): HTTP verb (POST, GET, PUT, PATCH, DELETE)
- **headers** (object): Custom request headers
- **timeoutSeconds** (number): Request timeout (default: 20)
- **credentialId** (string): Authentication credential reference
- **backoffPlan** (BackoffPlan): Retry strategy for failed requests

### Message Handling
Control assistant responses at different tool lifecycle stages:
- **ToolMessageStart**: Spoken when tool execution begins
- **ToolMessageComplete**: Response upon successful completion
- **ToolMessageFailed**: Fallback message if execution fails
- **ToolMessageDelayed**: Message if processing exceeds timing threshold

Messages support:
- Conditional triggering via `conditions` array
- Multi-language variants through `contents` array
- Role designation (assistant speaks, system hints to model)

### Advanced Features

**Variable Extraction:**
- `variableExtractionPlan.schema`: JSON Schema defining data to extract from responses
- `variableExtractionPlan.aliases`: Additional computed variables with Liquid template syntax

**Rejection Plan:**
- `rejectionPlan.conditions`: Regex, Liquid, or grouped conditions preventing tool execution

**Transfer Capabilities:**
- Transfer to phone numbers, SIP URIs, or other assistants
- Multiple transfer modes (blind, warm, experimental)
- Context engineering for conversation history

## Response

**Status Code:** `201 Created`

**Response Body:**
Returns the created tool object with assigned `id` and all configuration details.

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "parameters": {
    "type": "object",
    "properties": {},
    "required": []
  },
  "server": {
    "url": "string",
    "method": "POST"
  }
}
```

## Key Schema Components

**JsonSchema**: Supports primitive types (string, number, integer, boolean) and complex types (array, object) with recursive nesting for nested structures.

**BackoffPlan**: Configures retry behavior with type ("fixed" or "exponential"), max retries, and base delay in seconds.

**Conditions**: Enable conditional messaging using regex patterns, Liquid templates, or grouped boolean logic (AND/OR).

**TextContent**: Multi-language message support with type, text content, and ISO language code.
