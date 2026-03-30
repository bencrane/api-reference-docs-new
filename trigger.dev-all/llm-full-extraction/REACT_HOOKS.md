> Sources:
> - https://trigger.dev/docs/realtime/react-hooks/overview
> - https://trigger.dev/docs/realtime/react-hooks/streams
> - https://trigger.dev/docs/realtime/react-hooks/subscribe
> - https://trigger.dev/docs/realtime/react-hooks/swr
> - https://trigger.dev/docs/realtime/react-hooks/triggering
> - https://trigger.dev/docs/realtime/react-hooks/use-wait-token

# React Hooks

## React hooks for real-time task updates

Subscribe to background task progress, stream AI responses, and trigger tasks from React components using @trigger.dev/react-hooks.

**`@trigger.dev/react-hooks` gives your React components live access to background tasks.** Subscribe to run progress, stream AI output as it generates, or trigger tasks directly from the browser.

## Installation

Install the `@trigger.dev/react-hooks` package in your project:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npm add @trigger.dev/react-hooks
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm add @trigger.dev/react-hooks
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn install @trigger.dev/react-hooks
  ```
</CodeGroup>

## Authentication

All hooks require authentication with a Public Access Token. Pass the token via the `accessToken` option:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    baseURL: "https://your-trigger-dev-instance.com", // optional, only needed if you are self-hosting Trigger.dev
  });

  // ...
}
```

Learn more about [generating and managing tokens in our authentication guide](/realtime/auth).

## Available hooks

| Hook category     | What it does                                                 | Guide                                          |
| ----------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| **Trigger hooks** | Trigger tasks from the browser                               | [Triggering](/realtime/react-hooks/triggering) |
| **Run updates**   | Subscribe to run status, metadata, and tags                  | [Run updates](/realtime/react-hooks/subscribe) |
| **Streaming**     | Consume AI output, file chunks, or any continuous data       | [Streaming](/realtime/react-hooks/streams)     |
| **SWR hooks**     | One-time fetch with caching (not recommended for most cases) | [SWR](/realtime/react-hooks/swr)               |

## SWR vs Realtime hooks

We offer two "styles" of hooks: SWR and Realtime. SWR hooks use the [swr](https://swr.vercel.app/) library to fetch data once and cache it. Realtime hooks use [Trigger.dev Realtime](/realtime) to subscribe to updates as they happen.

<Note>
  It can be a little confusing which one to use because [swr](https://swr.vercel.app/) can also be
  configured to poll for updates. But because of rate-limits and the way the Trigger.dev API works,
  we recommend using the Realtime hooks for most use cases.
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

## Run updates in React

Build progress bars, status indicators, and live dashboards by subscribing to background task updates from React components.

**Subscribe to a run and your component re-renders whenever its status, metadata, or tags change.** Build progress bars, deployment monitors, or any UI that needs to reflect what a background task is doing right now.

For streaming continuous data (AI tokens, file chunks), see [Streaming](/realtime/react-hooks/streams) instead.

## Trigger + subscribe combo hooks

Trigger a task and immediately subscribe to its run. Details in the [triggering](/realtime/react-hooks/triggering) section.

* **[`useRealtimeTaskTrigger`](/realtime/react-hooks/triggering#userealtimetasktrigger)** - Trigger a task and subscribe to the run
* **[`useRealtimeTaskTriggerWithStreams`](/realtime/react-hooks/triggering#userealtimetasktriggerwithstreams)** - Trigger a task and subscribe to both run updates and streams

## Subscribe hooks

### useRealtimeRun

The `useRealtimeRun` hook allows you to subscribe to a run by its ID.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

To correctly type the run's payload and output, you can provide the type of your task to the `useRealtimeRun` hook:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun<typeof myTask>(runId, {
    accessToken: publicAccessToken,
  });

  if (error) return <div>Error: {error.message}</div>;

  // Now run.payload and run.output are correctly typed

  return <div>Run: {run.id}</div>;
}
```

You can supply an `onComplete` callback to the `useRealtimeRun` hook to be called when the run is completed or errored. This is useful if you want to perform some action when the run is completed, like navigating to a different page or showing a notification.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    onComplete: (run, error) => {
      console.log("Run completed", run);
    },
  });

  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

When you only need run status (for example, a progress bar or completion badge), you can omit large fields like `payload` and `output` by passing `skipColumns`. This reduces the data sent over the wire and avoids issues such as "Large HTTP Payload" warnings in tools like Sentry.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function RunStatusBadge({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    skipColumns: ["payload", "output"],
  });

  if (error) return <span>Error</span>;
  if (!run) return <span>Loading…</span>;

  return <span>Status: {run.status}</span>;
}
```

You can skip any of: `payload`, `output`, `metadata`, `startedAt`, `delayUntil`, `queuedAt`, `expiredAt`, `completedAt`, `number`, `isTest`, `usageDurationMs`, `costInCents`, `baseCostInCents`, `ttl`, `payloadType`, `outputType`, `runTags`, `error`. The `useRealtimeRunsWithTag` hook also accepts a `skipColumns` option in the same way.

See our [run object reference](/realtime/run-object) for the complete schema and [How it Works documentation](/realtime/how-it-works) for more technical details.

### useRealtimeRunsWithTag

The `useRealtimeRunsWithTag` hook allows you to subscribe to multiple runs with a specific tag.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeRunsWithTag } from "@trigger.dev/react-hooks";

