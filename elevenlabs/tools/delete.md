# Delete Tool API Documentation

## Endpoint Overview

The ElevenLabs Delete Tool endpoint removes tools from a workspace via a DELETE request to `https://api.elevenlabs.io/v1/convai/tools/{tool_id}`.

## Key Parameters

The API accepts the following parameters:

- **tool_id** (path, required): The identifier for the tool being removed
- **force** (query, optional): Boolean flag (defaults to false) that when enabled allows deletion even if the tool is actively used by agents
- **xi-api-key** (header, optional): Authentication credential

## Responses

Success returns a 200 status code with JSON content. A 422 status indicates validation errors with detailed error information.

## Implementation Examples

The documentation provides code samples across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.

For instance, the TypeScript example demonstrates: "await client.conversationalAi.tools.delete("tool_id", { force: true });"

The Python equivalent uses: "client.conversational_ai.tools.delete(tool_id="tool_id", force=True)"

## Important Behavior

When the `force` parameter is set to true, dependent agents and branches are automatically updated to remove references to the deleted tool, enabling complete removal regardless of existing dependencies.
