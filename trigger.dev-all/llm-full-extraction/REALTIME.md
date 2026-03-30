> Sources:
> - https://trigger.dev/docs/realtime/overview
> - https://trigger.dev/docs/realtime/how-it-works
> - https://trigger.dev/docs/realtime/run-object
> - https://trigger.dev/docs/realtime/auth
> - https://trigger.dev/docs/realtime/backend/overview
> - https://trigger.dev/docs/realtime/backend/subscribe
> - https://trigger.dev/docs/realtime/backend/streams

# Realtime

## Realtime overview

Get live run updates and stream data from background tasks to your frontend or backend. No polling.

**Realtime is the umbrella for everything live in Trigger.dev.** It covers two things: getting notified when a run's state changes, and streaming continuous data (like AI tokens) from a running task to your app.

Both use the same `@trigger.dev/react-hooks` package and the same authentication system. The difference is what they give you.

## Run updates vs Streaming

|                         | Run updates                                              | Streaming                                                     |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| **What you get**        | Run state: status, metadata, tags                        | Continuous data you define (AI tokens, file chunks, progress) |
| **When it fires**       | On state changes                                         | While the task runs, as data is produced                      |
| **Use case**            | Progress bars, status badges, dashboards                 | AI chat output, live logs, file processing                    |
| **React hook**          | [`useRealtimeRun`](/realtime/react-hooks/subscribe)      | [`useRealtimeStream`](/realtime/react-hooks/streams)          |
| **Setup in task code?** | No, automatic                                            | Yes, using `streams.define()`                                 |
| **Infrastructure**      | [Electric SQL](/realtime/how-it-works) (PostgreSQL sync) | Streams transport                                             |

You can use both at the same time. Subscribe to a run's status (to show a progress bar) while also streaming AI output (to display tokens as they arrive).

## Run updates

Subscribe to a run and your code gets called whenever its status, [metadata](/runs/metadata), or [tags](/tags) change. No setup needed in your task code.

You can subscribe to:

* **Specific runs** by run ID
* **Runs with specific tags** (e.g., all runs tagged with `user:123`)
* **Batch runs** within a specific batch
* **Trigger + subscribe combos** that trigger a task and immediately subscribe (frontend only)

→ [React hooks](/realtime/react-hooks/subscribe) | [Backend](/realtime/backend/subscribe)

## Streaming

Define typed streams in your task, pipe data to them, and read that data from your frontend or backend as it's produced. You need to set up streams in your task code using `streams.define()`.

→ [How to emit streams from tasks](/tasks/streams) | [React hooks](/realtime/react-hooks/streams) | [Backend](/realtime/backend/streams)

## Authentication

All Realtime hooks and functions require authentication. See the [authentication guide](/realtime/auth) for setup.

## Frequently asked questions

### How do I show a progress bar for a background task?

Use [run metadata](/runs/metadata) to store progress data (like a percentage), then subscribe to the run with [`useRealtimeRun`](/realtime/react-hooks/subscribe). Your component re-renders on every metadata update.

### How do I stream AI/LLM responses from a background task?

Define a stream in your task with `streams.define()`, pipe your AI SDK response to it, then consume it in React with [`useRealtimeStream`](/realtime/react-hooks/streams). See [Streaming data from tasks](/tasks/streams) for the full guide.

### Do I need WebSockets or polling?

No. Run updates are powered by [Electric SQL](/realtime/how-it-works) (HTTP-based PostgreSQL syncing). Streams use their own transport. The hooks handle connections automatically.

### Can I use both run updates and streaming together?

Yes. A common pattern: subscribe to run status with `useRealtimeRun` (progress indicator) while streaming AI output with `useRealtimeStream` (token-by-token display).

---

## How Realtime works

Technical architecture behind Trigger.dev's real-time run updates, built on Electric SQL and PostgreSQL syncing.

This page covers the infrastructure behind **run updates** (status, metadata, tags). [Streaming](/tasks/streams) uses a separate transport.

## Architecture

