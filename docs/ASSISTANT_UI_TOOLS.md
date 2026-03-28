# assistant-ui Tools Reference: Tool Contracts for chat-engine-x-api

Tools are functions that the LLM can call to perform actions. In the assistant-ui ecosystem, tools can be defined on the frontend, the backend, or both. This document covers every tool-related contract your backend needs to handle: how to define backend tools, how frontend tools arrive at your API, how they merge, and how tool calls flow through the SSE stream.

---

## 1. Tool Taxonomy

Three types of tools exist in assistant-ui. Only one type executes on your backend:

| Type | Where Defined | Where Executed | Backend Responsibility |
|---|---|---|---|
| **Backend tool** | Server-side (`tool()` from `ai`) | Server-side | Define, register with LLM, execute, stream result |
| **Frontend tool** | Client-side (`Tools()` API / `Toolkit`) | Browser | Receive serialized schema, pass to LLM, stream the tool-call back (do NOT execute) |
| **Human tool** | Client-side (variant of frontend) | Browser (with user approval) | Same as frontend — pass through, do not execute |

**ToolDefinition type** (frontend-side, for reference):

```typescript
type ToolDefinition =
  | {
      type?: "frontend";             // Executes in the browser
      description?: string;
      parameters: StandardSchemaV1 | JSONSchema7;
      execute: (args, context) => Promise<any>;
      render?: (props) => React.ReactNode;
    }
  | {
      type: "human";                 // Pauses for user input
      description?: string;
      parameters: StandardSchemaV1 | JSONSchema7;
      render: (props) => React.ReactNode;  // Required
    }
  | {
      type: "backend";              // Server-side execution (no execute/parameters needed on frontend)
      render?: (props) => React.ReactNode;
    };
```

> **Source**: `docs/guides/tools.mdx` (lines 94-116)

---

## 2. Backend Tool Definition (AI SDK v6)

### 2.1 The `tool()` Pattern

Backend tools use `tool()` from the `ai` package with `zodSchema()` for parameter validation:

```typescript
import { tool, zodSchema } from "ai";
import { z } from "zod";

const get_current_weather = tool({
  description: "Get the current weather for a city",
  inputSchema: zodSchema(
    z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["celsius", "fahrenheit"]).optional(),
    }),
  ),
  execute: async ({ city, unit }) => {
    const weather = await fetchWeatherAPI(city);
    return { temperature: weather.temp, unit: unit ?? "celsius", conditions: weather.conditions };
  },
});
```

**CRITICAL v6 GOTCHA**: The property is `inputSchema: zodSchema(z.object({...}))`, NOT `parameters: z.object({...})`. The v5 `parameters` form will silently fail in v6 — the LLM won't see the tool at all.

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 56-67)

### 2.2 Registering Backend Tools with `streamText`

Pass tools as a record to `streamText`:

```typescript
import { openai } from "@ai-sdk/openai";
import { streamText, convertToModelMessages, tool, zodSchema } from "ai";
import type { UIMessage } from "ai";
import { z } from "zod";

export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json();

  const result = streamText({
    model: openai("gpt-4o"),
    messages: await convertToModelMessages(messages),
    tools: {
      get_current_weather: tool({
        description: "Get the current weather",
        inputSchema: zodSchema(z.object({ city: z.string() })),
        execute: async ({ city }) => `The weather in ${city} is sunny`,
      }),
      query_database: tool({
        description: "Query the application database",
        inputSchema: zodSchema(z.object({
          query: z.string(),
          table: z.string(),
        })),
        execute: async ({ query, table }) => {
          return await db.query(query, { table });
        },
      }),
    },
  });

  return result.toUIMessageStreamResponse();
}
```

> **Source**: `docs/runtimes/ai-sdk/v6.mdx` (lines 52-71), `docs/guides/tools.mdx` (lines 394-422)

---

## 3. Frontend Tool Forwarding — The `frontendTools()` Flow

### 3.1 How Frontend Tools Arrive at Your Backend

1. The frontend defines tools using the `Tools()` API with a `Toolkit` object (React-side, not your code)
2. `AssistantChatTransport` automatically serializes these tool definitions and includes them in the POST body as the `tools` field
3. The `tools` field arrives as `Record<string, { description?: string; parameters: JSONSchema7 }>` — **JSON Schema format**, not Zod

You don't need to do anything to trigger this — `AssistantChatTransport` handles it automatically.

### 3.2 The `frontendTools()` Helper

Import from `@assistant-ui/react-ai-sdk` and use on your backend to convert the raw `tools` object from the request into AI SDK-compatible tool definitions:

```typescript
import { frontendTools } from "@assistant-ui/react-ai-sdk";
```

These converted tools will NOT have an `execute` function — they only provide schemas so the LLM can decide to call them. The actual execution happens in the browser.

