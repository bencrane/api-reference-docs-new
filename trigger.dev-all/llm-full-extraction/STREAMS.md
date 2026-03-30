> Sources:
> - https://trigger.dev/docs/tasks/streams
> - https://trigger.dev/docs/realtime/backend/streams
> - https://trigger.dev/docs/realtime/react-hooks/streams

# Streams

## Streaming data from tasks

Pipe continuous data from your Trigger.dev tasks to frontend or backend clients in real time. Stream AI completions, file chunks, progress updates, and more.

**Streams let you pipe data from a running task to your frontend or backend as it's produced.** Think AI completions token by token, progress updates, or file chunks. You can also **send data into** running tasks with [Input Streams](#input-streams) for bidirectional flows (cancel buttons, approvals).

For subscribing to **run state changes** (status, metadata, tags) instead, see [Realtime](/realtime/overview).

<Note>
  Streams require SDK version **4.1.0 or later** (`@trigger.dev/sdk` and `@trigger.dev/react-hooks`).
  This doc describes the current streams behavior (v2 is the default). For pre-4.1.0 streams, see
  [Pre-4.1.0 streams (legacy)](#pre-410-streams-legacy) below.
</Note>

## Overview

Streams provide:

* **Unlimited stream length** (previously capped at 2000 chunks)
* **Unlimited active streams per run** (previously 5)
* **Improved reliability** with automatic resumption on connection loss
* **28-day stream retention** (previously 1 day)
* **Multiple client streams** can pipe to a single stream
* **Enhanced dashboard visibility** for viewing stream data in real-time

Streams v2 is the **default** when using SDK 4.1.0 or later. If you trigger tasks outside the SDK, set the `x-trigger-realtime-streams-version=v2` header. To opt out, use `auth.configure({ future: { v2RealtimeStreams: false } })` or `TRIGGER_V2_REALTIME_STREAMS=0`.

## Limits Comparison

| Limit                            | Legacy (pre-4.1.0) | Current   |
| -------------------------------- | ------------------ | --------- |
| Maximum stream length            | 2000               | Unlimited |
| Number of active streams per run | 5                  | Unlimited |
| Maximum streams per run          | 10                 | Unlimited |
| Maximum stream TTL               | 1 day              | 28 days   |
| Maximum stream size              | 10MB               | 300 MiB   |

## Quick Start

The recommended workflow for **output** streams (data from task to client):

1. **Define your streams** in a shared location using `streams.define()`
2. **Use the defined stream** in your tasks with `.pipe()`, `.append()`, or `.writer()`
3. **Read from the stream** using `.read()` or the `useRealtimeStream` hook in React

This approach gives you full type safety, better code organization, and easier maintenance as your application grows. For **input** streams (sending data into a running task), see [Input Streams](#input-streams) below.

## Defining Typed Streams (Recommended)

The recommended way to work with streams is to define them once with `streams.define()`. This allows you to specify the chunk type and stream ID in one place, and then reuse that definition throughout your codebase with full type safety.

### Creating a Defined Stream

Define your streams in a shared location (like `app/streams.ts` or `trigger/streams.ts`):

```ts theme={"theme":"css-variables"}
import { streams, InferStreamType } from "@trigger.dev/sdk";

// Define a stream with a specific type
export const aiStream = streams.define<string>({
  id: "ai-output",
});

// Export the type for use in frontend components
export type AIStreamPart = InferStreamType<typeof aiStream>;
```

You can define streams for any JSON-serializable type:

```ts theme={"theme":"css-variables"}
import { streams, InferStreamType } from "@trigger.dev/sdk";
import { UIMessageChunk } from "ai";

// Stream for AI UI message chunks
export const aiStream = streams.define<UIMessageChunk>({
  id: "ai",
});

// Stream for progress updates
export const progressStream = streams.define<{ step: string; percent: number }>({
  id: "progress",
});

// Stream for simple text
export const logStream = streams.define<string>({
  id: "logs",
});

// Export types
export type AIStreamPart = InferStreamType<typeof aiStream>;
export type ProgressStreamPart = InferStreamType<typeof progressStream>;
export type LogStreamPart = InferStreamType<typeof logStream>;
```

### Using Defined Streams in Tasks

Once defined, you can use all stream methods on your defined stream:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { aiStream } from "./streams";

export const streamTask = task({
  id: "stream-task",
  run: async (payload: { prompt: string }) => {
    // Get a stream from an AI service, database, etc.
    const stream = await getAIStream(payload.prompt);

    // Pipe the stream using your defined stream
    const { stream: readableStream, waitUntilComplete } = aiStream.pipe(stream);

    // Option A: Iterate over the stream locally
    for await (const chunk of readableStream) {
      console.log("Received chunk:", chunk);
    }

    // Option B: Wait for the stream to complete
    await waitUntilComplete();

    return { message: "Stream completed" };
  },
});
```

#### Reading from a Stream

Use the defined stream's `read()` method to consume data from anywhere (frontend, backend, or another task):

```ts theme={"theme":"css-variables"}
import { aiStream } from "./streams";

const stream = await aiStream.read(runId);

for await (const chunk of stream) {
  console.log(chunk); // chunk is typed as the stream's chunk type
}
```

With options:

```ts theme={"theme":"css-variables"}
const stream = await aiStream.read(runId, {
  timeoutInSeconds: 60, // Stop if no data for 60 seconds
  startIndex: 10, // Start from the 10th chunk
});
```

#### Appending to a Stream

Use the defined stream's `append()` method to add a single chunk:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { aiStream, progressStream, logStream } from "./streams";

export const appendTask = task({
  id: "append-task",
  run: async (payload) => {
    // Append to different streams with full type safety
    await logStream.append("Processing started");
    await progressStream.append({ step: "Initialization", percent: 0 });

    // Do some work...

    await progressStream.append({ step: "Processing", percent: 50 });
    await logStream.append("Step 1 complete");

    // Do more work...

    await progressStream.append({ step: "Complete", percent: 100 });
    await logStream.append("All steps complete");
  },
});
```

#### Writing Multiple Chunks

Use the defined stream's `writer()` method for more complex stream writing:

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { logStream } from "./streams";

export const writerTask = task({
  id: "writer-task",
  run: async (payload) => {
    const { waitUntilComplete } = logStream.writer({
      execute: ({ write, merge }) => {
        // Write individual chunks
        write("Chunk 1");
        write("Chunk 2");

        // Merge another stream
        const additionalStream = ReadableStream.from(["Chunk 3", "Chunk 4", "Chunk 5"]);
        merge(additionalStream);
      },
    });

    await waitUntilComplete();
  },
});
```

### Using Defined Streams in React

Defined streams work seamlessly with the `useRealtimeStream` hook:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "@/app/streams";

export function StreamViewer({ accessToken, runId }: { accessToken: string; runId: string }) {
  // Pass the defined stream directly - full type safety!
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken,
    timeoutInSeconds: 600,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div>
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

## Direct Stream Methods (Without Defining)

<Warning>
  We strongly recommend using `streams.define()` instead of direct methods. Defined streams provide
  better organization, full type safety, and make it easier to maintain your codebase as it grows.
</Warning>

If you have a specific reason to avoid defined streams, you can use stream methods directly by specifying the stream key each time.

### Direct Piping

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const directStreamTask = task({
  id: "direct-stream",
  run: async (payload: { prompt: string }) => {
    const stream = await getAIStream(payload.prompt);

    // Specify the stream key directly
    const { stream: readableStream, waitUntilComplete } = streams.pipe("ai-output", stream);

    await waitUntilComplete();
  },
});
```

### Direct Reading

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";

// Specify the stream key when reading
const stream = await streams.read(runId, "ai-output");

for await (const chunk of stream) {
  console.log(chunk);
}
```

### Direct Appending

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const directAppendTask = task({
  id: "direct-append",
  run: async (payload) => {
    // Specify the stream key each time
    await streams.append("logs", "Processing started");
    await streams.append("progress", "50%");
    await streams.append("logs", "Complete");
  },
});
```

### Direct Writing

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const directWriterTask = task({
  id: "direct-writer",
  run: async (payload) => {
    const { waitUntilComplete } = streams.writer("output", {
      execute: ({ write, merge }) => {
        write("Chunk 1");
        write("Chunk 2");
      },
    });

    await waitUntilComplete();
  },
});
```

## Default Stream

Every run has a "default" stream, allowing you to skip the stream key entirely. This is useful for simple cases where you only need one stream per run.

Using direct methods:

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const defaultStreamTask = task({
  id: "default-stream",
  run: async (payload) => {
    const stream = getDataStream();

    // No stream key needed - uses "default"
    const { waitUntilComplete } = streams.pipe(stream);

    await waitUntilComplete();
  },
});

// Reading from the default stream
const readStream = await streams.read(runId);
```

## Targeting Different Runs

You can pipe streams to parent, root, or any other run using the `target` option. This works with both defined streams and direct methods.

### With Defined Streams

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { logStream } from "./streams";

export const childTask = task({
  id: "child-task",
  run: async (payload, { ctx }) => {
    const stream = getDataStream();

    // Pipe to parent run
    logStream.pipe(stream, { target: "parent" });

    // Pipe to root run
    logStream.pipe(stream, { target: "root" });

    // Pipe to self (default behavior)
    logStream.pipe(stream, { target: "self" });

    // Pipe to a specific run ID
    logStream.pipe(stream, { target: payload.otherRunId });
  },
});
```

### With Direct Methods

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const childTask = task({
  id: "child-task",
  run: async (payload, { ctx }) => {
    const stream = getDataStream();

    // Pipe to parent run
    streams.pipe("output", stream, { target: "parent" });

    // Pipe to root run
    streams.pipe("output", stream, { target: "root" });

    // Pipe to a specific run ID
    streams.pipe("output", stream, { target: payload.otherRunId });
  },
});
```

## Streaming from Outside a Task

If you specify a `target` run ID, you can pipe streams from anywhere (like a Next.js API route):

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";

export async function POST(req: Request) {
  const { messages, runId } = await req.json();

  const result = streamText({
    model: openai("gpt-4o"),
    messages,
  });

  // Pipe AI stream to a Trigger.dev run
  const { stream } = streams.pipe("ai-stream", result.toUIMessageStream(), {
    target: runId,
  });

  return new Response(stream as any, {
    headers: { "Content-Type": "text/event-stream" },
  });
}
```

## React Hook

Use the `useRealtimeStream` hook to subscribe to streams in your React components.

### With Defined Streams (Recommended)

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "@/app/streams";

export function StreamViewer({ accessToken, runId }: { accessToken: string; runId: string }) {
  // Pass the defined stream directly for full type safety
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken,
    timeoutInSeconds: 600,
    onData: (chunk) => {
      console.log("New chunk:", chunk); // chunk is typed!
    },
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div>
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

### With Direct Stream Keys

If you prefer not to use defined streams, you can specify the stream key directly:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";

export function StreamViewer({ accessToken, runId }: { accessToken: string; runId: string }) {
  const { parts, error } = useRealtimeStream<string>(runId, "ai-output", {
    accessToken,
    timeoutInSeconds: 600,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div>
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

### Using Default Stream

```tsx theme={"theme":"css-variables"}
// Omit stream key to use the default stream
const { parts, error } = useRealtimeStream<string>(runId, {
  accessToken,
});
```

### Hook Options

```tsx theme={"theme":"css-variables"}
const { parts, error } = useRealtimeStream(streamDef, runId, {
  accessToken: "pk_...", // Required: Public access token
  baseURL: "https://api.trigger.dev", // Optional: Custom API URL
  timeoutInSeconds: 60, // Optional: Timeout (default: 60)
  startIndex: 0, // Optional: Start from specific chunk
  throttleInMs: 16, // Optional: Throttle updates (default: 16ms)
  onData: (chunk) => {}, // Optional: Callback for each chunk
});
```

## Input Streams

Input Streams let you send data **into** a running task from your backend or frontend. While output streams (above) send data out of tasks, input streams complete the loop — enabling bidirectional communication.

<Note>
  Input Streams require SDK version **4.4.2 or later** and use the same streams infrastructure (v2 is the default). If you're on an older SDK, calling `.on()` or `.once()` will throw with instructions to enable v2 streams. See [Pre-4.1.0 streams (legacy)](#pre-410-streams-legacy) for the older metadata-based API.
</Note>

### Input Streams overview

Input Streams solve three common problems:

* **Cancelling AI streams mid-generation.** When you use AI SDK's `streamText` inside a task, the LLM keeps generating until it's done — even if the user clicked "Stop." With input streams, your frontend sends a cancel signal and the task aborts the LLM call immediately.
* **Human-in-the-loop workflows.** A task generates a draft, then pauses and waits for the user to approve or edit it before continuing.
* **Interactive agents.** An AI agent running as a task needs follow-up information from the user mid-execution — clarifying a question, choosing between options, or providing additional context.

### Quick Start (Input Streams)

1. **Define** input streams in a shared file with `streams.input<T>({ id: "..." })`.
2. **Receive** in your task with `.wait()`, `.once()`, `.on()`, or `.peek()`.
3. **Send** from your backend with `.send(runId, data)` or from the frontend with the `useInputStreamSend` hook (see [Realtime React hooks](/realtime/react-hooks/streams#useinputstreamsend)).

### Defining Input Streams

Use `streams.input()` to define a typed input stream. The generic parameter controls the shape of data that can be sent:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";

export const cancelSignal = streams.input<{ reason?: string }>({
  id: "cancel",
});

export const approval = streams.input<{ approved: boolean; reviewer: string }>({
  id: "approval",
});

export const userResponse = streams.input<{
  action: "approve" | "reject" | "edit";
  message?: string;
  edits?: Record<string, string>;
}>({
  id: "user-response",
});
```

Type safety is enforced through the generic — both `.send()` and the receiving methods (`.wait()`, `.once()`, `.on()`, `.peek()`) share the same type.

### Receiving data inside a task

| Method         | Task suspended? | Compute cost while waiting | Best for                                                             |
| -------------- | --------------- | -------------------------- | -------------------------------------------------------------------- |
| `.wait()`      | **Yes**         | **None** — process freed   | Approval gates, human-in-the-loop, long waits                        |
| `.once()`      | No              | Full — process stays alive | Short waits, concurrent work; returns result object with `.unwrap()` |
| `.on(handler)` | No              | Full — process stays alive | Continuous listening (cancel signals, live updates)                  |
| `.peek()`      | No              | None                       | Non-blocking check for latest buffered value                         |

#### `wait()` — Suspend until data arrives

Suspends the task entirely, freeing compute resources. The task resumes when data arrives via `.send()`. Returns a [`ManualWaitpointPromise`](/wait-for-token) — the same type as `wait.forToken()`.

```ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { approval } from "./streams";

export const publishPost = task({
  id: "publish-post",
  run: async (payload: { postId: string }) => {
    const draft = await prepareDraft(payload.postId);
    await notifyReviewer(draft);

    const result = await approval.wait({ timeout: "7d" });

    if (result.ok) {
      if (result.output.approved) {
        await publish(draft);
        return { published: true, reviewer: result.output.reviewer };
      }
      return { published: false, reviewer: result.output.reviewer };
    }
    return { published: false, timedOut: true };
  },
});
```

Use `.unwrap()` to throw on timeout: `const data = await approval.wait({ timeout: "24h" }).unwrap();`

**Options:** `timeout` (e.g. `"30s"`, `"5m"`, `"24h"`, `"7d"`), `idempotencyKey`, `idempotencyKeyTTL`, `tags`. Use `idempotencyKey` when your task has retries so the same waitpoint is resumed across retries.

#### `once()` — Wait for the next value (non-suspending)

Blocks until data arrives but keeps the task process alive. Returns a result object; use `.unwrap()` to get the data or throw on timeout.

```ts theme={"theme":"css-variables"}
const result = await approval.once({ timeoutMs: 300_000 });
if (result.ok) {
  console.log(result.output.approved);
}
// Or: const data = await approval.once({ timeoutMs: 300_000 }).unwrap();
```

`once()` also accepts a `signal` (e.g. `AbortController.signal`) for cancellation.

#### `on()` — Listen for every value

Registers a persistent handler that fires on every piece of data. Handlers are automatically cleaned up when the task run completes. Call `.off()` on the returned subscription to stop listening early.

```ts theme={"theme":"css-variables"}
const controller = new AbortController();
cancelSignal.on((data) => {
  console.log("Cancelled:", data.reason);
  controller.abort();
});
const result = streamText({ ..., abortSignal: controller.signal });
```

#### `peek()` — Non-blocking check

Returns the most recent buffered value without waiting, or `undefined` if nothing has been received yet.

```ts theme={"theme":"css-variables"}
const latest = cancelSignal.peek();
if (latest) {
  // A cancel was already sent before we checked
}
```

### Sending data to a running task

Use `.send(runId, data)` from your backend to push data into a running task. See the [backend input streams guide](/realtime/backend/input-streams) for API route patterns.

```ts theme={"theme":"css-variables"}
import { cancelSignal, approval } from "./trigger/streams";

await cancelSignal.send(runId, { reason: "User clicked stop" });
await approval.send(runId, { approved: true, reviewer: "alice@example.com" });
```

### Complete example: Cancellable AI streaming

Stream an AI response while allowing the user to cancel mid-generation.

**Define the streams:**

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";

export const aiOutput = streams.define<string>({ id: "ai" });
export const cancelStream = streams.input<{ reason?: string }>({ id: "cancel" });
```

**Task:** Register `cancelStream.on()` to abort an `AbortController`, then pipe `streamText(...).textStream` to `aiOutput`. **Backend:** POST to an API route that calls `cancelStream.send(runId, { reason: "User clicked stop" })`. **Frontend:** Use `useRealtimeStream(aiOutput, runId, { accessToken })` and a button that calls your cancel API (or use the `useInputStreamSend` hook; see [Realtime React hooks](/realtime/react-hooks/streams#useinputstreamsend)).

**Important notes (input streams):** You cannot send to a completed, failed, or canceled run. Max payload per `.send()` is 1MB. Data sent before a listener is registered is buffered and delivered when a listener attaches; `.wait()` handles the buffering race automatically. Use `.wait()` for long waits to free compute; use `.once()` for short waits or concurrent work. Define input streams in a shared location and combine with output streams for full bidirectional communication.

## Complete Example: AI Streaming

### Define the stream

```ts theme={"theme":"css-variables"}
// app/streams.ts
import { streams, InferStreamType } from "@trigger.dev/sdk";
import { UIMessageChunk } from "ai";

export const aiStream = streams.define<UIMessageChunk>({
  id: "ai",
});

export type AIStreamPart = InferStreamType<typeof aiStream>;
```

### Create the task

```ts theme={"theme":"css-variables"}
// trigger/ai-task.ts
import { task } from "@trigger.dev/sdk";
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";
import { aiStream } from "@/app/streams";

export const generateAI = task({
  id: "generate-ai",
  run: async (payload: { prompt: string }) => {
    const result = streamText({
      model: openai("gpt-4o"),
      prompt: payload.prompt,
    });

    const { waitUntilComplete } = aiStream.pipe(result.toUIMessageStream());

    await waitUntilComplete();

    return { success: true };
  },
});
```

### Frontend component

```tsx theme={"theme":"css-variables"}
// components/ai-stream.tsx
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "@/app/streams";

export function AIStream({ accessToken, runId }: { accessToken: string; runId: string }) {
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken,
    timeoutInSeconds: 300,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div className="prose">
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

## Migration from v1

If you're using the old `metadata.stream()` API, here's how to migrate to the recommended v2 approach:

### Step 1: Define Your Streams

Create a shared streams definition file:

```ts theme={"theme":"css-variables"}
// app/streams.ts or trigger/streams.ts
import { streams, InferStreamType } from "@trigger.dev/sdk";

export const myStream = streams.define<string>({
  id: "my-stream",
});

export type MyStreamPart = InferStreamType<typeof myStream>;
```

### Step 2: Update Your Tasks

Replace `metadata.stream()` with the defined stream's `pipe()` method:

```ts theme={"theme":"css-variables"}
// Before (v1)
import { metadata, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload) => {
    const stream = getDataStream();
    await metadata.stream("my-stream", stream);
  },
});
```

```ts theme={"theme":"css-variables"}
// After (v2 - Recommended)
import { task } from "@trigger.dev/sdk";
import { myStream } from "./streams";

export const myTask = task({
  id: "my-task",
  run: async (payload) => {
    const stream = getDataStream();

    // Don't await - returns immediately
    const { waitUntilComplete } = myStream.pipe(stream);

    // Optionally wait for completion
    await waitUntilComplete();
  },
});
```

### Step 3: Update Your Frontend

Use the defined stream with `useRealtimeStream`:

```tsx theme={"theme":"css-variables"}
// Before
const { parts, error } = useRealtimeStream<string>(runId, "my-stream", {
  accessToken,
});
```

```tsx theme={"theme":"css-variables"}
// After
import { myStream } from "@/app/streams";

const { parts, error } = useRealtimeStream(myStream, runId, {
  accessToken,
});
```

### Alternative: Direct Methods (Not Recommended)

If you prefer not to use defined streams, you can use direct methods:

```ts theme={"theme":"css-variables"}
import { streams, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload) => {
    const stream = getDataStream();
    const { waitUntilComplete } = streams.pipe("my-stream", stream);
    await waitUntilComplete();
  },
});
```

## Reliability Features

Streams v2 includes automatic reliability improvements:

* **Automatic resumption**: If a connection is lost, both appending and reading will automatically resume from the last successful chunk
* **No data loss**: Network issues won't cause stream data to be lost
* **Idempotent operations**: Duplicate chunks are automatically handled

These improvements happen automatically - no code changes needed.

## Dashboard Integration

Streams are now visible in the Trigger.dev dashboard, allowing you to:

* View stream data in real-time as it's generated
* Inspect historical stream data for completed runs
* Debug streaming issues with full visibility into chunk delivery

<video />

## Best Practices

1. **Always use `streams.define()`**: Define your streams in a shared location for better organization, type safety, and code reusability. This is the recommended approach for all streams.
2. **Export stream types**: Use `InferStreamType` to export types for your frontend components
3. **Handle errors gracefully**: Always check for errors when reading streams in your UI
4. **Set appropriate timeouts**: Adjust `timeoutInSeconds` based on your use case (AI completions may need longer timeouts)
5. **Target parent runs**: When orchestrating with child tasks, pipe to parent runs for easier consumption
6. **Throttle frontend updates**: Use `throttleInMs` in `useRealtimeStream` to prevent excessive re-renders
7. **Use descriptive stream IDs**: Choose clear, descriptive IDs like `"ai-output"` or `"progress"` instead of generic names

## Pre-4.1.0 streams (legacy)

Prior to SDK 4.1.0, streams used the older metadata-based API. If you're on an earlier version, see [metadata.stream()](/runs/metadata#stream) for legacy usage. With 4.4.2+, [Input Streams](#input-streams) are available and documented in this page.

## Troubleshooting

### Stream not appearing in dashboard

* Verify your task is actually writing to the stream
* Check that the stream key matches between writing and reading

### Stream timeout errors

* Increase `timeoutInSeconds` in your `read()` or `useRealtimeStream()` calls
* Ensure your stream source is actively producing data
* Check network connectivity between your application and Trigger.dev

### Missing chunks

* With the current streams implementation, chunks should not be lost due to automatic resumption
* Verify you're reading from the correct stream key
* Check the `startIndex` option if you're not seeing expected chunks

### Input streams not working

* Input streams require SDK **4.4.2 or later** and the default streams (v2) infrastructure. Ensure you're on a recent SDK and not using the legacy metadata.stream() API.
* If `.on()` or `.once()` throw, follow the error message to enable v2 streams (they are default in 4.1.0+).

---

## Stream data to your backend (AI, files)

Read AI/LLM output, file chunks, and other streaming data from your Trigger.dev tasks in backend code.

**Read streaming data from your tasks in backend code.** Consume AI completions as they generate, process file chunks, or handle any continuous data your tasks produce.

<Note>
  To emit streams from your tasks, see [Streaming data from tasks](/tasks/streams). For React components, see [Streaming in React](/realtime/react-hooks/streams).
</Note>

## Reading streams

### Using defined streams (Recommended)

The recommended approach is to use [defined streams](/tasks/streams#defining-typed-streams-recommended) for full type safety:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function consumeStream(runId: string) {
  // Read from the defined stream
  const stream = await aiStream.read(runId);

  let fullText = "";

  for await (const chunk of stream) {
    console.log("Received chunk:", chunk); // chunk is typed!
    fullText += chunk;
  }

  console.log("Final text:", fullText);
}
```

### Direct stream reading

If you prefer not to use defined streams, you can read directly by specifying the stream key:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";

async function consumeStream(runId: string) {
  // Read from a stream by key
  const stream = await streams.read<string>(runId, "ai-output");

  for await (const chunk of stream) {
    console.log("Received chunk:", chunk);
  }
}
```

### Reading from the default stream

Every run has a default stream, so you can omit the stream key:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";

async function consumeDefaultStream(runId: string) {
  // Read from the default stream
  const stream = await streams.read<string>(runId);

  for await (const chunk of stream) {
    console.log("Received chunk:", chunk);
  }
}
```

## Stream options

The `read()` method accepts several options for controlling stream behavior:

### Timeout

Set a timeout to stop reading if no data is received within a specified time:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function consumeWithTimeout(runId: string) {
  const stream = await aiStream.read(runId, {
    timeoutInSeconds: 120, // Wait up to 2 minutes for data
  });

  try {
    for await (const chunk of stream) {
      console.log("Received chunk:", chunk);
    }
  } catch (error) {
    if (error.name === "TimeoutError") {
      console.log("Stream timed out");
    }
  }
}
```

### Start index

Resume reading from a specific chunk index (useful for reconnection scenarios):

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function resumeStream(runId: string, lastChunkIndex: number) {
  // Start reading from the chunk after the last one we received
  const stream = await aiStream.read(runId, {
    startIndex: lastChunkIndex + 1,
  });

  for await (const chunk of stream) {
    console.log("Received chunk:", chunk);
  }
}
```

### Abort signal

Use an `AbortSignal` to cancel stream reading:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function consumeWithCancellation(runId: string) {
  const controller = new AbortController();

  // Cancel after 30 seconds
  setTimeout(() => controller.abort(), 30000);

  const stream = await aiStream.read(runId, {
    signal: controller.signal,
  });

  try {
    for await (const chunk of stream) {
      console.log("Received chunk:", chunk);

      // Optionally abort based on content
      if (chunk.includes("STOP")) {
        controller.abort();
      }
    }
  } catch (error) {
    if (error.name === "AbortError") {
      console.log("Stream was cancelled");
    }
  }
}
```

### Combining options

You can combine multiple options:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function advancedStreamConsumption(runId: string) {
  const controller = new AbortController();

  const stream = await aiStream.read(runId, {
    timeoutInSeconds: 300, // 5 minute timeout
    startIndex: 0, // Start from the beginning
    signal: controller.signal, // Allow cancellation
  });

  try {
    for await (const chunk of stream) {
      console.log("Received chunk:", chunk);
    }
  } catch (error) {
    if (error.name === "AbortError") {
      console.log("Stream was cancelled");
    } else if (error.name === "TimeoutError") {
      console.log("Stream timed out");
    } else {
      console.error("Stream error:", error);
    }
  }
}
```

## Practical examples

### Reading AI streaming responses

Here's a complete example of consuming an AI stream from your backend:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function consumeAIStream(runId: string) {
  const stream = await aiStream.read(runId, {
    timeoutInSeconds: 300, // AI responses can take time
  });

  let fullResponse = "";
  const chunks: string[] = [];

  for await (const chunk of stream) {
    chunks.push(chunk);
    fullResponse += chunk;

    // Process each chunk as it arrives
    console.log("Chunk received:", chunk);

    // Could send to websocket, SSE, etc.
    // await sendToClient(chunk);
  }

  console.log("Stream complete!");
  console.log("Total chunks:", chunks.length);
  console.log("Full response:", fullResponse);

  return { fullResponse, chunks };
}
```

### Reading multiple streams

If a task emits multiple streams, you can read them concurrently or sequentially:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream, progressStream } from "./trigger/streams";

async function consumeMultipleStreams(runId: string) {
  // Read streams concurrently
  const [aiData, progressData] = await Promise.all([
    consumeStream(aiStream, runId),
    consumeStream(progressStream, runId),
  ]);

  return { aiData, progressData };
}

async function consumeStream<T>(
  streamDef: { read: (runId: string) => Promise<AsyncIterableStream<T>> },
  runId: string
): Promise<T[]> {
  const stream = await streamDef.read(runId);
  const chunks: T[] = [];

  for await (const chunk of stream) {
    chunks.push(chunk);
  }

  return chunks;
}
```

### Piping streams to HTTP responses

You can pipe streams directly to HTTP responses for server-sent events (SSE):

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";
import type { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const runId = request.nextUrl.searchParams.get("runId");

  if (!runId) {
    return new Response("Missing runId", { status: 400 });
  }

  const stream = await aiStream.read(runId, {
    timeoutInSeconds: 300,
  });

  // Create a readable stream for SSE
  const encoder = new TextEncoder();
  const readableStream = new ReadableStream({
    async start(controller) {
      try {
        for await (const chunk of stream) {
          // Format as SSE
          const data = `data: ${JSON.stringify({ chunk })}\n\n`;
          controller.enqueue(encoder.encode(data));
        }
        controller.close();
      } catch (error) {
        controller.error(error);
      }
    },
  });

  return new Response(readableStream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    },
  });
}
```

### Implementing retry logic

Handle transient errors with retry logic:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function consumeStreamWithRetry(
  runId: string,
  maxRetries = 3
): Promise<string[]> {
  let lastChunkIndex = 0;
  const allChunks: string[] = [];
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      const stream = await aiStream.read(runId, {
        startIndex: lastChunkIndex,
        timeoutInSeconds: 120,
      });

      for await (const chunk of stream) {
        allChunks.push(chunk);
        lastChunkIndex++;
      }

      // Success! Break out of retry loop
      break;
    } catch (error) {
      attempt++;

      if (attempt >= maxRetries) {
        throw new Error(`Failed after ${maxRetries} attempts: ${error.message}`);
      }

      console.log(`Retry attempt ${attempt} after error:`, error.message);

      // Wait before retrying (exponential backoff)
      await new Promise((resolve) => setTimeout(resolve, 1000 * Math.pow(2, attempt)));
    }
  }

  return allChunks;
}
```

### Processing streams in chunks

Process streams in batches for efficiency:

```ts theme={"theme":"css-variables"}
import { streams } from "@trigger.dev/sdk";
import { aiStream } from "./trigger/streams";

