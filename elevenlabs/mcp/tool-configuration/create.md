# Create Configuration Override

## Endpoint Details

**POST** `https://api.elevenlabs.io/v1/convai/mcp-servers/{mcp_server_id}/tool-configs`

This endpoint enables developers to establish configuration overrides for specific MCP tools within an existing server setup.

## Request Parameters

The request requires a path parameter:
- **mcp_server_id** (required): The identifier of the MCP Server

An optional header is available:
- **xi-api-key**: Authentication header

## Request Body

The request body must include:
- **tool_name** (required, string): The name of the MCP tool being configured

Optional configuration fields include:

- **force_pre_tool_speech** (boolean): Overrides server-level speech requirement
- **disable_interruptions** (boolean): Prevents user interruption during execution
- **tool_call_sound**: Predefined audio (typing, elevator1-4)
- **tool_call_sound_behavior**: "auto" or "always" playback modes
- **execution_mode**: "immediate," "post_tool_speech," or "async"
- **assignments**: Dynamic variable extraction from tool responses
- **input_overrides**: Maps JSON paths to constant, dynamic variable, or LLM-based values

## Response Codes

- **200**: Successfully created configuration override
- **409**: Tool config override already exists
- **422**: Validation error in request

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to invoke this endpoint with minimal required parameters.