### 3.3 The Canonical Merge Pattern

This is the standard pattern for a backend route that supports both server tools and frontend tools:

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
      ...frontendTools(tools),          // Client-defined tools (no execute)
      // Server-defined tools below:
      query_database: tool({
        description: "Query the database",
        inputSchema: zodSchema(z.object({ query: z.string() })),
        execute: async ({ query }) => await db.query(query),
      }),
    },
  });

  return result.toUIMessageStreamResponse();
}
```

> **Source**: `docs/api-reference/integrations/vercel-ai-sdk.mdx` (lines 210-254), `docs/guides/tools.mdx` (lines 425-481)

### 3.4 What Happens When the LLM Calls a Frontend Tool

1. The LLM emits a tool call for a frontend-defined tool (e.g., `calculate`)
2. Because the tool has no `execute` function on the server, the AI SDK streams the tool-call event to the frontend
3. The frontend runtime intercepts it, runs the client-side `execute` function in the browser
4. The result is included in the **next request's** `messages` array as a `tool-result` part
5. Your backend sees the result and can pass it to the LLM for the next turn

**Your backend does NOT execute frontend tools** — just pass the schema to the LLM and let the tool call flow back through the stream.

---

## 4. Data Stream Path Tool Handling

When using the data stream protocol instead of the AI SDK path:

### Frontend → Backend

The frontend uses `toToolsJSONSchema` from `assistant-stream` to serialize tools:

```typescript
import { toToolsJSONSchema } from "assistant-stream";

const runtime = useDataStreamRuntime({
  api: "/api/chat",
  body: {
    tools: toToolsJSONSchema(myTools),
  },
});
```

`toToolsJSONSchema` returns `Record<string, { description?: string; parameters: JSONSchema7 }>`.

By default, it filters out disabled and backend-only tools. Override with `{ filter: () => true }`.

### Backend Processing

Your backend receives the `tools` field as JSON Schema. Parse and pass to your LLM provider's tool API:

```typescript
const { messages, tools, system, threadId } = await request.json();
// `tools` is already JSON Schema format — pass to your LLM provider
```

**Limitation**: Human-in-the-loop tools (`unstable_humanToolNames`) are NOT supported in the data stream runtime. Use `LocalRuntime` for those workflows.

> **Source**: `docs/runtimes/data-stream.mdx` (lines 157-209), `docs/api-reference/integrations/react-data-stream.mdx` (lines 244-261)

---

## 5. MCP (Model Context Protocol) Tools

MCP is a protocol for connecting to external tool servers. These are server-side tools that your backend manages directly — they do NOT go through the frontend tool forwarding flow.

```typescript
import { experimental_createMCPClient, streamText } from "ai";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

export async function POST(req: Request) {
  const { messages } = await req.json();

  const client = await experimental_createMCPClient({
    transport: new StdioClientTransport({
      command: "npx",
      args: ["@modelcontextprotocol/server-github"],
    }),
  });

  try {
    const mcpTools = await client.tools();

    const result = streamText({
      model: openai("gpt-4o"),
      tools: mcpTools,
      messages: await convertToModelMessages(messages),
    });

    return result.toUIMessageStreamResponse();
  } finally {
    await client.close();
  }
}
```

MCP tools can be merged with backend tools and frontend tools in the same `tools` object.

> **Source**: `docs/guides/tools.mdx` (lines 483-513)

---

## 6. Tool Execution Lifecycle

End-to-end sequence showing how both backend and frontend tools flow through the system:

```
Frontend (chat-package)         chat-engine-x-api              LLM Provider
        |                              |                           |
        |-- POST {messages, tools} --> |                           |
        |                              |-- streamText(tools) ----> |
        |                              |                           |
        |                              |    LLM decides to call    |
        |                              |    a BACKEND tool         |
        |                              | <-- tool-call: weather -- |
        |                              |                           |
        |                              |   execute() runs on       |
        |                              |   your server             |
        |                              | -- tool-result: 72F ----> |
        |                              |                           |
        |                              |    LLM decides to call    |
        |                              |    a FRONTEND tool        |
        |                              | <-- tool-call: calculate  |
        |                              |                           |
        | <-- SSE: tool-call event --- |   (no execute on server)  |
        |                              |                           |
        |   Browser executes the       |                           |
        |   tool locally               |                           |
        |                              |                           |
        |-- Next POST with result ---> |                           |
        |   (tool-result in messages)  |-- continue streamText --> |
        |                              |                           |
        |                              | <-- final text response - |
        | <-- SSE: text chunks ------- |                           |
        |                              |                           |