async function processStreamInBatches(runId: string, batchSize = 10) {
  const stream = await aiStream.read(runId);

  let batch: string[] = [];

  for await (const chunk of stream) {
    batch.push(chunk);

    if (batch.length >= batchSize) {
      // Process the batch
      await processBatch(batch);
      batch = [];
    }
  }

  // Process remaining chunks
  if (batch.length > 0) {
    await processBatch(batch);
  }
}

async function processBatch(chunks: string[]) {
  console.log(`Processing batch of ${chunks.length} chunks`);
  // Do something with the batch
  // e.g., save to database, send to queue, etc.
}
```

## Using with `runs.subscribeToRun()`

For more advanced use cases where you need both the run status and streams, you can use the `runs.subscribeToRun()` method with `.withStreams()`:

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/myTask";

async function subscribeToRunAndStreams(runId: string) {
  for await (const update of runs.subscribeToRun<typeof myTask>(runId).withStreams()) {
    switch (update.type) {
      case "run":
        console.log("Run update:", update.run.status);
        break;
      case "default":
        console.log("Stream chunk:", update.chunk);
        break;
    }
  }
}
```

<Note>
  For most use cases, we recommend using `streams.read()` with defined streams for better type safety and clearer code. Use `runs.subscribeToRun().withStreams()` only when you need to track both run status and stream data simultaneously.
