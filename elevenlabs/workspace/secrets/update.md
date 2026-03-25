# Update Secret API Documentation

## Endpoint Overview

The ElevenLabs API provides a PATCH endpoint for updating existing workspace secrets: `PATCH https://api.elevenlabs.io/v1/convai/secrets/{secret_id}`

## Request Requirements

The endpoint requires three mandatory fields in the JSON request body:
- **type**: Must be set to `"update"`
- **name**: The secret's identifier name
- **value**: The secret's value content

An optional `xi-api-key` header can be included for authentication purposes.

## Response Structure

On successful completion (HTTP 200), the API returns a response containing:
- **type**: Always `"stored"` to confirm persistence
- **secret_id**: The unique identifier for the secret
- **name**: The name provided in the request

## Available Servers

The endpoint is accessible across multiple regional servers:
- `https://api.elevenlabs.io` (primary)
- `https://api.us.elevenlabs.io` (US region)
- `https://api.eu.residency.elevenlabs.io` (EU region)
- `https://api.in.residency.elevenlabs.io` (India region)

## SDK Implementation Examples

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to invoke the update operation with the required parameters across different programming languages and HTTP clients.
