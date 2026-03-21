# Microsoft 365 Copilot + Enigma​

URL: https://documentation.enigma.com/guides/ai-mcp/ms-copilot

Beta
The Enigma remote MCP server is currently in beta.

Give Microsoft 365 Copilot the power of Enigma business intelligence. Through MCP, Microsoft 365 Copilot gains comprehensive business knowledge for building data-driven applications with real market insights.

## Prerequisites

- A Microsoft 365 Copilot agent in [Microsoft 365 Copilot Studio](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio)
- An Enigma API key, which you can find in the the [Enigma Console](https://console.enigma.com/settings/api-keys) under **Settings > Account > API Keys**

## Installation

1. Go to the Tools page for your agent.
2. Select Add a tool.
3. Select New tool.
4. Select Model Context Protocol. The MCP onboarding wizard appears.
5. Enter the following information:
- Server name: Enigma
- Server description: Enigma is the most reliable, trusted source of data on business in the United States.
- Server URL: [https://mcp.enigma.com/http-key](https://mcp.enigma.com/http-key)
- Authentication: API key
- Type: header
- Header: `x-api-key`
- Value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
6. Server name: Enigma
7. Server description: Enigma is the most reliable, trusted source of data on business in the United States.
8. Server URL: [https://mcp.enigma.com/http-key](https://mcp.enigma.com/http-key)
9. Authentication: API key
- Type: header
- Header: `x-api-key`
- Value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
10. Type: header
11. Header: `x-api-key`
12. Value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
13. Select Create.

## What Your Copilot Can Do

With Enigma business intelligence, your Microsoft 365 Copilot can:

- **Research any company** while you build business applications
- **Validate market assumptions** with real data during development
- **Analyze competitive landscapes** when designing product features
- **Access financial metrics** for building business intelligence dashboards
Your Microsoft 365 Copilot becomes a business research expert, seamlessly integrating market data into your development process.

## Resources

- [What is Microsoft 365 Copilot Studio?](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Connect your agent to an existing Model Context Protocol (MCP) server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent)