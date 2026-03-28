# assistant-ui Protocol Reference: HTTP Contracts for chat-engine-x-api

This document defines the exact HTTP contracts that `chat-engine-x-api` must implement to be compatible with assistant-ui's frontend runtime. It covers request shapes, response stream formats, message type definitions, conversion utilities, and version-specific gotchas.

---

## Protocol Decision Matrix

| Protocol Path | When to Use | Request Format | Response Format | Key Package |
|---|---|---|---|---|
| **AI SDK** (Primary) | Standard chat with streaming | `{ messages: UIMessage[], system?, tools? }` | `streamText().toUIMessageStreamResponse()` | `ai@^6` |
| **Data Stream** (Alternative) | Framework-agnostic backend | `{ messages, tools, system, threadId }` | `createAssistantStreamResponse()` | `assistant-stream` |
| **Assistant Transport** (Advanced) | Custom agent with arbitrary state | `{ state, commands[], system?, tools?, threadId }` | `aui-state:` operation stream | `assistant-stream` |

**For chat-engine-x-api, the AI SDK path is the primary implementation target.**

---

## 1. AI SDK Path (Primary) — Full Contract

### 1.1 Request Contract

- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body shape**:

```typescript
{
  messages: UIMessage[];        // Full conversation history
  system?: string;              // Optional system prompt (forwarded from frontend)
  tools?: Record<string, {      // Optional frontend tool definitions (JSON Schema)
    description?: string;
    parameters: JSONSchema7;
  }>;
}
```

**Field details:**

| Field | Type | Description |
|---|---|---|
| `messages` | `UIMessage[]` | Full conversation history. The frontend sends the **entire thread** on every request — there is no delta/incremental protocol. |
| `system` | `string \| undefined` | System prompt, forwarded automatically by `AssistantChatTransport` from the frontend's `useAssistantInstructions` hook. |
| `tools` | `Record<string, ToolSchema> \| undefined` | Serialized frontend tool definitions. See [ASSISTANT_UI_TOOLS.md](./ASSISTANT_UI_TOOLS.md) for the forwarding flow. |

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 49-51), `docs/api-reference/integrations/vercel-ai-sdk.mdx` (lines 204-213)

### 1.2 UIMessage Type

`UIMessage` is imported from the `ai` package (`ai@^6`):

```typescript
import type { UIMessage } from "ai";
```

**Structure:**

```typescript
interface UIMessage {
  id: string;
  role: "user" | "assistant" | "system";
  parts: MessagePart[];
}
```

**MessagePart** is a union of:

```typescript
// Text content
type TextPart = {
  type: "text";
  text: string;
};

// LLM requesting a tool call
type ToolCallPart = {
  type: "tool-call";
  toolCallId: string;
  toolName: string;
  args: unknown;        // Parsed JSON arguments matching the tool's schema
};

// Result of a tool execution (from a prior turn)
type ToolResultPart = {
  type: "tool-result";
  toolCallId: string;
  toolName: string;
  result: unknown;      // The return value of the tool's execute function
};
```

**Key points:**
- In v6, `UIMessage` uses a `parts` array, NOT a flat `content: string`. This is a breaking change from v5's `Message` type.
- A single assistant message can contain multiple parts (e.g., text + tool-call + more text).
- Tool results from frontend tool executions arrive as `tool-result` parts in subsequent messages — they are NOT sent as separate requests.

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 44-50)

### 1.3 Message Conversion

Your backend receives `UIMessage[]` but the LLM needs `LanguageModelV2Message[]`. Use `convertToModelMessages`:

```typescript
import { streamText, convertToModelMessages } from "ai";
import type { UIMessage } from "ai";

export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json();

  const result = streamText({
    model: openai("gpt-4o"),
    messages: await convertToModelMessages(messages),  // MUST await in v6
  });

  return result.toUIMessageStreamResponse();
}
```

**CRITICAL GOTCHA**: `convertToModelMessages` is **async** in AI SDK v6. It was sync in v5. If you forget `await`, you'll pass a Promise instead of messages and get silent failures.

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (line 54, lines 157-164)

