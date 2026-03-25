# List LLMs API Documentation

## Overview

The ElevenLabs List LLMs endpoint retrieves "a list of available LLM models that can be used with agents, including their capabilities and any deprecation status."

## Endpoint Details

**URL:** `GET https://api.elevenlabs.io/v1/convai/llm/list`

The endpoint filters results based on "the data residency of the deployment and any compliance requirements (e.g. HIPAA) of the workspace subscription."

## Key Response Components

The API returns information about available models including:

- **Model identifiers** - Names like `gpt-4o`, `claude-sonnet-4-5`, `gemini-2.5-flash`
- **Capabilities** - Support for images, documents, parallel tool calls, and reasoning effort levels
- **Token limits** - Maximum context and output token capacities
- **Deprecation status** - Whether models are deprecated or scheduled for deprecation with replacement information

## Supported Models

The endpoint supports numerous models across providers including OpenAI (GPT series), Google (Gemini), Anthropic (Claude), and others, plus custom LLM options.

## Authentication

The API accepts an optional `xi-api-key` header parameter for authentication.

## Implementation

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for easy integration across different development environments.
