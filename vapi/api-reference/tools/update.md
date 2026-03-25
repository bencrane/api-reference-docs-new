# Update Tool API Reference

## Endpoint

**Method:** PATCH
**URL:** `https://api.vapi.ai/tool/{id}`
**Content-Type:** `application/json`

## Description

Updates an existing tool configuration in the Vapi system, allowing modifications to tool properties, messages, server settings, and related configurations.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the tool to update |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from Dashboard (dashboard.vapi.ai) |

## Request Body

The request body accepts a JSON object with tool configuration properties. The schema supports multiple tool types with shared and type-specific fields.

### Common Tool Fields

- **messages** - Array of tool messages (request-start, request-complete, request-failed, request-response-delayed)
- **rejectionPlan** - Conditions for rejecting tool calls
- **variableExtractionPlan** - Schema and aliases for extracting variables from responses

### Tool Type: API Request Tool

Includes HTTP configuration:
- **method** - HTTP method (POST, GET, PUT, PATCH, DELETE)
- **url** - Request endpoint
- **server** - Server configuration with timeout, credentials, headers, backoff plan
- **parameters** - Dynamic parameters with Liquid template support

### Tool Type: Function Tool

OpenAI function definition:
- **name** - Function name (a-z, A-Z, 0-9, underscore, dash; max 64 chars)
- **description** - Function purpose for AI decision-making
- **parameters** - JSON Schema object describing accepted parameters
- **strict** - Boolean enabling strict schema adherence

### Tool Type: Transfer Call Tool

Handles call transfers with:
- **destinations** - Array of transfer targets (assistant, number, or SIP)
- Each destination supports custom messages and transfer plans

### Tool Type: Handoff Tool

Transfers calls between assistants with context engineering plans.

### Tool Type: DTMF Tool

Handles DTMF (keypad) input with tones and messages.

### Tool Type: End Call Tool

Terminates calls with optional messages.

## Response

**Status Code:** 200 OK

**Response Body:** Tool object reflecting applied updates, including all configured properties and nested schemas.

## Key Message Types

- **request-start** - Triggered when tool execution begins (blocking optional)
- **request-complete** - Triggered on successful completion (can end call)
- **request-failed** - Triggered on execution failure
- **request-response-delayed** - Triggered when response exceeds timing threshold

## Advanced Features

### Condition System
Tools support conditional execution via:
- **Regex conditions** - Pattern matching on message content
- **Liquid conditions** - Template-based logic evaluation
- **Group conditions** - Nested AND/OR logic

### Variable Extraction
Extract and transform data from tool responses using:
- JSON Schema-based extraction
- Custom aliases with Liquid template syntax
- Nested object and array support

### Backoff Plans
Configure retry behavior:
- **Type** - Fixed or exponential backoff
- **maxRetries** - Number of retry attempts
- **baseDelaySeconds** - Delay between retries
- **excludedStatusCodes** - Codes that skip retries

### Server Configuration
- **timeoutSeconds** - Request timeout (default 20)
- **credentialId** - Authentication credentials
- **staticIpAddressesEnabled** - Use static Vapi-owned IPs
- **encryptedPaths** - Paths to encrypt in request body
- **headers** - Custom HTTP headers

## Example Request

```json
{
  "messages": [
    {
      "type": "request-start",
      "content": "Processing your request"
    },
    {
      "type": "request-complete",
      "content": "Request completed successfully"
    }
  ],
  "server": {
    "url": "https://api.example.com/tool",
    "method": "POST",
    "timeoutSeconds": 30
  }
}
```
