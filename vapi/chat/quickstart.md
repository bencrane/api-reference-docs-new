# Chat Quickstart - Vapi Documentation

## Summary

This guide enables developers to create text-based conversational AI in approximately five minutes using Vapi's chat API. The tutorial covers building a customer support chatbot for "TechFlow" that manages inquiries through text interactions.

## Key Components

**Getting Started Requirements:**
- Active Vapi account with dashboard access
- API credentials (private key)
- An assistant (newly created or existing)

**Core Features Demonstrated:**
The tutorial covers initial message sending, multi-turn conversations maintaining context, dynamic variable injection, and TypeScript integration patterns for production environments.

**Essential Steps:**
1. Retrieve API credentials from the dashboard
2. Create/configure an assistant with system prompts
3. Execute initial API call using curl
4. Build conversation continuity via `previousChatId`
5. Implement variable substitution using `{{variableName}}` syntax
6. Develop TypeScript wrapper functions
7. Test multiple scenarios (general questions, technical issues)

**Integration Example:**
The documentation provides a TypeScript function accepting messages and optional chat IDs, returning structured responses including conversation ID, assistant output, and full API response data.

## Notable Limitations & Features

Current constraints exclude server webhook events for status updates. However, webhook support exists for `chat.created` and `chat.deleted` events through server messaging configuration in the dashboard.

## Progression Path

Advanced users can explore streaming responses, session management techniques, and OpenAI API compatibility for broader integration scenarios.
