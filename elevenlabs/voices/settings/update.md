# Edit Voice Settings

## Overview
The ElevenLabs API provides an endpoint to modify voice settings for text-to-speech synthesis. The "similarity_boost" corresponds to "Clarity + Similarity Enhancement" in the web app, while "stability" maps to the "Stability" slider.

## Endpoint Details
**POST** `https://api.elevenlabs.io/v1/voices/{voice_id}/settings/edit`

## Path Parameters

- **voice_id** (required, string): The voice identifier. Available voices can be listed via the voices endpoint.

## Optional Headers

- **xi-api-key**: API authentication key

## Request Body

The request body accepts a `VoiceSettings` object with the following properties:

- **stability** (number): Controls vocal consistency and emotional range. Lower values create broader emotional variation; higher values produce monotonous delivery.
- **use_speaker_boost** (boolean): Enhances similarity to the original speaker, though it increases computational load and latency.
- **similarity_boost** (number): Determines how closely the AI adheres to the original voice during replication.
- **style** (number): Controls stylistic exaggeration of the voice, amplifying speaker characteristics at the cost of additional computational resources.
- **speed** (number): Adjusts playback velocity, where 1.0 represents default speed, values below 1.0 slow the speech, and values above 1.0 accelerate it.

## Response

A successful request returns status 200 with an `EditVoiceSettingsResponseModel` containing a status field. The status will be "ok" for successful requests; errors return status 500.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Code Examples

Examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating how to update voice settings with consistent parameter values.
