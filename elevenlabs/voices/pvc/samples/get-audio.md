# Get PVC Voice Sample Audio

## Overview

This API endpoint retrieves the initial 30 seconds of voice sample audio, with optional noise removal capabilities.

**Endpoint:** `GET https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/audio`

## Parameters

| Parameter | Location | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| voice_id | path | string | Yes | Voice identifier; list available voices at `/v1/voices` |
| sample_id | path | string | Yes | Sample identifier |
| remove_background_noise | query | boolean | No | Applies audio isolation model (default: false) |
| xi-api-key | header | string | No | API authentication key |

## Response Format

A successful 200 response contains:

- **audio_base_64** (string): Base64-encoded audio data
- **voice_id** (string): The voice identifier
- **sample_id** (string): The sample identifier
- **media_type** (string): Audio format type
- **duration_secs** (number, optional): Audio length in seconds

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Examples

Code implementations are available in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for integrating this functionality into applications.
