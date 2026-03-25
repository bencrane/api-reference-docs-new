# Create Agent Branch API Documentation

## Endpoint Overview

The Create Agent Branch endpoint allows you to establish a new branch from a specific version of an agent's main branch using the ElevenLabs Conversational AI API.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches`

## Request Parameters

### Path Parameters
- **agent_id** (required, string): The identifier of an agent, provided upon agent creation

### Header Parameters
- **xi-api-key** (optional, string): Authentication key for API requests

## Request Body

The request accepts a JSON object with the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| parent_version_id | string | Yes | Identifier of the version to branch from |
| name | string | Yes | Branch name, unique within the agent |
| description | string | Yes | Descriptive text for the branch |
| conversation_config | object | No | Modifications to conversation settings |
| platform_settings | object | No | Changes to platform configuration |
| workflow | AgentWorkflowRequestModel | No | Updated workflow specification |

## Response

### Success Response (200 OK)
Returns a `CreateAgentBranchResponseModel` containing the newly created branch details.

### Error Response (422)
Returns validation errors in the format specified by `HTTPValidationError`.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
