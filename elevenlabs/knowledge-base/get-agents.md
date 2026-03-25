# Get Dependent Agents

## Overview

This API endpoint retrieves a list of agents that depend on a specific knowledge base document.

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/dependent-agents`

## Parameters

| Name | Location | Type | Required | Description |
|------|----------|------|----------|-------------|
| `documentation_id` | Path | String | Yes | The document ID from the knowledge base |
| `dependent_type` | Query | String | No | Filter by dependency type: `direct`, `transitive`, or `all` |
| `page_size` | Query | Integer | No | Maximum results (default: 30, max: 100) |
| `cursor` | Query | String | No | Pagination cursor for next page |
| `xi-api-key` | Header | String | No | API authentication key |

## Response

The API returns a JSON object containing:

- **agents**: Array of dependent agents (either `available` or `unknown` type)
- **branches**: Array of branch information for agents
- **next_cursor**: Cursor for pagination
- **has_more**: Boolean indicating if more results exist

Available agents include: `id`, `name`, `created_at_unix_secs`, `access_level`, and optionally `referenced_resource_ids` for transitive dependencies.

## Status Codes

- **200**: Successful response
- **422**: Validation error

## SDK Examples

Implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all following the same parameter structure.
