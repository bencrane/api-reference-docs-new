> Sources:
> - https://trigger.dev/docs/troubleshooting
> - https://trigger.dev/docs/how-to-reduce-your-spend
> - https://trigger.dev/docs/troubleshooting-debugging-in-vscode
> - https://trigger.dev/docs/upgrading-packages
> - https://trigger.dev/docs/troubleshooting-alerts
> - https://trigger.dev/docs/troubleshooting-uptime-status
> - https://trigger.dev/docs/troubleshooting-github-issues

# Troubleshooting

## Common problems

Some common problems you might experience and their solutions

## Development

### `EACCES: permission denied`

If you see this error:

```
6090 verbose stack Error: EACCES: permission denied, rename '/Users/user/.npm/_cacache/tmp/f1bfea11' -> '/Users/user/.npm/_cacache/content-v2/sha512/31/d8/e094a47a0105d06fd246892ed1736c02eae323726ec6a3f34734eeb71308895dfba4f4f82a88ffe7e480c90b388c91fc3d9f851ba7b96db4dc33fbc65528'
```

First, clear the npm cache:

```sh theme={"theme":"css-variables"}
npm cache clean --force
```

Then change the permissions of the npm folder (if 1 doesn't work):

```sh theme={"theme":"css-variables"}
sudo chown -R $(whoami) ~/.npm
```

### Clear the build cache

Ensure you have stopped your local dev server then locate the hidden `.trigger` folder in your project and delete it. You can then restart your local dev server.

### Yarn Plug'n'Play conflicts

If you see errors like this when running `trigger.dev dev`:

```
Could not resolve "@trigger.dev/core"
The Yarn Plug'n'Play manifest forbids importing "@trigger.dev/core" here because it's not listed as a dependency of this package
```

And you're using Yarn v1.22 or another package manager, check if you have a `.pnp.cjs` file in your home directory. This can happen if you previously had Yarn Plug'n'Play enabled globally. Remove the `.pnp.cjs` file to resolve the issue.

## Deployment

Running the \[trigger.dev deploy] command builds and deploys your code. Sometimes there can be issues building your code.

You can run the deploy command with `--log-level debug` at the end. This will spit out a lot of information about the deploy. If you can't figure out the problem from the information below please join [our Discord](https://trigger.dev/discord) and create a help forum post. Do NOT share the extended debug logs publicly as they might reveal private information about your project.

You can also review the build by supplying the `--dry-run` flag. This will build your project but not deploy it. You can then inspect the build output on your machine.

Here are some common problems and their solutions:

### `Failed to build project image: Error building image`

There should be a link below the error message to the full build logs on your machine. Take a look at these to see what went wrong. Join [our Discord](https://trigger.dev/discord) and you share it privately with us if you can't figure out what's going wrong. Do NOT share these publicly as the verbose logs might reveal private information about your project.

### `Error: failed to solve: failed to resolve source metadata for docker.io/docker/dockerfile:1`

If you see this error after uninstalling Docker Desktop:

```
Error: failed to solve: failed to resolve source metadata for docker.io/docker/dockerfile:1: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH
```

This happens because Docker Desktop left behind a config file that's still trying to use its credential store. To fix this, remove or update the `~/.docker/config.json` file. You don't need Docker Desktop installed to use Trigger.dev.

### `Deployment encountered an error`

Usually there will be some useful guidance below this message. If you can't figure out what's going wrong then join [our Discord](https://trigger.dev/discord) and create a Help forum post with a link to your deployment.

### `resource_exhausted`

If you see a `resource_exhausted` error during deploy, the build may have hit resource limits on our build infrastructure. Try our [native builder](https://trigger.dev/changelog/deployments-with-native-builds).

### `No loader is configured for ".node" files`

This happens because `.node` files are native code and can't be bundled like other packages. To fix this, add your package to [`build.external`](/config/config-file#external) in the `trigger.config.ts` file like this:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    external: ["your-node-package"],
  },
});
```

### `Cannot find module '/app/lib/worker.js"` when using pino

If you see this error, add pino (and any other associated packages) to your `external` build settings in your `trigger.config.ts` file. Learn more about the `external` setting in the [config docs](/config/config-file#external).

### `Failed to index deployment` with `Column must be greater than or equal to 0, got -1`

This can occur when using `runtime: "bun"` during the indexing phase (we load and execute your task files to discover exports). A short-term workaround is to [pnpm patch](https://pnpm.io/cli/patch) the `source-map` package. See [this GitHub issue](https://github.com/triggerdotdev/trigger.dev/issues/3045) for the patch details.

### `reactDOMServer.renderToPipeableStream is not a function` when using react-email

If you see this error when using `@react-email/render`:

```
TypeError: reactDOMServer.renderToPipeableStream is not a function
    at __spreadValues.selectors (file:///node_modules/.pnpm/@react-email+render@1.0.6_react-dom@19.0.0_react@19.0.0/node_modules/@react-email/render/dist/node/index.mjs:162:37)
```

This happens because react-email packages have bundling conflicts with our build process. To fix this, add the react-email packages to your `external` build settings in your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    external: ["react", "react-dom", "@react-email/render", "@react-email/components"],
  },
});
```

### `Cannot find matching keyid`

This error occurs when using Node.js v22 with corepack, as it's not yet compatible with the latest package manager signatures. To fix this, either:

1. Downgrade to Node.js v20 (LTS), or
2. Install corepack globally: `npm i -g corepack@latest`

The corepack bug and workaround are detailed in [this issue](https://github.com/npm/cli/issues/8075).

## Project setup issues

### `The requested module 'node:events' does not provide an export named 'addAbortListener'`

If you see this error it means you're not a supported version of Node:

```
SyntaxError: The requested module 'node:events' does not provide an export named 'addAbortListener'
at ModuleJob._instantiate (node:internal/modules/esm/module_job:123:21)
at async ModuleJob.run (node:internal/modules/esm/module_job:189:5)

