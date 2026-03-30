> Sources:
> - https://trigger.dev/docs/runs/metadata
> - https://trigger.dev/docs/tags
> - https://trigger.dev/docs/runs/priority

# Metadata, Tags & Priority

## Run metadata

Attach structured data to a run and update it as the task progresses. Use metadata for progress tracking, user context, intermediate results, and more.

**Metadata lets you attach up to 256KB of structured data to a run and update it while the task runs.** Subscribers (via [React hooks](/realtime/react-hooks/subscribe) or [backend](/realtime/backend/subscribe)) get those updates in real time, making metadata the simplest way to build progress bars, status indicators, and live dashboards.

You can access metadata from inside the run function, via the API, Realtime, and in the dashboard. Common uses: progress percentage, current step, user context, intermediate results.

## Usage

Add metadata to a run when triggering by passing it as an object to the `trigger` function:

```ts theme={"theme":"css-variables"}
const handle = await myTask.trigger(
  { message: "hello world" },
  { metadata: { user: { name: "Eric", id: "user_1234" } } }
);
```

You can get the current metadata at any time by calling `metadata.get()` or `metadata.current()` (only inside a run):

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Get the whole metadata object
    const currentMetadata = metadata.current();
    console.log(currentMetadata);

    // Get a specific key
    const user = metadata.get("user");
    console.log(user.name); // "Eric"
  },
});
```

Any of these methods can be called anywhere "inside" the run function, or a function called from the run function:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    doSomeWork();
  },
});

async function doSomeWork() {
  // Set the value of a specific key
  metadata.set("progress", 0.5);
}
```

If you call any of the metadata methods outside of the run function, they will have no effect:

```ts theme={"theme":"css-variables"}
import { metadata } from "@trigger.dev/sdk";

// Somewhere outside of the run function
function doSomeWork() {
  metadata.set("progress", 0.5); // This will do nothing
}
```

This means it's safe to call these methods anywhere in your code, and they will only have an effect when called inside the run function.

<Note>
  Calling `metadata.current()` or `metadata.get()` outside of the run function will always return
  undefined.
</Note>

These methods also work inside any task lifecycle hook, either attached to the specific task or the global hooks defined in your `trigger.config.ts` file.

<CodeGroup>
  ```ts myTasks.ts theme={"theme":"css-variables"}
  import { task, metadata } from "@trigger.dev/sdk";

  export const myTask = task({
    id: "my-task",
    run: async (payload: { message: string }) => {
      // Your run function work here
    },
    onStart: async () => {
      metadata.set("progress", 0.5);
    },
    onSuccess: async () => {
      metadata.set("progress", 1.0);
    },
  });
  ```

  ```ts trigger.config.ts theme={"theme":"css-variables"}
  import { defineConfig, metadata } from "@trigger.dev/sdk";

  export default defineConfig({
    project: "proj_1234",
    onStart: async () => {
      metadata.set("progress", 0.5);
    },
  });
  ```
</CodeGroup>

## Updates API

One of the more powerful features of metadata is the ability to update it as the run progresses. This is useful for tracking the progress of a run, storing intermediate results, or storing any other information that changes over time. (Combining metadata with [Realtime](/realtime) can give you a live view of the progress of your runs.)

All metadata update methods (accept for `flush` and `stream`) are synchronous and will not block the run function. We periodically flush metadata to the database in the background, so you can safely update the metadata inside a run as often as you need to, without worrying about impacting the run's performance.

### set

Set the value of a key in the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Do some more work
    metadata.set("progress", 0.5);

    // Do even more work
    metadata.set("progress", 1.0);
  },
});
```

### del

Delete a key from the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Do some more work
    metadata.set("progress", 0.5);

    // Remove the progress key
    metadata.del("progress");
  },
});
```

### replace

Replace the entire metadata object with a new object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Replace the metadata object
    metadata.replace({ user: { name: "Eric", id: "user_1234" } });
  },
});
```

### append

Append a value to an array in the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Append a value to an array
    metadata.append("logs", "Step 1 complete");

    console.log(metadata.get("logs")); // ["Step 1 complete"]
  },
});
```

