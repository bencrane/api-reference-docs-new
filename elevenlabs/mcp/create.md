# Create MCP Server

This endpoint allows you to establish a new MCP server configuration within your workspace.

## Endpoint Details

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/convai/mcp-servers`
**Content-Type:** application/json

## Required Parameters

The request body must include a `config` object with these mandatory fields:

- **url** (string): "The URL of the MCP server, if this contains a secret please store as a workspace secret, otherwise store as a plain string. Must use https"
- **name** (string): The identifier for your MCP server configuration

## Optional Configuration Parameters

You can customize server behavior with:

- **description** (string): Additional context about the server
- **approval_policy**: Control tool execution permissions (auto_approve_all, require_approval_all, or require_approval_per_tool)
- **transport**: Specify SSE or STREAMABLE_HTTP
- **secret_token**: Authorization credentials for the MCP server
- **request_headers**: Custom headers for requests
- **auth_connection**: Reference to workspace authentication settings
- **force_pre_tool_speech** (boolean): Require spoken confirmation before tool execution
- **disable_interruptions** (boolean): Prevent user interruption during tool execution
- **tool_call_sound**: Audio feedback during tool execution (typing, elevator1-4)
- **execution_mode**: Control execution timing (immediate, post_tool_speech, async)
- **tool_config_overrides**: Per-tool customization settings
- **disable_compression** (boolean): Disable HTTP compression if unsupported by your server

## Response

The API returns a `McpServerResponseModel` containing:

- **id**: Unique server identifier
- **config**: Your submitted configuration
- **access_info**: Permission details for the MCP server
- **dependent_agents**: Agents utilizing this server
- **metadata**: Creation timestamp and owner information

## SDK Examples

SDK implementations are available in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for integration into your applications.
