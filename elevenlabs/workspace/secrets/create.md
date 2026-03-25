# Create Secret - ElevenLabs API Documentation

## Endpoint Overview
The "Create secret" endpoint is a POST request to `https://api.elevenlabs.io/v1/convai/secrets` that "Create[s] a new secret for the workspace."

## Request Details
The endpoint requires three JSON body parameters:
- **type**: Must be set to "new"
- **name**: The secret's identifier name
- **value**: The secret's actual value

An optional `xi-api-key` header can be included for authentication.

## Response
Upon successful creation, the API returns a 200 status with an object containing:
- **type**: Always "stored"
- **secret_id**: A unique identifier for the created secret
- **name**: Echo of the submitted name

## Available Servers
The API is accessible through four regional endpoints:
- Standard US: `https://api.elevenlabs.io`
- US regional: `https://api.us.elevenlabs.io`
- EU residency: `https://api.eu.residency.elevenlabs.io`
- India residency: `https://api.in.residency.elevenlabs.io`

## SDK Support
The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating consistent patterns across supported languages for calling this workspace secret creation function.
