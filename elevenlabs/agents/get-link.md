# Get Link - ElevenLabs Agent API

## Endpoint Overview

The GET endpoint at `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/link` retrieves the current link used to share the agent with others.

## Key Parameters

- **agent_id** (path, required): The agent identifier returned upon creation
- **xi-api-key** (header, optional): API authentication key

## Response Structure

A successful 200 response returns an object containing:
- `agent_id`: The agent's unique identifier
- `token`: A nested object with conversation token data, including expiration time and purpose

## Usage Examples

The documentation provides implementation samples across multiple languages:

- **TypeScript/JavaScript**: Uses the ElevenLabs SDK's `conversationalAi.agents.link.get()` method
- **Python**: Implements via the ElevenLabs client library
- **Go, Ruby, Java, PHP, C#, and Swift**: Direct HTTP GET requests to the endpoint

## Error Handling

A 422 response indicates validation errors, returning details about malformed requests or missing required parameters.
