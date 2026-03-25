# Get Conversation Audio

## Endpoint Overview

The ElevenLabs API provides a GET endpoint to retrieve audio recordings from conversations: `GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/audio`

## Key Parameters

- **conversation_id** (path, required): Identifies the specific conversation
- **xi-api-key** (header, optional): Authentication credential

## Response Details

A successful request returns a "200" status with audio data in "application/octet-stream" format as binary content. The API can respond with validation errors (422 status) if parameters are invalid.

## Available Servers

The endpoint is accessible through multiple regional servers:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Support

ElevenLabs provides native implementations across TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each SDK abstracts the HTTP complexity, allowing developers to call the audio retrieval method directly with the conversation identifier.

For example, the TypeScript SDK enables retrieval through: `client.conversationalAi.conversations.audio.get(conversation_id)`
