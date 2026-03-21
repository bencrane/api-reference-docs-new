# Gemini CLI + Enigma​

URL: https://documentation.enigma.com/guides/ai-mcp/gemini-cli

Beta
The Enigma remote MCP server is currently in beta.

Give the Gemini CLI the power of Enigma business intelligence. With Enigma MCP tools, your AI agent becomes a business research expert for quick analysis and market insights.

## Prerequisites

- An Enigma API key, which you can find in the the [Enigma Console](https://console.enigma.com/settings/api-keys) under **Settings > Account > API Keys**
- A [Gemini API key](https://aistudio.google.com/app/apikey)
- [Gemini CLI installed](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#quickstart)

## Installation

Locate the Gemini CLI settings file (usually `~/.gemini/settings.json` ) and add:

```json
{
  "mcpServers": {
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

**Test the connection:** Try this example in Gemini CLI:

> "Analyze Tacombi's market position and growth trends"

You should see your Gemini AI intelligently using Enigma business intelligence to provide comprehensive market analysis.

## What Your Gemini CLI Can Do

With Enigma business intelligence, your Gemini CLI can:

- **Research any business** instantly during command line sessions
- **Analyze competitive landscapes** for market research
- **Access financial data** for investment and performance analysis
- **Perform compliance checks** for due diligence workflows
Your command line AI becomes a business intelligence expert, providing instant access to comprehensive business data.

## Troubleshooting

**MCP authentication failing?**

- Ensure you're logged into [Enigma Console](https://console.enigma.com/) in your default browser
- Restart Gemini CLI after configuration changes
- Try clearing browser cache and re-authenticating
**Tools not working in chat?**

- Verify the MCP server is properly configured in settings.json
- Check that your Gemini API key is valid and active
- Use `/mcp status` to check connection status

## Resources

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- [Configure MCP servers | Gemini for Google Cloud](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#configure-mcp-servers)