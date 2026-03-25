# Delete MCP Server Tool Approval

## Overview

This API endpoint removes approval for a specific MCP tool when operating in per-tool approval mode.

**Endpoint:** `DELETE https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}`

## Parameters

The request requires two path parameters:

- **mcp_server_id** (string, required): The identifier of the MCP Server
- **tool_name** (string, required): The name of the MCP tool to remove approval for

An optional header parameter is available:
- **xi-api-key** (string, optional): API authentication key

## Response

A successful request returns a 200 status with an `McpServerResponseModel` containing the updated MCP server configuration.

Validation errors return a 422 status with detailed error information.

## Implementation Examples

The documentation provides code samples across multiple languages:

- **TypeScript/JavaScript:** Uses the ElevenLabs SDK with `client.conversationalAi.mcpServers.toolApprovals.delete()`
- **Python:** Implements deletion through `client.conversational_ai.mcp_servers.tool_approvals.delete()`
- **Go, Ruby, Java, PHP, C#, Swift:** HTTP DELETE implementations with standard libraries

All examples target the standard HTTPS endpoint at `api.elevenlabs.io`.
