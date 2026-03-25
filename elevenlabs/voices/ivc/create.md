# Create IVC Voice API Documentation

## Endpoint Overview

The Create IVC Voice endpoint allows developers to generate voice clones and integrate them into their voice library. This POST request accepts multipart form data containing audio samples and configuration parameters.

**Endpoint:** `POST https://api.elevenlabs.io/v1/voices/add`

## Key Parameters

The API requires:
- **name** (string, required): The name that identifies this voice. This will be displayed in the dropdown of the website.
- **files** (array, required): A list of file paths to audio recordings intended for voice cloning.

Optional parameters include:
- **remove_background_noise** (boolean): Applies audio isolation to samples; default is false
- **description** (string): Additional voice information
- **labels** (object/string): Metadata including language, accent, gender, or age

## Response Structure

Successful requests return a 200 status with:
- **voice_id** (string): The ID of the newly created voice.
- **requires_verification** (boolean): Whether the voice requires verification

## Available Servers

The API operates across multiple regional endpoints:
- Standard: https://api.elevenlabs.io
- US: https://api.us.elevenlabs.io
- EU: https://api.eu.residency.elevenlabs.io
- India: https://api.in.residency.elevenlabs.io

## SDK Examples

Code samples are available in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating implementation across multiple programming environments.