export function MyComponent({ tag }: { tag: string }) {
  const { runs, error } = useRealtimeRunsWithTag(tag);

  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {runs.map((run) => (
        <div key={run.id}>Run: {run.id}</div>
      ))}
    </div>
  );
}
```

To correctly type the runs payload and output, you can provide the type of your task to the `useRealtimeRunsWithTag` hook:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunsWithTag } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

export function MyComponent({ tag }: { tag: string }) {
  const { runs, error } = useRealtimeRunsWithTag<typeof myTask>(tag);

  if (error) return <div>Error: {error.message}</div>;

  // Now runs[i].payload and runs[i].output are correctly typed

  return (
    <div>
      {runs.map((run) => (
        <div key={run.id}>Run: {run.id}</div>
      ))}
    </div>
  );
}
```

If `useRealtimeRunsWithTag` could return multiple different types of tasks, you can pass a union of all the task types to the hook:

```tsx theme={"theme":"css-variables"}
import { useRealtimeRunsWithTag } from "@trigger.dev/react-hooks";
import type { myTask1, myTask2 } from "@/trigger/myTasks";

export function MyComponent({ tag }: { tag: string }) {
  const { runs, error } = useRealtimeRunsWithTag<typeof myTask1 | typeof myTask2>(tag);

  if (error) return <div>Error: {error.message}</div>;

  // You can narrow down the type of the run based on the taskIdentifier
  for (const run of runs) {
    if (run.taskIdentifier === "my-task-1") {
      // run is correctly typed as myTask1
    } else if (run.taskIdentifier === "my-task-2") {
      // run is correctly typed as myTask2
    }
  }

  return (
    <div>
      {runs.map((run) => (
        <div key={run.id}>Run: {run.id}</div>
      ))}
    </div>
  );
}
```

### useRealtimeBatch

The `useRealtimeBatch` hook allows you to subscribe to a batch of runs by its the batch ID.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeBatch } from "@trigger.dev/react-hooks";

