# Create Tool API Endpoint

## Overview
The Create Tool endpoint allows you to add new tools to your workspace for use with conversational AI agents. This POST endpoint is located at `https://api.elevenlabs.io/v1/convai/tools`.

## Request Structure
The request requires a `tool_config` object that defines the tool's behavior and properties. The API accepts `application/json` content type and supports an optional `xi-api-key` header parameter.

## Tool Types
The API supports four distinct tool type configurations:

**Client Tools**: Custom tools that communicate with external systems, accepting parameters schema and supporting dynamic variable assignments.

**System Tools**: Built-in tools including call termination, language detection, keypad tone playing, agent transfers, and voicemail detection capabilities.

**Webhook Tools**: Integration tools that send HTTP requests to external APIs with configurable schemas for request headers, body, query parameters, and authentication.

**MCP Tools**: Model Context Protocol tools that accept flexible value configurations.

## Common Configuration Options
All tool types share several standard properties:
- `name` (required): The tool identifier
- `description`: Explains when and how the tool should be used
- `response_timeout_secs`: Maximum wait time (defaults to 20 seconds)
- `disable_interruptions`: Prevents user interruption during execution
- `force_pre_tool_speech`: Enables agent speech before tool invocation
- `tool_call_sound`: Optional audio feedback during execution
- `tool_error_handling_mode`: Controls error message processing

## Response
Successful requests return a `ToolResponseModel` containing the tool's unique ID, complete configuration, access information, and usage statistics including total calls and average latency.
