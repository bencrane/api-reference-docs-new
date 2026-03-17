# MCP Server Integration

## Core Concept
The Blitz API MCP Server connects compatible AI tools to live API documentation using the Model Context Protocol standard, enabling "hallucination-free code generation."

## Key Features
- **Live Documentation Access**: AI assistants query actual API reference instead of relying on training data
- **Complete Coverage**: Endpoints, parameters, response schemas, and code examples
- **Server URL**: `https://docs.blitz-api.ai/mcp`

## Problems It Solves

| Without MCP | With MCP |
|-------------|----------|
| AI guesses endpoint URLs | AI reads the real API reference |
| Outdated parameters | Up-to-date schemas |
| Incorrect response structures | Accurate response data |

## Available Content
- API v2 endpoint references with methods and parameters
- Request/response schema specifications with field descriptions
- Waterfall search logic and ICP scoring details
- Code examples in cURL, Node.js, and Python
- Integration guides and enrichment workflows

## Setup Instructions

### Claude.ai
Add custom connector via attachments menu.

### Cursor
Configure `mcp.json` with server URL:
```json
{
  "mcpServers": {
    "blitz-api": {
      "url": "https://docs.blitz-api.ai/mcp"
    }
  }
}
```

### VS Code
Create `.vscode/mcp.json` with HTTP server configuration:
```json
{
  "servers": {
    "blitz-api": {
      "type": "http",
      "url": "https://docs.blitz-api.ai/mcp"
    }
  }
}
```

### Claude Desktop
Use `mcp-remote` wrapper for older versions.

## Example Use Cases
- Python scripts for finding decision-makers via LinkedIn
- Node.js enrichment functions for email discovery
- Complete enrichment pipelines combining domain-to-LinkedIn conversion with waterfall search

## Example Prompt

> "Write a Python script that uses BlitzAPI to find the VP of Sales at Stripe and get their verified email address."

With MCP connected, the AI will:
1. Query the live API documentation
2. Use correct endpoint paths and parameters
3. Generate working code with proper error handling
