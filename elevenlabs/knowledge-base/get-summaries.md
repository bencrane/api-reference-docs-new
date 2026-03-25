# Get Knowledge Base Summaries

## Overview
This endpoint retrieves multiple knowledge base document summaries using their IDs through a GET request to `https://api.elevenlabs.io/v1/convai/knowledge-base/summaries`.

## Request Parameters
The API accepts one optional query parameter:
- **document_ids** (string): "The ids of knowledge base documents."

An optional header parameter is also available:
- **xi-api-key** (string): Authentication key for the request

## Response Structure
Success responses (HTTP 200) return an object with document summaries mapped by their IDs. Each summary can represent one of four document types:

**File Type** - Contains metadata, supported usage modes, access information, folder hierarchy, and dependent agents list.

**Folder Type** - Includes children count and auto-sync information alongside standard metadata fields.

**Text Type** - Text-based knowledge documents with standard summary fields.

**URL Type** - Web-sourced documents with URL field included.

All response types share common fields: id, name, metadata (creation/update timestamps, file size), supported_usages, access_info, folder_parent_id, folder_path, and dependent_agents.

## Error Handling
Validation errors (HTTP 422) provide detailed error information including location, message, and error type. Individual document requests can also fail within batch responses, returning error_code, error_status, and error_message fields.

## Available SDKs
The endpoint supports implementation across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift with respective client libraries.
