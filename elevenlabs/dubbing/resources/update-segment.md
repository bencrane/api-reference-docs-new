# Update a Segment

## Endpoint Overview

The ElevenLabs dubbing API provides a PATCH endpoint for modifying individual segments within a dubbing project. According to the documentation, this operation "Modifies a single segment with new text and/or start/end times."

**URL:** `PATCH https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}`

## Key Parameters

The endpoint requires three path parameters:
- **dubbing_id**: Identifier for the dubbing project
- **segment_id**: Identifier for the specific segment being modified
- **language**: Language identifier for the segment

An optional `xi-api-key` header parameter can be included for authentication.

## Request Body

The request accepts a JSON object with optional properties:
- `start_time` (number): Beginning timestamp for the segment
- `end_time` (number): Ending timestamp for the segment
- `text` (string): The segment's textual content

All three fields are optional, allowing partial updates.

## Response

A successful request returns a 200 status with a JSON response containing a `version` field (integer). Validation errors return a 422 status with detailed error information.

## Implementation Notes

The operation "Does not automatically regenerate the dub," meaning audio regeneration requires a separate action. Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift formats.
