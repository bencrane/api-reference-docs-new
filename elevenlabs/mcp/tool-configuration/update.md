# Update Configuration Override

## Endpoint
**PATCH** `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}`

## Purpose
This endpoint allows you to "update configuration overrides for a specific MCP tool."

## Path Parameters
- **mcp_server_id**: ID of the MCP Server (required, string)
- **tool_name**: Name of the MCP tool to update (required, string)

## Optional Header
- **xi-api-key**: API authentication key

## Request Body
The PATCH request accepts a JSON object with these optional fields:

- `force_pre_tool_speech` (boolean): Overrides server setting for this tool
- `disable_interruptions` (boolean): Overrides server interruption setting
- `tool_call_sound` (enum): Sound type during execution (typing, elevator1-4)
- `tool_call_sound_behavior` (enum): When sound plays (auto, always)
- `execution_mode` (enum): Execution timing (immediate, post_tool_speech, async)
- `assignments` (array): Dynamic variable assignments from tool responses
- `input_overrides` (object): Maps JSON paths to input override configurations

## Responses
- **200**: Successful update returns McpServerResponseModel
- **404**: Tool config override not found
- **422**: Validation error in request

## Code Examples

**TypeScript:**
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.toolConfigs.update(
        "mcp_server_id",
        "tool_name",
        {}
    );
}
```

**Python:**
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.conversational_ai.mcp_servers.tool_configs.update(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name",
)
```
