# Get Audio from History Item

## Endpoint Overview

The ElevenLabs API provides a GET endpoint at `https://api.elevenlabs.io/v1/history/{history_item_id}/audio` that "Returns the audio of an history item."

## Key Parameters

- **history_item_id** (path, required): Identifier for the history item. The documentation notes you can retrieve these IDs using the list endpoint.
- **xi-api-key** (header, optional): Your API authentication key

## Response

A successful request returns a 200 status with the audio file in binary format (`application/octet-stream`). Error responses include 422 for validation failures.

## Available Servers

The endpoint operates across four regional servers:
- Global: `https://api.elevenlabs.io`
- US: `https://api.us.elevenlabs.io`
- EU: `https://api.eu.residency.elevenlabs.io`
- India: `https://api.in.residency.elevenlabs.io`

## SDK Implementation Examples

The documentation provides code examples across TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Most implementations follow this pattern: instantiate a client with your API key, then call the audio retrieval method with the history item ID.
