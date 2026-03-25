# Delete Agent API Documentation

## Endpoint Overview

The Delete Agent endpoint removes a conversational AI agent from the ElevenLabs platform via a DELETE request to `https://api.elevenlabs.io/v1/convai/agents/{agent_id}`.

## Key Parameters

The API requires an `agent_id` path parameter, described as "The id of an agent. This is returned on agent creation." An optional `xi-api-key` header can be included for authentication.

## Response Handling

A successful deletion returns a 200 status code. The API may also return a 422 validation error response with detailed error information if the request contains invalid parameters.

## Implementation Examples

The documentation provides code samples across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript example demonstrates using the ElevenLabs SDK:

```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.agents.delete("agent_3701k3ttaq12ewp8b7qv5rfyszkz");
```

The Python SDK approach is similarly straightforward, while lower-level implementations in Go and other languages show constructing raw HTTP DELETE requests to the endpoint with the agent ID.