The run updates system is built on top of [Electric SQL](https://electric-sql.com/), an open-source PostgreSQL syncing engine. The Trigger.dev API wraps Electric SQL and provides a simple API to subscribe to [runs](/runs) and get updates as they happen.

## Run changes

You will receive updates whenever a run changes for the following reasons:

* The run moves to a new state. See our [run lifecycle docs](/runs#the-run-lifecycle) for more information.
* [Run tags](/tags) are added or removed.
* [Run metadata](/runs/metadata) is updated.

## Run object

The run object returned by Realtime subscriptions is optimized for streaming updates and differs from the management API's run object. See [the run object](/realtime/run-object) page for the complete schema and field descriptions.

## Basic usage

After you trigger a task, you can subscribe to the run using the `runs.subscribeToRun` function. This function returns an async iterator that you can use to get updates on the run status.

```ts theme={"theme":"css-variables"}
import { runs, tasks } from "@trigger.dev/sdk";

// Somewhere in your backend code
async function myBackend() {
  const handle = await tasks.trigger("my-task", { some: "data" });

  for await (const run of runs.subscribeToRun(handle.id)) {
    // This will log the run every time it changes
    console.log(run);
  }
}
```

Every time the run changes, the async iterator will yield the updated run. You can use this to update your UI, log the run status, or take any other action.

Alternatively, you can subscribe to changes to any run that includes a specific tag (or tags) using the `runs.subscribeToRunsWithTag` function.

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

// Somewhere in your backend code
for await (const run of runs.subscribeToRunsWithTag("user:1234")) {
  // This will log the run every time it changes, for all runs with the tag "user:1234"
  console.log(run);
}
```

If you've used `batchTrigger` to trigger multiple runs, you can also subscribe to changes to all the runs triggered in the batch using the `runs.subscribeToBatch` function.

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

// Somewhere in your backend code
for await (const run of runs.subscribeToBatch("batch-id")) {
  // This will log the run every time it changes, for all runs in the batch with the ID "batch-id"
  console.log(run);
}
```

## Run metadata

The run metadata API gives you the ability to add or update custom metadata on a run, which will cause the run to be updated. This allows you to extend the Realtime API with custom data attached to a run that can be used for various purposes. Some common use cases include:

* Adding a link to a related resource
* Adding a reference to a user or organization
* Adding a custom status with progress information

See our [run metadata docs](/runs/metadata) for more on how to write tasks that use the metadata API.

### Using metadata with Realtime & React hooks

You can combine run metadata with the Realtime API to bridge the gap between your trigger.dev tasks and your applications in two ways:

1. Using our [React hooks](/realtime/react-hooks/subscribe#using-metadata) to subscribe to metadata updates and update your UI in real-time.
2. Using our [backend functions](/realtime/backend) to subscribe to metadata updates in your backend.

## Limits

The Realtime API in the Trigger.dev Cloud limits the number of concurrent subscriptions, depending on your plan. If you exceed the limit, you will receive an error when trying to subscribe to a run. For more information, see our [pricing page](https://trigger.dev/pricing).

## Learn more

* Read our Realtime blog post ["How we built a real-time service that handles 20,000 updates per second](https://trigger.dev/blog/how-we-built-realtime)
* Using Realtime: [React Hooks (frontend)](/realtime/react-hooks)
* Using [Backend (server-side)](/realtime/backend)

---

## The run object

The run object schema for Realtime subscriptions

The [run object](/realtime/run-object#the-run-object) is the main object returned by Realtime subscriptions (e.g., `runs.subscribeToRun()`). It contains all the information about the run, including the run ID, task identifier, payload, output, and more.

Type-safety is supported for the run object, so you can infer the types of the run's payload and output. See [type-safety](#type-safety) for more information.

## The run object

### Properties

<ParamField type="string">
  The run ID.
</ParamField>

<ParamField type="string">
  The task identifier.
</ParamField>

<ParamField type="object">
  The input payload for the run.
</ParamField>

<ParamField type="object">
  The output result of the run.
</ParamField>

<ParamField type="Date">
  Timestamp when the run was created.
</ParamField>

<ParamField type="Date">
  Timestamp when the run was last updated.
</ParamField>

<ParamField type="number">
  Sequential number assigned to the run.
</ParamField>

<ParamField type="RunStatus">
  Current status of the run.

  <Accordion title="RunStatus enum">
    | Status               | Description                                                                                               |
    | -------------------- | --------------------------------------------------------------------------------------------------------- |
    | `WAITING_FOR_DEPLOY` | Task hasn't been deployed yet but is waiting to be executed                                               |
    | `QUEUED`             | Run is waiting to be executed by a worker                                                                 |
    | `EXECUTING`          | Run is currently being executed by a worker                                                               |
    | `REATTEMPTING`       | Run has failed and is waiting to be retried                                                               |
    | `FROZEN`             | Run has been paused by the system, and will be resumed by the system                                      |
    | `COMPLETED`          | Run has been completed successfully                                                                       |
    | `CANCELED`           | Run has been canceled by the user                                                                         |
    | `FAILED`             | Run has been completed with errors                                                                        |
    | `CRASHED`            | Run has crashed and won't be retried, most likely the worker ran out of resources, e.g. memory or storage |
    | `INTERRUPTED`        | Run was interrupted during execution, mostly this happens in development environments                     |
    | `SYSTEM_FAILURE`     | Run has failed to complete, due to an error in the system                                                 |
    | `DELAYED`            | Run has been scheduled to run at a specific time                                                          |
    | `EXPIRED`            | Run has expired and won't be executed                                                                     |
    | `TIMED_OUT`          | Run has reached it's maxDuration and has been stopped                                                     |
  </Accordion>
</ParamField>

<ParamField type="number">
  Duration of the run in milliseconds.
</ParamField>

<ParamField type="number">
  Total cost of the run in cents.
</ParamField>

<ParamField type="number">
  Base cost of the run in cents before any additional charges.
</ParamField>

<ParamField type="string[]">
  Array of tags associated with the run.
</ParamField>

<ParamField type="string">
  Key used to ensure idempotent execution.
</ParamField>

<ParamField type="Date">
  Timestamp when the run expired.
</ParamField>

<ParamField type="string">
  Time-to-live duration for the run.
</ParamField>

<ParamField type="Date">
  Timestamp when the run finished.
</ParamField>

<ParamField type="Date">
  Timestamp when the run started.
</ParamField>

<ParamField type="Date">
  Timestamp until which the run is delayed.
</ParamField>

<ParamField type="Date">
  Timestamp when the run was queued.
</ParamField>

<ParamField type="Record<string, DeserializedJson>">
  Additional metadata associated with the run.
</ParamField>

<ParamField type="SerializedError">
  Error information if the run failed.
</ParamField>

<ParamField type="boolean">
  Indicates whether this is a test run.
</ParamField>

## Type-safety

You can infer the types of the run's payload and output by passing the type of the task to the `subscribeToRun` function. This will give you type-safe access to the run's payload and output.

```ts theme={"theme":"css-variables"}
import { runs, tasks } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/my-task";

// Somewhere in your backend code
async function myBackend() {
  const handle = await tasks.trigger("my-task", { some: "data" });

  for await (const run of runs.subscribeToRun<typeof myTask>(handle.id)) {
    // This will log the run every time it changes
    console.log(run.payload.some);

    if (run.output) {
      // This will log the output if it exists
      console.log(run.output.some);
    }
  }
}
```

When using `subscribeToRunsWithTag`, you can pass a union of task types for all the possible tasks that can have the tag.

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";
import type { myTask, myOtherTask } from "./trigger/my-task";

// Somewhere in your backend code
for await (const run of runs.subscribeToRunsWithTag<typeof myTask | typeof myOtherTask>("my-tag")) {
  // You can narrow down the type based on the taskIdentifier
  switch (run.taskIdentifier) {
    case "my-task": {
      console.log("Run output:", run.output.foo); // This will be type-safe
      break;
    }
    case "my-other-task": {
      console.log("Run output:", run.output.bar); // This will be type-safe
      break;
    }
  }
}
```

This works with all realtime subscription functions:

* `runs.subscribeToRun<TaskType>()`
* `runs.subscribeToRunsWithTag<TaskType>()`
* `runs.subscribeToBatch<TaskType>()`

---

## Realtime authentication

Authenticating real-time API requests with Public Access Tokens or Trigger Tokens

To use the Realtime API, you need to authenticate your requests with Public Access Tokens or Trigger Tokens. These tokens provide secure, scoped access to your runs and can be used in both frontend and backend applications.

## Token Types

There are two types of tokens you can use with the Realtime API:

* **[Public Access Tokens](#public-access-tokens-for-subscribing-to-runs)** - Used to read and subscribe to run data. Can be used in both the frontend and backend.
* **[Trigger Tokens](#trigger-tokens-for-frontend-triggering-only)** - Used to trigger tasks from your frontend. These are more secure, single-use tokens that can only be used in the frontend.

## Public Access Tokens (for subscribing to runs)

Use Public Access Tokens to subscribe to runs and receive real-time updates in your frontend or backend.

### Creating Public Access Tokens

You can create a Public Access Token using the `auth.createPublicToken` function in your **backend** code:

```tsx theme={"theme":"css-variables"}
// Somewhere in your backend code
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken(); // 👈 this public access token has no permissions, so is pretty useless!
```

### Scopes

By default a Public Access Token has no permissions. You must specify the scopes you need when creating a Public Access Token:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      runs: true, // ❌ this token can read all runs, possibly useful for debugging/testing
    },
  },
});
```

This will allow the token to read all runs, which is probably not what you want. You can specify only certain runs by passing an array of run IDs:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      runs: ["run_1234", "run_5678"], // ✅ this token can read only these runs
    },
  },
});
```

You can scope the token to only read certain tasks:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      tasks: ["my-task-1", "my-task-2"], // 👈 this token can read all runs of these tasks
    },
  },
});
```

Or tags:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      tags: ["my-tag-1", "my-tag-2"], // 👈 this token can read all runs with these tags
    },
  },
});
```

Or a specific batch of runs:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      batch: "batch_1234", // 👈 this token can read all runs in this batch
    },
  },
});
```

