# VS Code + Enigma​

URL: https://documentation.enigma.com/guides/ai-mcp/vscode

Beta
The Enigma remote MCP server is currently in beta.

Give VS Code Copilot the power of Enigma business intelligence. Through MCP, GitHub Copilot gains comprehensive business knowledge for building data-driven applications with real market insights.

## Prerequisites

- An Enigma API key, which you can find in the the [Enigma Console](https://console.enigma.com/settings/api-keys) under **Settings > Account > API Keys**
- [Visual Studio Code installed](https://code.visualstudio.com/download)
- GitHub Copilot extension (for MCP support)

## Installation

In your workspace, create `.vscode/mcp.json` :

```json
{
  "servers": {
    "enigma": {
      "command": "npx",
      "args": [
        "-y", "-p", "@enigma-com/enigma-mcp-remote@latest",
        "enigma-mcp-remote", 
        "https://mcp.enigma.com/http-key",
        "--header", "x-api-key:YOUR_API_KEY"
      ]
    }
  }
}
```

## Verify Your Setup

1. Restart VS Code to load the MCP configuration
2. Open GitHub Copilot Chat
3. Look for Enigma tools in the available capabilities
**Test the connection:** Try this example in Copilot Chat:

> "Research Tacombi's business model and competitive landscape"

You should see your Copilot intelligently using Enigma business intelligence to provide comprehensive analysis.

## What Your Copilot Can Do

With Enigma business intelligence, your GitHub Copilot can:

- **Research any company** while you build business applications
- **Validate market assumptions** with real data during development
- **Analyze competitive landscapes** when designing product features
- **Access financial metrics** for building business intelligence dashboards
Your AI coding assistant becomes a business research expert, seamlessly integrating market data into your development process.

## Troubleshooting

**Tools not showing up in Copilot Chat?**

- Ensure the `.vscode/mcp.json` file is in your workspace root
- Restart VS Code after creating or modifying the configuration
- Verify GitHub Copilot extension is installed and active
**Configuration not loading?**

- Check that the JSON syntax is valid
- Ensure you have the latest version of VS Code and Copilot extension

## Resources

- [Use MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)