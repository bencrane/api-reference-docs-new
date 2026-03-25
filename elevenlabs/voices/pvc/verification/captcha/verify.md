# Verify PVC Verification Captcha

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/captcha` that allows developers to submit captcha verification for a PVC voice.

## Request Details

**Method:** POST
**Path Parameter:** `voice_id` (required) - The voice identifier to verify
**Header:** `xi-api-key` (optional)
**Content-Type:** multipart/form-data

### Request Body

The endpoint requires a single binary file parameter:
- **recording** (required): Audio recording of the user in binary format

## Response Structure

A successful request (HTTP 200) returns a JSON object containing:
- **status** (string): Returns "ok" on success; otherwise an error message with status 500

## Error Handling

The API returns HTTP 422 for validation errors, providing details about malformed requests or missing required fields.

## Available Regional Endpoints

The service is accessible through multiple regional servers:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Examples

The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to construct and submit captcha verification requests across different programming languages and environments.