You can also combine scopes. For example, to read runs with specific tags and for specific tasks:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      tasks: ["my-task-1", "my-task-2"],
      tags: ["my-tag-1", "my-tag-2"],
    },
  },
});
```

### Expiration

By default, Public Access Token's expire after 15 minutes. You can specify a different expiration time when creating a Public Access Token:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

const publicToken = await auth.createPublicToken({
  expirationTime: "1hr",
});
```

* If `expirationTime` is a string, it will be treated as a time span
* If `expirationTime` is a number, it will be treated as a Unix timestamp
* If `expirationTime` is a `Date`, it will be treated as a date

The format used for a time span is the same as the [jose package](https://github.com/panva/jose), which is a number followed by a unit. Valid units are: "sec", "secs", "second", "seconds", "s", "minute", "minutes", "min", "mins", "m", "hour", "hours", "hr", "hrs", "h", "day", "days", "d", "week", "weeks", "w", "year", "years", "yr", "yrs", and "y". It is not possible to specify months. 365.25 days is used as an alias for a year. If the string is suffixed with "ago", or prefixed with a "-", the resulting time span gets subtracted from the current unix timestamp. A "from now" suffix can also be used for readability when adding to the current unix timestamp.

### Auto-generated tokens

When you [trigger tasks](/triggering) from your backend, the `handle` received includes a `publicAccessToken` field. This token can be used to authenticate real-time requests in your frontend application.

By default, auto-generated tokens expire after 15 minutes and have a read scope for the specific run(s) that were triggered. You can customize the expiration by passing a `publicTokenOptions` object to the trigger function.

See our [triggering documentation](/triggering) for detailed examples of how to trigger tasks and get auto-generated tokens.

<Note>
  **Where should I create tokens?** The standard pattern is to create tokens in your backend code (API route, server action) after triggering a task, then pass the token to your frontend. The `handle.publicAccessToken` returned by `tasks.trigger()` already does this for you. You rarely need to create tokens inside a task itself.
</Note>

### Subscribing to runs with Public Access Tokens

Once you have a Public Access Token, you can use it to authenticate requests to the Realtime API in both backend and frontend applications.

**Backend usage:** See our [backend documentation](/realtime/backend) for examples of what you can do with Realtime in your backend once you have authenticated with a token.

**Frontend usage:** See our [React hooks documentation](/realtime/react-hooks) for examples of using tokens with frontend components.

## Trigger Tokens (for frontend triggering only)

For triggering tasks from your frontend, you need special "trigger" tokens. These tokens can only be used once to trigger a task and are more secure than regular Public Access Tokens.

### Creating Trigger Tokens

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

// Somewhere in your backend code
const triggerToken = await auth.createTriggerPublicToken("my-task");
```

### Multiple tasks

You can pass multiple tasks to create a token that can trigger multiple tasks:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

// Somewhere in your backend code
const triggerToken = await auth.createTriggerPublicToken(["my-task-1", "my-task-2"]);
```

### Multiple use

You can also create tokens that can be used multiple times:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

// Somewhere in your backend code
const triggerToken = await auth.createTriggerPublicToken("my-task", {
  multipleUse: true, // ❌ Use this with caution!
});
```

### Expiration

These tokens also expire, with the default expiration time being 15 minutes. You can specify a custom expiration time:

```ts theme={"theme":"css-variables"}
import { auth } from "@trigger.dev/sdk";

// Somewhere in your backend code
const triggerToken = await auth.createTriggerPublicToken("my-task", {
  expirationTime: "24hr",
});
```

### Triggering tasks from the frontend with Trigger Tokens

Check out our [React hooks documentation](/realtime/react-hooks) for examples of how to use Trigger Tokens in your frontend applications.

---

## Subscribe to tasks from your backend

Subscribe to run progress, stream AI output, and react to task status changes from your backend code or other tasks.

**Subscribe to runs from your server-side code or other tasks using async iterators.** Get status updates, metadata changes, and streamed data without polling.

## What's available

| Category        | What it does                                                   | Guide                                      |
| --------------- | -------------------------------------------------------------- | ------------------------------------------ |
| **Run updates** | Subscribe to run status, metadata, and tag changes             | [Run updates](/realtime/backend/subscribe) |
| **Streaming**   | Read AI output, file chunks, or any continuous data from tasks | [Streaming](/realtime/backend/streams)     |

<Note>
  To learn how to emit streams from your tasks, see [Streaming data from tasks](/tasks/streams).
</Note>

## Authentication

All backend functions support both server-side and client-side authentication:

* **Server-side**: Use your API key (automatically handled in tasks)
* **Client-side**: Generate a Public Access Token with appropriate scopes

See our [authentication guide](/realtime/auth) for detailed information on creating and using tokens.

## Quick example

Subscribe to a run:

```ts theme={"theme":"css-variables"}
import { runs, tasks } from "@trigger.dev/sdk";

// Trigger a task
const handle = await tasks.trigger("my-task", { some: "data" });

// Subscribe to real-time updates
for await (const run of runs.subscribeToRun(handle.id)) {
  console.log(`Run ${run.id} status: ${run.status}`);
}
```

---

## Run updates (backend)

Subscribe to run status changes, metadata updates, and tag changes from your backend code using async iterators.

**Subscribe to runs from your backend and get updates whenever status, metadata, or tags change.** Each function returns an async iterator that yields the run object on every change.

## runs.subscribeToRun

Subscribes to all changes to a specific run.

```ts Example theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.subscribeToRun("run_1234")) {
  console.log(run);
}
```

This function subscribes to all changes to a run. It returns an async iterator that yields the run object whenever the run is updated. The iterator will complete when the run is finished.

**Authentication**: This function supports both server-side and client-side authentication. For server-side authentication, use your API key. For client-side authentication, you must generate a public access token with read access to the specific run. See our [authentication guide](/realtime/auth) for details.

**Response**: The AsyncIterator yields the [run object](/realtime/run-object).

## runs.subscribeToRunsWithTag

Subscribes to all changes to runs with a specific tag.

```ts Example theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.subscribeToRunsWithTag("user:1234")) {
  console.log(run);
}
```

This function subscribes to all changes to runs with a specific tag. It returns an async iterator that yields the run object whenever a run with the specified tag is updated. This iterator will never complete, so you must manually break out of the loop when you no longer want to receive updates.

**Authentication**: This function supports both server-side and client-side authentication. For server-side authentication, use your API key. For client-side authentication, you must generate a public access token with read access to the specific tag. See our [authentication guide](/realtime/auth) for details.

**Response**: The AsyncIterator yields the [run object](/realtime/run-object).

## runs.subscribeToBatch

Subscribes to all changes for runs in a batch.

```ts Example theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

