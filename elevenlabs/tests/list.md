# List Tests API Documentation

## Overview
This endpoint retrieves agent response tests from the ElevenLabs API with pagination and filtering capabilities.

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/agent-testing`

## Key Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cursor` | string | Pagination token for fetching subsequent pages |
| `page_size` | integer | Maximum results per request (default: 30, max: 100) |
| `search` | string | Filter tests by name |
| `parent_folder_id` | string | Restrict results to specific folder; use 'root' for root folder |
| `types` | string | Filter by test type (llm, tool, simulation, folder) |
| `sort_mode` | string | Ordering method ('default' or 'folders_first') |

## Supported Test Types
The endpoint supports filtering by four test types: "llm", "tool", "simulation", and "folder".

## Response Structure
The successful response returns a `GetTestsPageResponseModel` containing:
- Array of test objects with metadata (ID, name, timestamps, type, access info)
- Pagination cursor for next page
- Boolean flag indicating additional results exist

## API Server Locations
Four regional endpoints are available: standard US, dedicated US residency, EU residency, and India residency servers.
