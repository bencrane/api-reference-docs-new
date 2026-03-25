# Delete PVC Voice Sample

## Overview

The ElevenLabs API provides an endpoint to remove audio samples from Personal Voice Clone (PVC) voices using a DELETE request to `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}`.

## API Endpoint Details

**HTTP Method:** DELETE

**Base URLs:**
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Required Parameters

Two path parameters are required:

1. **voice_id** - The identifier for the PVC voice (obtainable via the voices list endpoint)
2. **sample_id** - The identifier for the specific audio sample to delete

An optional header parameter `xi-api-key` can be included for authentication.

## Response Schema

A successful deletion returns HTTP 200 with a response containing a "status" field that indicates "ok" when the deletion succeeds, or an error message with status 500 upon failure.

Validation errors trigger HTTP 422 responses with detailed error information.

## Code Examples

The documentation includes implementation examples across multiple programming languages: TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same deletion operation with example voice and sample IDs.
