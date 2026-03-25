# Update Agent - ElevenLabs API Reference

## Endpoint Overview

The Update Agent endpoint allows you to patch an agent's settings using a PATCH request to `https://api.elevenlabs.io/v1/convai/agents/{agent_id}`.

## Request Parameters

**Path Parameters:**
- `agent_id` (required): The identifier of an agent returned upon creation

**Query Parameters:**
- `enable_versioning_if_not_enabled` (optional, boolean): Activate versioning if not already enabled
- `branch_id` (optional, string): The branch identifier to utilize
- `xi-api-key` (optional, header): Your API authentication key

## Request Body

The request accepts a JSON object with these updatable fields:

- `name`: Agent identifier string
- `tags`: Array of classification strings
- `conversation_config`: Conversational settings including ASR, turn detection, TTS, and event configuration
- `platform_settings`: Non-conversation-related configuration
- `workflow`: Agent interaction and tool flow definition
- `version_description`: Version notes for published changes (versioned agents only)

## Response

**Success (200):**
Returns a `GetAgentResponseModel` containing the updated agent configuration.

**Validation Error (422):**
Returns an `HTTPValidationError` with details about invalid parameters.

## API Servers

The endpoint is available across multiple regional servers:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
