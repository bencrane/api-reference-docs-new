# Model Context Protocol (MCP) Integration

## Overview

The MCP integration enables Vapi assistants to dynamically access tools from MCP servers during calls. According to the documentation, this allows assistants to "Connect to any MCP-compatible server" and "Access tools dynamically at runtime."

## Prerequisites

To implement MCP integration, you need:
- Access to the Vapi Dashboard
- An existing assistant in Vapi
- An MCP server URL from providers like Make, Zapier, or Composio

## Setup Process

### Step 1: Obtain MCP Server URL
Obtain your server URL from your chosen MCP provider. For Zapier, visit their designated MCP configuration page. For Make, generate an MCP Token through your profile's API Access settings.

### Step 2: Create MCP Tool
Navigate to Dashboard > Tools, select "Create Tool," choose MCP, and enter:
- Tool name and description
- Required field: `serverUrl`

### Step 3: Add Tool to Assistant
Go to Dashboard > Assistants, select your assistant, access the Tools tab, and add your MCP tool before publishing.

## How MCP Works

The process involves these stages:

1. Upon session start, Vapi connects to the MCP server and fetches available tools
2. The assistant accesses these tools during interaction
3. Each tool invocation creates a new connection with identifying headers
4. Results return and the cycle repeats for subsequent invocations

The documentation notes that "multiple MCP sessions are created per call or chat" to maintain consistency.

## Request Headers

Vapi includes identifying headers:
- **X-Call-Id**: For voice calls
- **X-Chat-Id**: For chat interactions
- **X-Session-Id**: For chat sessions

## Tool Configuration

**Required:**
- `server.url`: MCP server URL

**Optional:**
- `server.headers`: Custom headers
- `metadata.protocol`: `"shttp"` (default) or `"sse"`

## Example MCP Providers

**Make MCP**: Define scenarios and use your MCP Token for custom tool provisioning.

**Zapier MCP**: Provides access to "over 7,000+ apps and 30,000+ actions" without complex integrations.

**Composio MCP**: Log in to dashboard, enable the MCP server for desired tools, and copy the generated URL.

## Best Practices

- Use default Streamable HTTP protocol for optimal performance
- Maintain clear system instructions for dynamic tool handling
- Implement error handling for tool failures
- Treat MCP server URLs as secure credentials
- Monitor token usage and context size to prevent overflow issues

## Important Note

The documentation includes a context overflow warning: tools returning large datasets may exceed model limits, potentially causing performance issues. Configure tools to return focused data and test integrations thoroughly before deployment.
