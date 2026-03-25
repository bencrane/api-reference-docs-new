# Client-side Tools (Web SDK)

## Overview

The Web SDK enables handling tool-calls entirely within the browser, allowing assistants to trigger UI effects like notifications or state changes without requiring a server URL.

**Key learning points:**
- Defining client-side tools with the Web SDK
- Receiving and handling `tool-calls` events on the client
- Using `addMessage` to inject contextual information during calls

### Important Limitation

"Client-side tools cannot send a tool 'result' back to the model." For scenarios requiring the model to use tool outputs for continued reasoning, implement server-based tools instead.

### How It Works

"To make a tool client-side, simply do not provide a server URL." The tool specification reaches the browser, and the Web SDK emits `tool-calls` messages that your frontend processes.

## Quickstart Steps

1. Install via npm: `npm install @vapi-ai/web`
2. Define your tool in `model.tools` and subscribe to `clientMessages: ['tool-calls']`
3. Listen for `message.type === 'tool-calls'` and execute UI updates (no response sent to model)
4. Optionally inject mid-call context using `vapi.addMessage(...)`

## React Implementation Example

The documentation includes a complete React example featuring:
- Event listener for tool-calls messages
- UI notification display triggered by tool execution
- Start/stop call functionality with styled buttons
- Tool definition for updating the user interface

## Adding Context Mid-Call

Use `addMessage` to provide additional context without expecting tool results:

```ts
vapi.addMessage({
  role: 'system',
  content: 'Context: userId=123, plan=premium, theme=dark',
});
```

## Essential Takeaways

- Client tools execute locally without server involvement
- One-way communication: tools trigger effects but don't return data to the model
- Subscribe to tool-calls using the `clientMessages` configuration
- Server-based tools are necessary when the model needs tool output for reasoning
