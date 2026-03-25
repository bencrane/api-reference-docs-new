# Delete Knowledge Base Document

## Endpoint Overview

The ElevenLabs API provides a DELETE endpoint at `https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}` for removing documents or folders from a knowledge base.

## Key Parameters

**Path Parameter:**
- `documentation_id` (required): The identifier for the document to remove, provided upon document creation

**Query Parameters:**
- `force` (optional, boolean): When set to true, enables deletion "regardless of whether it is used by any agents" and removes the item from dependent agents. For non-empty folders, this cascades to child items.

**Header:**
- `xi-api-key` (optional): Authentication credential

## Response

A successful deletion returns a 200 status code with a JSON response. Validation errors return a 422 status with detailed error information.

## Implementation Examples

The documentation provides code samples across multiple languages:
- **TypeScript/JavaScript**: Uses the ElevenLabs SDK with async/await syntax
- **Python**: Leverages the official ElevenLabs client library
- **Go, Ruby, Java, PHP, C#, Swift**: Native HTTP implementations showing URL construction with query parameters

All examples demonstrate deletion of the same sample document ID with the `force` parameter enabled.