### 1.4 Response Contract — SSE Stream

`streamText().toUIMessageStreamResponse()` returns a `Response` object that streams Server-Sent Events back to the frontend runtime.

**Complete backend handler:**

```typescript
import { openai } from "@ai-sdk/openai";
import { streamText, convertToModelMessages, tool, zodSchema } from "ai";
import type { UIMessage } from "ai";
import { frontendTools } from "@assistant-ui/react-ai-sdk";
import { z } from "zod";

export async function POST(req: Request) {
  const {
    messages,
    system,
    tools,
  }: {
    messages: UIMessage[];
    system?: string;
    tools?: any;
  } = await req.json();

  const result = streamText({
    model: openai("gpt-4o"),
    system,
    messages: await convertToModelMessages(messages),
    tools: {
      ...frontendTools(tools),      // Client-defined tools (no server-side execute)
      get_current_weather: tool({   // Server-defined tool
        description: "Get the current weather",
        inputSchema: zodSchema(
          z.object({ city: z.string() }),
        ),
        execute: async ({ city }) => {
          return `The weather in ${city} is sunny`;
        },
      }),
    },
  });

  return result.toUIMessageStreamResponse();
}
```

**Attaching metadata (usage, model ID):**

```typescript
return result.toUIMessageStreamResponse({
  messageMetadata: ({ part }) => {
    if (part.type === "finish") {
      return { usage: part.totalUsage };
    }
    if (part.type === "finish-step") {
      return { modelId: part.response.modelId };
    }
    return undefined;
  },
});
```

This metadata is consumed by the frontend for token usage display and, if using Assistant Cloud, for telemetry reporting.

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 37-71, 110-135), `docs/cloud/ai-sdk.mdx` (lines 224-252)

### 1.5 Custom API URL Configuration (Frontend Side)

For reference, this is how the frontend points at your service. You don't implement this, but understanding it helps debug integration issues:

```typescript
import { useChatRuntime, AssistantChatTransport } from "@assistant-ui/react-ai-sdk";

const runtime = useChatRuntime({
  transport: new AssistantChatTransport({
    api: "https://chat-engine-x.example.com/v1/chat",  // Your endpoint
    headers: { "Authorization": "Bearer ..." },          // Static headers
    credentials: "include",                               // Cookie forwarding
  }),
});
```

`AssistantChatTransport` accepts:
- `api` (string): Your API endpoint URL
- `headers` (Record<string, string> | Headers): Request headers
- `credentials` (RequestCredentials): Fetch credentials mode

> **Source**: `docs/api-reference/integrations/vercel-ai-sdk.mdx` (lines 163-208)

---

## 2. Data Stream Path (Alternative) — Full Contract

Use this path when you want a framework-agnostic backend that doesn't depend on the AI SDK's `streamText`.

### 2.1 Request Contract

- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body shape**:

```typescript
{
  messages: ThreadMessage[];     // Conversation history
  tools?: Record<string, {       // Tool definitions (JSON Schema)
    description?: string;
    parameters: JSONSchema7;
  }>;
  system?: string;               // System prompt
  threadId?: string;             // Current thread/conversation ID
}
```

The frontend connects via `useDataStreamRuntime`:

```typescript
import { useDataStreamRuntime } from "@assistant-ui/react-data-stream";

const runtime = useDataStreamRuntime({
  api: "https://chat-engine-x.example.com/v1/chat",
  headers: async () => ({
    "Authorization": `Bearer ${await getAuthToken()}`,
  }),
  body: async () => ({
    requestId: crypto.randomUUID(),
  }),
});
```

### 2.2 Response Contract

Use `createAssistantStreamResponse` from the `assistant-stream` package:

```typescript
import { createAssistantStreamResponse } from "assistant-stream";

export async function POST(request: Request) {
  const { messages, tools, system, threadId } = await request.json();

  return createAssistantStreamResponse(async (controller) => {
    // Process with your AI provider
    const stream = await processWithAI({ messages, tools, system });

    for await (const chunk of stream) {
      controller.appendText(chunk.text);
    }
  });
}
```

**Controller API:**
- `controller.appendText(text)` — Stream text incrementally

**Protocol options**: The frontend can specify `protocol: "ui-message-stream"` (default) or `protocol: "data-stream"` (legacy AI SDK compatibility).

**Limitation**: Human-in-the-loop tools (tool interrupts requiring user approval) are NOT supported in the data stream runtime. Use `LocalRuntime` or Assistant Cloud for those workflows.

> **Source**: `docs/runtimes/data-stream.mdx` (lines 61-78, 157-164), `docs/api-reference/integrations/react-data-stream.mdx` (lines 31-89)

---

## 3. Framework-Agnostic Message Conversion Utilities

These utilities help you convert messages between assistant-ui's internal format and whatever your LLM provider expects.

### `toGenericMessages` (Recommended for custom backends)

From the `assistant-stream` package. Converts thread messages to a framework-agnostic format:

```typescript
import { toGenericMessages } from "assistant-stream";

const genericMessages = toGenericMessages(messages);
```

Returns an array of `GenericMessage`:

```typescript
type GenericMessage =
  | { role: "system"; content: string }
  | { role: "user"; content: (GenericTextPart | GenericFilePart)[] }
  | { role: "assistant"; content: (GenericTextPart | GenericToolCallPart)[] }
  | { role: "tool"; content: GenericToolResultPart[] };
```

Use this when building a backend that isn't tied to the AI SDK. You can convert `GenericMessage` to whatever format your LLM provider expects (Anthropic, Google, etc.).

### `toLanguageModelMessages` (AI SDK specific)

From `@assistant-ui/react-data-stream`. Wraps `toGenericMessages` with AI SDK-specific transformations:

```typescript
import { toLanguageModelMessages } from "@assistant-ui/react-data-stream";

const languageModelMessages = toLanguageModelMessages(messages, {
  unstable_includeId: true,  // Include message IDs
});
```

For new custom integrations, prefer `toGenericMessages` directly — `toLanguageModelMessages` adds AI SDK-specific transforms you may not need.

### `toToolsJSONSchema` (Tool serialization)

From the `assistant-stream` package. Serializes tool definitions to JSON Schema:

```typescript
import { toToolsJSONSchema } from "assistant-stream";

const toolSchemas = toToolsJSONSchema(tools);
// Returns: Record<string, { description?: string; parameters: JSONSchema7 }>
```

By default, filters out disabled tools and backend-only tools. Override with:

```typescript
const allTools = toToolsJSONSchema(tools, { filter: () => true });
```

> **Source**: `docs/api-reference/integrations/react-data-stream.mdx` (lines 222-261), `docs/runtimes/data-stream.mdx` (lines 228-254)

---

## 4. Assistant Transport Path (Brief Overview)

For awareness. Use this when building a custom agent that streams arbitrary JSON state rather than a fixed message format.

**Request shape:**

```typescript
{
  state: T;                              // Previous state the frontend has
  commands: AssistantTransportCommand[];  // User actions (add-message, add-tool-result, custom)
  system?: string;
  tools?: Record<string, ToolJSONSchema>;
  threadId: string | null;
  parentId?: string | null;
}
```

**Standard commands:**
- `add-message` — User sent a message
- `add-tool-result` — Tool execution completed
- Custom commands via module augmentation

**Response wire format** (inspired by AI SDK's data stream protocol):

```
aui-state:[{"type":"set","path":["status"],"value":"completed"}]
aui-state:[{"type":"append-text","path":["message"],"value":" World"}]
3:"error message"
```

Two operations: `set` (replace value at path) and `append-text` (append to string at path).

**Python backend example:**

```python
from assistant_stream import RunController, create_run
from assistant_stream.serialization import DataStreamResponse

async def run_callback(controller: RunController):
    controller.state["message"] = "Hello"
    controller.state["message"] += " World"  # Emits append-text

stream = create_run(run_callback, state=request.state)
return DataStreamResponse(stream)
```

The `assistant-stream` package is available on both npm and PyPI.

> **Source**: `docs/runtimes/assistant-transport.mdx`

---

## 5. AI SDK v5 vs v6 Gotchas

If you encounter code examples or existing implementations using v5, here's what changed:

| Feature | v5 (`ai@^5`) | v6 (`ai@^6`) |
|---|---|---|
| **Message type** | `Message` | `UIMessage` |
| **Message structure** | `content: string` | `parts: MessagePart[]` |
| **`convertToModelMessages`** | Sync | **Async** (`await` required) |
| **Tool schema** | `parameters: z.object({...})` | `inputSchema: zodSchema(z.object({...}))` |
| **Response method** | `toDataStreamResponse()` | `toUIMessageStreamResponse()` |
| **`@ai-sdk/react`** | `@ai-sdk/react@^2` | `@ai-sdk/react@^3` |
| **`@assistant-ui/react-ai-sdk`** | `@0.x` | `@latest` |

**v5 is no longer supported. Build on v6.**

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 157-164), `docs/runtimes/ai-sdk/v5-legacy.mdx`

---

## 6. CORS and Authentication

When `chat-engine-x-api` runs on a different origin from the frontend:

- **CORS**: Your API must handle preflight `OPTIONS` requests and return appropriate `Access-Control-Allow-Origin`, `Access-Control-Allow-Headers`, and `Access-Control-Allow-Credentials` headers.

- **Headers**: The frontend can send static or dynamic headers:
  ```typescript
  // Static
  new AssistantChatTransport({
    api: "https://chat-engine-x.example.com/v1/chat",
    headers: { "Authorization": "Bearer static-token" },
  });

  // Dynamic (evaluated per request)
  useDataStreamRuntime({
    api: "https://chat-engine-x.example.com/v1/chat",
    headers: async () => ({
      "Authorization": `Bearer ${await getAuthToken()}`,
    }),
  });
  ```

- **Credentials**: If `credentials: "include"` is set, cookies are forwarded. Your API must explicitly allow credentials in CORS headers.

> **Source**: `docs/runtimes/data-stream.mdx` (lines 96-118), `docs/api-reference/integrations/vercel-ai-sdk.mdx` (lines 190-207)

---

## 7. Error Handling

The frontend runtime handles errors as follows:

| Scenario | Frontend Behavior |
|---|---|
| Network errors | Retried with exponential backoff |
| Stream interruptions | Partial content preserved, error state shown |
| Tool execution errors | Displayed in UI with error states |
| Cancellation | Clean abort signal sent; partial content preserved |

Your backend should:
- Return appropriate HTTP status codes (4xx for client errors, 5xx for server errors)
- Stream errors within the response when possible (the frontend renders them inline)
- Respect the `AbortSignal` — when the frontend cancels a request, stop LLM processing to save costs

---

## See Also

- [ASSISTANT_UI_ARCHITECTURE.md](./ASSISTANT_UI_ARCHITECTURE.md) — System overview, where your service fits
- [ASSISTANT_UI_TOOLS.md](./ASSISTANT_UI_TOOLS.md) — Tool definition patterns, frontend tool forwarding, execution lifecycle

### Source Reference Files

| Source File | Topic |
|---|---|
| `docs/runtimes/ai-sdk/v6.mdx` | AI SDK v6 backend handler, UIMessage, convertToModelMessages, v5→v6 migration |
| `docs/api-reference/integrations/vercel-ai-sdk.mdx` | AssistantChatTransport API, frontendTools(), useChatRuntime |
| `docs/runtimes/data-stream.mdx` | Data stream protocol, createAssistantStreamResponse, message conversion |
| `docs/api-reference/integrations/react-data-stream.mdx` | useDataStreamRuntime API, toLanguageModelMessages, toGenericMessages, toToolsJSONSchema |
| `docs/runtimes/assistant-transport.mdx` | Assistant Transport protocol, state streaming, command handling, Python backend |
| `docs/cloud/ai-sdk.mdx` | messageMetadata for telemetry, useCloudChat |
| `docs/runtimes/ai-sdk/v5-legacy.mdx` | v5 reference (for migration context) |
