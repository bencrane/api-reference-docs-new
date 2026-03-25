# Update PVC Voice

## Overview
This API endpoint allows you to edit metadata for a Personal Voice Clone (PVC) using the ElevenLabs API.

**Endpoint:** `POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}`

## Request Parameters

### Path Parameters
- **voice_id** (required): The identifier for the voice you want to modify. You can retrieve available voices from the voices list endpoint.

### Headers
- **xi-api-key** (optional): Your API authentication key

### Request Body
The request accepts a JSON object with these optional fields:

| Field | Type | Description |
|-------|------|-------------|
| name | string | The voice's display name shown in dropdowns |
| language | string | Language of the voice samples |
| description | string | Metadata describing the voice |
| labels | object | Key-value pairs for categorization (e.g., language, accent, gender, age) |

## Response

**Success (200):** Returns a JSON object containing:
```json
{
  "voice_id": "string"
}
```

**Validation Error (422):** Returns detailed validation error information

## Available Servers
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples
The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating how to call this endpoint with a voice ID and optional metadata parameters.
