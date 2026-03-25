# Delete Voice API Documentation

## Overview
The Delete Voice endpoint allows you to remove a voice from the ElevenLabs API by providing its ID. This is a DELETE request to the `/v1/voices/{voice_id}` endpoint.

## Endpoint Details

**HTTP Method:** DELETE
**URL:** `https://api.elevenlabs.io/v1/voices/{voice_id}`

## Parameters

- **voice_id** (required, path): The identifier for the voice you wish to delete. Reference the Get Voices endpoint to retrieve available voice IDs.
- **xi-api-key** (optional, header): Authentication key for the request

## Response

A successful deletion (HTTP 200) returns a response containing a `status` field that confirms the operation completed. The status value will be "ok" if successful, otherwise a 500 error is returned.

## Error Handling

Validation errors return HTTP 422 responses with detailed error information including location, message, and error type.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Implementation Examples

The documentation provides code samples across multiple programming languages including TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
