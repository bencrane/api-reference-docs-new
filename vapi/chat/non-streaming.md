# Non-Streaming Chat Documentation

## Overview
This guide covers building chat integrations that return complete responses after processing, suitable for batch systems and straightforward interfaces where real-time display isn't necessary.

## Key Concepts

**Complete Response Pattern**: Rather than streaming tokens progressively, the system processes the entire message and returns a finished response object containing user input and assistant output.

**Context Linking**: The documentation explains that conversations can be connected through a `previousChatId` parameter, enabling the system to maintain awareness of prior exchanges without requiring session management infrastructure.

## Implementation Approach

The guide demonstrates three implementation strategies:

1. **Basic Request-Response**: A straightforward curl example showing the minimal payload needed to send a message and receive a complete reply.

2. **Conversation Chains**: A TypeScript pattern that stores the most recent chat ID and passes it with subsequent messages, creating a linked conversation history.

3. **Inline Configuration**: Rather than using pre-configured assistants, developers can define behavior per request using system prompts and model parameters directly in the API call.

## Code Patterns

The documentation provides reusable TypeScript functions showing how to extract response content, handle the JSON structure, and manage conversation state across multiple turns.

## Related Resources

The page references complementary topics including streaming alternatives, OpenAI SDK compatibility, tool integration, and session management options for more sophisticated context handling.
