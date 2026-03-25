# Project Integration Documentation

## Overview

The `vapi init` command provides "intelligent integration of Vapi into your existing codebase" with automatic framework detection and SDK installation.

## Quick Start

Execute from your project directory:
```bash
cd my-project
vapi init
```

The tool will automatically detect your project type, install relevant SDKs, generate example components, create configuration templates, and provide framework-specific guidance.

## Framework Detection Process

The CLI examines package files, configuration settings, directory structures, and installed dependencies to identify your technology stack.

## Generated Files by Framework

**React/Next.js** produces:
- Voice call button component
- Webhook handler endpoint
- Client setup file
- Environment template

**Python** generates:
- Basic assistant example
- Webhook handler
- Requirements file
- Environment template

**Node.js** creates:
- Usage example file
- Express webhook handler
- Environment template

## Supported Technologies

The tool supports numerous frontend frameworks (React, Vue, Angular, Next.js, Svelte), mobile platforms (React Native, Flutter), and backend systems (Express, Django, FastAPI, Spring Boot, Rails, and others).

## Advanced Options

- Specify target directory: `vapi init /path/to/project`
- Skip installation: `vapi init --skip-install`
- Override detection: `vapi init --framework react`
- Custom templates: `vapi init --template @myorg/vapi-templates`

## Environment Configuration

Copy the template file, add your API key from the dashboard, and optionally configure webhook URLs.

## Integration Patterns

Monorepo support, CI/CD workflows, and Docker containerization are documented with example configurations.

## Troubleshooting

Solutions provided for detection failures, permission issues, and file conflicts. The `--force` flag bypasses confirmation prompts.

## Next Steps

Users can test locally with webhook listeners, create voice assistants, or configure MCP integration.
