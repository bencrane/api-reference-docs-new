# Get Separated Speaker Audio

## Endpoint Overview

The API endpoint retrieves isolated audio for a specific speaker from a voice sample:

**GET** `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio`

## Path Parameters

Three required identifiers must be provided:

- **voice_id**: The voice identifier (available via the voices list endpoint)
- **sample_id**: The sample identifier to query
- **speaker_id**: The speaker identifier (obtainable from the speakers list endpoint for a given sample)

## Optional Headers

- **xi-api-key**: API authentication key

## Response Format

A successful request returns a JSON object containing:

- **audio_base_64**: The encoded audio data
- **media_type**: Format specification for the audio content
- **duration_secs**: Audio length as a numeric value

## Available Servers

The API is accessible through multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Implementation Examples

SDK implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The examples demonstrate consistent parameter passing across different programming languages for retrieving speaker-separated audio content.
