# Create Draft API Documentation

## Endpoint Overview

The Create Draft endpoint allows you to generate a new draft for an agent using the ElevenLabs Conversational AI API.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/drafts`

**Content-Type:** `application/json`

## Parameters

### Path Parameters
- **agent_id** (required, string): The identifier of an agent, returned upon agent creation

### Query Parameters
- **branch_id** (required, string): The ID of the agent branch to utilize

### Header Parameters
- **xi-api-key** (optional, string): API authentication key

## Request Body

The request requires a JSON payload with the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conversation_config` | object | Yes | Configuration settings for agent conversations |
| `platform_settings` | object | Yes | Platform-specific configuration options |
| `workflow` | AgentWorkflowRequestModel | Yes | The workflow definition for the draft |
| `name` | string | Yes | Identifier name for the draft |
| `tags` | array[string] | No | Labels for organizing and filtering agents |

## Response

**Status Code:** `200 OK`

**Content-Type:** `application/json`

Returns a response object containing the draft details (schema varies based on implementation).

## Error Responses

- **422 Unprocessable Entity**: Validation error in request parameters or body

## API Servers

The API is accessible through multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
