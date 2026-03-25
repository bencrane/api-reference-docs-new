# Create MCP Server Tool Approval

## Overview
This API endpoint allows you to add approval for a specific MCP tool when using per-tool approval mode.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-approvals`

## Request Parameters

### Path Parameters
- **mcp_server_id** (required): ID of the MCP Server

### Headers
- **xi-api-key** (optional): Authentication key

### Request Body
The endpoint accepts a JSON payload with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| tool_name | string | Yes | Name of the MCP tool |
| tool_description | string | Yes | Description of the MCP tool |
| input_schema | object | No | Input schema of the tool as defined on the MCP server |
| approval_policy | string | No | Tool-level approval policy: `auto_approved` or `requires_approval` |

## Response

**Status:** 200 (Successful Response)

Returns a `McpServerResponseModel` containing:
- Server ID
- Complete configuration
- Access information
- Dependent agents list
- Metadata (creation timestamp, owner)

## Available Servers
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Code Examples
The documentation provides implementations in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for integrating this endpoint.
