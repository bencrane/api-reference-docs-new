# Get Tool

## Overview

The **Get Tool** endpoint retrieves a specific tool available in your workspace using its unique identifier.

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/tools/{tool_id}`

## Parameters

| Name | Location | Type | Required | Description |
|------|----------|------|----------|-------------|
| `tool_id` | Path | String | Yes | The identifier of the requested tool |
| `xi-api-key` | Header | String | No | API authentication key |

## Response

A successful request returns a `200` status with a `ToolResponseModel` containing:

- **id**: Tool identifier
- **tool_config**: Configuration details for the tool (can be of type: `client`, `mcp`, `system`, or `webhook`)
- **access_info**: Information about resource access and user permissions
- **usage_stats**: Statistics including total calls and average latency

## Tool Configuration Types

The tool configuration supports multiple variants:

1. **Client Tools**: Custom tools requiring client-side execution with parameters schema
2. **System Tools**: Built-in tools like call transfers, voicemail detection, or keypad tone playback
3. **Webhook Tools**: External API integrations with customizable request schemas
4. **MCP Tools**: Model Context Protocol implementations

## Common Configuration Options

Most tool types support:

- `response_timeout_secs`: Maximum wait time (1-120 seconds)
- `disable_interruptions`: Prevent user interruption during execution
- `force_pre_tool_speech`: Require agent speech before tool invocation
- `tool_call_sound`: Audio feedback during execution
- `execution_mode`: Control timing (`immediate`, `post_tool_speech`, or `async`)
- `assignments`: Extract and map response values to dynamic variables

## Usage Examples

**TypeScript:**
```typescript
const tool = await client.conversationalAi.tools.get("tool_id");
```

**Python:**
```python
tool = client.conversational_ai.tools.get(tool_id="tool_id")
```

**cURL:**
```bash
curl -X GET "https://api.elevenlabs.io/v1/convai/tools/tool_id"
```