### remove

Remove a value from an array in the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Append a value to an array
    metadata.append("logs", "Step 1 complete");

    // Remove a value from the array
    metadata.remove("logs", "Step 1 complete");

    console.log(metadata.get("logs")); // []
  },
});
```

### increment

Increment a numeric value in the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Increment a value
    metadata.increment("progress", 0.4);

    console.log(metadata.get("progress")); // 0.5
  },
});
```

### decrement

Decrement a numeric value in the metadata object:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.5);

    // Decrement a value
    metadata.decrement("progress", 0.4);

    console.log(metadata.get("progress")); // 0.1
  },
});
```

### stream

<Note>
  As of SDK version **4.1.0**, `metadata.stream()` has been replaced by [Realtime Streams
  v2](/tasks/streams). We recommend using the new `streams.pipe()` API for better reliability,
  unlimited stream length, and improved developer experience. The examples below are provided for
  backward compatibility.
</Note>

Capture a stream of values and make the stream available when using Realtime. See our [Realtime Streams v2](/tasks/streams) documentation for the recommended approach.

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    const readableStream = new ReadableStream({
      start(controller) {
        controller.enqueue("Step 1 complete");
        controller.enqueue("Step 2 complete");
        controller.enqueue("Step 3 complete");
        controller.close();
      },
    });

    // IMPORTANT: you must await the stream method
    const stream = await metadata.stream("logs", readableStream);

    // You can read from the returned stream locally
    for await (const value of stream) {
      console.log(value);
    }
  },
});
```

`metadata.stream` accepts any `AsyncIterable` or `ReadableStream` object. The stream will be captured and made available in the Realtime API. So for example, you could pass the body of a fetch response to `metadata.stream` to capture the response body and make it available in Realtime:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { url: string }) => {
    logger.info("Streaming response", { url });

    const response = await fetch(url);

    if (!response.body) {
      throw new Error("Response body is not readable");
    }

    const stream = await metadata.stream(
      "fetch",
      response.body.pipeThrough(new TextDecoderStream())
    );

    let text = "";

    for await (const chunk of stream) {
      logger.log("Received chunk", { chunk });

      text += chunk;
    }

    return { text };
  },
});
```

Or the results of a streaming call to the OpenAI SDK:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export const myTask = task({
  id: "my-task",
  run: async (payload: { prompt: string }) => {
    const completion = await openai.chat.completions.create({
      messages: [{ role: "user", content: payload.prompt }],
      model: "gpt-3.5-turbo",
      stream: true,
    });

    const stream = await metadata.stream("openai", completion);

    let text = "";

    for await (const chunk of stream) {
      logger.log("Received chunk", { chunk });

      text += chunk.choices.map((choice) => choice.delta?.content).join("");
    }

    return { text };
  },
});
```

### flush

Flush the metadata to the database. The SDK will automatically flush the metadata periodically, so you don't need to call this method unless you need to ensure that the metadata is persisted immediately.

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Flush the metadata to the database
    await metadata.flush();
  },
});
```

## Fluent API

All of the update methods can be chained together in a fluent API:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    metadata
      .set("progress", 0.1)
      .append("logs", "Step 1 complete")
      .increment("progress", 0.4)
      .decrement("otherProgress", 0.1);
  },
});
```

## Parent & root updates

Tasks that have been triggered by a parent task (a.k.a. a "child task") can update the metadata of the parent task. This is useful for propagating progress information up the task hierarchy. You can also update the metadata of the root task (root = the initial task that was triggered externally, like from your backend).

To update the parent task's metadata, use the `metadata.parent` accessor:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myParentTask = task({
  id: "my-parent-task",
  run: async (payload: { message: string }) => {
    // Do some work
    metadata.set("progress", 0.1);

    // Trigger a child task
    await childTask.triggerAndWait({ message: "hello world" });
  },
});

