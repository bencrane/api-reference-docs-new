# Delete MCP Server

## Endpoint Overview

The DELETE endpoint at `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}` allows users to "Delete a specific MCP server configuration from the workspace."

## Key Parameters

The API requires:
- **mcp_server_id** (path parameter): The identifier for the MCP Server being removed
- **xi-api-key** (header, optional): Authentication credential

## Response Codes

- **200**: Successful deletion returning JSON content
- **422**: Validation error with detailed error information

## Implementation Examples

The documentation provides code samples across multiple languages including TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates how to construct and execute the DELETE request to remove an MCP server configuration.

The TypeScript SDK example shows the simplest implementation: `client.conversationalAi.mcpServers.delete("mcp_server_id")`, while lower-level language examples demonstrate manual HTTP request construction to the API endpoint.
