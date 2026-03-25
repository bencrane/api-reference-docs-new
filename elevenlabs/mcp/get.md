# Get MCP Server

## Endpoint Overview

This API endpoint retrieves a specific MCP server configuration from your workspace using a GET request to `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}`.

## Request Parameters

The endpoint requires:
- **mcp_server_id** (path parameter, required): The identifier for the MCP Server
- **xi-api-key** (header parameter, optional): Authentication key

## Response Structure

A successful 200 response returns an `McpServerResponseModel` containing:

- **id**: Server identifier
- **config**: MCP server configuration details including URL, transport type, approval policies, and tool settings
- **access_info**: Resource access information showing creator details and user role
- **dependent_agents**: "List of agents that depend on this MCP Server"
- **metadata**: Creation timestamp and owner information

## Configuration Details

The server configuration includes:
- Transport protocol (SSE or STREAMABLE_HTTP)
- Authentication settings (secret tokens, auth connections, headers)
- Tool execution settings (immediate, post_tool_speech, or async modes)
- Sound effects for tool calls (typing, elevator variants)
- Per-tool overrides for specific MCP tools
- Approval policies (auto_approve_all, require_approval_all, or require_approval_per_tool)

## Error Handling

A 422 response indicates a validation error with detailed error information.

## Available Code Examples

SDK implementations are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
