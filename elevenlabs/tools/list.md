# List Tools API Documentation

## Endpoint Overview

The **List Tools** endpoint retrieves all available tools within a workspace using a GET request to `https://api.elevenlabs.io/v1/convai/tools`.

## Key Parameters

The API accepts several optional query parameters:

- **search**: Filters tools by name prefix
- **page_size**: Controls result count (max 100, default 30)
- **show_only_owned_documents**: Returns only user-created tools (deprecated)
- **created_by_user_id**: Filters by creator; use '@me' for current user
- **types**: Narrows results to specific tool categories (webhook, client, api_integration_webhook)
- **sort_direction**: Orders results ascending or descending
- **sort_by**: Sorts by name or creation date
- **cursor**: Enables pagination through result sets

## Response Structure

Successful requests return a `ToolsResponseModel` containing:

- **tools**: Array of tool objects with configuration and metadata
- **next_cursor**: Pagination token for subsequent requests
- **has_more**: Boolean indicating additional results exist

## Tool Configuration Types

The endpoint supports multiple tool types:

1. **Client tools**: Execute on client-side with customizable parameters
2. **Webhook tools**: Send HTTP requests with schema-defined payloads
3. **System tools**: Built-in functions (transfers, voicemail detection, call ending)
4. **MCP tools**: Model Context Protocol integrations

Each tool includes execution modes (immediate, post_tool_speech, async), error handling strategies, and optional dynamic variable assignments.

## Error Handling

Validation errors return HTTP 422 with detailed error information. The `response_timeout_secs` parameter (default 20 seconds) governs maximum execution duration.