export const childTask = task({
  id: "child-task",
  run: async (payload: { message: string }) => {
    // This will update the parent task's metadata
    metadata.parent.set("progress", 0.5);
  },
});
```

All of the update methods are available on `metadata.parent` and `metadata.root`:

```ts theme={"theme":"css-variables"}
metadata.parent.set("progress", 0.5);
metadata.parent.append("logs", "Step 1 complete");
metadata.parent.remove("logs", "Step 1 complete");
metadata.parent.increment("progress", 0.4);
metadata.parent.decrement("otherProgress", 0.1);
metadata.parent.stream("llm", readableStream); // Use streams.pipe() instead (v4.1+)

metadata.root.set("progress", 0.5);
metadata.root.append("logs", "Step 1 complete");
metadata.root.remove("logs", "Step 1 complete");
metadata.root.increment("progress", 0.4);
metadata.root.decrement("otherProgress", 0.1);
metadata.root.stream("llm", readableStream); // Use streams.pipe() instead (v4.1+)
```

You can also chain the update methods together:

```ts theme={"theme":"css-variables"}
metadata.parent
  .set("progress", 0.1)
  .append("logs", "Step 1 complete")
  .increment("progress", 0.4)
  .decrement("otherProgress", 0.1);
```

### Example

An example of where you might use parent and root updates is in a task that triggers multiple child tasks in parallel. You could use the parent metadata to track the progress of the child tasks and update the parent task's progress as each child task completes:

```ts theme={"theme":"css-variables"}
import { CSVRow, UploadedFileData, parseCSVFromUrl } from "@/utils";
import { batch, logger, metadata, schemaTask } from "@trigger.dev/sdk";

export const handleCSVRow = schemaTask({
  id: "handle-csv-row",
  schema: CSVRow,
  run: async (row, { ctx }) => {
    // Do some work with the row

    // Update the parent task's metadata with the progress of this row
    metadata.parent.increment("processedRows", 1).append("rowRuns", ctx.run.id);

    return row;
  },
});

export const handleCSVUpload = schemaTask({
  id: "handle-csv-upload",
  schema: UploadedFileData,
  run: async (file, { ctx }) => {
    metadata.set("status", "fetching");

    const rows = await parseCSVFromUrl(file.url);

    metadata.set("status", "processing").set("totalRows", rows.length);

    const results = await batch.triggerAndWait<typeof handleCSVRow>(
      rows.map((row) => ({ id: "handle-csv-row", payload: row }))
    );

    metadata.set("status", "complete");

    return {
      file,
      rows,
      results,
    };
  },
});
```

Combined with [Realtime](/realtime), you could use this to show a live progress bar of the CSV processing in your frontend, like this:

<video />

## More metadata task examples

Using metadata updates in conjunction with our [Realtime React hooks](/realtime/react-hooks/overview) can be a powerful way to build real-time UIs. Here are some example tasks demonstrating how to use metadata in your tasks to track progress, status, and more:

### Progress tracking

Track progress with percentage and current step:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const batchProcessingTask = task({
  id: "batch-processing",
  run: async (payload: { records: any[] }) => {
    for (let i = 0; i < payload.records.length; i++) {
      const record = payload.records[i];

      // Update progress
      metadata.set("progress", {
        step: i + 1,
        total: payload.records.length,
        percentage: Math.round(((i + 1) / payload.records.length) * 100),
        currentRecord: record.id,
      });

      await processRecord(record);
    }
  },
});
```

### Status updates with logs

Append log entries while maintaining status:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const deploymentTask = task({
  id: "deployment",
  run: async (payload: { version: string }) => {
    metadata.set("status", "initializing");
    metadata.append("logs", "Starting deployment...");

    // Step 1
    metadata.set("status", "building");
    metadata.append("logs", "Building application...");
    await buildApplication();

    // Step 2
    metadata.set("status", "deploying");
    metadata.append("logs", "Deploying to production...");
    await deployToProduction();

    // Step 3
    metadata.set("status", "verifying");
    metadata.append("logs", "Running health checks...");
    await runHealthChecks();

    metadata.set("status", "completed");
    metadata.append("logs", "Deployment successful!");
  },
});
```

### User context and notifications

Store user information and notification preferences:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const userTask = task({
  id: "user-task",
  run: async (payload: { userId: string; action: string }) => {
    // Set user context in metadata
    metadata.set("user", {
      id: payload.userId,
      action: payload.action,
      startedAt: new Date().toISOString(),
    });

    // Update status for user notifications
    metadata.set("notification", {
      type: "info",
      message: `Starting ${payload.action} for user ${payload.userId}`,
    });

    await performUserAction(payload);

    metadata.set("notification", {
      type: "success",
      message: `${payload.action} completed successfully`,
    });
  },
});
```