Node.js v19.9.0
```

You need to be on at least these minor versions:

| Version | Minimum |
| ------- | ------- |
| 18      | 18.20+  |
| 20      | 20.5+   |
| 21      | 21.0+   |
| 22      | 22.0+   |

## Runtime issues

### `Environment variable not found:`

Your code is deployed separately from the rest of your app(s) so you need to make sure that you set any environment variables you use in your tasks in the Trigger.dev dashboard. [Read the guide](/deploy-environment-variables).

### `Error: @prisma/client did not initialize yet.`

Prisma uses code generation to create the client from your schema file. This means you need to add a bit of config so we can generate this file before your tasks run: [Read the guide](/config/extensions/prismaExtension).

### Database connection requires IPv4

Trigger.dev currently only supports IPv4 database connections. If your database provider only provides an IPv6 connection string, you'll need to use an IPv4 address instead. [Upvote IPv6 support](https://triggerdev.featurebase.app/p/support-ipv6-database-connections).

### `Parallel waits are not supported`

In the current version, you can't perform more that one "wait" in parallel.

Waits include:

* `wait.for()`
* `wait.until()`
* `task.triggerAndWait()`
* `task.batchTriggerAndWait()`
* And any of our functions with `wait` in the name.

This restriction exists because we suspend the task server after a wait, and resume it when the wait is done. At the moment, if you do more than one wait, the run will never continue when deployed, so we throw this error instead.

The most common situation this happens is if you're using `Promise.all` around some of our wait functions. Instead of doing this use our built-in functions for [triggering tasks](/triggering#triggering-from-inside-another-task). We have functions that allow you to trigger different tasks in parallel.

### When triggering subtasks the parent task finishes too soon

Make sure that you always use `await` when you call `trigger`, `triggerAndWait`, `batchTrigger`, and `batchTriggerAndWait`. If you don't then it's likely the task(s) won't be triggered because the calling function process can be terminated before the networks calls are sent.

### `COULD_NOT_FIND_EXECUTOR`

If you see a `COULD_NOT_FIND_EXECUTOR` error when triggering a task, it may be caused by dynamically importing the child task. When tasks are dynamically imported, the executor may not be properly registered.

Use a top-level import instead:

```ts theme={"theme":"css-variables"}
import { myChildTask } from "~/trigger/my-child-task";

