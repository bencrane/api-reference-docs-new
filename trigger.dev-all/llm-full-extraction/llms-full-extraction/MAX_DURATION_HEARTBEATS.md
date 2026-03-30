> Sources:
> - https://trigger.dev/docs/runs/max-duration
> - https://trigger.dev/docs/runs/heartbeats

# Max Duration & Heartbeats

## Max duration

Set a maximum duration for a task to run.

The `maxDuration` parameter sets a maximum compute time limit for tasks. When a task exceeds this duration, it will be automatically stopped. This helps prevent runaway tasks and manage compute resources effectively.

You must set a default maxDuration in your `trigger.config.ts` file, which will apply to all tasks unless overridden:

```ts /config/trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "proj_gtcwttqhhtlasxgfuhxs",
  maxDuration: 60, // 60 seconds or 1 minute
});
```

<Note>
  The minimum maxDuration is 5 seconds. If you want to avoid timeouts, set this value to a very large number of seconds.
</Note>

You can set the `maxDuration` for a run in the following ways:

* Across all your tasks in the [config](/config/config-file#max-duration)
* On a specific task
* On a specific run when you [trigger a task](/triggering#maxduration)

## How it works

The `maxDuration` is set in seconds, and is compared to the CPU time elapsed since the start of a single execution (which we call [attempts](/runs#attempts)) of the task. The CPU time is the time that the task has been actively running on the CPU, and does not include time spent waiting during the following:

* `wait.for` calls
* `triggerAndWait` calls
* `batchTriggerAndWait` calls

You can inspect the CPU time of a task inside the run function with our `usage` utility:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { task, usage } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    let currentUsage = usage.getCurrent();

    currentUsage.attempt.durationMs; // The CPU time in milliseconds since the start of the run
  },
});
```

The above value will be compared to the `maxDuration` you set. If the task exceeds the `maxDuration`, it will be stopped with the following error:

<img alt="Max duration error" />

## Configuring for a task

You can set a `maxDuration` on a specific task:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

This will override the default `maxDuration` set in the config file. If you have a config file with a default `maxDuration` of 60 seconds, and you set a `maxDuration` of 300 seconds on a task, the task will run for 300 seconds.

You can "turn off" the Max duration set in your config file for a specific task like so:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task, timeout } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: timeout.None, // No max duration
  run: async (payload: any, { ctx }) => {
    //...
  },
});
```

## Configuring for a run

You can set a `maxDuration` on a specific run when you trigger a task:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { maxDurationTask } from "./trigger/max-duration-task";

// Trigger the task with a maxDuration of 300 seconds
const run = await maxDurationTask.trigger(
  { foo: "bar" },
  {
    maxDuration: 300, // 300 seconds or 5 minutes
  }
);
```

You can also set the `maxDuration` to `timeout.None` to turn off the max duration for a specific run:

```ts /trigger/max-duration.ts theme={"theme":"css-variables"}
import { maxDurationTask } from "./trigger/max-duration-task";
import { timeout } from "@trigger.dev/sdk";

// Trigger the task with no maxDuration
const run = await maxDurationTask.trigger(
  { foo: "bar" },
  {
    maxDuration: timeout.None, // No max duration
  }
);
```

## maxDuration in run context

You can access the `maxDuration` set for a run in the run context:

```ts /trigger/max-duration-task.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const maxDurationTask = task({
  id: "max-duration-task",
  maxDuration: 300, // 300 seconds or 5 minutes
  run: async (payload: any, { ctx }) => {
    console.log(ctx.run.maxDuration); // 300
  },
});
```

## maxDuration and lifecycle functions

When a task run exceeds the `maxDuration`, the lifecycle functions `cleanup`, `onSuccess`, and `onFailure` will not be called.

---

## Heartbeats

Keep long-running or CPU-heavy tasks from being marked as stalled.

We send a heartbeat from your task to the platform every 30 seconds. If we don't receive a heartbeat within 5 minutes, we mark the run as stalled and stop it with a `TASK_RUN_STALLED_EXECUTING` error.

Code that blocks the event loop for too long (for example, a tight loop doing synchronous work on a large dataset) can prevent heartbeats from being sent. In that case, use `heartbeats.yield()` inside the loop so the runtime can yield to the event loop and send a heartbeat. You can call it every iteration; the implementation only yields when needed.

```ts theme={"theme":"css-variables"}
import { task, heartbeats } from "@trigger.dev/sdk";

export const processLargeDataset = task({
  id: "process-large-dataset",
  run: async (payload: { items: string[] }) => {
    for (const row of payload.items) {
      await heartbeats.yield();
      processRow(row);
    }
    return { processed: payload.items.length };
  },
});

function processRow(row: string) {
  // synchronous CPU-heavy work
}
```

If you see `TASK_RUN_STALLED_EXECUTING`, see [Task run stalled executing](/troubleshooting#task-run-stalled-executing) in the troubleshooting guide.

## Sending progress to Trigger.dev

To stream progress or status updates to the dashboard and your app, use [run metadata](/runs/metadata). Call `metadata.set()` (or `metadata.append()`) as the task runs. The dashboard and [Realtime](/realtime) (including `runs.subscribeToRun` and the React hooks) receive those updates as they happen. See [Progress monitoring](/realtime/backend/subscribe#progress-monitoring) for a full example.

## Sending updates to your own system

Trigger.dev doesn’t push run updates to external services. To send progress or heartbeats to your own backend (for example Supabase Realtime), call your API or client from inside the task when you want to emit an update—e.g. in the same loop where you call `heartbeats.yield()` or `metadata.set()`. Use whatever your stack supports: HTTP, the Supabase client, or another SDK.

---
