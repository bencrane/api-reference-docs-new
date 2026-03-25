# List MCP Servers API Documentation

## Overview
The **List MCP Servers** endpoint retrieves all MCP server configurations available in a workspace via a GET request to `https://api.elevenlabs.io/v1/convai/mcp-servers`.

## Key Details

**Endpoint:** `GET /v1/convai/mcp-servers`

**Authentication:** Optional `xi-api-key` header parameter

**Response:** Returns a `McpServersResponseModel` containing an array of MCP server configurations, each with:
- Server ID and configuration details
- Access information (creator, role, permissions)
- Dependent agents that reference the server
- Metadata (creation timestamp, owner user ID)

## Response Structure

Each MCP server object includes:
- **Configuration:** URL, transport type (SSE or STREAMABLE_HTTP), approval policies, authentication details
- **Tool Settings:** Execution mode (immediate, post_tool_speech, or async), sound effects, interruption controls
- **Tool Overrides:** Per-tool customizations for sound, execution behavior, and input parameters
- **Access Control:** Creator information and role-based permissions

## Available Servers

Multiple API endpoints support this operation across regional servers:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Implementation Examples

SDK examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating straightforward list retrieval syntax across languages.
