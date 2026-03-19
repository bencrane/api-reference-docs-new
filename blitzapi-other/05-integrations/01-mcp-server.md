> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server

> Connect any AI tool directly to the Blitz API documentation for hallucination-free code generation.

## What is the Blitz API MCP Server?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open standard that lets AI assistants connect directly to external data sources instead of relying on their training data.

The **Blitz API MCP Server** gives any compatible AI tool live access to the complete Blitz API documentation — every endpoint, parameter, response schema, and code example.

When your AI assistant needs to write code that calls Blitz API, it searches the actual documentation instead of guessing.

**MCP Server URL**

```text  theme={null}
https://docs.blitz-api.ai/mcp
```

***

## Why Use It?

AI models are trained on static snapshots of the internet. When they generate code for an API, they often:

* Hallucinate endpoints that don't exist
* Use outdated parameter names
* Return incorrect response shapes

With the Blitz API MCP Server connected:

| Without MCP                | With MCP                                 |
| :------------------------- | :--------------------------------------- |
| AI guesses endpoint URLs   | AI reads the real API reference          |
| Outdated parameter names   | Always up-to-date parameter schemas      |
| Incorrect response shapes  | Accurate response structures from source |
| Back-and-forth corrections | Ship correct code on the first try       |

***

## What Content is Available?

The MCP server provides a search tool that covers the entire Blitz API documentation:

| Content          | Description                                                          |
| :--------------- | :------------------------------------------------------------------- |
| API endpoints    | Full reference for every v2 endpoint — methods, URLs, and parameters |
| Request schemas  | Required and optional fields, types, and example payloads            |
| Response schemas | Complete response structures with field descriptions                 |
| Waterfall logic  | How cascade/waterfall search works, ICP scoring, and priority levels |
| Code examples    | cURL commands, Node.js, Python, and integration patterns             |
| Guides & recipes | Enrichment workflows, CRM hygiene, and integration tutorials         |

***

## Setup

<Tabs>
  <Tab title="Claude (claude.ai)">
    1. Open [Claude.ai](https://claude.ai) and start a new conversation.
    2. Click the **"+"** or attachments button.
    3. Select **"Manage Connectors"** and click on **"Add custom Connector"**.
    4. Copy / Paste this URL into "Remote MCP server URL": [https://docs.blitz-api.ai/mcp](https://docs.blitz-api.ai/mcp).

    <Note>
      You may need to explicitly enable the connector for each new conversation using the attachments button.
    </Note>
  </Tab>

  <Tab title="Cursor">
    Press `Cmd + Shift + P` (macOS) or `Ctrl + Shift + P` (Windows/Linux) to open the command palette, then search for **"Open MCP Settings"**.

    In your `mcp.json` file, add:

    ```json  theme={null}
    {
      "mcpServers": {
        "blitz-api": {
          "url": "https://docs.blitz-api.ai/mcp"
        }
      }
    }
    ```

    In Cursor's Agent chat, ask: `"What tools do you have available?"` — you should see the Blitz API documentation search tool listed.

    <Tip>
      Make sure the MCP server shows a **green status indicator** in your MCP settings after adding it.
    </Tip>
  </Tab>

  <Tab title="VS Code">
    In your project root, create a `.vscode/mcp.json` file (or open it if it already exists):

    ```json  theme={null}
    {
      "servers": {
        "blitz-api": {
          "type": "http",
          "url": "https://docs.blitz-api.ai/mcp"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Claude Desktop">
    Older versions of Claude Desktop don't support remote MCP servers natively. Use the `mcp-remote` wrapper:

    ```json  theme={null}
    {
      "mcpServers": {
        "blitz-api": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://docs.blitz-api.ai/mcp"]
        }
      }
    }
    ```

    Save this in your Claude Desktop config file and restart the application.
  </Tab>
</Tabs>

***

## Example Prompts

Once connected, try these prompts with your AI tool:

<AccordionGroup>
  <Accordion title="Write a Python script to find decision-makers">
    ```text  theme={null}
    Using Blitz API, write a Python script to find the Head of Sales at a company given its LinkedIn URL. Include rate limiting and error handling.
    ```
  </Accordion>

  <Accordion title="Get parameters for an endpoint">
    ```text  theme={null}
    What parameters does the waterfall ICP keyword search endpoint accept? Show me a complete example JSON body.
    ```
  </Accordion>

  <Accordion title="Generate a Node.js enrichment function">
    ```text  theme={null}
    Generate a Node.js function that enriches a list of LinkedIn profile URLs with work emails using Blitz API. Handle the case where the email is not found.
    ```
  </Accordion>

  <Accordion title="Build a full enrichment pipeline">
    ```text  theme={null}
    Write a Python script that takes a list of company domains, converts each to a LinkedIn URL, then finds the VP of Sales using the Blitz API waterfall search. Include retry logic.
    ```
  </Accordion>
</AccordionGroup>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="The AI tool doesn't seem to use the documentation">
    Some AI tools require you to explicitly enable the connector for each conversation. In Claude, use the attachments button to select the Blitz API connector. In Cursor, make sure the MCP server shows a green status indicator in your MCP settings.
  </Accordion>

  <Accordion title="Connection fails after adding the config">
    Restart your AI tool after adding the MCP configuration. Most clients need a full restart to detect new MCP servers. Verify the URL is exactly `https://docs.blitz-api.ai/mcp` — no trailing slash, no extra path segments.
  </Accordion>

  <Accordion title="Claude Desktop doesn't connect">
    Older versions of Claude Desktop don't support remote MCP servers natively. Use the `mcp-remote` wrapper shown in the Claude Desktop tab above.
  </Accordion>

  <Accordion title="Network or timeout errors">
    Check your network connection and try again. If the issue persists, verify the server is reachable by opening `https://docs.blitz-api.ai/mcp` in your browser.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).