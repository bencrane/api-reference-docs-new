# Delete Chapter API Documentation

## Endpoint Overview

The Delete Chapter endpoint removes a chapter from an ElevenLabs Studio project using a DELETE request to `https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}`.

## Required Parameters

Two path parameters are needed:

1. **project_id** - The Studio project identifier (obtainable via the List projects endpoint)
2. **chapter_id** - The chapter identifier (obtainable via the List project chapters endpoint)

An optional header parameter `xi-api-key` can be included for authentication.

## Response Format

A successful deletion (HTTP 200) returns a JSON object with a status field. The documentation indicates that "the status of the studio chapter deletion request" will be `'ok'` when successful, or an error message with status 500 otherwise.

## Implementation Examples

The documentation provides code samples across multiple languages:

- **TypeScript/JavaScript** using the ElevenLabs SDK
- **Python** with the ElevenLabs client library
- **Go** with native HTTP requests
- **Ruby**, **Java**, **PHP**, **C#**, and **Swift** implementations

All examples demonstrate the same operation: deleting a chapter with IDs "21m00Tcm4TlvDq8ikWAM" for both project and chapter.

## Error Handling

A 422 response indicates validation errors, returning HTTPValidationError details including location, message, and error type information.
