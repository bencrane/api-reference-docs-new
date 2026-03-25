# Delete Configuration Override

## Endpoint Details

The DELETE endpoint at `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}` enables removal of configuration overrides for a specific MCP tool.

## Path Parameters

- **mcp_server_id** (required, string): Identifier for the MCP Server
- **tool_name** (required, string): Name of the MCP tool for which to remove config overrides

## Optional Headers

- **xi-api-key**: API authentication key (optional)

## Response

A successful 200 response returns an `McpServerResponseModel` containing:
- Server ID and configuration details
- Access information for the requesting user
- List of dependent agents using this server
- Metadata including creation timestamp and owner information

Validation errors (422) return details about any malformed requests.

## Implementation Examples

Code samples are available in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript example demonstrates basic usage:

```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.mcpServers.toolConfigs.delete(
  "mcp_server_id",
  "tool_name"
);
```

The operation removes tool-specific overrides while preserving server-level settings for that tool.