export function MyComponent({ batchId }: { batchId: string }) {
  const { runs, error } = useRealtimeBatch(batchId);

  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {runs.map((run) => (
        <div key={run.id}>Run: {run.id}</div>
      ))}
    </div>
  );
}
```

See our [Realtime documentation](/realtime) for more information.

## Using metadata to show progress in your UI

All realtime hooks automatically include metadata updates. Whenever your task updates metadata using `metadata.set()`, `metadata.append()`, or other metadata methods, your component will re-render with the updated data.

<Note>To learn how to write tasks using metadata, see our [metadata](/runs/metadata) guide.</Note>

### Progress monitoring

This example demonstrates how to create a progress monitor component that can be used to display the progress of a run:

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function ProgressMonitor({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error, isLoading } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  if (isLoading) return <div>Loading run...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!run) return <div>Run not found</div>;

  const progress = run.metadata?.progress as
    | {
        current: number;
        total: number;
        percentage: number;
        currentItem: string;
      }
    | undefined;

  return (
    <div className="space-y-4">
      <div>
        <h3>Run Status: {run.status}</h3>
        <p>Run ID: {run.id}</p>
      </div>

      {progress && (
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>Progress</span>
            <span>{progress.percentage}%</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${progress.percentage}%` }}
            />
          </div>
          <p className="text-sm text-gray-600">
            Processing: {progress.currentItem} ({progress.current}/{progress.total})
          </p>
        </div>
      )}
    </div>
  );
}
```

### Reusable progress bar

This example demonstrates how to create a reusable progress bar component that can be used to display the percentage progress of a run:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeRun } from "@trigger.dev/react-hooks";

interface ProgressBarProps {
  runId: string;
  publicAccessToken: string;
  title?: string;
}

export function ProgressBar({ runId, publicAccessToken, title }: ProgressBarProps) {
  const { run } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  const progress = run?.metadata?.progress as
    | {
        current?: number;
        total?: number;
        percentage?: number;
        currentItem?: string;
      }
    | undefined;

  const percentage = progress?.percentage ?? 0;
  const isComplete = run?.status === "COMPLETED";
  const isFailed = run?.status === "FAILED";

  return (
    <div className="w-full space-y-2">
      {title && <h4 className="font-medium">{title}</h4>}

      <div className="w-full bg-gray-200 rounded-full h-3">
        <div
          className={`h-3 rounded-full transition-all duration-500 ${
            isFailed ? "bg-red-500" : isComplete ? "bg-green-500" : "bg-blue-500"
          }`}
          style={{ width: `${percentage}%` }}
        />
      </div>

      <div className="flex justify-between text-sm text-gray-600">
        <span>
          {progress?.current && progress?.total
            ? `${progress.current}/${progress.total} items`
            : "Processing..."}
        </span>
        <span>{percentage}%</span>
      </div>

      {progress?.currentItem && (
        <p className="text-sm text-gray-500 truncate">Current: {progress.currentItem}</p>
      )}
    </div>
  );
}
```

### Status indicator with logs

This example demonstrates how to create a status indicator component that can be used to display the status of a run, and also logs that are emitted by the task:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeRun } from "@trigger.dev/react-hooks";

interface StatusIndicatorProps {
  runId: string;
  publicAccessToken: string;
}

