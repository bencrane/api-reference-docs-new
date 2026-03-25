# Get PVC Voice Sample Waveform

## Endpoint Overview

The API provides a GET endpoint to retrieve the visual waveform representation of a voice sample:

**`GET https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}/waveform`**

This endpoint retrieves the visual waveform of a voice sample.

## Parameters

The request requires two path parameters:

- **voice_id**: The voice identifier (can be listed via the voices endpoint)
- **sample_id**: The specific sample identifier

An optional header parameter `xi-api-key` may be included for authentication.

## Response Structure

A successful 200 response returns a JSON object containing:

- **sample_id** (string): The identifier of the sample
- **visual_waveform** (array of numbers): The visual waveform of the sample, represented as a list of floats

## Error Handling

A 422 response indicates validation errors with details about malformed requests.

## Available Server Endpoints

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to integrate this endpoint across various development environments.
