# Get Dependent Agents

## Endpoint Overview

This API retrieves agents that depend on a specific tool via a GET request to `https://api.elevenlabs.io/v1/convai/tools/{tool_id}/dependent-agents`.

## Key Parameters

The endpoint accepts three main parameters:

- **tool_id** (path, required): Identifies which tool to query
- **cursor** (query, optional): Enables pagination for result sets
- **page_size** (query, optional): Controls result count, maximum 100, defaults to 30

An optional `xi-api-key` header supports authentication.

## Response Structure

Successful responses (200) return a `GetToolDependentAgentsResponseModel` containing:

- **agents**: Array of dependent agent objects, which may be "available" (with id, name, creation timestamp, access level) or "unknown" types
- **branches**: Array of branch information objects including agent/branch identifiers and main branch status
- **next_cursor**: Pagination token for subsequent requests
- **has_more**: Boolean indicating additional results exist

## Error Handling

Validation errors (422) return detailed error information including location, message, and error type.

## Available SDK Examples

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift formats, demonstrating how to construct and execute the request across different development environments.
