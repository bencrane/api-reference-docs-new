# Get Source File URL

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/source-file-url`

## Purpose

This endpoint retrieves a signed URL for downloading the original source file of a document stored in the knowledge base.

## Parameters

- **documentation_id** (path, required): The document identifier returned when the document was added to the knowledge base
- **xi-api-key** (header, optional): API authentication key

## Response

Success returns a JSON object containing:
- **signed_url** (string): A downloadable link for the source file

## Error Handling

A 422 response indicates validation errors in the request parameters.

## Implementation Examples

The documentation provides code samples in multiple languages:
- **TypeScript/JavaScript**: Using the official ElevenLabs SDK
- **Python**: Native client library integration
- **Go, Ruby, Java, PHP, C#, Swift**: HTTP request implementations using language-specific libraries

Each example demonstrates making a GET request to retrieve the signed URL for a specific document by its ID.
