# Get Voice Settings

**Endpoint:** `GET https://api.elevenlabs.io/v1/voices/{voice_id}/settings`

## Overview

This API retrieves configuration parameters for a specific voice. The "similarity_boost" setting maps to the web app's "Clarity + Similarity Enhancement" control, while "stability" corresponds to the "Stability" slider.

## Parameters

**Path Parameter:**
- `voice_id` (required, string): The voice identifier. Available voices can be listed via the voices endpoint.

**Header Parameter:**
- `xi-api-key` (optional, string): API authentication key

## Response Schema

The successful response returns a `VoiceSettings` object containing:

- **stability** (number): Controls voice consistency and emotional variation. Lower values increase emotional range; higher values create monotonous output.
- **use_speaker_boost** (boolean): Enhances similarity to original speaker but increases latency.
- **similarity_boost** (number): Determines how closely the output matches the original voice.
- **style** (number): Amplifies original speaker characteristics; values above 0 increase latency.
- **speed** (number): Controls speech rate (1.0 is default; <1.0 slows down, >1.0 speeds up).

## Status Codes

- **200**: Successful retrieval
- **422**: Validation error

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Code Examples

Available implementations in: TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
