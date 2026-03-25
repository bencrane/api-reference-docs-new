# Delete Voice Sample

This API endpoint enables removal of a voice sample by its identifier.

## Endpoint Details

**DELETE** `https://api.elevenlabs.io/v1/voices/{voice_id}/samples/{sample_id}`

The operation removes a sample by its ID and requires two path parameters: the voice identifier and the sample identifier.

## Required Parameters

- **voice_id**: Identifier for the voice (can be obtained via the Get voices endpoint)
- **sample_id**: Identifier for the sample to remove (retrievable via the Get voices endpoint)

## Optional Headers

- **xi-api-key**: Authentication header (optional in schema)

## Response Format

**Success (200)**: Returns a `DeleteSampleResponse` object containing a `status` field. On success, this field contains "ok"; otherwise, an error message with status 500 is provided.

**Validation Error (422)**: Returns an `HTTPValidationError` with validation details.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating deletion of a sample using voice ID "21m00Tcm4TlvDq8ikWAM" and sample ID "VW7YKqPnjY4h39yTbx2L".
