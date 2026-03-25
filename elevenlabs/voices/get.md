# Get Voice API Reference

## Endpoint Overview

The Get Voice endpoint retrieves metadata about a specific voice from the ElevenLabs API.

**Endpoint:** `GET https://api.elevenlabs.io/v1/voices/{voice_id}`

**Purpose:** Returns metadata about a specific voice.

## Required Parameters

- **voice_id** (path parameter): The identifier needed to access a particular voice. You can use the Get voices endpoint to list all the available voices.

## Optional Parameters

- **with_settings** (query): This parameter is now deprecated. It is ignored and will be removed in a future version.
- **xi-api-key** (header): API authentication key

## Response Schema

A successful request returns a Voice object containing:

- Core properties: voice_id, name, category, description
- Audio samples and preview URL
- Voice settings (stability, similarity_boost, style, speed)
- Fine-tuning information
- Sharing and verification details
- Tier availability and language support

## Available Server Regions

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Examples

Code implementations are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript example demonstrates:

```typescript
await client.voices.get("21m00Tcm4TlvDq8ikWAM", { withSettings: true });
```
