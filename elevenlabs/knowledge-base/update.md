# Update Knowledge Base Document

## Endpoint Overview

This API endpoint allows you to modify the name of a document within the ElevenLabs knowledge base system. It uses the PATCH HTTP method at the path `/v1/convai/knowledge-base/{documentation_id}`.

## Key Details

**Method:** PATCH
**Base URL:** https://api.elevenlabs.io
**Content-Type:** application/json

## Required Parameters

- **documentation_id** (path parameter): "The id of a document from the knowledge base. This is returned on document addition."
- **name** (request body): A custom, human-readable name for the document (required)

## Response

A successful request (200 status) returns a `DocumentsUpdateResponse` object. This response is discriminated by the `type` field and can represent one of four document types:

- **url**: URL-based documents with fields for sync information
- **file**: Uploaded file documents with filename
- **text**: Text-based documents
- **folder**: Folder entities with children count

All response types include core fields like id, name, metadata, supported_usages, access_info, and folder information.

## Error Handling

A 422 response indicates validation errors with details about what failed in the request.

## SDK Examples

The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating how to update a document's name using the respective client libraries or HTTP methods.
