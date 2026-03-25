# Move Document API Reference

## Endpoint Overview

The Move Document endpoint enables relocation of knowledge base documents to different folders via a POST request to `https://api.elevenlabs.io/v1/convai/knowledge-base/{document_id}/move`.

## Key Parameters

**Path Parameter:**
- `document_id` (required, string): The identifier of the document to relocate, provided upon document creation

**Request Body:**
- `move_to` (optional, string): Target folder identifier. Omitting this parameter moves the document to the root folder

**Header:**
- `xi-api-key` (optional): Authentication credential

## Response Codes

- **200**: Operation completed successfully
- **422**: Request validation failed

## Implementation Examples

The documentation provides code samples across multiple programming languages:

- **TypeScript/JavaScript**: Uses the ElevenLabs SDK with `client.conversationalAi.knowledgeBase.documents.move()`
- **Python**: Implements via the ElevenLabs client library
- **Go, Ruby, Java, PHP, C#, Swift**: Raw HTTP implementations demonstrating the REST interface

## Server Options

Three regional API endpoints are available: US-based, EU-based, and India-based residency options.
