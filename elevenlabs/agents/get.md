# Get Agent API Documentation

## Endpoint Overview

The **Get Agent** endpoint retrieves configuration details for a conversational AI agent by its ID.

**Request Details:**
- **Method:** GET
- **URL:** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}`

## Required Parameters

| Parameter | Location | Type | Description |
|-----------|----------|------|-------------|
| `agent_id` | Path | string | The id of an agent. This is returned on agent creation. |

## Optional Parameters

| Parameter | Location | Type | Description |
|-----------|----------|------|-------------|
| `version_id` | Query | string | The ID of the agent version to use |
| `branch_id` | Query | string | The ID of the branch to use |
| `xi-api-key` | Header | string | API key for authentication |

## Server Endpoints

The API is available across multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Response Format

**Success Response (200):**
- Content-Type: `application/json`
- Schema: `GetAgentResponseModel`

**Validation Error (422):**
- Content-Type: `application/json`
- Schema: `HTTPValidationError`

The response returns comprehensive agent configuration including conversational settings, LLM parameters, tools, knowledge bases, TTS/ASR settings, and widget customization options.
