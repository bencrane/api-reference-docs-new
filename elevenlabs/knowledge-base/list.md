# List Knowledge Base Documents

## Endpoint Overview

The GET `https://api.elevenlabs.io/v1/convai/knowledge-base` endpoint retrieves "a list of available knowledge base documents."

## Key Parameters

The endpoint accepts the following query parameters:

- **page_size**: Maximum documents to return (max 100, defaults to 30)
- **search**: Filter documents by name prefix
- **show_only_owned_documents**: Returns only your documents (deprecated)
- **created_by_user_id**: Filter by creator ID; use '@me' for current user
- **types**: Restrict to specific document types (file, url, text, folder)
- **parent_folder_id**: Get direct children of a folder
- **ancestor_folder_id**: Get all descendants of a folder
- **folders_first**: Return folders before other documents
- **sort_direction**: Sort ascending or descending
- **sort_by**: Sort by name, created_at, updated_at, or size
- **cursor**: Pagination cursor for subsequent requests

## Response Structure

The successful 200 response contains:

- **documents**: Array of knowledge base items with discriminated types
- **next_cursor**: Pagination cursor for fetching additional results
- **has_more**: Boolean indicating whether more documents exist

## Document Types

Returned documents can be:
- **file**: Uploaded files with metadata and usage modes
- **folder**: Containers with children count and auto-sync information
- **text**: Text content documents
- **url**: Web resources with associated URLs

Each document includes metadata (creation date, update date, size), access information, folder hierarchy, and deprecated dependent agent references.