export const myTask = task({
  id: "my-task",
  run: async (payload: string) => {
    await myChildTask.trigger({ payload: "data" });
  },
});
```

Alternatively, use `tasks.trigger()` or `batch.triggerAndWait()` without importing the task:

```ts theme={"theme":"css-variables"}
import { batch } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: string) => {
    await batch.triggerAndWait([{ id: "my-child-task", payload: "data" }]);
  },
});
```

### Rate limit exceeded

The most common cause of hitting the API rate limit is if you're calling `trigger()` on a task in a loop, instead of doing this use `batchTrigger()` which will trigger multiple tasks in a single API call. You can have up to 1,000 tasks in a single batch trigger call with SDK 4.3.1+ (500 in prior versions).

View the [rate limits](/limits) page for more information.

### Runs waiting in queue due to concurrency limits

If runs are staying in the `QUEUED` state for extended periods, check your concurrency usage in the dashboard. Review how many runs are `EXECUTING` or `DEQUEUED` (these count against limits) and check if any runs are stuck in `EXECUTING` state, as they may be blocking new runs.

**Solutions:**

* **Increase concurrency limits** - If you're on a paid plan, increase your environment concurrency limit via the dashboard
* **Review queue concurrency limits** - Check if individual queues have restrictive `concurrencyLimit` settings
* **Check for stuck runs** - See if stalled runs are blocking new executions

### `Crypto is not defined`

This can happen in different situations, for example when using plain strings as idempotency keys. Support for `Crypto` without a special flag was added in Node `v19.0.0`. You will have to upgrade Node - we recommend even-numbered major releases, e.g. `v20` or `v22`. Alternatively, you can switch from plain strings to the `idempotencyKeys.create` SDK function. [Read the guide](/idempotency).

### Task run stalled executing

If you see a `TASK_RUN_STALLED_EXECUTING` error it means that we didn't receive a heartbeat from your task before the stall timeout. We automatically heartbeat runs every 30 seconds, and the heartbeat timeout is 5 minutes.

<Note>
  If this was a dev run, then most likely the `trigger.dev dev` CLI was stopped, and it wasn't an issue with your code.
</Note>

These errors can happen when code inside your task is blocking the event loop for too long. The most likely cause would be an accidental infinite loop. It could also be a CPU-heavy operation that's blocking the event loop, like nested loops with very large arrays.

If you use **Prisma 7.x**, query compilation and caching run on the main thread and can block the event loop during heavy or repeated database work. In tasks that do a lot of Prisma calls (e.g. in loops or many sequential queries), add `await heartbeats.yield()` periodically so the event loop can run and send heartbeats.

We recommend reading the [Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) guide from Node.js for common patterns that can cause this.

If you are doing a continuous CPU-heavy task, then we recommend you try using our `heartbeats.yield` function to automatically yield to the event loop periodically:

```ts theme={"theme":"css-variables"}
import { heartbeats } from "@trigger.dev/sdk";

