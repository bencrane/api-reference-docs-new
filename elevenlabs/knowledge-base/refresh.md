# Refresh Knowledge Base Document

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/refresh`

This API operation allows developers to "manually refresh a URL document by re-fetching its content from the source URL."

## Key Parameters

- **documentation_id** (path, required): The document identifier returned upon initial addition to the knowledge base
- **xi-api-key** (header, optional): Authentication credential

## Response Structure

The endpoint returns a `DocumentRefreshResponse` with a discriminated union supporting four document types:

1. **URL documents** - Include `url` and `extracted_inner_html` fields, plus `auto_sync_info`
2. **File documents** - Contain `filename` and `extracted_inner_html`
3. **Text documents** - Include `extracted_inner_html`
4. **Folder documents** - Feature `children_count` and `auto_sync_info`

All response types include metadata (creation/update timestamps, size), access information, supported usage modes, and folder path information.

## Status Codes

- **200**: Successful refresh operation
- **422**: Validation error

## Implementation Examples

SDK implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with a shared pattern of making a POST request to the endpoint with the document ID.
