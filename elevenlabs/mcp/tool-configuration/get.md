# Get Configuration Override

**GET** `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}`

This endpoint retrieves configuration overrides for a specific MCP tool.

## Parameters

| Parameter | Location | Required | Type | Description |
|-----------|----------|----------|------|-------------|
| mcp_server_id | path | Yes | string | ID of the MCP Server |
| tool_name | path | Yes | string | Name of the MCP tool to retrieve config overrides for |
| xi-api-key | header | No | string | API authentication key |

## Response Codes

- **200**: Successful response containing `McpToolConfigOverride` object
- **404**: Tool config override not found
- **422**: Validation error

## Response Schema

The successful response returns a `McpToolConfigOverride` object with:

- `tool_name` (string, required): The name of the MCP tool
- `force_pre_tool_speech` (boolean, optional): Overrides server setting for this tool
- `disable_interruptions` (boolean, optional): Overrides server setting for this tool
- `tool_call_sound` (enum, optional): Predefined sound types (typing, elevator1-4)
- `tool_call_sound_behavior` (enum, optional): Sound playback behavior (auto/always)
- `execution_mode` (enum, optional): Execution timing (immediate/post_tool_speech/async)
- `assignments` (array, optional): Dynamic variable assignment configurations
- `input_overrides` (object, optional): Input parameter overrides with constant, dynamic variable, or LLM sources

## SDK Examples

**TypeScript:**
```typescript
const client = new ElevenLabsClient();
await client.conversationalAi.mcpServers.toolConfigs.get("mcp_server_id", "tool_name");
```

**Python:**
```python
client = ElevenLabs()
client.conversational_ai.mcp_servers.tool_configs.get(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name",
)
```

Additional examples provided for Go, Ruby, Java, PHP, C#, and Swift.
