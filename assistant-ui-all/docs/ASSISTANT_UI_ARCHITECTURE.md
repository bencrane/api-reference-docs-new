# assistant-ui Architecture Reference for Backend Engineers

assistant-ui is a React frontend framework for AI chat applications. It has three architectural layers: **frontend components**, a **runtime**, and an optional **cloud persistence service**. When building `chat-engine-x-api`, you are replacing the backend API box — your service receives HTTP requests from the runtime and streams LLM responses back. This document explains each layer so you know exactly what your service touches and what it does not.

---

## The Three Pillars

### 1. Frontend Components (not your concern)

Pre-built React chat components (`<Thread />`, `<ThreadList />`, `<Composer />`, etc.) that render messages, tool calls, and streaming state. In our system, these live in `chat-package` and use assistant-ui primitives from `@assistant-ui/react`.

You will never touch these. They render messages that your API streams back.

> **Deep dive**: `docs/primitives/message.mdx`, `docs/ui/thread.mdx`

### 2. Runtime (the bridge between frontend and your API)

The runtime is a React state management layer that sits between the UI components and your backend HTTP endpoint. It:

1. Serializes the conversation (messages, system prompt, tool definitions) into a POST request body
2. Sends the POST to your API endpoint
3. Consumes the SSE stream you return and updates the UI in real time

There are three runtime options relevant to `chat-engine-x-api`:

| Runtime Hook | Package | Wire Format | When to Use |
|---|---|---|---|
| `useChatRuntime` + `AssistantChatTransport` | `@assistant-ui/react-ai-sdk` | AI SDK UIMessage stream | **Primary path.** Standard chat with Vercel AI SDK on the backend. |
| `useDataStreamRuntime` | `@assistant-ui/react-data-stream` | `assistant-stream` data stream | Alternative when you want a framework-agnostic backend (not tied to AI SDK). |
| `useAssistantTransportRuntime` | `@assistant-ui/react` | `aui-state:` operations | Advanced. For custom agents that stream arbitrary JSON state. |

**The key configuration point**: the frontend tells the runtime where your API lives via `AssistantChatTransport`:

```typescript
import { useChatRuntime, AssistantChatTransport } from "@assistant-ui/react-ai-sdk";

const runtime = useChatRuntime({
  transport: new AssistantChatTransport({
    api: "https://chat-engine-x.example.com/v1/chat",
    headers: { "Authorization": "Bearer ..." },
    credentials: "include",
  }),
});
```

This is how frontends point at `chat-engine-x` instead of a local `/api/chat` route.

> **Deep dive**: `docs/runtimes/pick-a-runtime.mdx`, `docs/runtimes/ai-sdk/v6.mdx`

### 3. Assistant Cloud (optional persistence layer)

Assistant Cloud is a hosted service for thread management and message history. It is **purely a persistence layer**.

**What it does:**
- Thread CRUD (create, read, update, delete, archive, rename)
- Automatic message persistence as conversations progress
- Auto-generated thread titles after the first response
- User authorization (scopes threads per user/workspace)
- Thread list management

**What it does NOT do:**
- Make LLM calls
- Execute tools
- Hold system prompts
- Route requests to your backend

`chat-engine-x-api` does NOT depend on Assistant Cloud. Cloud is an orthogonal add-on that the frontend team can independently choose to use for persistence. Your service handles LLM orchestration; Cloud handles storage.

> **Deep dive**: `docs/cloud/index.mdx`, `docs/cloud/ai-sdk.mdx`, `docs/cloud/authorization.mdx`

---

## Where chat-engine-x-api Sits

