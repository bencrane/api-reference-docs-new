# OpenAI Playground + Enigma​

URL: https://documentation.enigma.com/guides/ai-mcp/openai-playground

Beta

- MCP Server support in OpenAI Playground is currently in beta.
- The Enigma remote MCP server is currently in beta.

Give the agents you build with OpenAI Playground the power of Enigma business intelligence.

## Prerequisites

- An Enigma API key, which you can find in the the [Enigma Console](https://console.enigma.com/settings/api-keys) under **Settings > Account > API Keys**
- An [OpenAI Playground account](https://platform.openai.com)

## Installation

Once you've created a project in OpenAI Playground, you can set up the Enigma AI Connector.

1. Create a new chat prompt that uses's Enigma tools by selecting **Chat → Create**
2. Next to tools, select **Add → MCP Server**
3. Select the **+ Server** button
4. Enter the following information and select **Connect** :
- URL: [https://mcp.enigma.com/http-key](https://mcp.enigma.com/http-key)
- Authentication: Custom headers
- header: `x-api-key`
- value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
5. URL: [https://mcp.enigma.com/http-key](https://mcp.enigma.com/http-key)
6. Authentication: Custom headers
- header: `x-api-key`
- value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
7. header: `x-api-key`
8. value: your Enigma API key, which you can find in the [Enigma Console](https://console.enigma.com)
9. Once the connection has been established, select the settings and the tools you want, then select **Add**
10. Configure the rest of your prompt for your use case
- Ensure to select a model that supports tool use, such as GPT-5
11. Ensure to select a model that supports tool use, such as GPT-5

## Verify Your Setup

Chat with your prompt to verify that the connector is working

- "Should I invest in fiddlehead bistro in saranac lake NY?"
- "Use only the internal Enigma data to find 2 coffee shops in 10026 with highest revenue as determined by current revenue figures"

## Resources

- [OpenAI Playground | Connectors and MCP servers](https://platform.openai.com/docs/guides/tools-connectors-mcp#connectors)