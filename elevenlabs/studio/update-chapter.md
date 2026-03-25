# Update Chapter API Documentation

## Endpoint Overview

The Update Chapter endpoint allows modifications to existing chapters in ElevenLabs Studio projects via a POST request to `https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}`.

## Request Parameters

**Path Parameters:**
- `project_id` (required): Project identifier, obtainable from the List projects endpoint
- `chapter_id` (required): Chapter identifier, obtainable from the List project chapters endpoint

**Header:**
- `xi-api-key` (optional): API authentication key

**Request Body:**
The endpoint accepts JSON with two optional fields:
- `name`: String identifying the chapter
- `content`: Chapter content structure containing blocks with TTS nodes

## Response Schema

On successful completion (HTTP 200), the API returns an `EditChapterResponseModel` containing a chapter object with:

- Chapter metadata (ID, name, state)
- Conversion status information
- Content structure with blocks and TTS nodes
- Statistics including character and paragraph counts by voice
- Visual content indicators
- Download availability status

## Error Handling

Validation errors (HTTP 422) return detailed error information including location, message, and error type.

## SDK Examples

Official implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating basic usage patterns with the two required path parameters.
