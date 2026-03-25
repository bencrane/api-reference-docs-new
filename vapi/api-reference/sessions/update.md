# Update Session API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/session/{id}`

Updates an existing session with new configuration, messages, status, or expiration settings.

## Parameters

### Path Parameters
- **id** (string, required): The unique identifier of the session to update

### Header Parameters
- **Authorization** (string, required): "Retrieve your API Key from Dashboard"

## Request Body

The request accepts a `UpdateSessionDTO` object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| name | string | New session name (max 40 characters) |
| status | enum | New status: `active` or `completed` |
| expirationSeconds | number | Session expiration in seconds (defaults to 86400) |
| messages | array | Updated array of chat messages |

### Message Types

Messages can be one of:
- **SystemMessage**: Contains role, message, time, and secondsFromStart
- **UserMessage**: Includes role, message, timestamps, duration, filtering info, and metadata
- **AssistantMessage**: Contains role, content, optional refusal, tool calls, and metadata
- **ToolMessage**: Response to tool calls with role, content, and tool_call_id
- **DeveloperMessage**: Developer-generated messages with role and content

## Response

Returns a `Session` object (HTTP 200) containing the updated session details, including all configuration properties and message history.

## Cost Tracking

The response may include `SessionCostsItems` data tracking:
- **ModelCost**: Token usage and pricing for language models
- **AnalysisCost**: Analysis operation costs
- **SessionCost**: Overall session costs in USD

## Status Values

Sessions support two states: `active` (ongoing) or `completed` (finished).