## Metadata propagation

Metadata is NOT propagated to child tasks. If you want to pass metadata to a child task, you must do so explicitly:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    await metadata.set("progress", 0.5);
    await childTask.trigger(payload, { metadata: metadata.current() });
  },
});
```

## Type-safe metadata

The metadata APIs are currently loosely typed, accepting any object that is JSON-serializable:

```ts theme={"theme":"css-variables"}
// ❌ You can't pass a top-level array
const handle = await myTask.trigger(
  { message: "hello world" },
  { metadata: [{ user: { name: "Eric", id: "user_1234" } }] }
);

// ❌ You can't pass a string as the entire metadata:
const handle = await myTask.trigger(
  { message: "hello world" },
  { metadata: "this is the metadata" }
);

// ❌ You can't pass in a function or a class instance
const handle = await myTask.trigger(
  { message: "hello world" },
  { metadata: { user: () => "Eric", classInstance: new HelloWorld() } }
);

// ✅ You can pass in dates and other JSON-serializable objects
const handle = await myTask.trigger(
  { message: "hello world" },
  { metadata: { user: { name: "Eric", id: "user_1234" }, date: new Date() } }
);
```

<Note>
  If you pass in an object like a Date, it will be serialized to a string when stored in the
  metadata. That also means that when you retrieve it using `metadata.get()` or
  `metadata.current()`, you will get a string back. You will need to deserialize it back to a Date
  object if you need to use it as a Date.
</Note>

We recommend wrapping the metadata API in a [Zod](https://zod.dev) schema (or your validator library of choice) to provide type safety:

```ts theme={"theme":"css-variables"}
import { task, metadata } from "@trigger.dev/sdk";
import { z } from "zod";

const Metadata = z.object({
  user: z.object({
    name: z.string(),
    id: z.string(),
  }),
  date: z.coerce.date(), // Coerce the date string back to a Date object
});

type Metadata = z.infer<typeof Metadata>;

// Helper function to get the metadata object in a type-safe way
// Note: you would probably want to use .safeParse instead of .parse in a real-world scenario
function getMetadata() {
  return Metadata.parse(metadata.current());
}

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }) => {
    const metadata = getMetadata();
    console.log(metadata.user.name); // "Eric"
    console.log(metadata.user.id); // "user_1234"
    console.log(metadata.date); // Date object
  },
});
```

## Inspecting metadata

### Dashboard

You can view the metadata for a run in the Trigger.dev dashboard. The metadata will be displayed in the run details view:

<img alt="View run metadata dashboard" />

### API

You can use the `runs.retrieve()` SDK function to get the metadata for a run:

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

const run = await runs.retrieve("run_1234");

console.log(run.metadata);
```

See the [API reference](/management/runs/retrieve) for more information.

## Size limit

The maximum size of the metadata object is 256KB. If you exceed this limit, the SDK will throw an error. If you are self-hosting Trigger.dev, you can increase this limit by setting the `TASK_RUN_METADATA_MAXIMUM_SIZE` environment variable. For example, to increase the limit to 16KB, you would set `TASK_RUN_METADATA_MAXIMUM_SIZE=16384`.

---

## Tags

Tags allow you to easily filter runs in the dashboard and when using the SDK.

## What are tags?

We support up to 10 tags per run. Each one must be a string between 1 and 128 characters long.

We recommend prefixing your tags with their type and then an underscore or colon. For example, `user_123456` or `video:123`.

<Info>
  Many great APIs, like Stripe, already prefix their IDs with the type and an underscore. Like
  `cus_123456` for a customer.
