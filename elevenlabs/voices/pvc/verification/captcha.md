# Get PVC Verification Captcha

This endpoint retrieves a captcha for PVC (Professional Voice Cloning) voice verification purposes.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/captcha`

## Parameters

The request requires:
- **voice_id** (path parameter, required): The identifier for the voice, obtainable via the voices listing endpoint
- **xi-api-key** (header, optional): Authentication key for the API

## Response

A successful request returns a 200 status code. Validation errors result in a 422 response containing details about what failed validation.

## Available Servers

The API operates across multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Implementation Examples

The documentation provides working code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. All examples demonstrate passing a voice ID like "21m00Tcm4TlvDq8ikWAM" to retrieve the corresponding captcha for verification workflows.