// code inside your task
for (const row of bigDataset) {
  await heartbeats.yield(); // safe to call every iteration, we will only actually yield when we need to
  process(row); // this is a synchronous operation
}
```

<Note>
  You could also offload the CPU-heavy work to a Node.js worker thread, but this is more complex to setup currently. We are planning on adding support for this in the future.
</Note>

If the above doesn't work, then we recommend you try increasing the machine size of your task. See our [machines guide](/machines) for more information.

## Framework specific issues

### NestJS swallows all errors/exceptions

If you're using NestJS and you add code like this into your tasks you will prevent any errors from being surfaced:

```ts theme={"theme":"css-variables"}
export const simplestTask = task({
  id: "nestjs-example",
  run: async (payload) => {
    //by doing this you're swallowing any errors
    const app = await NestFactory.createApplicationContext(AppModule);
    await app.init();

    //etc...
  },
});
```

NestJS has a global exception filter that catches all errors and swallows them, so we can't receive them. Our current recommendation is to not use NestJS inside your tasks. If you're a NestJS user you can still use Trigger.dev but just don't use NestJS inside your tasks like this.

### React is not defined

If you see this error:

```
Worker failed to start ReferenceError: React is not defined
```

Either add this to your file:

```ts theme={"theme":"css-variables"}
import React from "react";
```

Or change the tsconfig jsx setting:

```json theme={"theme":"css-variables"}
{
  "compilerOptions": {
    //...
    "jsx": "react-jsx"
  }
}
```

### Next.js build failing due to missing API key in GitHub CI

This issue occurs during the Next.js app build process on GitHub CI where the Trigger.dev SDK is expecting the TRIGGER\_SECRET\_KEY environment variable to be set at build time. Next.js attempts to compile routes and creates static pages, which can cause issues with SDKs that require runtime environment variables. The solution is to mark the relevant pages as dynamic to prevent Next.js from trying to make them static. You can do this by adding the following line to the route file:

```ts theme={"theme":"css-variables"} theme={"theme":"css-variables"}
export const dynamic = "force-dynamic";
```

### Correctly passing event handlers to React components

An issue can sometimes arise when you try to pass a function directly to the `onClick` prop. This is because the function may require specific arguments or context that are not available when the event occurs. By wrapping the function call in an arrow function, you ensure that the handler is called with the correct context and any necessary arguments. For example:

This works:

```tsx theme={"theme":"css-variables"} theme={"theme":"css-variables"}
<Button onClick={() => myTask()}>Trigger my task</Button>
```

Whereas this does not work:

```tsx theme={"theme":"css-variables"} theme={"theme":"css-variables"}
<Button onClick={myTask}>Trigger my task</Button>
```

---

## How to reduce your spend

Tips and best practices to reduce your costs on Trigger.dev

## Check out your usage page regularly

Monitor your usage dashboard to understand your spending patterns. You can see:

* Your most expensive tasks
* Your total duration by task
* Number of runs by task
* Spikes in your daily usage

<img alt="Usage dashboard" />

You can view your usage page by clicking the "Organization" menu in the top left of the dashboard and then clicking "Usage".

## Create billing alerts

Configure billing alerts in your dashboard to get notified when you approach spending thresholds. This helps you:

* Catch unexpected cost increases early
* Identify runaway tasks before they become expensive

The billing alerts page includes two types of alerts:

* **Standard alerts**: Get notified at 75%, 90%, 100%, 200%, and 500% of your monthly budget
* **Spike alerts**: Catch runaway usage from bugs or errors with alerts at 10x (1000%), 20x (2000%), 50x (5000%), and 100x (10000%) of your monthly budget. We recommend keeping these enabled as a safety net.

<img alt="Billing alerts" />

You can view your billing alerts page by clicking the "Organization" menu in the top left of the dashboard and then clicking "Settings".

## Reduce your machine sizes

The larger the machine, the more it costs per second. [View the machine pricing](https://trigger.dev/pricing#computePricing).

Start with the smallest machine that works, then scale up only if needed:

```ts theme={"theme":"css-variables"}
// Default: small-1x (0.5 vCPU, 0.5 GB RAM)
export const lightTask = task({
  id: "light-task",
  // No machine config needed - uses small-1x by default
  run: async (payload) => {
    // Simple operations
  },
});

// Only use larger machines when necessary
export const heavyTask = task({
  id: "heavy-task",
  machine: "medium-1x", // 1 vCPU, 2 GB RAM
  run: async (payload) => {
    // CPU/memory intensive operations
  },
});
```

You can also override machine size when triggering if you know certain payloads need more resources. [Read more about machine sizes](/machines).

## Avoid duplicate work using idempotencyKey

Idempotency keys prevent expensive duplicate work by ensuring the same operation isn't performed multiple times. This is especially valuable during task retries or when the same trigger might fire multiple times.

When you use an idempotency key, Trigger.dev remembers the result and skips re-execution, saving you compute costs:

```ts theme={"theme":"css-variables"}
export const expensiveApiCall = task({
  id: "expensive-api-call",
  run: async (payload: { userId: string }) => {
    // This expensive operation will only run once per user
    await wait.for(
      { seconds: 30 },
      {
        idempotencyKey: `user-processing-${payload.userId}`,
        idempotencyKeyTTL: "1h",
      }
    );

    const result = await processUserData(payload.userId);
    return result;
  },
});
```

You can use idempotency keys with various wait functions:

```ts theme={"theme":"css-variables"}
// Skip waits during retries
const token = await wait.createToken({
  idempotencyKey: `daily-report-${new Date().toDateString()}`,
  idempotencyKeyTTL: "24h",
});

