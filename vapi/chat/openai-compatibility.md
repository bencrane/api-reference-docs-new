# OpenAI Compatibility Documentation

## Overview

This documentation guide explains how to migrate existing OpenAI integrations to Vapi without modifying your codebase. The approach involves changing only the API endpoint and credentials while maintaining compatibility with the OpenAI SDK.

## Key Migration Steps

**Configuration Changes:**
The primary modification involves updating the client initialization. Instead of using OpenAI's default endpoint, developers set the `baseURL` to Vapi's service and provide a Vapi API key.

**Function Call Updates:**
Existing `chat.completions.create()` calls need adjustment to use Vapi's `responses.create()` method, with the addition of an `assistantId` parameter.

**Response Format:**
Vapi maintains OpenAI-compatible response structures while returning data in slightly different object paths (using `output` instead of `choices`).

## Implementation Features

The documentation covers four main implementation areas:

1. **Quick Migration Testing** - Initial validation using curl and response verification
2. **Code Migration** - Converting existing OpenAI implementations with minimal changes
3. **Streaming Support** - Handling real-time responses via Server-Sent Events
4. **Framework Integration** - Connecting with LangChain, Vercel AI SDK, and custom servers

## Notable Capabilities

- Conversation context management through `previousChatId` parameters
- Both streaming and non-streaming request modes
- Token usage tracking in response metadata
- Production-ready server implementations

## Integration Examples

The guide includes practical implementations for popular frameworks and provides a simple Express.js server example that exposes Vapi through OpenAI-compatible endpoints on port 3000.
