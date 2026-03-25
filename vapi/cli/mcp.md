# MCP Integration Documentation

## Overview

The Model Context Protocol (MCP) integration enhances IDE capabilities by making an AI assistant knowledgeable about Vapi's APIs and features. As stated in the documentation, this setup "transforms your IDE's AI assistant into a Vapi expert" and eliminates inaccurate information generation.

## Quick Setup

Users can configure MCP across supported environments using simple commands:

```bash
vapi mcp setup
```

Individual IDEs (Cursor, Windsurf, VSCode) can be configured separately with specific commands.

## Supported Development Environments

The integration works with three primary IDEs:

- **Cursor** - Creates `.cursor/mcp.json` configuration
- **Windsurf** - Creates `.windsurf/mcp.json` configuration
- **VSCode** - Configures GitHub Copilot settings

## Knowledge Base Access

Once configured, the IDE gains access to comprehensive resources including API documentation, code samples, implementation patterns, and troubleshooting guidance. The system maintains current information about Vapi features and releases.

## Practical Implementation

The documentation provides accordion-style examples for common tasks like creating voice assistants, managing webhooks, and configuring call recording with custom storage solutions.

## Maintenance Commands

Users can check configuration status, update the MCP server, or remove configurations using dedicated CLI commands like `vapi mcp status` and `vapi mcp remove`.

## Troubleshooting

The guide addresses common issues including IDE restarts, permission challenges, outdated information, and multi-workspace scenarios.