// Prevent duplicate child task execution
await childTask.triggerAndWait(
  { data: payload },
  {
    idempotencyKey: `process-${payload.id}`,
    idempotencyKeyTTL: "1h",
  }
);
```

The `idempotencyKeyTTL` controls how long the result is cached. Use shorter TTLs (like "1h") for time-sensitive operations, or longer ones (up to 30 days default) for expensive operations that rarely need re-execution. This prevents both unnecessary duplicate work and stale data issues.

## Do more work in parallel in a single task

Sometimes it's more efficient to do more work in a single task than split across many. This is particularly true when you're doing lots of async work such as API calls – most of the time is spent waiting, so it's an ideal candidate for doing calls in parallel inside the same task.

```ts theme={"theme":"css-variables"}
export const processItems = task({
  id: "process-items",
  run: async (payload: { items: string[] }) => {
    // Process all items in parallel
    const promises = payload.items.map((item) => processItem(item));
    // This works very well for API calls
    await Promise.all(promises);
  },
});
```

## Don't needlessly retry

When an error is thrown in a task, your run will be automatically reattempted based on your [retry settings](/tasks/overview#retry-options).

Try setting lower `maxAttempts` for less critical tasks:

```ts theme={"theme":"css-variables"}
export const apiTask = task({
  id: "api-task",
  retry: {
    maxAttempts: 2, // Don't retry forever
  },
  run: async (payload) => {
    // API calls that might fail
  },
});
```

This is very useful for intermittent errors, but if there's a permanent error you don't want to retry because you will just keep failing and waste compute. Use [AbortTaskRunError](/errors-retrying#using-aborttaskrunerror) to prevent a retry:

```ts theme={"theme":"css-variables"}
import { task, AbortTaskRunError } from "@trigger.dev/sdk";

export const someTask = task({
  id: "some-task",
  run: async (payload) => {
    const result = await doSomething(payload);

    if (!result.success) {
      // This is a known permanent error, so don't retry
      throw new AbortTaskRunError(result.error);
    }

    return result;
  },
});
```

## Use appropriate maxDuration settings

Set realistic maxDurations to prevent runs from executing for too long:

```ts theme={"theme":"css-variables"}
export const boundedTask = task({
  id: "bounded-task",
  maxDuration: 300, // 5 minutes max
  run: async (payload) => {
    // Task will be terminated after 5 minutes
  },
});
```

## Use waitpoints instead of polling

Waits longer than 5 seconds automatically checkpoint your task, meaning you don't pay for compute while waiting. Use `wait.for()`, `wait.until()`, or `triggerAndWait()` instead of polling loops.

```ts theme={"theme":"css-variables"}
import { task, wait } from "@trigger.dev/sdk";

export const waitpointTask = task({
  id: "waitpoint-task",
  run: async (payload) => {
    // This wait is free - your task is checkpointed
    await wait.for({ minutes: 5 });

    // Parent is also checkpointed while waiting for child tasks
    const result = await childTask.triggerAndWait({ data: payload });
    return result;
  },
});
```

[Read more about waitpoints](/wait-for).

## Use debounce to consolidate multiple triggers

When a task might be triggered multiple times in quick succession, use debounce to consolidate them into a single run. This is useful for document indexing, webhook aggregation, cache invalidation, and real-time sync scenarios.

```ts theme={"theme":"css-variables"}
// Multiple rapid triggers consolidate into 1 run
await updateIndex.trigger(
  { docId: "doc-123" },
  { debounce: { key: "doc-123", delay: "5s" } }
);

// Use trailing mode to process the most recent payload
await processUpdate.trigger(
  { version: 2 },
  { debounce: { key: "update-123", delay: "10s", mode: "trailing" } }
);
```

[Read more about debounce](/triggering#debounce).

---

## Debugging in VS Code

Debugging your task code in `dev` is supported via VS Code, without having to pass in any additional flags. Create a launch configuration in `.vscode/launch.json`:

```json launch.json theme={"theme":"css-variables"}
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Trigger.dev: Dev",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "runtimeExecutable": "npx",
      "runtimeArgs": ["trigger.dev@latest", "dev"],
      "skipFiles": ["<node_internals>/**"],
      "sourceMaps": true
    }
  ]
}
```

Then you can start debugging your tasks code by selecting the `Trigger.dev: Dev` configuration in the debug panel, and set breakpoints in your tasks code.

---

## How to upgrade the Trigger.dev packages

When we release fixes and new features we recommend you upgrade your Trigger.dev packages.

## Update command

Run this command in your project:

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest update
```

