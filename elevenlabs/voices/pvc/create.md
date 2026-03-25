# Create PVC Voice API Documentation

## Endpoint Overview

The Create PVC Voice endpoint allows developers to establish a new PVC (Personal Voice Clone) voice with metadata but without audio samples.

**Endpoint:** `POST https://api.elevenlabs.io/v1/voices/pvc`

## Required Parameters

The request body must include two mandatory fields:

- **name** (string): "The name that identifies this voice. This will be displayed in the dropdown of the website."
- **language** (string): Language used in the samples

## Optional Parameters

- **description** (string): Description for the created voice
- **labels** (object): Voice characteristics with keys for language, accent, gender, or age

## Response Format

A successful request returns HTTP 200 with:
```json
{
  "voice_id": "string"
}
```

## Available Server URLs

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. All examples demonstrate the basic pattern of providing a name and language to create a voice.
