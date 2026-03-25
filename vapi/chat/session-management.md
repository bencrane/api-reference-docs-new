# Session Management Documentation

## Key Concepts

Vapi offers two distinct methods for preserving conversation context: **`previousChatId`** for sequential chat linking and **`sessionId`** for grouping multiple interactions under one persistent session. These approaches are mutually exclusive and cannot be combined in a single request.

## Method Comparison

**previousChatId Approach:**
This technique chains conversations by referencing the preceding chat's identifier. Each message includes the ID from the prior exchange, enabling the system to maintain context through a linear conversation flow.

**sessionId Approach:**
This method establishes a durable session container that persists for 24 hours by default. Multiple chat interactions reference the same session identifier, allowing context to be maintained across all exchanges within that timeframe.

## Implementation Guidance

The documentation provides TypeScript examples demonstrating both approaches. The conversation chain example shows how to progressively track chat IDs, while the session manager example illustrates creating a session once and reusing its identifier across multiple requests.

## When to Select Each Method

Choose `previousChatId` for straightforward back-and-forth exchanges requiring minimal configuration. Opt for `sessionId` when handling elaborate workflows, extended conversations, or situations where fault tolerance becomes important.

## Special Considerations

Sessions cannot be shared across multiple assistants—create separate sessions for each assistant in multi-assistant workflows. The system automatically manages sessions for web chat widgets and SMS channels without requiring manual intervention.

Webhook support enables tracking session lifecycle events through "server messaging" in the Dashboard, useful for maintaining session state in external databases.
