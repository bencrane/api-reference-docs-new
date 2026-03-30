> Sources:
> - https://trigger.dev/docs/tasks/overview
> - https://trigger.dev/docs/writing-tasks-introduction
> - https://trigger.dev/docs/tasks/schemaTask
> - https://trigger.dev/docs/tasks/scheduled
> - https://trigger.dev/docs/hidden-tasks
> - https://trigger.dev/docs/context
> - https://trigger.dev/docs/run-usage

# Tasks

## Tasks: Overview

Tasks are functions that can run for a long time and provide strong resilience to failure.

There are different types of tasks including regular tasks and [scheduled tasks](/tasks/scheduled).

## Hello world task and how to trigger it

Here's an incredibly simple task:

```ts /trigger/hello-world.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

const helloWorld = task({
  //1. Use a unique id for each task
  id: "hello-world",
  //2. The run function is the main function of the task
  run: async (payload: { message: string }) => {
    //3. You can write code that runs for a long time here, there are no timeouts
    console.log(payload.message);
  },
});
```

You can trigger this in two ways:

1. From the dashboard [using the "Test" feature](/run-tests).
2. Trigger it from your backend code. See the [full triggering guide here](/triggering).

Here's how to trigger a single run from elsewhere in your code:

```ts Your backend code theme={"theme":"css-variables"}
import { helloWorld } from "./trigger/hello-world";

async function triggerHelloWorld() {
  //This triggers the task and returns a handle
  const handle = await helloWorld.trigger({ message: "Hello world!" });

  //You can use the handle to check the status of the task, cancel and retry it.
  console.log("Task is running with handle", handle.id);
}
```

You can also [trigger a task from another task](/triggering), and wait for the result.

## Defining a `task`

The task function takes an object with the following fields.

### The `id` field

This is used to identify your task so it can be triggered, managed, and you can view runs in the dashboard. This must be unique in your project – we recommend making it descriptive and unique.

### The `run` function

Your custom code inside `run()` will be executed when your task is triggered. It’s an async function that has two arguments:

1. The run payload - the data that you pass to the task when you trigger it.
2. An object with `ctx` about the run (Context), and any output from the optional `init` function that runs before every run attempt.

Anything you return from the `run` function will be the result of the task. Data you return must be JSON serializable: strings, numbers, booleans, arrays, objects, and null.

### `retry` options

A task is retried if an error is thrown. By default, we retry 3 times.

You can set the number of retries and the delay between retries in the `retry` field:

