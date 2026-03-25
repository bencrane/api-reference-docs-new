# Update MCP Server Configuration

## Endpoint Overview

The PATCH endpoint at `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}` enables modifications to MCP server settings.

## Key Parameters

**Path Parameter:**
- `mcp_server_id` (required, string): Identifier for the MCP Server

**Header:**
- `xi-api-key` (optional, string): Authentication header

## Configurable Settings

The request body supports the following optional properties:

- **approval_policy**: Server-level approval mode (`auto_approve_all`, `require_approval_all`, `require_approval_per_tool`)
- **force_pre_tool_speech**: Boolean override for pre-tool execution speech
- **disable_interruptions**: Boolean to prevent user interruption during tool execution
- **tool_call_sound**: Sound type played during execution (`typing`, `elevator1-4`)
- **tool_call_sound_behavior**: When sound plays (`auto`, `always`)
- **execution_mode**: Tool execution timing (`immediate`, `post_tool_speech`, `async`)
- **request_headers**: Custom headers supporting strings, secrets, dynamic variables, or environment variables
- **disable_compression**: Boolean to disable HTTP compression
- **secret_token**: Authentication secret reference
- **auth_connection**: Authentication connection reference

## Response

A successful 200 response returns an `McpServerResponseModel` containing:
- Server configuration details
- Access information and role
- Dependent agents list
- Server metadata (creation timestamp, owner)

Validation errors (422) are returned with detailed error information.