```

**Key observations:**
- Backend tools are executed server-side within the same `streamText` call — results feed back to the LLM immediately
- Frontend tools cause the stream to include the tool-call, and the frontend handles execution — the result comes back in the next HTTP request
- The LLM can call multiple tools in a single turn (both backend and frontend)

---

## 7. Capability Module Pattern (chat-engine-x-api Design Decision)

This is a design pattern for `chat-engine-x-api`, not an assistant-ui requirement. Tools are grouped into **capability modules** based on domain:

```
src/capabilities/
  list-building/
    tools.ts          -- tool definitions (tool() + zodSchema())
    handlers.ts       -- execute functions, business logic
    system-prompt.ts  -- module-specific system prompt sections
  creative-generation/
    tools.ts
    handlers.ts
    system-prompt.ts
  campaign-orchestration/
    tools.ts
    handlers.ts
    system-prompt.ts
  index.ts            -- aggregates all modules
```

Each module exports a `Record<string, Tool>` that gets spread into the `tools` object:

```typescript
// src/capabilities/index.ts
import { listBuildingTools } from "./list-building/tools";
import { creativeTools } from "./creative-generation/tools";
import { campaignTools } from "./campaign-orchestration/tools";

export function getToolsForPlatform(platformConfig: PlatformConfig) {
  const tools: Record<string, Tool> = {};

  if (platformConfig.capabilities.includes("list-building")) {
    Object.assign(tools, listBuildingTools);
  }
  if (platformConfig.capabilities.includes("creative-generation")) {
    Object.assign(tools, creativeTools);
  }
  if (platformConfig.capabilities.includes("campaign-orchestration")) {
    Object.assign(tools, campaignTools);
  }

  return tools;
}

// In your route handler:
const result = streamText({
  model: openai("gpt-4o"),
  tools: {
    ...frontendTools(tools),
    ...getToolsForPlatform(platformConfig),
  },
});
```

The platform config determines which modules are loaded per tenant/request. Each module brings its own tools and system prompt sections.

---

## 8. Tool Schema Reference Table

How tool schemas look at each layer:

| Property | AI SDK v6 (Backend) | Frontend (Toolkit) | JSON Schema (Wire Format) |
|---|---|---|---|
| **Schema** | `inputSchema: zodSchema(z.object({...}))` | `parameters: z.object({...})` | `parameters: JSONSchema7` |
| **Description** | `description: string` | `description: string` | `description: string` |
| **Execute** | `execute: async (args) => result` | `execute: async (args, ctx) => result` | N/A (not serialized) |
| **Package** | `ai` | `@assistant-ui/react` | `assistant-stream` |

---

## 9. Gotchas and Common Mistakes

1. **v6 uses `inputSchema`, not `parameters`**: `tool({ inputSchema: zodSchema(z.object({...})) })` is correct. Using `parameters: z.object({...})` silently fails — the LLM never sees the tool.

2. **`frontendTools(tools)` handles `undefined`**: If no frontend tools are defined, `tools` in the request body will be `undefined`. The spread `...frontendTools(undefined)` is safe — it returns an empty object.

3. **Tool name collisions**: If both frontend and backend define a tool with the same name, the **last one in the spread wins**. In the canonical pattern (`...frontendTools(tools), myBackendTool: ...`), backend tools override frontend tools with the same name.

4. **Tool results arrive as message parts**: Frontend tool results come back in the next request's `messages` array as `tool-result` parts on a `tool` or `assistant` role message — they are NOT sent as separate HTTP requests or in a special field.

5. **`zodSchema()` wrapper is required in v6**: Plain `z.object({...})` won't work with `inputSchema`. You must wrap it: `inputSchema: zodSchema(z.object({...}))`.

6. **MCP tools are server-managed**: MCP tools go directly into your `tools` object. They don't flow through the frontend forwarding path.

---

## See Also

- [ASSISTANT_UI_ARCHITECTURE.md](./ASSISTANT_UI_ARCHITECTURE.md) — System overview, where your service fits
- [ASSISTANT_UI_PROTOCOL.md](./ASSISTANT_UI_PROTOCOL.md) — HTTP request/response contracts, message types, SSE stream format

### Source Reference Files

| Source File | Topic |
|---|---|
| `docs/guides/tools.mdx` | Tool taxonomy, Tools() API, Toolkit, frontendTools flow, MCP integration |
| `docs/runtimes/ai-sdk/v6.mdx` | AI SDK v6 tool definition pattern, backend handler example |
| `docs/api-reference/integrations/vercel-ai-sdk.mdx` | frontendTools() API reference, AssistantChatTransport |
| `docs/runtimes/data-stream.mdx` | Data stream tool handling, toToolsJSONSchema |
| `docs/api-reference/integrations/react-data-stream.mdx` | toToolsJSONSchema API, toGenericMessages |
| `docs/guides/tool-ui.mdx` | Generative UI for tools (frontend reference) |