export function StatusIndicator({ runId, publicAccessToken }: StatusIndicatorProps) {
  const { run } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  const status = run?.metadata?.status as string | undefined;
  const logs = run?.metadata?.logs as string[] | undefined;

  const getStatusColor = (status: string | undefined) => {
    switch (status) {
      case "completed":
        return "text-green-600 bg-green-100";
      case "failed":
        return "text-red-600 bg-red-100";
      case "running":
        return "text-blue-600 bg-blue-100";
      default:
        return "text-gray-600 bg-gray-100";
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center space-x-2">
        <span className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(status)}`}>
          {status || run?.status || "Unknown"}
        </span>
        <span className="text-sm text-gray-500">Run {run?.id}</span>
      </div>

      {logs && logs.length > 0 && (
        <div className="bg-gray-50 rounded-lg p-4">
          <h4 className="font-medium mb-2">Logs</h4>
          <div className="space-y-1 max-h-48 overflow-y-auto">
            {logs.map((log, index) => (
              <div key={index} className="text-sm text-gray-700 font-mono">
                {log}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
```

### Multi-stage deployment monitor

This example demonstrates how to create a multi-stage deployment monitor component that can be used to display the progress of a deployment:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeRun } from "@trigger.dev/react-hooks";

interface DeploymentMonitorProps {
  runId: string;
  publicAccessToken: string;
}

const DEPLOYMENT_STAGES = [
  "initializing",
  "building",
  "testing",
  "deploying",
  "verifying",
  "completed",
] as const;

export function DeploymentMonitor({ runId, publicAccessToken }: DeploymentMonitorProps) {
  const { run } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  const status = run?.metadata?.status as string | undefined;
  const logs = run?.metadata?.logs as string[] | undefined;
  const currentStageIndex = DEPLOYMENT_STAGES.indexOf(status as any);

  return (
    <div className="space-y-6">
      <h3 className="text-lg font-semibold">Deployment Progress</h3>

      {/* Stage indicators */}
      <div className="space-y-4">
        {DEPLOYMENT_STAGES.map((stage, index) => {
          const isActive = currentStageIndex === index;
          const isCompleted = currentStageIndex > index;
          const isFailed = run?.status === "FAILED" && currentStageIndex === index;

          return (
            <div key={stage} className="flex items-center space-x-3">
              <div
                className={`w-6 h-6 rounded-full flex items-center justify-center text-sm font-medium ${
                  isFailed
                    ? "bg-red-500 text-white"
                    : isCompleted
                    ? "bg-green-500 text-white"
                    : isActive
                    ? "bg-blue-500 text-white"
                    : "bg-gray-200 text-gray-600"
                }`}
              >
                {isCompleted ? "✓" : index + 1}
              </div>
              <span
                className={`capitalize ${
                  isActive
                    ? "font-medium text-blue-600"
                    : isCompleted
                    ? "text-green-600"
                    : isFailed
                    ? "text-red-600"
                    : "text-gray-500"
                }`}
              >
                {stage}
              </span>
              {isActive && (
                <div className="animate-spin w-4 h-4 border-2 border-blue-500 border-t-transparent rounded-full" />
              )}
            </div>
          );
        })}
      </div>

      {/* Recent logs */}
      {logs && logs.length > 0 && (
        <div className="bg-black text-green-400 rounded-lg p-4 font-mono text-sm">
          <div className="space-y-1 max-h-32 overflow-y-auto">
            {logs.slice(-5).map((log, index) => (
              <div key={index}>
                <span className="text-gray-500">$ </span>
                {log}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
```

### Type safety

Define TypeScript interfaces for your metadata to get full type safety:

```tsx theme={"theme":"css-variables"}
"use client";

import { useRealtimeRun } from "@trigger.dev/react-hooks";

interface TaskMetadata {
  progress?: {
    current: number;
    total: number;
    percentage: number;
    currentItem: string;
  };
  status?: "initializing" | "processing" | "completed" | "failed";
  user?: {
    id: string;
    name: string;
  };
  logs?: string[];
}

export function TypedMetadataComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
  });

  // Type-safe metadata access
  const metadata = run?.metadata as TaskMetadata | undefined;

  return (
    <div>
      {metadata?.progress && <p>Progress: {metadata.progress.percentage}%</p>}

      {metadata?.user && (
        <p>
          User: {metadata.user.name} ({metadata.user.id})
        </p>
      )}

      {metadata?.status && <p>Status: {metadata.status}</p>}
    </div>
  );
}
```

## Common options

### accessToken & baseURL

You can pass the `accessToken` option to the Realtime hooks to authenticate the subscription.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
}: {
  runId: string;
  publicAccessToken: string;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    baseURL: "https://my-self-hosted-trigger.com", // Optional if you are using a self-hosted Trigger.dev instance
  });

  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

### enabled

You can pass the `enabled` option to the Realtime hooks to enable or disable the subscription.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  runId,
  publicAccessToken,
  enabled,
}: {
  runId: string;
  publicAccessToken: string;
  enabled: boolean;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    enabled,
  });

  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

This allows you to conditionally disable using the hook based on some state.

### id

You can pass the `id` option to the Realtime hooks to change the ID of the subscription.

```tsx theme={"theme":"css-variables"}
import { useRealtimeRun } from "@trigger.dev/react-hooks";

export function MyComponent({
  id,
  runId,
  publicAccessToken,
  enabled,
}: {
  id: string;
  runId: string;
  publicAccessToken: string;
  enabled: boolean;
}) {
  const { run, error } = useRealtimeRun(runId, {
    accessToken: publicAccessToken,
    enabled,
    id,
  });

  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

This allows you to change the ID of the subscription based on some state. Passing in a different ID will unsubscribe from the current subscription and subscribe to the new one (and remove any cached data).

## Frequently asked questions

### How do I show a progress bar for a background task in React?

Use `metadata.set()` inside your task to update a progress value, then read it with `useRealtimeRun` in your component. The hook re-renders your component on every metadata change. See [Using metadata to show progress](#using-metadata-to-show-progress-in-your-ui) above for a complete example.

### What's the difference between run updates and streaming?

Run updates (this page) give you **run state**: status, metadata, and tags. They're for progress bars, status badges, and dashboards. [Streaming](/realtime/react-hooks/streams) gives you **continuous data** like AI tokens or file chunks. Use run updates for "how far along is my task?" and streaming for "show me the output as it generates."

### Can I subscribe to multiple runs at once?

Yes. Use `useRealtimeRunsWithTag` to subscribe to all runs with a specific tag (e.g., `user:123`), or `useRealtimeBatch` for all runs in a batch. Each yields an array of run objects that update in real time.

### Do I need to set up polling or WebSockets?

No. The hooks handle the connection automatically using Trigger.dev's Realtime infrastructure (built on [Electric SQL](/realtime/how-it-works)). Just pass a run ID and an access token.

---

## SWR hooks

Fetch and cache data using SWR-based hooks

SWR hooks use the [swr](https://swr.vercel.app/) library to fetch data once and cache it. These hooks are useful when you need to fetch data without real-time updates.

<Note>
  While SWR can be configured to poll for updates, we recommend using our other [Realtime
  hooks](/realtime/react-hooks/) for most use-cases due to rate-limits and the way the Trigger.dev
  API works.
</Note>

## useRun

The `useRun` hook allows you to fetch a run by its ID.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRun } from "@trigger.dev/react-hooks";

export function MyComponent({ runId }: { runId: string }) {
  const { run, error, isLoading } = useRun(runId);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

The `run` object returned is the same as the [run object](/management/runs/retrieve) returned by the Trigger.dev API. To correctly type the run's payload and output, you can provide the type of your task to the `useRun` hook:

```tsx theme={"theme":"css-variables"}
import { useRun } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

export function MyComponent({ runId }: { runId: string }) {
  const { run, error, isLoading } = useRun<typeof myTask>(runId, {
    refreshInterval: 0, // Disable polling
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  // Now run.payload and run.output are correctly typed

  return <div>Run: {run.id}</div>;
}
```

## Common SWR options

You can pass the following options to the all SWR hooks:

<ParamField type="boolean">
  Revalidate the data when the window regains focus.
</ParamField>

<ParamField type="boolean">
  Revalidate the data when the browser regains a network connection.
</ParamField>

<ParamField type="number">
  Poll for updates at the specified interval (in milliseconds). Polling is not recommended for most
  use-cases. Use the Realtime hooks instead.
</ParamField>

## Common SWR return values

<ResponseField name="error" type="Error">
  An error object if an error occurred while fetching the data.
</ResponseField>

<ResponseField name="isLoading" type="boolean">
  A boolean indicating if the data is currently being fetched.
</ResponseField>

<ResponseField name="isValidating" type="boolean">
  A boolean indicating if the data is currently being revalidated.
</ResponseField>

<ResponseField name="isError" type="boolean">
  A boolean indicating if an error occurred while fetching the data.
</ResponseField>

---

## Trigger tasks from React

Trigger background tasks from React components and optionally subscribe to their progress or stream their output.

Trigger tasks directly from your React components. You can fire-and-forget, or trigger and immediately subscribe to the run's progress or streamed output.

<Note>
  For triggering tasks from your frontend, you need to use “trigger” tokens. These can only be used
  once to trigger a task and are more secure than regular Public Access Tokens. To learn more about
  how to create and use these tokens, see our [Trigger
  Tokens](/realtime/auth#trigger-tokens-for-frontend-triggering-only) documentation.
</Note>

## Hooks

We provide three hooks for triggering tasks from your frontend application:

* `useTaskTrigger` - Trigger a task from your frontend application.
* `useRealtimeTaskTrigger` - Trigger a task from your frontend application and subscribe to the run.
* `useRealtimeTaskTriggerWithStreams` - Trigger a task from your frontend application and subscribe to the run, and also receive any streams that are emitted by the task.

### useTaskTrigger

The `useTaskTrigger` hook allows you to trigger a task from your frontend application.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useTaskTrigger } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";
//     👆 This is the type of your task, include this to get type-safety

export function MyComponent({ publicAccessToken }: { publicAccessToken: string }) {
  //                         pass the type of your task here 👇
  const { submit, handle, error, isLoading } = useTaskTrigger<typeof myTask>("my-task", {
    accessToken: publicAccessToken, // 👈 this is the "trigger" token
  });

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (handle) {
    return <div>Run ID: {handle.id}</div>;
  }

  return (
    <button onClick={() => submit({ foo: "bar" })} disabled={isLoading}>
      {isLoading ? "Loading..." : "Trigger Task"}
    </button>
  );
}
```

`useTaskTrigger` returns an object with the following properties:

* `submit`: A function that triggers the task. It takes the payload of the task as an argument.
* `handle`: The run handle object. This object contains the ID of the run that was triggered, along with a Public Access Token that can be used to access the run.
* `isLoading`: A boolean that indicates whether the task is currently being triggered.
* `error`: An error object that contains any errors that occurred while triggering the task.

The `submit` function triggers the task with the specified payload. You can additionally pass an optional [options](/triggering#options) argument to the `submit` function:

```tsx theme={"theme":"css-variables"}
submit({ foo: "bar" }, { tags: ["tag1", "tag2"] });
```

#### Using the handle object

You can use the `handle` object to initiate a subsequent [Realtime hook](/realtime/react-hooks/subscribe#userealtimerun) to subscribe to the run.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useTaskTrigger, useRealtimeRun } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";
//     👆 This is the type of your task

export function MyComponent({ publicAccessToken }: { publicAccessToken: string }) {
  //                         pass the type of your task here 👇
  const { submit, handle, error, isLoading } = useTaskTrigger<typeof myTask>("my-task", {
    accessToken: publicAccessToken, // 👈 this is the "trigger" token
  });

  //     use the handle object to preserve type-safety 👇
  const { run, error: realtimeError } = useRealtimeRun(handle, {
    accessToken: handle?.publicAccessToken,
    enabled: !!handle, // Only subscribe to the run if the handle is available
  });

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (handle) {
    return <div>Run ID: {handle.id}</div>;
  }

  if (realtimeError) {
    return <div>Error: {realtimeError.message}</div>;
  }

  if (run) {
    return <div>Run ID: {run.id}</div>;
  }

  return (
    <button onClick={() => submit({ foo: "bar" })} disabled={isLoading}>
      {isLoading ? "Loading..." : "Trigger Task"}
    </button>
  );
}
```

We've also created some additional hooks that allow you to trigger tasks and subscribe to the run in one step:

### useRealtimeTaskTrigger

The `useRealtimeTaskTrigger` hook allows you to trigger a task from your frontend application and then subscribe to the run in using Realtime:

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeTaskTrigger } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

export function MyComponent({ publicAccessToken }: { publicAccessToken: string }) {
  const { submit, run, error, isLoading } = useRealtimeTaskTrigger<typeof myTask>("my-task", {
    accessToken: publicAccessToken,
  });

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  // This is the Realtime run object, which will automatically update when the run changes
  if (run) {
    return <div>Run ID: {run.id}</div>;
  }

  return (
    <button onClick={() => submit({ foo: "bar" })} disabled={isLoading}>
      {isLoading ? "Loading..." : "Trigger Task"}
    </button>
  );
}
```

### useRealtimeTaskTriggerWithStreams

The `useRealtimeTaskTriggerWithStreams` hook allows you to trigger a task from your frontend application and then subscribe to the run in using Realtime, and also receive any streams that are emitted by the task.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRealtimeTaskTriggerWithStreams } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

type STREAMS = {
  openai: string; // this is the type of each "part" of the stream
};

export function MyComponent({ publicAccessToken }: { publicAccessToken: string }) {
  const { submit, run, streams, error, isLoading } = useRealtimeTaskTriggerWithStreams<
    typeof myTask,
    STREAMS
  >("my-task", {
    accessToken: publicAccessToken,
  });

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (streams && run) {
    const text = streams.openai?.map((part) => part).join("");

    return (
      <div>
        <div>Run ID: {run.id}</div>
        <div>{text}</div>
      </div>
    );
  }

  return (
    <button onClick={() => submit({ foo: "bar" })} disabled={isLoading}>
      {isLoading ? "Loading..." : "Trigger Task"}
    </button>
  );
}
```

---

## useWaitToken

Use the useWaitToken hook to complete a wait token from a React component

We've added a new `useWaitToken` react hook that allows you to complete a wait token from a React component, using a Public Access Token.

```ts backend.ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

// Somewhere in your code, you'll need to create the token and then pass the token ID and the public token to the frontend
const token = await wait.createToken({
  timeout: "10m",
});

return {
  tokenId: token.id,
  publicToken: token.publicAccessToken, // An automatically generated public access token that expires in 1 hour
};
```

Now you can use the `useWaitToken` hook in your frontend code:

```tsx frontend.tsx theme={"theme":"css-variables"}
import { useWaitToken } from "@trigger.dev/react-hooks";

export function MyComponent({ publicToken, tokenId }: { publicToken: string; tokenId: string }) {
  const { complete } = useWaitToken(tokenId, {
    accessToken: publicToken,
  });

  return <button onClick={() => complete({ foo: "bar" })}>Complete</button>;
}
```

---