</Info>

We don't enforce prefixes but if you use them you'll find it easier to filter and it will be clearer what the tag represents.

## How to add tags

There are two ways to add tags to a run:

1. When triggering the run.
2. Inside the `run` function, using `tags.add()`.

### 1. Adding tags when triggering the run

You can add tags when triggering a run using the `tags` option. All the different [trigger](/triggering) methods support this.

<CodeGroup>
  ```ts trigger theme={"theme":"css-variables"}
  const handle = await myTask.trigger(
    { message: "hello world" },
    { tags: ["user_123456", "org_abcdefg"] }
  );
  ```

  ```ts batchTrigger theme={"theme":"css-variables"}
  const batch = await myTask.batchTrigger([
    {
      payload: { message: "foo" },
      options: { tags: "product_123456" },
    },
    {
      payload: { message: "bar" },
      options: { tags: ["user_123456", "product_3456789"] },
    },
  ]);
  ```
</CodeGroup>

This will create a run with the tags `user_123456` and `org_abcdefg`. They look like this in the runs table:

<img alt="How tags appear in the dashboard" />

### 2. Adding tags inside the `run` function

Use the `tags.add()` function to add tags to a run from inside the `run` function. This will add the tag `product_1234567` to the run:

```ts theme={"theme":"css-variables"}
import { task, tags } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { message: string }, { ctx }) => {
    // Get the tags from when the run was triggered using the context
    // This is not updated if you add tags during the run
    logger.log("Tags from the run context", { tags: ctx.run.tags });

    // Add tags during the run (a single string or array of strings)
    await tags.add("product_1234567");
  },
});
```

Reminder: you can only have up to 10 tags per run. If you call `tags.add()` and the total number of tags will be more than 10 we log an error and ignore the new tags. That includes tags from triggering and from inside the run function.

### Propagating tags to child runs

Tags do not propagate to child runs automatically. By default runs have no tags and you have to set them explicitly.

It's easy to propagate tags if you want:

```ts theme={"theme":"css-variables"}
export const myTask = task({
  id: "my-task",
  run: async (payload: Payload, { ctx }) => {
    // Pass the tags from ctx into the child run
    const { id } = await otherTask.trigger(
      { message: "triggered from myTask" },
      { tags: ctx.run.tags }
    );
  },
});
```

## Filtering runs by tags

You can filter runs by tags in the dashboard and in the SDK.

### In the dashboard

On the Runs page open the filter menu, choose "Tags" and then start typing in the name of the tag you want to filter by. You can select it and it will restrict the results to only runs with that tag. You can add multiple tags to filter by more than one.

<img alt="Filter by tags" />

### Using `runs.list()`

You can provide filters to the `runs.list` SDK function, including an array of tags.

```ts theme={"theme":"css-variables"}
import { runs } from "@trigger.dev/sdk";

// Loop through all runs with the tag "user_123456" that have completed
for await (const run of runs.list({ tag: "user_123456", status: ["COMPLETED"] })) {
  console.log(run.id, run.taskIdentifier, run.finishedAt, run.tags);
}
```

---

## Priority

Specify a priority when triggering a run.

You can set a priority when you trigger a run. This allows you to prioritize some of your runs over others, so they are started sooner. This is very useful when:

* You have critical work that needs to start more quickly (and you have long queues).
* You want runs for your premium users to take priority over free users.

The value for priority is a time offset in seconds that determines the order of dequeuing.

<img alt="Priority runs" />

If you specify a priority of `10` the run will dequeue before runs that were triggered with no priority 8 seconds ago, like in this example:

```ts theme={"theme":"css-variables"}
// no priority = 0
await myTask.trigger({ foo: "bar" });

//... imagine 8s pass by

// this run will start before the run above that was triggered 8s ago (with no priority)
await myTask.trigger({ foo: "bar" }, { priority: 10 });
```

If you passed a value of `3600` the run would dequeue before runs that were triggered an hour ago (with no priority).

<Note>
  Setting a high priority will not allow you to beat runs from other organizations. It will only affect the order of your own runs.
</Note>

---
