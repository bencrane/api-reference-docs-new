# Train PVC Voice API Documentation

## Endpoint Overview

The Train PVC Voice endpoint initiates a voice training process using ElevenLabs' PVC (Personal Voice Cloning) technology. It's a POST request to `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/train`.

## Key Parameters

**Path Parameter:**
- `voice_id` (required, string): Identifier for the target voice

**Header:**
- `xi-api-key` (optional, string): Authentication token

**Request Body:**
- `model_id` (string): The model identifier for conversion processing

## Response Schema

On success (HTTP 200), the API returns a response containing:
- `status` (string): Confirms request outcome with "ok" for successful submissions

Error responses (HTTP 422) include validation details with location, message, and error type information.

## Available Server Endpoints

The service operates across multiple regional servers:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Implementation Examples

The documentation provides working examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same core operation with language-specific syntax variations.
