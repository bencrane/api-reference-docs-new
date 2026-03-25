# Update Tool - ElevenLabs API Documentation

## Endpoint Overview

The Update Tool endpoint allows modifications to tools available within a workspace using a PATCH request.

**Endpoint:** `PATCH https://api.elevenlabs.io/v1/convai/tools/{tool_id}`

## Request Details

### Path Parameters
- **tool_id** (required, string): Identifier for the tool being updated

### Headers
- **Content-Type:** application/json
- **xi-api-key** (optional, string): Authentication header

### Request Body

The request requires a `ToolRequestModel` containing `tool_config`. The tool configuration supports four distinct types:

**Client Tool:**
- type: "client"
- name: string (required)
- description: string (required)
- parameters: JSON schema for client parameters
- expects_response: boolean (default: false)
- Additional options: response_timeout_secs, disable_interruptions, force_pre_tool_speech, tool_call_sound, execution_mode

**Webhook Tool:**
- type: "webhook"
- name: string (required)
- description: string (required)
- api_schema: configuration for URL, HTTP method, headers, request body
- response_timeout_secs: 5-120 seconds
- Additional configuration options for error handling and execution

**System Tool:**
- type: "system"
- name: string (required)
- params: system-specific configuration
- Supports: end_call, language_detection, play_keypad_touch_tone, skip_turn, transfer_to_agent, transfer_to_number, voicemail_detection

**MCP Tool:**
- type: "mcp"
- value: any type configuration

## Response

**Success Response (200):**
Returns a `ToolResponseModel` containing:
- id: tool identifier
- tool_config: the updated configuration
- access_info: creator details and user role
- usage_stats: total_calls and avg_latency_secs

**Error Response (422):**
Returns validation errors with details about invalid fields

## Common Configuration Options

- **response_timeout_secs:** Maximum wait time for tool completion (1-120 seconds depending on tool type)
- **disable_interruptions:** Prevents user interruption during tool execution
- **force_pre_tool_speech:** Agent speaks before calling the tool
- **tool_call_sound:** Predefined sounds (typing, elevator1-4) during execution
- **tool_error_handling_mode:** Controls error processing (auto, summarized, passthrough, hide)
- **execution_mode:** Determines execution timing (immediate, post_tool_speech, async)
- **dynamic_variables:** Configuration for extracting and assigning response values to variables
