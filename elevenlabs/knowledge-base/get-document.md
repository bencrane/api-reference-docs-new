# Get Knowledge Base Document

## Endpoint Overview

This API endpoint retrieves details about a specific documentation entry within an agent's knowledge base using a GET request to `https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}`.

## Parameters

The request accepts three parameters:

- **documentation_id** (path, required): "The id of a document from the knowledge base. This is returned on document addition."
- **agent_id** (query, optional): String parameter with default empty value
- **xi-api-key** (header, optional): API authentication key

## Response Format

The endpoint returns a 200 success response containing a discriminated union of four possible document types:

1. **URL documents** - Include properties like `url`, `extracted_inner_html`, and `auto_sync_info` for automatic refresh configuration
2. **File documents** - Contain `filename` and `extracted_inner_html` fields
3. **Text documents** - Feature `extracted_inner_html` content
4. **Folder documents** - Include `children_count` and `auto_sync_info` properties

All response types share common fields including `id`, `name`, `metadata`, `supported_usages`, `access_info`, `folder_parent_id`, and `folder_path`.

## Code Examples

SDK implementations are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The examples demonstrate passing the documentation ID and optional agent ID parameters to retrieve document details.