```ts /trigger/retry.ts theme={"theme":"css-variables"}
export const taskWithRetries = task({
  id: "task-with-retries",
  retry: {
    maxAttempts: 10,
    factor: 1.8,
    minTimeoutInMs: 500,
    maxTimeoutInMs: 30_000,
    randomize: false,
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

| Option           | What it does                                                                                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `maxAttempts`    | Total number of attempts (including the first). Default: 3                                                                                                        |
| `factor`         | Exponential backoff multiplier. Each retry delay = previous delay x factor. With `factor: 1.8` and `minTimeoutInMs: 500`, retries wait 500ms, 900ms, 1620ms, etc. |
| `minTimeoutInMs` | Delay before the first retry                                                                                                                                      |
| `maxTimeoutInMs` | Cap on the delay between retries                                                                                                                                  |
| `randomize`      | Add jitter to retry delays to prevent multiple failing tasks from retrying in lockstep                                                                            |

<Note>Task-level retry settings override the defaults in your `trigger.config` file.</Note>

For more information read [the retrying guide](/errors-retrying).

It's also worth mentioning that you can [retry a block of code](/errors-retrying) inside your tasks as well.

### `queue` options

Queues allow you to control the concurrency of your tasks. This allows you to have one-at-a-time execution and parallel executions. There are also more advanced techniques like having different concurrencies for different sets of your users. For more information read [the concurrency & queues guide](/queue-concurrency).

```ts /trigger/one-at-a-time.ts theme={"theme":"css-variables"}
export const oneAtATime = task({
  id: "one-at-a-time",
  queue: {
    concurrencyLimit: 1,
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

### `machine` options

Some tasks require more vCPUs or GBs of RAM. You can specify these requirements in the `machine` field. For more information read [the machines guide](/machines).

```ts /trigger/heavy-task.ts theme={"theme":"css-variables"}
export const heavyTask = task({
  id: "heavy-task",
  machine: {
    preset: "large-1x", // 4 vCPU, 8 GB RAM
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

### `maxDuration` option

By default tasks can execute indefinitely, which can be great! But you also might want to set a `maxDuration` to prevent a task from running too long. You can set the `maxDuration` on a task, and all runs of that task will be stopped if they exceed the duration.

```ts /trigger/long-task.ts theme={"theme":"css-variables"}
export const longTask = task({
  id: "long-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

See our [maxDuration guide](/runs/max-duration) for more information.

## Global lifecycle hooks

<Note>When specifying global lifecycle hooks, we recommend using the `init.ts` file.</Note>

You can register global lifecycle hooks that are executed for all runs, regardless of the task. While you can still define these in the `trigger.config.ts` file, you can also register them anywhere in your codebase:

```ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onStartAttempt(({ ctx, payload, task }) => {
  console.log("Run started", ctx.run);
});

tasks.onSuccess(({ ctx, output }) => {
  console.log("Run finished", ctx.run);
});

tasks.onFailure(({ ctx, error }) => {
  console.log("Run failed", ctx.run);
});
```

### `init.ts`

If you create an `init.ts` file at the root of your trigger directory, it will be automatically loaded when a task is executed. This is useful for registering global lifecycle hooks, initializing a database connection, etc.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onStartAttempt(({ ctx, payload, task }) => {
  console.log("Run started", ctx.run);
});
```

## Lifecycle functions

<img alt="Lifecycle functions" />

### `middleware` and `locals` functions

Our task middleware system runs at the top level, executing before and after all lifecycle hooks. This allows you to wrap the entire task execution lifecycle with custom logic.

<Info>
  An error thrown in `middleware` is just like an uncaught error in the run function: it will
  propagate through to `catchError()` function and then will fail the attempt (either causing a
  retry or failing the run).
</Info>

The `locals` API allows you to share data between middleware and hooks.

```ts db.ts theme={"theme":"css-variables"}
import { locals } from "@trigger.dev/sdk";
import { logger, tasks } from "@trigger.dev/sdk";

// This would be type of your database client here
const DbLocal = locals.create<{ connect: () => Promise<void>; disconnect: () => Promise<void> }>(
  "db"
);

export function getDb() {
  return locals.getOrThrow(DbLocal);
}

export function setDb(db: { connect: () => Promise<void> }) {
  locals.set(DbLocal, db);
}

tasks.middleware("db", async ({ ctx, payload, next, task }) => {
  // This would be your database client here
  const db = locals.set(DbLocal, {
    connect: async () => {
      logger.info("Connecting to the database");
    },
    disconnect: async () => {
      logger.info("Disconnecting from the database");
    },
  });

  await db.connect();

  await next();

  await db.disconnect();
});

// Disconnect when the run is paused
tasks.onWait("db", async ({ ctx, payload, task }) => {
  const db = getDb();
  await db.disconnect();
});

// Reconnect when the run is resumed
tasks.onResume("db", async ({ ctx, payload, task }) => {
  const db = getDb();
  await db.connect();
});
```

You can access the database client using `getDb()` in your tasks `run` function and all your hooks (global or task specific):

```ts theme={"theme":"css-variables"}
import { getDb } from "./db";

export const myTask = task({
  run: async (payload: any, { ctx }) => {
    const db = getDb();
    await db.query("SELECT 1");
  },
});
```

### `onStartAttempt` function

<Info>The `onStartAttempt` function was introduced in v4.1.0</Info>

Before a task run attempt starts, the `onStartAttempt` function is called. It's useful for sending notifications, logging, and other side effects.

```ts /trigger/on-start.ts theme={"theme":"css-variables"}
export const taskWithOnStartAttempt = task({
  id: "task-with-on-start-attempt",
  onStartAttempt: async ({ payload, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

You can also define a global `onStartAttempt` function using `tasks.onStartAttempt()`.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onStartAttempt(({ ctx, payload, task }) => {
  console.log(
    `Run ${ctx.run.id} started on task ${task} attempt ${ctx.run.attempt.number}`,
    ctx.run
  );
});
```

<Info>Errors thrown in the `onStartAttempt` function will cause the attempt to fail.</Info>

If you want to execute code before just the first attempt, you can use the `onStartAttempt` function and check `ctx.run.attempt.number === 1`:

```ts /trigger/on-start-attempt.ts theme={"theme":"css-variables"}
export const taskWithOnStartAttempt = task({
  id: "task-with-on-start-attempt",
  onStartAttempt: async ({ payload, ctx }) => {
    if (ctx.run.attempt.number === 1) {
      console.log("Run started on attempt 1", ctx.run);
    }
  },
});
```

### `onWait` and `onResume` functions

These lifecycle hooks allow you to run code when a run is paused or resumed because of a wait:

```ts theme={"theme":"css-variables"}
export const myTask = task({
  id: "my-task",
  onWait: async ({ wait }) => {
    console.log("Run paused", wait);
  },
  onResume: async ({ wait }) => {
    console.log("Run resumed", wait);
  },
  run: async (payload: any, { ctx }) => {
    console.log("Run started", ctx.run);

    await wait.for({ seconds: 10 });

    console.log("Run finished", ctx.run);
  },
});
```

You can also define global `onWait` and `onResume` functions using `tasks.onWait()` and `tasks.onResume()`:

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onWait(({ ctx, payload, wait, task }) => {
  console.log("Run paused", ctx.run, wait);
});

tasks.onResume(({ ctx, payload, wait, task }) => {
  console.log("Run resumed", ctx.run, wait);
});
```

### `onSuccess` function

When a task run succeeds, the `onSuccess` function is called. It's useful for sending notifications, logging, syncing state to your database, or other side effects.

```ts /trigger/on-success.ts theme={"theme":"css-variables"}
export const taskWithOnSuccess = task({
  id: "task-with-on-success",
  onSuccess: async ({ payload, output, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

You can also define a global `onSuccess` function using `tasks.onSuccess()`.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onSuccess(({ ctx, payload, output }) => {
  console.log("Task succeeded", ctx.task.id);
});
```

<Info>
  Errors thrown in the `onSuccess` function will be ignored, but you will still be able to see them
  in the dashboard.
</Info>

### `onComplete` function

This hook is executed when a run completes, regardless of whether it succeeded or failed:

```ts /trigger/on-complete.ts theme={"theme":"css-variables"}
export const taskWithOnComplete = task({
  id: "task-with-on-complete",
  onComplete: async ({ payload, output, ctx }) => {
  if (result.ok) {
    console.log("Run succeeded", result.data);
  } else {
    console.log("Run failed", result.error);
  }
});
```

You can also define a global `onComplete` function using `tasks.onComplete()`.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onComplete(({ ctx, payload, output }) => {
  console.log("Task completed", ctx.task.id);
});
```

<Info>
  Errors thrown in the `onComplete` function will be ignored, but you will still be able to see them
  in the dashboard.
</Info>

### `onFailure` function

When a task run fails, the `onFailure` function is called. It's useful for sending notifications, logging, or other side effects. It will only be executed once the task run has exhausted all its retries.

```ts /trigger/on-failure.ts theme={"theme":"css-variables"}
export const taskWithOnFailure = task({
  id: "task-with-on-failure",
  onFailure: async ({ payload, error, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

You can also define a global `onFailure` function using `tasks.onFailure()`.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onFailure(({ ctx, payload, error }) => {
  console.log("Task failed", ctx.task.id);
});
```

<Info>
  Errors thrown in the `onFailure` function will be ignored, but you will still be able to see them
  in the dashboard.
</Info>

<Note>
  `onFailure` doesn’t fire for some of the run statuses like `Crashed`, `System failures`, and
  `Canceled`.
</Note>

### `catchError` functions

You can define a function that will be called when an error is thrown in the `run` function, that allows you to control how the error is handled and whether the task should be retried.

Read more about `catchError` in our [Errors and Retrying guide](/errors-retrying).

<Info>Uncaught errors will throw a special internal error of the type `HANDLE_ERROR_ERROR`.</Info>

### `onCancel` function

You can define an `onCancel` hook that is called when a run is cancelled. This is useful if you want to clean up any resources that were allocated for the run.

```ts theme={"theme":"css-variables"}
tasks.onCancel(({ ctx, signal }) => {
  console.log("Run cancelled", signal);
});
```

You can use the `onCancel` hook along with the `signal` passed into the run function to interrupt a call to an external service, for example using the [streamText](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-text) function from the AI SDK:

```ts theme={"theme":"css-variables"}
import { logger, tasks, schemaTask } from "@trigger.dev/sdk";
import { streamText } from "ai";
import { z } from "zod";

export const interruptibleChat = schemaTask({
  id: "interruptible-chat",
  description: "Chat with the AI",
  schema: z.object({
    prompt: z.string().describe("The prompt to chat with the AI"),
  }),
  run: async ({ prompt }, { signal }) => {
    const chunks: TextStreamPart<{}>[] = [];

    // 👇 This is a global onCancel hook, but it's inside of the run function
    tasks.onCancel(async () => {
      // We have access to the chunks here, and can save them to the database
      await saveChunksToDatabase(chunks);
    });

    try {
      const result = streamText({
        model: getModel(),
        prompt,
        experimental_telemetry: {
          isEnabled: true,
        },
        tools: {},
        abortSignal: signal, // 👈 Pass the signal to the streamText function, which aborts with the run is cancelled
        onChunk: ({ chunk }) => {
          chunks.push(chunk);
        },
      });

      const textParts = [];

      for await (const part of result.textStream) {
        textParts.push(part);
      }

      return textParts.join("");
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") {
        // streamText will throw an AbortError if the signal is aborted, so we can handle it here
      } else {
        throw error;
      }
    }
  },
});
```

The `onCancel` hook can optionally wait for the `run` function to finish, and access the output of the run:

```ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { setTimeout } from "node:timers/promises";

export const cancelExampleTask = task({
  id: "cancel-example",
  // Signal will be aborted when the task is cancelled 👇
  run: async (payload: { message: string }, { signal }) => {
    try {
      // We pass the signal to setTimeout to abort the timeout if the task is cancelled
      await setTimeout(10_000, undefined, { signal });
    } catch (error) {
      // Ignore the abort error
    }

    // Do some more work here

    return {
      message: "Hello, world!",
    };
  },
  onCancel: async ({ runPromise }) => {
    // You can await the runPromise to get the output of the task
    const output = await runPromise;
  },
});
```

<Note>
  You will have up to 30 seconds to complete the `runPromise` in the `onCancel` hook. After that
  point the process will be killed.
</Note>

<Warning>
  `onCancel` only runs if the run is actively executing. If a run is cancelled while queued or
  suspended (e.g. waiting for a token), no machine is spun up and `onCancel` will not be called.
  This is a known limitation we're planning to address. Follow the progress on our [feedback
  board](https://feedback.trigger.dev/p/call-the-onfailure-hook-for-runs-that-were-canceled-expired).
</Warning>

### `onStart` function (deprecated)

<Info>The `onStart` function was deprecated in v4.1.0. Use `onStartAttempt` instead.</Info>

When a task run starts, the `onStart` function is called. It's useful for sending notifications, logging, and other side effects.

<Warning>
  This function will only be called once per run (not per attempt). If you want to run code before
  each attempt, use a middleware function or the `onStartAttempt` function.
</Warning>

```ts /trigger/on-start.ts theme={"theme":"css-variables"}
export const taskWithOnStart = task({
  id: "task-with-on-start",
  onStart: async ({ payload, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

You can also define a global `onStart` function using `tasks.onStart()`.

```ts init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";

tasks.onStart(({ ctx, payload, task }) => {
  console.log(`Run ${ctx.run.id} started on task ${task}`, ctx.run);
});
```

<Info>Errors thrown in the `onStart` function will cause the attempt to fail.</Info>

### `init` function (deprecated)

<Warning>
  The `init` hook is deprecated and will be removed in the future. Use
  [middleware](/tasks/overview#middleware-and-locals-functions) instead.
</Warning>

This function is called before a run attempt:

```ts /trigger/init.ts theme={"theme":"css-variables"}
export const taskWithInit = task({
  id: "task-with-init",
  init: async ({ payload, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

You can also return data from the `init` function that will be available in the params of the `run`, `cleanup`, `onSuccess`, and `onFailure` functions.

```ts /trigger/init-return.ts theme={"theme":"css-variables"}
export const taskWithInitReturn = task({
  id: "task-with-init-return",
  init: async ({ payload, ctx }) => {
    return { someData: "someValue" };
  },
  run: async (payload: any, { ctx, init }) => {
    console.log(init.someData); // "someValue"
  },
});
```

<Info>Errors thrown in the `init` function will cause the attempt to fail.</Info>

### `cleanup` function (deprecated)

<Warning>
  The `cleanup` hook is deprecated and will be removed in the future. Use
  [middleware](/tasks/overview#middleware-and-locals-functions) instead.
</Warning>

This function is called after the `run` function is executed, regardless of whether the run was successful or not. It's useful for cleaning up resources, logging, or other side effects.

```ts /trigger/cleanup.ts theme={"theme":"css-variables"}
export const taskWithCleanup = task({
  id: "task-with-cleanup",
  cleanup: async ({ payload, ctx }) => {
    //...
  },
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

<Info>Errors thrown in the `cleanup` function will cause the attempt to fail.</Info>

## Next steps

<CardGroup>
  <Card title="Triggering" icon="bolt" href="/triggering">
    Learn how to trigger your tasks from your code.
  </Card>

  <Card title="Writing tasks" icon="wand-magic-sparkles" href="/writing-tasks-introduction">
    Tasks are the core of Trigger.dev. Learn how to write them.
  </Card>
</CardGroup>

---

## Writing tasks: Overview

Tasks are the core of Trigger.dev. They are long-running processes that are triggered by events.

Before digging deeper into the details of writing tasks, you should read the [fundamentals of tasks](/tasks/overview) to understand what tasks are and how they work.

## Writing tasks

| Topic                                        | Description                                                                                         |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| [Logging](/logging)                          | View and send logs and traces from your tasks.                                                      |
| [Errors & retrying](/errors-retrying)        | How to deal with errors and write reliable tasks.                                                   |
| [Wait](/wait)                                | Wait for periods of time or for external events to occur before continuing.                         |
| [Concurrency & Queues](/queue-concurrency)   | Configure what you want to happen when there is more than one run at a time.                        |
| [Realtime notifications](/realtime/overview) | Send realtime notifications from your task that you can subscribe to from your backend or frontend. |
| [Versioning](/versioning)                    | How versioning works.                                                                               |
| [Machines](/machines)                        | Configure the CPU and RAM of the machine your task runs on                                          |
| [Idempotency](/idempotency)                  | Protect against mutations happening twice.                                                          |
| [Replaying](/replaying)                      | You can replay a single task or many at once with a new version of your code.                       |
| [Max duration](/runs/max-duration)           | Set a maximum duration for your task to run.                                                        |
| [Tags](/tags)                                | Tags allow you to easily filter runs in the dashboard and when using the SDK.                       |
| [Metadata](/runs/metadata)                   | Attach a small amount of data to a run and update it as the run progresses.                         |
| [Usage](/run-usage)                          | Get compute duration and cost from inside a run, or for a specific block of code.                   |
| [Context](/context)                          | Access the context of the task run.                                                                 |
| [Bulk actions](/bulk-actions)                | Run actions on many task runs at once.                                                              |
| [Priority](/runs/priority)                   | Specify a priority when triggering a task.                                                          |
| [Hidden tasks](/hidden-tasks)                | Create tasks that are not exported from your trigger files but can still be executed.               |

## Our library of examples, guides and projects

<CardGroup>
  <Card title="Walkthrough guides" icon="book" href="/guides/introduction">
    Detailed guides for setting up Trigger.dev with popular frameworks and services, including
    Next.js, Remix, Supabase, Stripe and more.
  </Card>

  <Card title="Example tasks" icon="code" href="/guides/introduction#example-tasks">
    Task code you can copy and paste to use in your own projects, including OpenAI, Vercel AI SDK,
    Deepgram, FFmpeg, Puppeteer, Stripe, Supabase and more.
  </Card>

  <Card title="Webhook guides" icon="code" href="/guides/frameworks/webhooks-guides-overview">
    Learn how to trigger tasks from webhooks, including Next.js, Remix, Supabase and Stripe and
    more.
  </Card>

  <Card title="Example projects" icon="GitHub" href="/guides/introduction#example-projects">
    Full-stack projects demonstrating how to use Trigger.dev. Fork them in GitHub as a starting
    point for your own projects.
  </Card>
</CardGroup>

---

## schemaTask

Define tasks with a runtime payload schema and validate the payload before running the task.

The `schemaTask` function allows you to define a task with a runtime payload schema. This schema is used to validate the payload before running the task or when triggering a task directly. If the payload does not match the schema, the task will not execute.

## Usage

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

const myTask = schemaTask({
  id: "my-task",
  schema: z.object({
    name: z.string(),
    age: z.number(),
  }),
  run: async (payload) => {
    console.log(payload.name, payload.age);
  },
});
```

`schemaTask` takes all the same options as [task](/tasks/overview), with the addition of a `schema` field. The `schema` field is a schema parser function from a schema library or or a custom parser function.

<Note>
  We will probably eventually combine `task` and `schemaTask` into a single function, but because
  that would be a breaking change, we are keeping them separate for now.
</Note>

When you trigger the task directly, the payload will be validated against the schema before the [run](/runs) is created:

```ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";
import { myTask } from "./trigger/myTasks";

// This will call the schema parser function and validate the payload
await myTask.trigger({ name: "Alice", age: "oops" }); // this will throw an error

// This will NOT call the schema parser function
await tasks.trigger<typeof myTask>("my-task", { name: "Alice", age: "oops" }); // this will not throw an error
```

The error thrown when the payload does not match the schema will be the same as the error thrown by the schema parser function. For example, if you are using Zod, the error will be a `ZodError`.

We will also validate the payload every time before the task is run, so you can be sure that the payload is always valid. In the example above, the task would fail with a `TaskPayloadParsedError` error and skip retrying if the payload does not match the schema.

## Input/output schemas

Certain schema libraries, like Zod, split their type inference into "schema in" and "schema out". This means that you can define a single schema that will produce different types when triggering the task and when running the task. For example, you can define a schema that has a default value for a field, or a string coerced into a date:

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

const myTask = schemaTask({
  id: "my-task",
  schema: z.object({
    name: z.string().default("John"),
    age: z.number(),
    dob: z.coerce.date(),
  }),
  run: async (payload) => {
    console.log(payload.name, payload.age);
  },
});
```

In this case, the trigger payload type is `{ name?: string, age: number; dob: string }`, but the run payload type is `{ name: string, age: number; dob: Date }`. So you can trigger the task with a payload like this:

```ts theme={"theme":"css-variables"}
await myTask.trigger({ age: 30, dob: "2020-01-01" }); // this is valid
await myTask.trigger({ name: "Alice", age: 30, dob: "2020-01-01" }); // this is also valid
```

## `ai.tool`

The `ai.tool` function allows you to create an AI tool from an existing `schemaTask` to use with the Vercel [AI SDK](https://vercel.com/docs/ai-sdk):

```ts theme={"theme":"css-variables"}
import { ai } from "@trigger.dev/sdk/ai";
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";
import { generateText } from "ai";

const myToolTask = schemaTask({
  id: "my-tool-task",
  schema: z.object({
    foo: z.string(),
  }),
  run: async (payload: any, { ctx }) => {},
});

const myTool = ai.tool(myToolTask);

export const myAiTask = schemaTask({
  id: "my-ai-task",
  schema: z.object({
    text: z.string(),
  }),
  run: async (payload, { ctx }) => {
    const { text } = await generateText({
      prompt: payload.text,
      model: openai("gpt-4o"),
      tools: {
        myTool,
      },
    });
  },
});
```

You can also pass the `experimental_toToolResultContent` option to the `ai.tool` function to customize the content of the tool result:

```ts theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { Sandbox } from "@e2b/code-interpreter";
import { ai } from "@trigger.dev/sdk/ai";
import { schemaTask } from "@trigger.dev/sdk";
import { generateObject } from "ai";
import { z } from "zod";

const chartTask = schemaTask({
  id: "chart",
  description: "Generate a chart using natural language",
  schema: z.object({
    input: z.string().describe("The chart to generate"),
  }),
  run: async ({ input }) => {
    const code = await generateObject({
      model: openai("gpt-4o"),
      schema: z.object({
        code: z.string().describe("The Python code to execute"),
      }),
      system: `
        You are a helpful assistant that can generate Python code to be executed in a sandbox, using matplotlib.pyplot.

        For example: 
        
        import matplotlib.pyplot as plt
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()
        
        Make sure the code ends with plt.show()
      `,
      prompt: input,
    });

    const sandbox = await Sandbox.create();

    const execution = await sandbox.runCode(code.object.code);

    const firstResult = execution.results[0];

    if (firstResult.png) {
      return {
        chart: firstResult.png,
      };
    } else {
      throw new Error("No chart generated");
    }
  },
});

// This is useful if you want to return an image from the tool
export const chartTool = ai.tool(chartTask, {
  experimental_toToolResultContent: (result) => {
    return [
      {
        type: "image",
        data: result.chart,
        mimeType: "image/png",
      },
    ];
  },
});
```

You can access the current tool execution options inside the task run function using the `ai.currentToolOptions()` function:

```ts theme={"theme":"css-variables"}
import { ai } from "@trigger.dev/sdk/ai";
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

const myToolTask = schemaTask({
  id: "my-tool-task",
  schema: z.object({
    foo: z.string(),
  }),
  run: async (payload, { ctx }) => {
    const toolOptions = ai.currentToolOptions();
    console.log(toolOptions);
  },
});

export const myAiTask = ai.tool(myToolTask);
```

See the [AI SDK tool execution options docs](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling#tool-execution-options) for more details on the tool execution options.

<Note>
  `ai.tool` is compatible with `schemaTask`'s defined with Zod and ArkType schemas, or any schemas
  that implement a `.toJsonSchema()` function.
</Note>

## Supported schema types

### Zod

You can use the [Zod](https://zod.dev) schema library to define your schema. The schema will be validated using Zod's `parse` function.

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const zodTask = schemaTask({
  id: "types/zod",
  schema: z.object({
    bar: z.string(),
    baz: z.string().default("foo"),
  }),
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### Yup

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import * as yup from "yup";

export const yupTask = schemaTask({
  id: "types/yup",
  schema: yup.object({
    bar: yup.string().required(),
    baz: yup.string().default("foo"),
  }),
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### Superstruct

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { object, string } from "superstruct";

export const superstructTask = schemaTask({
  id: "types/superstruct",
  schema: object({
    bar: string(),
    baz: string(),
  }),
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### ArkType

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { type } from "arktype";

export const arktypeTask = schemaTask({
  id: "types/arktype",
  schema: type({
    bar: "string",
    baz: "string",
  }).assert,
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### @effect/schema

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import * as Schema from "@effect/schema/Schema";

// For some funny typescript reason, you cannot pass the Schema.decodeUnknownSync directly to schemaTask
const effectSchemaParser = Schema.decodeUnknownSync(
  Schema.Struct({ bar: Schema.String, baz: Schema.String })
);

export const effectTask = schemaTask({
  id: "types/effect",
  schema: effectSchemaParser,
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### runtypes

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import * as T from "runtypes";

export const runtypesTask = schemaTask({
  id: "types/runtypes",
  schema: T.Record({
    bar: T.String,
    baz: T.String,
  }),
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### valibot

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";

import * as v from "valibot";

// For some funny typescript reason, you cannot pass the v.parser directly to schemaTask
const valibotParser = v.parser(
  v.object({
    bar: v.string(),
    baz: v.string(),
  })
);

export const valibotTask = schemaTask({
  id: "types/valibot",
  schema: valibotParser,
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### typebox

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { Type } from "@sinclair/typebox";
import { wrap } from "@typeschema/typebox";

export const typeboxTask = schemaTask({
  id: "types/typebox",
  schema: wrap(
    Type.Object({
      bar: Type.String(),
      baz: Type.String(),
    })
  ),
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

### Custom parser function

You can also define a custom parser function that will be called with the payload before the task is run. The parser function should return the parsed payload or throw an error if the payload is invalid.

```ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";

export const customParserTask = schemaTask({
  id: "types/custom-parser",
  schema: (data: unknown) => {
    // This is a custom parser, and should do actual parsing (not just casting)
    if (typeof data !== "object") {
      throw new Error("Invalid data");
    }

    const { bar, baz } = data as { bar: string; baz: string };

    return { bar, baz };
  },
  run: async (payload) => {
    console.log(payload.bar, payload.baz);
  },
});
```

---

## Scheduled tasks (cron)

A task that is triggered on a recurring schedule using cron syntax.

<Note>
  Scheduled tasks are only for recurring tasks. If you want to trigger a one-off task at a future
  time, you should [use the delay option](/triggering#delay).
</Note>

## Defining a scheduled task

This task will run when any of the attached schedules trigger. They have a predefined payload with some useful properties:

```ts theme={"theme":"css-variables"}
import { schedules } from "@trigger.dev/sdk";

export const firstScheduledTask = schedules.task({
  id: "first-scheduled-task",
  run: async (payload) => {
    //when the task was scheduled to run
    //note this will be slightly different from new Date() because it takes a few ms to run the task
    console.log(payload.timestamp); //is a Date object

    //when the task was last run
    //this can be undefined if it's never been run
    console.log(payload.lastTimestamp); //is a Date object or undefined

    //the timezone the schedule was registered with, defaults to "UTC"
    //this is in IANA format, e.g. "America/New_York"
    //See the full list here: https://cloud.trigger.dev/timezones
    console.log(payload.timezone); //is a string

    //If you want to output the time in the user's timezone do this:
    const formatted = payload.timestamp.toLocaleString("en-US", {
      timeZone: payload.timezone,
    });

    //the schedule id (you can have many schedules for the same task)
    //using this you can remove the schedule, update it, etc
    console.log(payload.scheduleId); //is a string

    //you can optionally provide an external id when creating the schedule
    //usually you would set this to a userId or some other unique identifier
    //this can be undefined if you didn't provide one
    console.log(payload.externalId); //is a string or undefined

    //the next 5 dates this task is scheduled to run
    console.log(payload.upcoming); //is an array of Date objects
  },
});
```

You can see from the comments that the payload has several useful properties:

* `timestamp` - the time the task was scheduled to run, as a UTC date.
* `lastTimestamp` - the time the task was last run, as a UTC date.
* `timezone` - the timezone the schedule was registered with, defaults to "UTC". In IANA format, e.g. "America/New\_York".
* `scheduleId` - the id of the schedule that triggered the task
* `externalId` - the external id you (optionally) provided when creating the schedule
* `upcoming` - the next 5 times the task is scheduled to run

<Note>
  This task will NOT get triggered on a schedule until you attach a schedule to it. Read on for how
  to do that.
</Note>

Like all tasks they don't have timeouts, they should be placed inside a [/trigger folder](/config/config-file), and you [can configure them](/tasks/overview#defining-a-task).

## How to attach a schedule

Now that we've defined a scheduled task, we need to define when it will actually run. To do this we need to attach one or more schedules.

There are two ways of doing this:

* **Declarative:** defined on your `schedules.task`. They sync when you run the dev command or deploy.
* **Imperative:** created from the dashboard or by using the imperative SDK functions like `schedules.create()`.

<Info>
  A scheduled task can have multiple schedules attached to it, including a declarative schedule
  and/or many imperative schedules.
</Info>

### Declarative schedules

These sync when you run the [dev](/cli-dev) or [deploy](/cli-deploy) commands.

To create them you add the `cron` property to your `schedules.task()`. This property is optional and is only used if you want to add a declarative schedule to your task:

```ts theme={"theme":"css-variables"}
export const firstScheduledTask = schedules.task({
  id: "first-scheduled-task",
  //every two hours (UTC timezone)
  cron: "0 */2 * * *",
  run: async (payload, { ctx }) => {
    //do something
  },
});
```

If you use a string it will be in UTC. Alternatively, you can specify a timezone like this:

```ts theme={"theme":"css-variables"}
export const secondScheduledTask = schedules.task({
  id: "second-scheduled-task",
  cron: {
    //5am every day Tokyo time
    pattern: "0 5 * * *",
    timezone: "Asia/Tokyo",
    //optional, defaults to all environments
    //possible values are "PRODUCTION", "STAGING", "PREVIEW" and "DEVELOPMENT"
    environments: ["PRODUCTION", "STAGING"],
  },
  run: async (payload) => {},
});
```

When you run the [dev](/cli-dev) or [deploy](/cli-deploy) commands, declarative schedules will be synced. If you add, delete or edit the `cron` property it will be updated when you run these commands. You can view your schedules on the Schedules page in the dashboard.

### Imperative schedules

Alternatively you can explicitly attach schedules to a `schedules.task`. You can do this in the Schedules page in the dashboard by just pressing the "New schedule" button, or you can use the SDK to create schedules.

The advantage of imperative schedules is that they can be created dynamically, for example, you could create a schedule for each user in your database. They can also be activated, disabled, edited, and deleted without deploying new code by using the SDK or dashboard.

To use imperative schedules you need to do two things:

1. Define a task in your code using `schedules.task()`.
2. Attach 1+ schedules to the task either using the dashboard or the SDK.

## Supported cron syntax

```
*    *    *    *    *
┬    ┬    ┬    ┬    ┬
│    │    │    │    |
│    │    │    │    └ day of week (0 - 7, 1L - 7L) (0 or 7 is Sun)
│    │    │    └───── month (1 - 12)
│    │    └────────── day of month (1 - 31, L)
│    └─────────────── hour (0 - 23)
└──────────────────── minute (0 - 59)
```

"L" means the last. In the "day of week" field, 1L means the last Monday of the month. In the "day of month" field, L means the last day of the month.

We do not support seconds in the cron syntax.

## When schedules won't trigger

There are two situations when a scheduled task won't trigger:

* For Dev environments scheduled tasks will only trigger if you're running the dev CLI.
* For Staging/Production environments scheduled tasks will only trigger if the task is in the current deployment (latest version). We won't trigger tasks from previous deployments.

## Attaching schedules in the dashboard

You need to attach a schedule to a task before it will run on a schedule. You can attach static schedules in the dashboard:

<Steps>
  <Step title="Go to the Schedules page">
    In the sidebar select the "Schedules" page, then press the "New schedule" button. Or you can
    follow the onboarding and press the create in dashboard button. <img alt="Blank schedules
    page" />
  </Step>

  <Step title="Create your schedule">
    Fill in the form and press "Create schedule" when you're done. <img alt="Environment variables
    page" />

    These are the options when creating a schedule:

    | Name              | Description                                                                                   |
    | ----------------- | --------------------------------------------------------------------------------------------- |
    | Task              | The id of the task you want to attach to.                                                     |
    | Cron pattern      | The schedule in cron format.                                                                  |
    | Timezone          | The timezone the schedule will run in. Defaults to "UTC"                                      |
    | External id       | An optional external id, usually you'd use a userId.                                          |
    | Deduplication key | An optional deduplication key. If you pass the same value, it will update rather than create. |
    | Environments      | The environments this schedule will run in.                                                   |
  </Step>
</Steps>

## Attaching schedules with the SDK

You call `schedules.create()` to create a schedule from your code. Here's the simplest possible example:

```ts theme={"theme":"css-variables"}
const createdSchedule = await schedules.create({
  //The id of the scheduled task you want to attach to.
  task: firstScheduledTask.id,
  //The schedule in cron format.
  cron: "0 0 * * *",
  //this is required, it prevents you from creating duplicate schedules. It will update the schedule if it already exists.
  deduplicationKey: "my-deduplication-key",
});
```

<Note>The `task` id must be a task that you defined using `schedules.task()`.</Note>

You can create many schedules with the same `task`, `cron`, and `externalId` but only one with the same `deduplicationKey`.

This means you can have thousands of schedules attached to a single task, but only one schedule per `deduplicationKey`. Here's an example with all the options:

```ts theme={"theme":"css-variables"}
const createdSchedule = await schedules.create({
  //The id of the scheduled task you want to attach to.
  task: firstScheduledTask.id,
  //The schedule in cron format.
  cron: "0 0 * * *",
  // Optional, it defaults to "UTC". In IANA format, e.g. "America/New_York".
  // In this case, the task will run at midnight every day in New York time.
  // If you specify a timezone it will automatically work with daylight saving time.
  timezone: "America/New_York",
  //Optionally, you can specify your own IDs (like a user ID) and then use it inside the run function of your task.
  //This allows you to have per-user cron tasks.
  externalId: "user_123456",
  //You can only create one schedule with this key.
  //If you use it twice, the second call will update the schedule.
  //This is useful because you don't want to create duplicate schedules for a user.
  deduplicationKey: "user_123456-todo_reminder",
});
```

See [the SDK reference](/management/schedules/create) for full details.

### Dynamic schedules (or multi-tenant schedules)

By using the `externalId` you can have schedules for your users. This is useful for things like reminders, where you want to have a schedule for each user.

A reminder task:

```ts /trigger/reminder.ts theme={"theme":"css-variables"}
import { schedules } from "@trigger.dev/sdk";

//this task will run when any of the attached schedules trigger
export const reminderTask = schedules.task({
  id: "todo-reminder",
  run: async (payload) => {
    if (!payload.externalId) {
      throw new Error("externalId is required");
    }

    //get user using the externalId you used when creating the schedule
    const user = await db.getUser(payload.externalId);

    //send a reminder email
    await sendReminderEmail(user);
  },
});
```

Then in your backend code, you can create a schedule for each user:

```ts Next.js API route theme={"theme":"css-variables"}
import { reminderTask } from "~/trigger/reminder";

//app/reminders/route.ts
export async function POST(request: Request) {
  //get the JSON from the request
  const data = await request.json();

  //create a schedule for the user
  const createdSchedule = await schedules.create({
    task: reminderTask.id,
    //8am every day
    cron: "0 8 * * *",
    //the user's timezone
    timezone: data.timezone,
    //the user id
    externalId: data.userId,
    //this makes it impossible to have two reminder schedules for the same user
    deduplicationKey: `${data.userId}-reminder`,
  });

  //return a success response with the schedule
  return Response.json(createdSchedule);
}
```

You can also retrieve, list, delete, deactivate and re-activate schedules using the SDK. More on that later.

## Testing schedules

You can test a scheduled task in the dashboard. Note that the `scheduleId` will always come through as `sched_1234` to the run.

<Steps>
  <Step title="Go to the Test page">
    In the sidebar select the "Test" page, then select a scheduled task from the list (they have a
    clock icon on them) <img alt="Test page" />
  </Step>

  <Step title="Create your schedule">
    Fill in the form \[1]. You can select from a recent run \[2] to pre-populate the fields. Press "Run
    test" when you're ready <img alt="Schedule test form" />
  </Step>
</Steps>

## Managing schedules with the SDK

### Retrieving an existing schedule

```ts theme={"theme":"css-variables"}
const retrievedSchedule = await schedules.retrieve(scheduleId);
```

See [the SDK reference](/management/schedules/retrieve) for full details.

### Listing schedules

```ts theme={"theme":"css-variables"}
const allSchedules = await schedules.list();
```

See [the SDK reference](/management/schedules/list) for full details.

### Updating a schedule

```ts theme={"theme":"css-variables"}
const updatedSchedule = await schedules.update(scheduleId, {
  task: firstScheduledTask.id,
  cron: "0 0 1 * *",
  externalId: "ext_1234444",
  deduplicationKey: "my-deduplication-key",
});
```

See [the SDK reference](/management/schedules/update) for full details.

### Deactivating a schedule

```ts theme={"theme":"css-variables"}
const deactivatedSchedule = await schedules.deactivate(scheduleId);
```

See [the SDK reference](/management/schedules/deactivate) for full details.

### Activating a schedule

```ts theme={"theme":"css-variables"}
const activatedSchedule = await schedules.activate(scheduleId);
```

See [the SDK reference](/management/schedules/activate) for full details.

### Deleting a schedule

```ts theme={"theme":"css-variables"}
const deletedSchedule = await schedules.del(scheduleId);
```

See [the SDK reference](/management/schedules/delete) for full details.

### Getting possible timezones

You might want to show a dropdown menu in your UI so your users can select their timezone. You can get a list of all possible timezones using the SDK:

```ts theme={"theme":"css-variables"}
const timezones = await schedules.timezones();
```

See [the SDK reference](/management/schedules/timezones) for full details.

---

## Hidden tasks

Create tasks that are not exported from your trigger files but can still be executed.

Hidden tasks are tasks that are not exported from your trigger files but can still be executed. These tasks are only accessible to other tasks within the same file or module where they're defined.

```ts trigger/my-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

// This is a hidden task - not exported
const internalTask = task({
  id: "internal-processing",
  run: async (payload: any, { ctx }) => {
    // Internal processing logic
  },
});
```

Hidden tasks are useful for creating internal workflows that should only be triggered by other tasks in the same file:

```ts trigger/my-workflow.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

// Hidden task for internal use
const processData = task({
  id: "process-data",
  run: async (payload: { data: string }, { ctx }) => {
    // Process the data
    return { processed: payload.data.toUpperCase() };
  },
});

// Public task that uses the hidden task
export const mainWorkflow = task({
  id: "main-workflow",
  run: async (payload: any, { ctx }) => {
    const result = await processData.trigger({ data: payload.input });
    return result;
  },
});
```

You can also create packages of reusable tasks that can be imported and used without needing to re-export them:

```ts trigger/my-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { sendToSlack } from "@repo/tasks"; // Hidden task from another package

export const notificationTask = task({
  id: "send-notification",
  run: async (payload: any, { ctx }) => {
    await sendToSlack.trigger(payload);
  },
});
```

---

## Context

Get the context of a task run.

Context (`ctx`) is a way to get information about a run.

<Note>
  The context object does not change whilst your code is executing. This means values like
  `ctx.run.durationMs` will be fixed at the moment the `run()` function is called.
</Note>

<RequestExample>
  ```typescript Context example theme={"theme":"css-variables"}
  import { task } from "@trigger.dev/sdk";

  export const parentTask = task({
    id: "parent-task",
    run: async (payload: { message: string }, { ctx }) => {
      if (ctx.environment.type === "DEVELOPMENT") {
        return;
      }
    },
  });
  ```
</RequestExample>

## Context properties

<ResponseField name="task" type="object">
  <Expandable title="properties">
    <ResponseField name="exportName" type="string">
      The exported function name of the task e.g. `myTask` if you defined it like this: `export
                  const myTask = task(...)`.
    </ResponseField>

    <ResponseField name="id" type="string">
      The ID of the task.
    </ResponseField>

    <ResponseField name="filePath" type="string">
      The file path of the task.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="attempt" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the execution attempt.
    </ResponseField>

    <ResponseField name="number" type="number">
      The attempt number.
    </ResponseField>

    <ResponseField name="startedAt" type="date">
      The start time of the attempt.
    </ResponseField>

    <ResponseField name="backgroundWorkerId" type="string">
      The ID of the background worker.
    </ResponseField>

    <ResponseField name="backgroundWorkerTaskId" type="string">
      The ID of the background worker task.
    </ResponseField>

    <ResponseField name="status" type="string">
      The current status of the attempt.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="run" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the task run.
    </ResponseField>

    <ResponseField name="context" type="any">
      The context of the task run.
    </ResponseField>

    <ResponseField name="tags" type="array">
      An array of [tags](/tags) associated with the task run.
    </ResponseField>

    <ResponseField name="isTest" type="boolean">
      Whether this is a [test run](/run-tests).
    </ResponseField>

    <ResponseField name="createdAt" type="date">
      The creation time of the task run.
    </ResponseField>

    <ResponseField name="startedAt" type="date">
      The start time of the task run.
    </ResponseField>

    <ResponseField name="idempotencyKey" type="string">
      An optional [idempotency key](/idempotency) for the task run.
    </ResponseField>

    <ResponseField name="maxAttempts" type="number">
      The [maximum number of attempts](/triggering#maxattempts) allowed for this task run.
    </ResponseField>

    <ResponseField name="durationMs" type="number">
      The duration of the task run in milliseconds when the `run()` function is called. For live
      values use the [usage SDK functions](/run-usage).
    </ResponseField>

    <ResponseField name="costInCents" type="number">
      The cost of the task run in cents when the `run()` function is called. For live values use the
      [usage SDK functions](/run-usage).
    </ResponseField>

    <ResponseField name="baseCostInCents" type="number">
      The base cost of the task run in cents when the `run()` function is called. For live values
      use the [usage SDK functions](/run-usage).
    </ResponseField>

    <ResponseField name="version" type="string">
      The [version](/versioning) of the task run.
    </ResponseField>

    <ResponseField name="maxDuration" type="number">
      The [maximum allowed duration](/runs/max-duration) for the task run.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="queue" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the queue.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the queue.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="environment" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the environment.
    </ResponseField>

    <ResponseField name="slug" type="string">
      The slug of the environment.
    </ResponseField>

    <ResponseField name="type" type="string">
      The type of the environment (PRODUCTION, STAGING, DEVELOPMENT, or PREVIEW).
    </ResponseField>

    <ResponseField name="branchName" type="string">
      If the environment is `PREVIEW` then this will be the branch name.
    </ResponseField>

    <ResponseField name="git" type="object">
      <Expandable title="properties">
        <ResponseField name="commitAuthorName" type="string">
          The name of the commit author.
        </ResponseField>

        <ResponseField name="commitMessage" type="string">
          The message of the commit.
        </ResponseField>

        <ResponseField name="commitRef" type="string">
          The ref of the commit.
        </ResponseField>

        <ResponseField name="commitSha" type="string">
          The SHA of the commit.
        </ResponseField>

        <ResponseField name="dirty" type="boolean">
          Whether the commit is dirty, i.e. there are uncommitted changes.
        </ResponseField>

        <ResponseField name="remoteUrl" type="string">
          The remote URL of the repository.
        </ResponseField>

        <ResponseField name="pullRequestNumber" type="number">
          The number of the pull request.
        </ResponseField>

        <ResponseField name="pullRequestTitle" type="string">
          The title of the pull request.
        </ResponseField>

        <ResponseField name="pullRequestState" type="string">
          The state of the pull request (open, closed, or merged).
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="organization" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the organization.
    </ResponseField>

    <ResponseField name="slug" type="string">
      The slug of the organization.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the organization.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="project" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the project.
    </ResponseField>

    <ResponseField name="ref" type="string">
      The reference of the project.
    </ResponseField>

    <ResponseField name="slug" type="string">
      The slug of the project.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="batch" type="object">
  Optional information about the batch, if applicable.

  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The ID of the batch.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="machine" type="object">
  Optional information about the machine preset used for execution.

  <Expandable title="properties">
    <ResponseField name="name" type="string">
      The name of the machine preset.
    </ResponseField>

    <ResponseField name="cpu" type="number">
      The CPU allocation for the machine.
    </ResponseField>

    <ResponseField name="memory" type="number">
      The memory allocation for the machine.
    </ResponseField>

    <ResponseField name="centsPerMs" type="number">
      The cost in cents per millisecond for this machine preset.
    </ResponseField>
  </Expandable>
</ResponseField>

---

## Usage

Get compute duration and cost from inside a run, or for a specific block of code.

## Getting the run cost and duration

You can get the cost and duration of the current including retries of the same run.

```ts theme={"theme":"css-variables"}
import { task, usage, wait } from "@trigger.dev/sdk";

export const heavyTask = task({
  id: "heavy-task",
  machine: {
    preset: "medium-2x",
  },
  run: async (payload, { ctx }) => {
    // Do some compute
    const result = await convertVideo(payload.videoUrl);

    // Get the current cost and duration up until this line of code
    // This includes the compute time of the previous lines
    let currentUsage = usage.getCurrent();
    /* currentUsage = {
        compute: {
          attempt: {
            costInCents: 0.01700,
            durationMs: 1000,
          },
          total: {
            costInCents: 0.0255,
            durationMs: 1500,
          },
        },
        baseCostInCents: 0.0025,
        totalCostInCents: 0.028,
      } 
      */

    // In the cloud product we do not count waits towards the compute cost or duration.
    // We also don't include time between attempts or before the run starts executing your code.
    // So this line does not affect the cost or duration.
    await wait.for({ seconds: 5 });

    // This will give the same result as before the wait.
    currentUsage = usage.getCurrent();

    // Do more compute
    const result = await convertVideo(payload.videoUrl);

    // This would give a different value
    currentUsage = usage.getCurrent();
  },
});
```

<Note>
  In Trigger.dev cloud we do not include time between attempts, before your code executes, or waits
  towards the compute cost or duration.
</Note>

## Getting the run cost and duration from your backend

You can use [runs.retrieve()](/management/runs/retrieve) to get a single run or [runs.list()](/management/runs/list) to get a list of runs. The response will include `costInCents` `baseCostInCents` and `durationMs` fields.

```ts single run theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

const run = await runs.retrieve("run-id");
console.log(run.costInCents, run.baseCostInCents, run.durationMs);
const totalCost = run.costInCents + run.baseCostInCents;
```

```ts multiple runs theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

let totalCost = 0;
for await (const run of runs.list({ tag: "user_123456" })) {
  totalCost += run.costInCents + run.baseCostInCents;
  console.log(run.costInCents, run.baseCostInCents, run.durationMs);
}

console.log("Total cost", totalCost);
```

## Getting the cost and duration of a block of code

You can also wrap code with `usage.measure` to get the cost and duration of that block of code:

```ts theme={"theme":"css-variables"}
import { usage, logger } from "@trigger.dev/sdk";

// Inside a task run function, or inside a function that's called from there.
const { result, compute } = await usage.measure(async () => {
  //...Do something for 1 second
  return {
    foo: "bar",
  };
});

logger.info("Result", { result, compute });
/* result = {
    foo: "bar"
  }
  compute = {
    costInCents: 0.01700,
    durationMs: 1000,
  }
*/
```

This will work from inside the `run` function, our lifecycle hooks (like `onStart`, `onFailure`, `onSuccess`, etc.), or any function you're calling from the `run` function. It won't work for code that's not executed using Trigger.dev.

---
