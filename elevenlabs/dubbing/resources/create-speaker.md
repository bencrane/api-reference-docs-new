# Create Speaker API Documentation

## Endpoint Overview

The Create Speaker endpoint allows you to add a new speaker to a dubbing project via a POST request to `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker`.

## Request Parameters

**Path Parameter:**
- `dubbing_id` (required): Identifier for the dubbing project

**Header:**
- `xi-api-key` (optional): Authentication key

**Request Body Properties:**
- `speaker_name`: Name assigned to the speaker
- `voice_id`: Either a voice library identifier or 'track-clone'/'clip-clone'
- `voice_stability`: Numerical value (0.0-1.0, defaults to 0.65) for voice consistency
- `voice_similarity`: Numerical value (0.0-1.0, defaults to 1.0) for voice matching
- `voice_style`: Numerical value (0.0-1.0, defaults to 1.0) for stylistic variation

## Response

A successful request returns HTTP 200 with a JSON response containing:
- `version`: Integer version identifier
- `speaker_id`: String identifier for the created speaker

## API Servers

The service operates across multiple regional endpoints including standard US, EU, and India residency options.

## SDK Implementation Examples

The documentation provides complete code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to invoke the speaker creation method with various client libraries.
