# Custom LLM Tool Calling Integration

## Overview

A Custom LLM functions as more than a text generator—it's a conversational system capable of invoking external functions, automating processes, and implementing specialized logic during user interactions.

**Key Benefits:**
- Blends natural language responses with executable functions
- Combines built-in capabilities with external tools via Vapi or custom endpoints
- Returns structured directives (call transfers, custom processes) as needed
- Integrates quickly into Vapi assistants

## Basic Response Generation Setup

The foundational approach involves receiving conversation payloads and streaming generated replies back as Server-Sent Events.

**Process Flow:**
1. Your endpoint receives model details, conversation history, temperature settings, and optional tool definitions
2. An OpenAI API request incorporating the context gets constructed
3. Generated text streams back as SSE

**Implementation Overview:**
The endpoint accepts POST requests containing model specifications and message arrays. It forwards these to OpenAI with streaming enabled, then pipes response chunks back to the client with appropriate SSE headers.

## Three Tool Integration Approaches

### Native LLM Tools
Built-in functions like payment link generation execute directly within your LLM integration. When the model produces a tool call, arguments get parsed, the function runs, and results feed into a follow-up API request.

### Vapi-Attached Tools
Pre-configured tools such as call transfer don't require execution—instead, the integration detects them and immediately returns function call payloads instructing Vapi to handle the action.

### Custom Tools
Application-specific functions route through dedicated endpoints. Tool call payloads go to specialized routes where custom logic determines results, which then return as JSON responses with tool call IDs and results.

## Testing Approaches

cURL commands facilitate endpoint validation before production deployment. Each tool type has specific payload structures:

- Native tools include tool definitions with function names and parameters
- Vapi-attached tools include destination specifications
- Custom tools send payloads with toolCallList arrays to dedicated endpoints

## Vapi Integration

After local testing, assistants get configured via PATCH requests to Vapi's API. Configurations can include:
- Response generation only (simpler setup)
- Response generation plus tools (native, Vapi-attached, and custom)

System prompts guide the LLM on when to trigger specific tools based on user requests.

## Complete Implementation Resource

The documentation references a [CodeSandbox project](https://codesandbox.io/p/devbox/gfwztp) containing full working code examples for the entire integration pattern.
