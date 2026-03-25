# Vapi CLI Documentation

## Overview

The Vapi CLI serves as an official command-line interface enabling developers to construct voice AI applications directly from their terminal. According to the documentation, it allows users to "Build, test, and deploy voice AI applications without leaving your development environment."

## Installation Methods

Three installation approaches are available:

**macOS/Linux:** Uses a curl-based automated script
**Windows:** Implements PowerShell installation
**Docker:** Provides containerized CLI access

## Core Capabilities

The CLI encompasses several primary functions:

- **Project Integration:** Automatically detects technology stacks (React, Vue, Next.js, Python, Go, Flutter, etc.) and configures necessary files
- **IDE Enhancement:** MCP integration enables AI assistants within code editors like Cursor and VSCode to access Vapi API documentation
- **Local Development:** Webhook forwarding to localhost for testing purposes (requires separate tunneling service)
- **Multi-Account Support:** Seamless switching between organizations and environments
- **Feature Parity:** Terminal-based management of assistants, phone numbers, calls, workflows, campaigns, tools, webhooks, and logs

## Authentication & Configuration

The CLI stores settings in `~/.vapi-cli.yaml` with environment variable override support. Initial setup requires OAuth authentication via browser.

## Additional Resources

- GitHub repository for source code
- Discord community for support
- Issue tracking on GitHub
