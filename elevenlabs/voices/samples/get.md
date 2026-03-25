# Get Voice Sample Audio

## Endpoint Overview

The `GET /v1/voices/{voice_id}/samples/{sample_id}/audio` endpoint retrieves audio data from a sample attached to a voice on the ElevenLabs API.

## Key Parameters

- **voice_id** (path, required): Identifies the voice. The Get voices endpoint lists available voices.
- **sample_id** (path, required): Identifies the sample. The Get voices endpoint lists available samples for a voice.
- **xi-api-key** (header, optional): API authentication key

## Response

A successful request returns a 200 status with binary audio data in `application/octet-stream` format. Validation errors return a 422 status with error details.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

**TypeScript** uses `client.voices.samples.audio.get("voice_id", "sample_id")`

**Python** implements the same call through the ElevenLabs client library

Additional code examples are provided for Go, Ruby, Java, PHP, C#, and Swift, demonstrating HTTP GET requests to the endpoint with appropriate response handling for binary audio data.