This will update all of the Trigger.dev packages in your project to the latest version.

## Running the CLI locally

When you run the CLI locally use the latest version for the `dev` and `deploy` commands:

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest dev
```

```sh theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

These commands will also give you the option to upgrade if you are behind on versions.

## Deploying with GitHub Actions

You can deploy using [GitHub Actions](/github-actions). We recommend that you lock your version in the workflow file so make sure to upgrade.

<Warning>
  The deploy step will fail if version mismatches are detected. It's important that you update the
  version using the steps below.
</Warning>

<Steps>
  <Step title="Find your workflow file">
    In your `.githubs/workflows` folder you can find your workflow yml files. You may have a prod
    and staging one.
  </Step>

  <Step title="Update the version for the run command">
    In the steps you'll see a `run` command. It will run the trigger.dev deploy CLI command. Make
    sure to update this version to the latest version (e.g. `npx trigger.dev@3.0.0 deploy`).
  </Step>
</Steps>

## package.json dev dependency

Instead of using `npx`, `pnpm dlx` or `yarn dlx` you can add the Trigger.dev CLI as a dev dependency to your package.json file.

For example:

```json theme={"theme":"css-variables"}
{
  "devDependencies": {
    "trigger.dev": "3.0.0"
  }
}
```

If you've done this make sure to update the version to match the `@trigger.dev/sdk` package.

Once you have added the `trigger.dev` package to your `devDependencies`, you can use `npm exec trigger.dev`, `pnpm exec trigger.dev`, or `yarn exec trigger.dev` to run the CLI.

But we recommend adding your dev and deploy commands to the `scripts` section of your `package.json` file:

```json theme={"theme":"css-variables"}
{
  "scripts": {
    "dev:trigger": "trigger dev",
    "deploy:trigger": "trigger deploy"
  }
}
```

Then you can run `npm run dev:trigger` and `npm run deploy:trigger` to run the CLI.

---

## Alerts

Get alerted when runs or deployments fail, or when deployments succeed.

We support receiving alerts for the following events:

* Run fails
* Deployment fails
* Deployment succeeds

## How to setup alerts

<Steps>
  <Step title="Create a new alert">
    Click on "Alerts" in the left hand side menu, then click on "New alert" to open the new alert modal.

    <img alt="Email alerts" />
  </Step>

  <Step title="Choose your alert method">
    Choose to be notified by email, Slack notification or webhook whenever:

    * a run fails
    * a deployment fails
    * a deployment succeeds

      <img alt="Email alerts" />
  </Step>

  <Step title="Delete or disable alerts">
    Click on the triple dot menu on the right side of the table row and select "Disable" or "Delete".

    <img alt="Disable and delete alerts" />
  </Step>
</Steps>

## Alert webhooks

For the alert webhooks you can use the SDK to parse them. Here is an example of how to parse the webhook payload in Remix:

```ts theme={"theme":"css-variables"}
import { ActionFunctionArgs, json } from "@remix-run/server-runtime";
import { webhooks, WebhookError } from "@trigger.dev/sdk";

export async function action({ request }: ActionFunctionArgs) {
  // Make sure this is a POST request
  if (request.method !== "POST") {
    return json({ error: "Method not allowed" }, { status: 405 });
  }

  try {
    // Construct and verify the webhook event
    // This secret can be found on your Alerts page when you create a webhook alert
    const event = await webhooks.constructEvent(request, process.env.ALERT_WEBHOOK_SECRET!);

    // Process the event based on its type
    switch (event.type) {
      case "alert.run.failed": {
        console.log("[Webhook Internal Test] Run failed alert webhook received", { event });
        break;
      }
      case "alert.deployment.success": {
        console.log("[Webhook Internal Test] Deployment success alert webhook received", { event });
        break;
      }
      case "alert.deployment.failed": {
        console.log("[Webhook Internal Test] Deployment failed alert webhook received", { event });
        break;
      }
      default: {
        console.log("[Webhook Internal Test] Unhandled webhook type", { event });
      }
    }

    // Return a success response
    return json({ received: true }, { status: 200 });
  } catch (err) {
    // Handle webhook errors
    if (err instanceof WebhookError) {
      console.error("Webhook error:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    if (err instanceof Error) {
      console.error("Error processing webhook:", { message: err.message });
      return json({ error: err.message }, { status: 400 });
    }

    // Handle other errors
    console.error("Error processing webhook:", { err });
    return json({ error: "Internal server error" }, { status: 500 });
  }
}
```

