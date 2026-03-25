# Update MCP Server Approval Policy

## Endpoint Overview

This API endpoint allows you to modify the approval policy configuration for an MCP (Model Context Protocol) server via a PATCH request to `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/approval-policy`.

**Note:** This endpoint is deprecated. The documentation recommends using `PATCH /mcp-servers/{id}` instead for new implementations.

## Request Details

**HTTP Method:** PATCH
**Content-Type:** application/json

### Path Parameter
- `mcp_server_id` (required): The unique identifier of the MCP Server to update

### Optional Header
- `xi-api-key`: API key for authentication

### Request Body
The request requires a JSON object with:
- `approval_policy` (required): One of three options -- `auto_approve_all`, `require_approval_all`, or `require_approval_per_tool`

## Response

**Success (200):** Returns an `McpServerResponseModel` containing the updated server configuration, including its ID, settings, access information, dependent agents, and metadata.

**Validation Error (422):** Returns validation error details if the request is malformed.

## Approval Policy Options

- **auto_approve_all**: Automatically approves all tool executions
- **require_approval_all**: Requires approval for all tools
- **require_approval_per_tool**: Applies approval on a per-tool basis

## Available Servers

The API supports multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Code Examples

The documentation includes implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to construct and send the PATCH request with the appropriate approval policy value.