</Note>

---

## Stream data to React (AI, files, progress)

Display AI/LLM output token by token, stream file chunks, or pipe any continuous data from a background task into your React components.

**Display AI responses as they generate, stream file processing results, or pipe any continuous data from a running task into your React components.** Unlike [progress and status hooks](/realtime/react-hooks/subscribe) (which track run state), streaming hooks give you the raw data your task produces while it runs.

<Note>
  To learn how to emit streams from your tasks, see [Streaming data from tasks](/tasks/streams).
</Note>

## useRealtimeStream (Recommended)

<Note>
  Available in SDK version **4.1.0 or later**. This is the recommended way to consume streams in
  your React components.
</Note>

The `useRealtimeStream` hook allows you to subscribe to a specific stream by its run ID and stream key. This hook is designed to work seamlessly with [defined streams](/tasks/streams#defining-typed-streams-recommended) for full type safety.

### Basic Usage

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";

export function StreamViewer({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { parts, error } = useRealtimeStream<string>(runId, "ai-output", {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div>
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

### With Defined Streams

The recommended approach is to use defined streams for full type safety:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "@/app/streams";

export function StreamViewer({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  // Pass the defined stream directly - full type safety!
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken: publicAccessToken,
    timeoutInSeconds: 600,
    onData: (chunk) => {
      console.log("New chunk:", chunk); // chunk is typed!
    },
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading...</div>;

  return (
    <div>
      {parts.map((part, i) => (
        <span key={i}>{part}</span>
      ))}
    </div>
  );
}
```

### Streaming AI Responses

Here's a complete example showing how to display streaming AI responses:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "@/trigger/streams";
import { Streamdown } from "streamdown";

export function AIStreamViewer({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken: publicAccessToken,
    timeoutInSeconds: 300,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Loading stream...</div>;

  const text = parts.join("");

  return (
    <div className="prose">
      <Streamdown isAnimating={true}>{text}</Streamdown>
    </div>
  );
}
```

### Options

The `useRealtimeStream` hook accepts the following options:

```tsx theme={"theme":"css-variables"}
const { parts, error } = useRealtimeStream(streamOrRunId, streamKeyOrOptions, {
  accessToken: "pk_...", // Required: Public access token
  baseURL: "https://api.trigger.dev", // Optional: Custom API URL
  timeoutInSeconds: 60, // Optional: Timeout (default: 60)
  startIndex: 0, // Optional: Start from specific chunk
  throttleInMs: 16, // Optional: Throttle updates (default: 16ms)
  onData: (chunk) => {}, // Optional: Callback for each chunk
});
```

### Using Default Stream

You can omit the stream key to use the default stream:

```tsx theme={"theme":"css-variables"}
const { parts, error } = useRealtimeStream<string>(runId, {
  accessToken: publicAccessToken,
});
```

For more information on defining and using streams, see the [Streaming data from tasks](/tasks/streams) documentation.

## useInputStreamSend

The `useInputStreamSend` hook lets you send data from your frontend into a running task's [input stream](/tasks/streams#input-streams). Use it for cancel buttons, approval forms, or any UI that needs to push typed data into a running task.

### Basic usage

Pass the input stream's `id` (string), the run ID, and options such as `accessToken`. You typically get `runId` and `accessToken` from the object returned when you trigger the task (e.g. `handle.id`, `handle.publicAccessToken`). The hook returns `send`, `isLoading`, `error`, and `isReady`:

```tsx theme={"theme":"css-variables"}
"use client";

import { useInputStreamSend } from "@trigger.dev/react-hooks";
import { approval } from "@/trigger/streams";

export function ApprovalForm({
  runId,
  accessToken,
}: {
  runId: string;
  accessToken: string;
}) {
  const { send, isLoading, isReady } = useInputStreamSend(
    approval.id,
    runId,
    { accessToken }
  );

  return (
    <button
      disabled={!isReady || isLoading}
      onClick={() => send({ approved: true, reviewer: "alice" })}
    >
      Approve
    </button>
  );
}
```

With a generic for type-safe payloads when not using a defined stream:

```tsx theme={"theme":"css-variables"}
type ApprovalPayload = { approved: boolean; reviewer: string };
const { send } = useInputStreamSend<ApprovalPayload>("approval", runId, {
  accessToken,
});
send({ approved: true, reviewer: "alice" });
```

### Options and return value

* **`streamId`**: The input stream identifier (string). Use the `id` from your defined stream (e.g. `approval.id`) or the same string you used in `streams.input<T>({ id: "approval" })`.
* **`runId`**: The run to send input to. When `runId` is undefined, `isReady` is false and `send` will not trigger.
* **`options`**: `accessToken` (required for client usage), `baseURL` (optional). See [Realtime auth](/realtime/auth) for generating a public access token with the right scopes (e.g. input streams write for that run).

Return value:

* **`send(data)`**: Sends typed data to the input stream. Uses SWR mutation under the hood.
* **`isLoading`**: True while a send is in progress.
* **`error`**: Set if the last send failed.
* **`isReady`**: True when both `runId` and access token are available.

For receiving input stream data inside a task (`.wait()`, `.once()`, `.on()`), see [Input Streams](/tasks/streams#input-streams) in the Streams doc.

## useRealtimeRunWithStreams

<Note>
  For new projects, we recommend using `useRealtimeStream` instead (available in SDK 4.1.0+). This
  hook is still supported for backward compatibility and use cases where you need to subscribe to
  both the run and all its streams at once.
</Note>

The `useRealtimeRunWithStreams` hook allows you to subscribe to a run by its ID and also receive any streams that are emitted by the task. This is useful when you need to access both the run metadata and multiple streams simultaneously.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeRunWithStreams } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, streams, error } = useRealtimeRunWithStreams(runId, {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <div>Run: {run.id}</div>
      <div>
        {Object.keys(streams).map((stream) => (
          <div key={stream}>Stream: {stream}</div>
        ))}
      </div>
    </div>
  );
}
```

You can also provide the type of the streams to the `useRealtimeRunWithStreams` hook to get type-safety:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunWithStreams } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

type STREAMS = {
  openai: string; // this is the type of each "part" of the stream
};

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, streams, error } = useRealtimeRunWithStreams<typeof myTask, STREAMS>(runId, {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;

  const text = streams.openai?.map((part) => part).join("");

  return (
    <div>
      <div>Run: {run.id}</div>
      <div>{text}</div>
    </div>
  );
}
```

As you can see above, each stream is an array of the type you provided, keyed by the stream name. If instead of a pure text stream you have a stream of objects, you can provide the type of the object:

```tsx theme={"theme":"css-variables"}
import type { TextStreamPart } from "ai";
import type { myTask } from "@/trigger/myTask";

type STREAMS = { openai: TextStreamPart<{}> };

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, streams, error } = useRealtimeRunWithStreams<typeof myTask, STREAMS>(runId, {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;

  const text = streams.openai
    ?.filter((stream) => stream.type === "text-delta")
    ?.map((part) => part.text)
    .join("");

  return (
    <div>
      <div>Run: {run.id}</div>
      <div>{text}</div>
    </div>
  );
}
```

### Streaming AI responses with useRealtimeRunWithStreams

Here's an example showing how to display streaming OpenAI responses using `useRealtimeRunWithStreams`:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunWithStreams } from "@trigger.dev/react-hooks";
import type { aiStreaming, STREAMS } from "./trigger/ai-streaming";

function MyComponent({ runId, publicAccessToken }: { runId: string; publicAccessToken: string }) {
  const { streams } = useRealtimeRunWithStreams<typeof aiStreaming, STREAMS>(runId, {
    accessToken: publicAccessToken,
  });

  if (!streams.openai) {
    return <div>Loading...</div>;
  }

  const text = streams.openai.join(""); // `streams.openai` is an array of strings

  return (
    <div>
      <h2>OpenAI response:</h2>
      <p>{text}</p>
    </div>
  );
}
```

### AI SDK with tools

When using the AI SDK with tools with `useRealtimeRunWithStreams`, you can access tool calls and results:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunWithStreams } from "@trigger.dev/react-hooks";
import type { aiStreamingWithTools, STREAMS } from "./trigger/ai-streaming";

function MyComponent({ runId, publicAccessToken }: { runId: string; publicAccessToken: string }) {
  const { streams } = useRealtimeRunWithStreams<typeof aiStreamingWithTools, STREAMS>(runId, {
    accessToken: publicAccessToken,
  });

  if (!streams.openai) {
    return <div>Loading...</div>;
  }

  // streams.openai is an array of TextStreamPart
  const toolCall = streams.openai.find(
    (stream) => stream.type === "tool-call" && stream.toolName === "getWeather"
  );
  const toolResult = streams.openai.find((stream) => stream.type === "tool-result");
  const textDeltas = streams.openai.filter((stream) => stream.type === "text-delta");

  const text = textDeltas.map((delta) => delta.textDelta).join("");
  const weatherLocation = toolCall ? toolCall.args.location : undefined;
  const weather = toolResult ? toolResult.result.temperature : undefined;

  return (
    <div>
      <h2>OpenAI response:</h2>
      <p>{text}</p>
      <h2>Weather:</h2>
      <p>
        {weatherLocation
          ? `The weather in ${weatherLocation} is ${weather} degrees.`
          : "No weather data"}
      </p>
    </div>
  );
}
```

### Throttling updates

The `useRealtimeRunWithStreams` hook accepts an `experimental_throttleInMs` option to throttle the updates from the server. This can be useful if you are getting too many updates and want to reduce the number of updates.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunWithStreams } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, streams, error } = useRealtimeRunWithStreams(runId, {
    accessToken: publicAccessToken,
    experimental_throttleInMs: 1000, // Throttle updates to once per second
  });

  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <div>Run: {run.id}</div>
      {/* Display streams */}
    </div>
  );
}
```

All other options (accessToken, baseURL, enabled, id) work the same as the other realtime hooks.

For the newer `useRealtimeStream` hook, use the `throttleInMs` option instead (see [options above](#options)).

## Frequently asked questions

### How do I stream AI/LLM responses from a background task to React?

Define a typed stream in your task with `streams.define<string>()`, pipe your AI SDK response to it with `.pipe()`, then consume it in your component with `useRealtimeStream`. See [Streaming data from tasks](/tasks/streams) for the task-side setup.

### What's the difference between streaming and run updates?

[Run updates](/realtime/react-hooks/subscribe) track **run state** (status, metadata, tags). Streaming (this page) pipes **continuous data** your task produces. Use run updates for progress bars and status badges. Use streaming for AI chat output, live logs, or file processing results. You can use both at the same time.

### Can I send data back into a running task from React?

Yes. Use the `useInputStreamSend` hook to send data into a running task's input stream. This is useful for cancel buttons, user approvals, or any interactive flow. See [Input Streams](/tasks/streams#input-streams) for the full guide.

### Do streams work with the Vercel AI SDK?

Yes. You can pipe a Vercel AI SDK `streamText` response directly into a Trigger.dev stream using `.pipe()`. The [Streaming data from tasks](/tasks/streams) page has a complete AI streaming example.

---
