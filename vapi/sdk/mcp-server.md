# Vapi MCP Server Documentation

## Overview

The **Vapi MCP Server** makes Vapi APIs available as tools through the Model Context Protocol (MCP), enabling integration with AI assistants like Claude Desktop and various agent frameworks. This service facilitates management of assistants, phone numbers, and calls while automating voice-based workflows.

## Quick Setup for Claude Desktop

To connect Claude Desktop with the Vapi MCP Server:

1. Retrieve your API key from the [Vapi dashboard](https://dashboard.vapi.ai/org/api-keys)
2. Navigate to Settings → Developer → Edit Config
3. Insert the server configuration into `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "vapi-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.vapi.ai/mcp",
        "--header",
        "Authorization: Bearer ${VAPI_TOKEN}"
      ],
      "env": {
        "VAPI_TOKEN": "YOUR_VAPI_API_KEY"
      }
    }
  }
}
```

4. Save and restart Claude Desktop

**Example usage:** "Have my customer support assistant call Jeremy at +1555123456."

## Available Tools

| Tool | Purpose |
|------|---------|
| `list_assistants` | Display all configured assistants |
| `create_assistant` | Set up a new assistant |
| `get_assistant` | Retrieve assistant configuration by ID |
| `list_calls` | View all call records |
| `create_call` | Initiate or schedule outbound calls |
| `get_call` | Check call status and details |
| `list_phone_numbers` | View available phone numbers |
| `get_phone_number` | Inspect specific phone number info |
| `list_tools` | Discover available tools |
| `get_tool` | View tool integration details |

The `create_call` tool supports scheduling via the optional `scheduledAt` parameter.

## Connection Methods

### Remote (Streamable-HTTP)
- **Endpoint:** `https://mcp.vapi.ai/mcp`
- **Authentication:** Bearer token format
- Recommended for production deployments

### Remote (SSE)
- **Endpoint:** `https://mcp.vapi.ai/sse`
- **Protocol:** Server-Sent Events
- Suitable for SSE-compatible clients

### OpenAI Responses API
The OpenAI `responses` API supports MCP integration with TypeScript and Python implementations available.

### Local Development
```bash
npx -y @vapi-ai/mcp-server
```
Set `VAPI_TOKEN` environment variable for authentication.

## Custom Client Integration

Multiple MCP client SDKs are available:
- TypeScript
- Python
- Java
- Kotlin
- C#

Configure your SDK to connect to `https://mcp.vapi.ai/sse` with API key authentication.

## Node.js Implementation Examples

Both Streamable-HTTP and SSE transports include detailed client examples with tool response parsing, assistant listing, phone number retrieval, and call creation functionality.

## Resources

- [GitHub Repository](https://github.com/VapiAI/mcp-server)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [Vapi Dashboard](https://dashboard.vapi.ai)
- [MCP Client Quickstart](https://modelcontextprotocol.io/quickstart/client)
- [Discord Community Support](https://discord.gg/pUFNcf2WmH)
