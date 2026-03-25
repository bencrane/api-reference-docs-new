# Get Tool API Reference

## Endpoint

**GET** `https://api.vapi.ai/tool/{id}`

## Description

Retrieves a specific tool by its ID from the Vapi API.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the tool to retrieve |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from your Vapi Dashboard |

## Response

### 200 Success Response

Returns the complete tool configuration object in JSON format.

The response includes comprehensive tool settings such as:

- **Messages**: Configuration for request-start, request-complete, request-failed, and request-response-delayed messages
- **Server Configuration**: URL, headers, timeout, and retry/backoff settings
- **Function Definition**: OpenAI function parameters and schema
- **Parameters**: Tool input parameters with types and descriptions
- **Variable Extraction**: Schema and aliases for extracting values from tool responses
- **Rejection Plans**: Conditional logic for preventing tool execution
- **Transfer Configuration**: Destination and transfer mode settings

### Key Response Properties

- `type`: Discriminator indicating tool type (apiRequest, code, dtmf, endCall, function, transferCall, handoff)
- `messages`: Array containing ToolMessageStart, ToolMessageComplete, ToolMessageFailed, ToolMessageDelayed
- `server`: Server endpoint configuration with authentication and timeout
- `function`: OpenAI function definition with name, description, and parameters
- `rejectionPlan`: Conditions determining when tool execution should be blocked
- `variableExtractionPlan`: Schema for extracting structured data from responses

## Notes

- The response structure varies based on the tool's type and configuration complexity
- Messages support multilingual content through the `contents` array property
- All string values in parameters support Liquid template syntax for dynamic values