### Common properties

When you create a webhook alert, you'll receive different payloads depending on the type of alert. All webhooks share some common properties:

<ParamField type="string">
  A unique identifier for this webhook event
</ParamField>

<ParamField type="datetime">
  When this webhook event was created
</ParamField>

<ParamField type="string">
  The version of the webhook payload format
</ParamField>

<ParamField type="string">
  The type of alert webhook. One of: `alert.run.failed`, `alert.deployment.success`, or `alert.deployment.failed`
</ParamField>

### Run Failed Alert

This webhook is sent when a run fails. The payload is available on the `object` property:

<ParamField type="string">
  Unique identifier for the task
</ParamField>

<ParamField type="string">
  File path where the task is defined
</ParamField>

<ParamField type="string">
  Name of the exported task function
</ParamField>

<ParamField type="string">
  Version of the task
</ParamField>

<ParamField type="string">
  Version of the SDK used
</ParamField>

<ParamField type="string">
  Version of the CLI used
</ParamField>

<ParamField type="string">
  Unique identifier for the run
</ParamField>

<ParamField type="number">
  Run number
</ParamField>

<ParamField type="string">
  Current status of the run
</ParamField>

<ParamField type="datetime">
  When the run was created
</ParamField>

<ParamField type="datetime">
  When the run started executing
</ParamField>

<ParamField type="datetime">
  When the run finished executing
</ParamField>

<ParamField type="boolean">
  Whether this is a test run
</ParamField>

<ParamField type="string">
  Idempotency key for the run
</ParamField>

<ParamField type="string[]">
  Associated tags
</ParamField>

<ParamField type="object">
  Error information
</ParamField>

<ParamField type="boolean">
  Whether the run was an out-of-memory error
</ParamField>

<ParamField type="string">
  Machine preset used for the run
</ParamField>

<ParamField type="string">
  URL to view the run in the dashboard
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>

### Deployment Success Alert

This webhook is sent when a deployment succeeds. The payload is available on the `object` property:

<ParamField type="string">
  Deployment ID
</ParamField>

<ParamField type="string">
  Deployment status
</ParamField>

<ParamField type="string">
  Deployment version
</ParamField>

<ParamField type="string">
  Short code identifier
</ParamField>

<ParamField type="datetime">
  When the deployment completed
</ParamField>

<ParamField type="array">
  Array of deployed tasks with properties: id, filePath, exportName, and triggerSource
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>

### Deployment Failed Alert

This webhook is sent when a deployment fails. The payload is available on the `object` property:

<ParamField type="string">
  Deployment ID
</ParamField>

<ParamField type="string">
  Deployment status
</ParamField>

<ParamField type="string">
  Deployment version
</ParamField>

<ParamField type="string">
  Short code identifier
</ParamField>

<ParamField type="datetime">
  When the deployment failed
</ParamField>

<ParamField type="string">
  Error name
</ParamField>

<ParamField type="string">
  Error message
</ParamField>

<ParamField type="string">
  Error stack trace (optional)
</ParamField>

<ParamField type="string">
  Standard error output (optional)
</ParamField>

<ParamField type="string">
  Environment ID
</ParamField>

<ParamField type="string">
  Environment type (STAGING or PRODUCTION)
</ParamField>

<ParamField type="string">
  Environment slug
</ParamField>

<ParamField type="string">
  Organization ID
</ParamField>

<ParamField type="string">
  Organization slug
</ParamField>

<ParamField type="string">
  Organization name
</ParamField>

<ParamField type="string">
  Project ID
</ParamField>

<ParamField type="string">
  Project reference
</ParamField>

<ParamField type="string">
  Project slug
</ParamField>

<ParamField type="string">
  Project name
</ParamField>

---

## Uptime Status

Get email notifications when Trigger.dev creates, updates or resolves a platform incident.
[Subscribe](https://status.trigger.dev/)

---

## GitHub Issues

Please [join our community on Discord](https://github.com/triggerdotdev/trigger.dev/issues) to ask questions, share your projects, and get help from other developers.

---