```
┌──────────────┐     ┌──────────────┐     ┌────────────────────┐     ┌──────────────┐
│              │     │              │     │                    │     │              │
│ chat-package │────>│   Runtime    │────>│ chat-engine-x-api  │────>│ LLM Provider │
│   (React)    │<────│  (React ctx) │<────│   (your service)   │<────│  (OpenAI etc)│
│              │     │              │     │                    │     │              │
└──────────────┘     └──────────────┘     └────────────────────┘     └──────────────┘
  @assistant-ui/       @assistant-ui/        POST + SSE stream         @ai-sdk/openai
  react                react-ai-sdk                                    or any provider

                       Optional:
                    ┌──────────────┐
                    │   Assistant  │
                    │    Cloud     │  (thread persistence only)
                    └──────────────┘
```

---

## What chat-engine-x-api Is Responsible For

- Accepting POST requests from the runtime at your configured endpoint
- Deserializing `UIMessage[]` (AI SDK path) or `GenericMessage[]` (data stream path) into LLM-provider-native format
- Applying the system prompt
- Merging frontend-forwarded tools with server-side tools
- Calling the LLM provider
- Executing backend tools when the LLM invokes them
- Streaming responses back as SSE using `toUIMessageStreamResponse()` (AI SDK) or `createAssistantStreamResponse()` (data stream)
- Handling CORS for cross-origin frontend requests

## What chat-engine-x-api Is NOT Responsible For

- Rendering UI (that's `chat-package`)
- Managing React state (that's the runtime)
- Thread persistence or message history (that's Assistant Cloud or your own DB)
- Frontend tool execution (those run in the browser; you just pass the schema to the LLM)
- System prompt authoring on the frontend (the runtime forwards it, you consume it)

---

## Package Inventory

Every npm package a backend engineer building `chat-engine-x-api` may encounter:

| Package | Layer | Backend Relevance |
|---|---|---|
| `ai@^6` | **Backend** | Core. Provides `streamText`, `convertToModelMessages`, `tool`, `zodSchema`, `UIMessage` type |
| `@assistant-ui/react-ai-sdk` | Frontend (but exports backend helper) | `frontendTools()` function — used in your backend route to merge frontend tool definitions |
| `assistant-stream` | **Backend** | Framework-agnostic. `createAssistantStreamResponse`, `toGenericMessages`, `toToolsJSONSchema` |
| `@assistant-ui/react-data-stream` | Frontend (but exports conversion utils) | `toLanguageModelMessages` (wraps `toGenericMessages` with AI SDK transforms) |
| `@ai-sdk/openai` (or other providers) | **Backend** | LLM provider adapters for the AI SDK |
| `zod` | **Backend** | Schema definitions for tool parameters |
| `@assistant-ui/react` | Frontend only | UI components and runtime provider. Not used in your backend. |
| `assistant-cloud` | Frontend only | Cloud client for thread persistence. Not used in your backend. |

---

## See Also

- [ASSISTANT_UI_PROTOCOL.md](./ASSISTANT_UI_PROTOCOL.md) — Exact HTTP request/response contracts, message types, SSE stream format
- [ASSISTANT_UI_TOOLS.md](./ASSISTANT_UI_TOOLS.md) — Tool definition patterns, frontend tool forwarding, execution lifecycle

### Source Reference Files

| Source File | Topic |
|---|---|
| `docs/architecture.mdx` | Three pillars overview, architecture diagrams |
| `docs/runtimes/pick-a-runtime.mdx` | Runtime comparison and selection guide |
| `docs/runtimes/ai-sdk/v6.mdx` | AI SDK v6 integration (primary path) |
| `docs/runtimes/data-stream.mdx` | Data stream protocol (alternative path) |
| `docs/runtimes/assistant-transport.mdx` | Custom agent state streaming (advanced) |
| `docs/cloud/index.mdx` | Assistant Cloud overview |
| `docs/cloud/ai-sdk.mdx` | Cloud persistence with AI SDK |
| `docs/cloud/authorization.mdx` | Cloud authentication patterns |
| `docs/api-reference/integrations/vercel-ai-sdk.mdx` | AssistantChatTransport, frontendTools API reference |
| `docs/api-reference/integrations/react-data-stream.mdx` | Data stream API reference, conversion utilities |