for await (const run of runs.subscribeToBatch("batch_1234")) {
  console.log(run);
}
```

This function subscribes to all changes for runs in a batch. It returns an async iterator that yields a run object whenever a run in the batch is updated. The iterator does not complete on its own, you must manually `break` the loop when you want to stop listening for updates.

**Authentication**: This function supports both server-side and client-side authentication. For server-side authentication, use your API key. For client-side authentication, you must generate a public access token with read access to the specific batch. See our [authentication guide](/realtime/auth) for details.

**Response**: The AsyncIterator yields the [run object](/realtime/run-object).

## Type safety

You can infer the types of the run's payload and output by passing the type of the task to the subscribe functions:

```ts theme={"theme":"css-variables"}
import { runs, tasks } from "@trigger.dev/sdk";
import type { myTask } from "./trigger/my-task";

async function myBackend() {
  const handle = await tasks.trigger("my-task", { some: "data" });

  for await (const run of runs.subscribeToRun<typeof myTask>(handle.id)) {
    // run.payload and run.output are now typed
    console.log(run.payload.some);

    if (run.output) {
      console.log(run.output.some);
    }
  }
}
```

When using `subscribeToRunsWithTag`, you can pass a union of task types:

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";
import type { myTask, myOtherTask } from "./trigger/my-task";

for await (const run of runs.subscribeToRunsWithTag<typeof myTask | typeof myOtherTask>("my-tag")) {
  // Narrow down the type based on the taskIdentifier
  switch (run.taskIdentifier) {
    case "my-task": {
      console.log("Run output:", run.output.foo); // Type-safe
      break;
    }
    case "my-other-task": {
      console.log("Run output:", run.output.bar); // Type-safe
      break;
    }
  }
}
```

