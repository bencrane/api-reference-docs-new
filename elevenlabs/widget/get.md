# Get Widget API Documentation

## Endpoint Overview

The Get Widget endpoint retrieves widget configuration settings for a conversational AI agent. It's accessed via:

**GET** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/widget`

## Parameters

### Path Parameter
- **agent_id** (required): The unique identifier returned when creating an agent

### Query Parameters
- **conversation_signature** (optional): An expiring token enabling websocket conversation initiation, generated through the `/v1/convai/conversation/get-signed-url` endpoint

### Headers
- **xi-api-key** (optional): API authentication key

## Response Structure

The successful 200 response returns a `GetAgentEmbedResponseModel` containing:

- **agent_id**: The agent identifier
- **widget_config**: Comprehensive configuration object with these key sections:

### Widget Display Options
- Variant types: tiny, compact, full, expandable
- Placement positions: top-left, top, top-right, bottom-left, bottom, bottom-right
- Expandability settings: never, mobile, desktop, always

### Styling Configuration
- Color properties for backgrounds, text, buttons, borders, and focus states
- Border and button radius values
- Advanced style system with base and accent color variants

### Content Customization
- Avatar configuration (orb, URL, or image types)
- Comprehensive text contents for UI elements (labels, statuses, placeholders)
- Language presets and multi-language support
- Terms and conditions text/HTML

### Feature Toggles
- Microphone muting capability
- Transcript display
- Text input functionality
- Conversation mode toggle
- Agent status visibility
- Markdown link allowlisting with domain restrictions

### Behavioral Settings
- Default expanded state
- Dismissibility options
- WebRTC usage preference
- Text-only mode support

## Error Handling

A 422 response indicates validation errors, returned in `HTTPValidationError` format with detailed error information.

## Code Examples

The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same basic GET request with optional parameters.