## Subscribe to metadata updates from your tasks

The metadata API allows you to update custom metadata on runs and receive real-time updates when metadata changes. This is useful for tracking progress, storing intermediate results, or adding custom status information that can be monitored in real-time.

<Note>
  For frontend applications using React, see our [React hooks metadata
  documentation](/realtime/react-hooks/subscribe#using-metadata-to-show-progress-in-your-ui) for
  consuming metadata updates in your UI.
</Note>

When you update metadata from within a task using `metadata.set()`, `metadata.append()`, or other metadata methods, all subscribers to that run will automatically receive the updated run object containing the new metadata.

This makes metadata perfect for:

* Progress tracking
* Status updates
* Intermediate results
* Custom notifications

Use the metadata API within your task to update metadata in real-time. In this basic example task, we're updating the progress of a task as it processes items.

### How to subscribe to metadata updates

This example task updates the progress of a task as it processes items.

```ts theme={"theme":"css-variables"}
// Your task code
import { task, metadata } from "@trigger.dev/sdk";

export const progressTask = task({
  id: "progress-task",
  run: async (payload: { items: string[] }) => {
    const total = payload.items.length;

    for (let i = 0; i < payload.items.length; i++) {
      // Update progress metadata
      metadata.set("progress", {
        current: i + 1,
        total: total,
        percentage: Math.round(((i + 1) / total) * 100),
        currentItem: payload.items[i],
      });

      // Process the item
      await processItem(payload.items[i]);
    }

    metadata.set("status", "completed");
    return { processed: total };
  },
});

async function processItem(item: string) {
  // Simulate work
  await new Promise((resolve) => setTimeout(resolve, 1000));
}
```

We can now subscribe to the runs and receive real-time metadata updates.

```ts theme={"theme":"css-variables"}
// Somewhere in your backend code
import { runs } from "@trigger.dev/sdk";
import type { progressTask } from "./trigger/progress-task";

async function monitorProgress(runId: string) {
  for await (const run of runs.subscribeToRun<typeof progressTask>(runId)) {
    console.log(`Run ${run.id} status: ${run.status}`);

    if (run.metadata?.progress) {
      const progress = run.metadata.progress as {
        current: number;
        total: number;
        percentage: number;
        currentItem: string;
      };

      console.log(`Progress: ${progress.current}/${progress.total} (${progress.percentage}%)`);
      console.log(`Processing: ${progress.currentItem}`);
    }

    if (run.metadata?.status === "completed") {
      console.log("Task completed!");
      break;
    }
  }
}
```

For more information on how to write tasks that use the metadata API, as well as more examples, see our [run metadata docs](/runs/metadata#more-metadata-task-examples).

### Type safety

You can get type safety for your metadata by defining types:

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";
import type { progressTask } from "./trigger/progress-task";

interface ProgressMetadata {
  progress?: {
    current: number;
    total: number;
    percentage: number;
    currentItem: string;
  };
  status?: "running" | "completed" | "failed";
}

async function monitorTypedProgress(runId: string) {
  for await (const run of runs.subscribeToRun<typeof progressTask>(runId)) {
    const metadata = run.metadata as ProgressMetadata;

    if (metadata?.progress) {
      // Now you have full type safety
      console.log(`Progress: ${metadata.progress.percentage}%`);
    }
  }
}
```

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
