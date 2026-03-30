> Sources:
> - https://trigger.dev/docs/guides/example-projects/anchor-browser-web-scraper
> - https://trigger.dev/docs/guides/example-projects/batch-llm-evaluator
> - https://trigger.dev/docs/guides/example-projects/claude-changelog-generator
> - https://trigger.dev/docs/guides/example-projects/claude-github-wiki
> - https://trigger.dev/docs/guides/example-projects/claude-thinking-chatbot
> - https://trigger.dev/docs/guides/example-projects/cursor-background-agent
> - https://trigger.dev/docs/guides/example-projects/human-in-the-loop-workflow
> - https://trigger.dev/docs/guides/example-projects/mastra-agents-with-memory
> - https://trigger.dev/docs/guides/example-projects/meme-generator-human-in-the-loop
> - https://trigger.dev/docs/guides/example-projects/openai-agent-sdk-guardrails
> - https://trigger.dev/docs/guides/example-projects/openai-agents-sdk-typescript-playground
> - https://trigger.dev/docs/guides/example-projects/product-image-generator
> - https://trigger.dev/docs/guides/example-projects/realtime-csv-importer
> - https://trigger.dev/docs/guides/example-projects/realtime-fal-ai
> - https://trigger.dev/docs/guides/example-projects/smart-spreadsheet
> - https://trigger.dev/docs/guides/example-projects/turborepo-monorepo-prisma
> - https://trigger.dev/docs/guides/example-projects/vercel-ai-sdk-deep-research
> - https://trigger.dev/docs/guides/example-projects/vercel-ai-sdk-image-generator

# Example Projects

## Automated website monitoring with Anchor Browser

Automated web monitoring using Trigger.dev's task scheduling and Anchor Browser's AI-powered browser automation.

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

## Overview

This example demonstrates automated web monitoring using Trigger.dev's task scheduling and Anchor Browser's AI-powered browser automation tools.

The task runs daily at 5pm ET to find the cheapest Broadway tickets available for same-day shows.

**How it works:**

* Trigger.dev schedules and executes the monitoring task
* Anchor Browser spins up a remote browser session with an AI agent
* The AI agent uses computer vision and natural language processing to analyze the TDF website
* AI agent returns the lowest-priced show with specific details: name, price, and showtime

## Tech stack

* **[Node.js](https://nodejs.org)** runtime environment (version 18.2 or higher)
* **[Trigger.dev](https://trigger.dev)** for task scheduling and task orchestration
* **[Anchor Browser](https://anchorbrowser.io/)** for AI-powered browser automation
* **[Playwright](https://playwright.dev/)** for browser automation libraries (handled via external dependencies)

## GitHub repo

<Card title="View the Anchor Browser web scraper repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Relevant code

### Broadway ticket monitor task

This task runs daily at 5pm ET, in [src/trigger/broadway-monitor.ts](https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper/src/trigger/broadway-monitor.ts):

```ts theme={"theme":"css-variables"}
import { schedules } from "@trigger.dev/sdk";
import Anchorbrowser from "anchorbrowser";

export const broadwayMonitor = schedules.task({
  id: "broadway-ticket-monitor",
  cron: "0 21 * * *",
  run: async (payload, { ctx }) => {
    const client = new Anchorbrowser({
      apiKey: process.env.ANCHOR_BROWSER_API_KEY!,
    });

    let session;
    try {
      // Create explicit session to get live view URL
      session = await client.sessions.create();
      console.log(`Session ID: ${session.data.id}`);
      console.log(`Live View URL: https://live.anchorbrowser.io?sessionId=${session.data.id}`);

      const response = await client.tools.performWebTask({
        sessionId: session.data.id,
        url: "https://www.tdf.org/discount-ticket-programs/tkts-by-tdf/tkts-live/",
        prompt: `Look for the "Broadway Shows" section on this page. Find the show with the absolute lowest starting price available right now and return the show name, current lowest price, and show time. Be very specific about the current price you see. Format as: Show: [name], Price: [exact current price], Time: [time]`,
      });

      console.log("Raw response:", response);

      const result = response.data.result?.result || response.data.result || response.data;

      if (result && typeof result === "string" && result.includes("Show:")) {
        console.log(`🎭 Best Broadway Deal Found!`);
        console.log(result);

        return {
          success: true,
          bestDeal: result,
          liveViewUrl: `https://live.anchorbrowser.io?sessionId=${session.data.id}`,
        };
      } else {
        console.log("No Broadway deals found today");
        return { success: true, message: "No deals found" };
      }
    } finally {
      if (session?.data?.id) {
        try {
          await client.sessions.delete(session.data.id);
        } catch (cleanupError) {
          console.warn("Failed to cleanup session:", cleanupError);
        }
      }
    }
  },
});
```

### Build configuration

Since Anchor Browser uses browser automation libraries (Playwright) under the hood, we need to configure Trigger.dev to handle these dependencies properly by excluding them from the build bundle in [trigger.config.ts](https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper/trigger.config.ts):

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "proj_your_project_id_here", // Get from Trigger.dev dashboard
  maxDuration: 3600, // 1 hour - plenty of time for web automation
  dirs: ["./src/trigger"],
  build: {
    external: ["playwright-core", "playwright", "chromium-bidi"],
  },
});
```

## Learn more

* View the [Anchor Browser docs](https://anchorbrowser.io/docs) to learn more about Anchor Browser's AI-powered browser automation tools.
* Check out the source code for the [Anchor Browser web scraper repo](https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper) on GitHub.
* Browser our [example projects](/guides/introduction) to see how you can use Trigger.dev with other services.

---

## Next.js Batch LLM Evaluator

This example Next.js project evaluates multiple LLM models using the Vercel AI SDK and streams updates to the frontend using Trigger.dev Realtime.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app with [Prisma](https://www.prisma.io/) for the database.
* Trigger.dev [Realtime](https://trigger.dev/launchweek/0/realtime) to stream updates to the frontend.
* Work with multiple LLM models using the Vercel [AI SDK](https://sdk.vercel.ai/docs/introduction). (OpenAI, Anthropic, XAI)
* Distribute tasks across multiple tasks using the new [`batch.triggerByTaskAndWait`](https://trigger.dev/docs/triggering#batch-triggerbytaskandwait) method.

## GitHub repo

<Card title="View the Batch LLM Evaluator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/batch-llm-evaluator">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* View the Trigger.dev task code in the [src/trigger/batch.ts](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/trigger/batch.ts) file.
* The `evaluateModels` task uses the `batch.triggerByTaskAndWait` method to distribute the task to the different LLM models.
* It then passes the results through to a `summarizeEvals` task that calculates some dummy "tags" for each LLM response.
* We use a [useRealtimeRunsWithTag](/realtime/react-hooks/subscribe#userealtimerunswithtag) hook to subscribe to the different evaluation tasks runs in the [src/components/llm-evaluator.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/llm-evaluator.tsx) file.
* We then pass the relevant run down into three different components for the different models:
  * The `AnthropicEval` component: [src/components/evals/Anthropic.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/Anthropic.tsx)
  * The `XAIEval` component: [src/components/evals/XAI.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/XAI.tsx)
  * The `OpenAIEval` component: [src/components/evals/OpenAI.tsx](https://github.com/triggerdotdev/examples/blob/main/batch-llm-evaluator/src/components/evals/OpenAI.tsx)
* Each of these components then uses [useRealtimeRunWithStreams](/realtime/react-hooks/streams#userealtimerunwithstreams) to subscribe to the different LLM responses.

<Note>
  This example uses the older `useRealtimeRunWithStreams` hook. For new projects, consider using the new [`useRealtimeStream`](/realtime/react-hooks/streams#userealtimestream-recommended) hook (SDK 4.1.0+) for a simpler API and better type safety with defined streams.
</Note>

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Changelog generator using Claude Agent SDK

Automatically generate changelogs from your git commit history using the Claude Agent SDK and Trigger.dev.

## Overview

This demo how to build an AI agent using the Claude Agent SDK that explores GitHub commits, investigates unclear changes by fetching diffs on demand, and generates developer-friendly changelogs.

## Tech stack

* **[Next.js](https://nextjs.org)** – Frontend framework using App Router
* **[Claude Agent SDK](https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk)** – Anthropic's agent SDK for building AI agents with custom tools
* **[Trigger.dev](https://trigger.dev)** – workflow orchestration with real-time streaming, observability, and deployment
* **[Octokit](https://github.com/octokit/octokit.js)** – GitHub API client for fetching commits and diffs

## Demo video

<video />

## GitHub repo

<Card title="View the changelog generator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/changelog-generator">
  Click here to view the full open source code for this project in our examples repository on
  GitHub. You can fork it and use it as a starting point for your own project.
</Card>

## How it works

The agent workflow:

1. **Receive request** – User provides a GitHub repo URL and date range
2. **List commits** – Agent calls `list_commits` MCP tool to get all commits
3. **Analyze commits** – Agent categorizes each commit:
   * Skip trivial commits (typos, formatting)
   * Include clear features/improvements directly
   * Investigate unclear commits by fetching their diffs
4. **Generate changelog** – Agent writes a categorized markdown changelog
5. **Stream output** – Changelog streams to the frontend in real-time

## Features

* **Two-phase analysis** – Lists all commits first, then selectively fetches diffs only for ambiguous ones
* **Custom tools** – `list_commits` and `get_commit_diff` called autonomously by Claude
* **Real-time streaming** – Changelog streams to the frontend as it's generated via Trigger.dev Realtime
* **Live observability** – Agent phase, turn count, and tool calls broadcast via run metadata
* **Private repo support** – Optional GitHub token for private repositories

## Relevant code

| File                                                                                                                                                 | Description                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [`trigger/generate-changelog.ts`](https://github.com/triggerdotdev/examples/blob/main/changelog-generator/trigger/generate-changelog.ts)             | Main task with custom tools            |
| [`trigger/changelog-stream.ts`](https://github.com/triggerdotdev/examples/blob/main/changelog-generator/trigger/changelog-stream.ts)                 | Stream definition for real-time output |
| [`app/api/generate-changelog/route.ts`](https://github.com/triggerdotdev/examples/blob/main/changelog-generator/app/api/generate-changelog/route.ts) | API endpoint that triggers the task    |
| [`app/response/[runId]/page.tsx`](https://github.com/triggerdotdev/examples/blob/main/changelog-generator/app/response/%5BrunId%5D/page.tsx)         | Streaming display page                 |

## trigger.config.ts

You need to mark the Claude Agent SDK as external in your trigger.config.ts file.

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: process.env.TRIGGER_PROJECT_REF!,
  runtime: "node",
  logLevel: "log",
  maxDuration: 300,
  build: {
    external: ["@anthropic-ai/claude-agent-sdk"],
  },
  machine: "small-2x",
});
```

<Note>
  Adding packages to `external` prevents them from being bundled, which is necessary for the Claude
  Agent SDK. See the [build configuration docs](/config/config-file#external) for more details.
</Note>

## Learn more

* [**Building agents with Claude Agent SDK**](/guides/ai-agents/claude-code-trigger) – Comprehensive guide for using Claude Agent SDK with Trigger.dev
* [**Realtime**](/realtime/overview) – Stream task progress to your frontend
* [**Scheduled tasks**](/tasks/scheduled) – Automate changelog generation on a schedule

---

## Claude GitHub wiki

Ask questions about any public GitHub repository and get AI-powered analysis using the Claude Agent SDK and Trigger.dev.

## Overview

This demo shows how to build an AI agent using the Claude Agent SDK that clones any public GitHub repo and uses Claude to answer questions about its codebase. The agent explores the code using `Grep` and `Read` tools to provide detailed, accurate answers.

## Tech stack

* **[Next.js](https://nextjs.org/)** – React framework with App Router for the frontend
* **[Claude Agent SDK](https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk)** – Anthropic's SDK for building AI agents with file system and search tools
* **[Trigger.dev](https://trigger.dev/)** – workflow orchestration with real-time streaming, observability, and deployment

## Demo video

<video />

## GitHub repo

<Card title="View the Claude GitHub wiki agent repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/claude-agent-github-wiki">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## How it works

The agent workflow:

1. **Receive question** – User provides a GitHub URL and question about the repo
2. **Clone repository** – Shallow clone to a temp directory (depth=1 for speed)
3. **Analyze with Claude** – Agent explores the codebase using allowed tools:
   * `Grep` – Search for patterns across files
   * `Read` – Read file contents
4. **Stream response** – Analysis streams to the frontend in real-time
5. **Cleanup** – Temp directory is always deleted, even on failure

## Features

* **Ask anything about any public repo** – Architecture, security vulnerabilities, API endpoints, testing strategies, etc.
* **Claude Agent SDK exploration** – Claude explores the codebase using `Grep` and `Read` tools
* **Cancel anytime** – Abort long-running tasks with proper cleanup
* **Trigger.dev [Realtime](/realtime/overview) streaming** – Watch Claude's analysis stream in as it's generated
* **Progress tracking** – See clone status, analysis progress, and repo size via Trigger.dev metadata

## Relevant code

| File                                                                                                                                              | Description                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`trigger/analyze-repo.ts`](https://github.com/triggerdotdev/examples/blob/main/claude-agent-github-wiki/trigger/analyze-repo.ts)                 | Main task that clones repo, runs Claude agent, and streams response |
| [`trigger/agent-stream.ts`](https://github.com/triggerdotdev/examples/blob/main/claude-agent-github-wiki/trigger/agent-stream.ts)                 | Typed stream definition for real-time text responses                |
| [`app/api/analyze-repo/route.ts`](https://github.com/triggerdotdev/examples/blob/main/claude-agent-github-wiki/app/api/analyze-repo/route.ts)     | API endpoint that triggers the task                                 |
| [`app/response/[runId]/page.tsx`](https://github.com/triggerdotdev/examples/blob/main/claude-agent-github-wiki/app/response/%5BrunId%5D/page.tsx) | Real-time streaming display with progress                           |

## trigger.config.ts

You need to mark the Claude Agent SDK as external in your trigger.config.ts file.

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: process.env.TRIGGER_PROJECT_REF!,
  runtime: "node",
  logLevel: "log",
  maxDuration: 3600, // 60 minutes for large repos
  build: {
    external: ["@anthropic-ai/claude-agent-sdk"],
  },
  machine: "medium-2x",
});
```

<Note>
  Adding packages to `external` prevents them from being bundled, which is necessary for the Claude
  Agent SDK. See the [build configuration docs](/config/config-file#external) for more details.
</Note>

## Learn more

* [**Building agents with Claude Agent SDK**](/guides/ai-agents/claude-code-trigger) – Comprehensive guide for using Claude Agent SDK with Trigger.dev
* [**Trigger.dev Realtime**](/realtime/overview) – Stream task progress to your frontend
* [**Errors and retrying**](/errors-retrying) – Handle failures gracefully

---

## Claude 3.7 thinking chatbot

This example Next.js project uses Vercel's AI SDK and Anthropic's Claude 3.7 model to create a thinking chatbot.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app for the chat interface
* [Trigger.dev Realtime](/realtime/overview) to stream AI responses and thinking/reasoning process to the frontend
* [Claude 3.7 Sonnet](https://www.anthropic.com/claude) for generating AI responses
* [AI SDK](https://sdk.vercel.ai/docs/introduction) for working with the Claude model

## GitHub repo

<Card title="View the Claude thinking chatbot repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/claude-thinking-chatbot">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* **Claude Stream Task**: View the Trigger.dev task code in the [src/trigger/claude-stream.ts](https://github.com/triggerdotdev/examples/tree/main/claude-thinking-chatbot/src/trigger/claude-stream.ts) file, which sets up the streaming connection with Claude.
* **Chat Component**: The main chat interface is in [app/components/claude-chat.tsx](https://github.com/triggerdotdev/examples/tree/main/claude-thinking-chatbot/app/components/claude-chat.tsx), which handles:
  * Message state management
  * User input handling
  * Rendering of message bubbles
  * Integration with Trigger.dev for streaming
* **Stream Response**: The `StreamResponse` component within the chat component handles:
  * Displaying streaming text from Claude
  * Showing/hiding the thinking process with an animated toggle
  * Auto-scrolling as new content arrives

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Background Cursor agent using the Cursor CLI

Run Cursor's headless CLI agent in a Trigger.dev task and stream the live output to the frontend using Trigger.dev Realtime Streams.

## Overview

This example runs [Cursor's headless CLI](https://cursor.com/cli) in a Trigger.dev task. The agent spawns as a child process, and its NDJSON stdout is parsed and piped to the browser in real-time using [Realtime Streams](/realtime/react-hooks/streams). The result is a live terminal UI that renders each Cursor event (system messages, assistant responses, tool calls, results) as it happens.

**Tech stack:**

* **[Next.js](https://nextjs.org/)** for the web app (App Router with server actions)
* **[Cursor CLI](https://cursor.com/cli)** for the headless AI coding agent
* **[Trigger.dev](https://trigger.dev)** for task orchestration, real-time streaming, and deployment

## Video

<video />

**Features:**

* **Build extensions**: Installs the `cursor-agent` binary into the task container image using `addLayer`, demonstrating how to ship system binaries with your tasks
* **Realtime Streams v2**: NDJSON from a child process stdout is parsed and piped directly to the browser using `streams.define()` and `.pipe()`
* **Live terminal rendering**: Each Cursor event renders as a distinct row with auto-scroll
* **Long-running tasks**: Cursor agent runs for minutes; Trigger.dev handles lifecycle, timeouts, and retries automatically
* **Machine selection**: Uses the `medium-2x` preset for resource-intensive CLI tools
* **LLM model picker**: Switch between models from the UI before triggering a run

## GitHub repo

<Card title="View the Cursor background agent repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/cursor-cli-demo">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## How it works

### Task orchestration

The task spawns the Cursor CLI as a child process and streams its output to the frontend:

1. A Next.js server action triggers the `cursor-agent` task with the user's prompt and selected model
2. The task spawns the Cursor CLI binary using a helper that returns a typed NDJSON stream and a `waitUntilExit()` promise
3. Each line of NDJSON stdout is parsed into typed Cursor events and piped to a Realtime Stream
4. The frontend subscribes to the stream using `useRealtimeRunWithStreams` and renders each event in a terminal UI
5. The task waits for the CLI process to exit and returns the result

### Build extension for system binaries

The example includes a custom build extension that installs `cursor-agent` into the container image using `addLayer`. The official install script is run at build time, then the resolved entry point and its dependencies are copied to a fixed path so the task can invoke them at runtime with the bundled Node binary.

```ts extensions/cursor-cli.ts theme={"theme":"css-variables"}
const CURSOR_AGENT_DIR = "/usr/local/lib/cursor-agent";

export const cursorCli = (): BuildExtension => ({
  name: "cursor-cli",
  onBuildComplete(context) {
    if (context.target === "dev") return;

    context.addLayer({
      id: "cursor-cli",
      image: {
        instructions: [
          "RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*",
          'ENV PATH="/root/.local/bin:$PATH"',
          "RUN curl -fsSL https://cursor.com/install | bash",
          `RUN cp -r $(dirname $(readlink -f /root/.local/bin/cursor-agent)) ${CURSOR_AGENT_DIR}`,
        ],
      },
    });
  },
});
```

### Streaming with Realtime Streams v2

The stream is defined with a typed schema and piped from the child process:

```ts trigger/cursor-stream.ts theme={"theme":"css-variables"}
export const cursorStream = streams.define("cursor", cursorEventSchema);
```

```ts trigger/cursor-agent.ts theme={"theme":"css-variables"}
const { stream, waitUntilExit } = spawnCursorAgent({ prompt, model });
cursorStream.pipe(stream);
await waitUntilExit();
```

On the frontend, the `useRealtimeRunWithStreams` hook subscribes to these events and renders them as they arrive.

## Relevant code

* **Build extension + spawn helper**: [extensions/cursor-cli.ts](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/extensions/cursor-cli.ts): installs the binary and provides a typed NDJSON stream with `waitUntilExit()`
* **Task definition**: [trigger/cursor-agent.ts](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/trigger/cursor-agent.ts): spawns the CLI, pipes the stream, waits for exit
* **Stream definition**: [trigger/cursor-stream.ts](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/trigger/cursor-stream.ts): Realtime Streams v2 stream with typed schema
* **Terminal UI**: [components/terminal.tsx](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/components/terminal.tsx): renders live events using `useRealtimeRunWithStreams`
* **Event types**: [lib/cursor-events.ts](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/lib/cursor-events.ts): TypeScript types and parsers for Cursor NDJSON events
* **Trigger config**: [trigger.config.ts](https://github.com/triggerdotdev/examples/blob/main/cursor-cli-demo/trigger.config.ts): project config with the cursor CLI build extension

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Human-in-the-loop workflow with ReactFlow and Trigger.dev waitpoint tokens

This example project creates audio summaries of newspaper articles using a human-in-the-loop workflow built with ReactFlow and Trigger.dev waitpoint tokens.

## Overview

This demo is a full stack example that uses the following:

* [Next.js](https://nextjs.org/) for the web application
* [ReactFlow](https://reactflow.dev/) for the workflow UI
* [Trigger.dev Realtime](/realtime/overview) to subscribe to task runs and show the real-time status of the workflow steps
* [Trigger.dev waitpoint tokens](/wait-for-token) to create a human-in-the-loop flow with a review step
* [OpenAI API](https://openai.com/api/) to generate article summaries
* [ElevenLabs](https://elevenlabs.io/text-to-speech) to convert text to speech

## GitHub repo

<Card title="View the human-in-the-loop workflow repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/article-summary-workflow">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

Each node in the workflow corresponds to a Trigger.dev task. The idea is to enable building flows by composition of different tasks. The output of one task serves as input for another.

* **Trigger.dev task splitting**:
  * The [summarizeArticle](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/trigger/summarizeArticle.ts) task uses the OpenAI API to generate a summary an article.
  * The [convertTextToSpeech](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/trigger/convertTextToSpeech.ts) task uses the ElevenLabs API to convert the summary into an audio stream and upload it to an S3 bucket.
  * The [reviewSummary](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/trigger/reviewSummary.ts) task is a human-in-the-loop step that shows the result and waits for approval of the summary before continuing.
  * [articleWorkflow](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/trigger/articleWorkflow.ts) is the entrypoint that ties the workflow together and orchestrates the tasks. You might choose to approach the orchestration differently, depending on your use case.
* **ReactFlow Nodes**: there are three types of nodes in this example. All of them are custom ReactFlow nodes.
  * The [InputNode](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/components/InputNode.tsx) is the starting node of the workflow. It triggers the workflow by submitting an article URL.
  * The [ActionNode](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/components/ActionNode.tsx) is a node that shows the status of a task run in Trigger.dev, in real-time using the React hooks for Trigger.dev.
  * The [ReviewNode](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/components/ReviewNode.tsx) is a node that shows the summary result and prompts the user for approval before continuing. It uses the Realtime API to fetch details about the review status. Also, it interacts with the Trigger.dev waitpoint API for completing the waitpoint token using Next.js server actions.
* **Workflow orchestration**:
  * The workflow is orchestrated by the [Flow](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/components/Flow.tsx) component. It lays out the nodes, the connections between them, as well as the mapping to the Trigger.dev tasks.
    It also uses the `useRealtimeRunsWithTag` hook to subscribe to task runs associated with the workflow and passes down the run details to the nodes.

The waitpoint token is created in [a Next.js server action](https://github.com/triggerdotdev/examples/blob/main/article-summary-workflow/src/app/actions.ts#L26):

```ts theme={"theme":"css-variables"}
const reviewWaitpointToken = await wait.createToken({
  tags: [workflowTag],
  timeout: "1h",
  idempotencyKey: `review-summary-${workflowTag}`,
});
```

and later completed in another server action in the same file:

```ts theme={"theme":"css-variables"}
await wait.completeToken<ReviewPayload>(
  { id: tokenId },
  {
    approved: true,
    approvedAt: new Date(),
    approvedBy: user,
  }
);
```

While the workflow in this example is static and does not allow changing the connections between nodes in the UI, it serves as a good baseline for understanding how to build completely custom workflow builders using Trigger.dev and ReactFlow.

## Learn more about Trigger.dev Realtime and waitpoint tokens

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API
* [Waitpoint tokens](/wait-for-token) - learn about waitpoint tokens in Trigger.dev and human-in-the-loop flows

---

## Mastra agents with memory sharing + Trigger.dev task orchestration

Multi-agent workflow with persistent memory sharing using Mastra and Trigger.dev for clothing recommendations based on weather data.

## Overview

Enter a city and an activity, and get a clothing recommendation generated for you based on today's weather.

![Generated clothing recommendations](https://github.com/user-attachments/assets/edfca304-6b22-4fa8-9362-71ecb3fe4903)

By combining Mastra's persistent memory system and agent orchestration with Trigger.dev's durable task execution, retries and observability, you get production-ready AI workflows that survive failures, scale automatically, and maintain context across long-running operations.

## Tech stack

* **[Node.js](https://nodejs.org)** runtime environment
* **[Mastra](https://mastra.ai)** for AI agent orchestration and memory management (Mastra is a Typescript framework for building AI agents, and uses Vercel's AI Agent SDK under the hood.)
* **[PostgreSQL](https://postgresql.org)** for persistent storage and memory sharing
* **[Trigger.dev](https://trigger.dev)** for task orchestration, batching, and observability
* **[OpenAI GPT-4](https://openai.com)** for natural language processing
* **[Open-Meteo API](https://open-meteo.com)** for weather data (no API key required)
* **[Zod](https://zod.dev)** for schema validation and type safety

## GitHub repo

<Card title="View the Mastra agents with memory repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/mastra-agents">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Featured patterns

* **[Agent Memory Sharing](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/trigger/weather-task.ts)**: Efficient data sharing between agents using Mastra's working memory system
* **[Task Orchestration](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/trigger/weather-task.ts)**: Multi-step workflows with `triggerAndWait` for sequential agent execution
* **[Centralized Storage](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/index.ts)**: Single PostgreSQL storage instance shared across all agents to prevent connection duplication
* **[Custom Tools](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/tools/weather-tool.ts)**: External API integration with structured output validation
* **[Agent Specialization](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/agents/)**: Purpose-built agents with specific roles and instructions
* **[Schema Optimization](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/schemas/weather-data.ts)**: Lightweight data structures for performance

## Project Structure

```
src/
├── mastra/
│   ├── agents/
│   │   ├── weather-analyst.ts    # Weather data collection
│   │   ├── clothing-advisor.ts   # Clothing recommendations
│   ├── tools/
│   │   └── weather-tool.ts       # Enhanced weather API tool
│   ├── schemas/
│   │   └── weather-data.ts       # Weather schema
│   └── index.ts                  # Mastra configuration
├── trigger/
│   └── weather-task.ts           # Trigger.dev tasks
```

## Relevant code

* **[Multi-step task orchestration](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/trigger/weather-task.ts)**: Multi-step task orchestration with `triggerAndWait` for sequential agent execution and shared memory context
* **[Weather analyst agent](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/agents/weather-analyst.ts)**: Specialized agent for weather data collection with external API integration and memory storage
* **[Clothing advisor agent](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/agents/clothing-advisor.ts)**: Purpose-built agent that reads from working memory and generates natural language responses
* **[Weather tool](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/tools/weather-tool.ts)**: Custom Mastra tool with Zod validation for external API calls and error handling
* **[Weather data schema](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/schemas/weather-data.ts)**: Optimized Zod schema for efficient memory storage and type safety
* **[Mastra configuration](https://github.com/triggerdotdev/examples/blob/main/mastra-agents/src/mastra/index.ts)**: Mastra configuration with PostgreSQL storage and agent registration

## Storage Architecture

This project uses a **centralized PostgreSQL storage** approach where a single database connection is shared across all Mastra agents. This prevents duplicate database connections and ensures efficient memory sharing between the weather analyst and clothing advisor agents.

### Storage Configuration

The storage is configured once in the main Mastra instance (`src/mastra/index.ts`) and automatically inherited by all agent Memory instances. This eliminates the "duplicate database object" warning that can occur with multiple PostgreSQL connections.

The PostgreSQL storage works seamlessly in both local development and serverless environments with any PostgreSQL provider, such as:

* [Local PostgreSQL instance](https://postgresql.org)
* [Supabase](https://supabase.com) - Serverless PostgreSQL
* [Neon](https://neon.tech) - Serverless PostgreSQL
* [Railway](https://railway.app) - Simple PostgreSQL hosting
* [AWS RDS](https://aws.amazon.com/rds/postgresql/) - Managed PostgreSQL

## Learn More

To learn more about the technologies used in this project, check out the following resources:

* [Mastra docs](https://mastra.ai/en/docs) - learn about AI agent orchestration and memory management
* [Mastra working memory](https://mastra.ai/en/docs/memory/overview) - learn about efficient data sharing between agents

---

## Meme generator with human-in-the-loop approval

This example project creates memes using OpenAI's DALL-E 3 with a human-in-the-loop approval workflow built using Trigger.dev waitpoint tokens.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app, with an [endpoint](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/app/endpoints/\[slug]/page.tsx) for approving the generated memes
* [Trigger.dev](https://trigger.dev) tasks to generate the images and orchestrate the waitpoint workflow
* [OpenAI DALL-E 3](https://platform.openai.com/docs/guides/images) for generating the images
* A [Slack app](https://api.slack.com/quickstart) for the human-in-the-loop step, with the approval buttons linked to the endpoint

## GitHub repo

<Card title="View the meme generator human-in-the-loop example repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/meme-generator-human-in-the-loop">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Post to Slack

<img alt="Meme Generator with Human-in-the-Loop Approval" />

## Relevant code

* **Meme generator task**:

  * The [memegenerator.ts](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/trigger/memegenerator.ts) task:
    * Generates two meme variants using DALL-E 3
    * Uses [batchTriggerAndWait](/triggering#yourtask-batchtriggerandwait) to generate multiple meme variants simultaneously (this is because you can only generate 1 image at a time with DALL-E 3)
    * Creates a [waitpoint token](/wait-for-token)
    * Sends the generated images with approval buttons to Slack for review
    * Handles the approval workflow

* **Approval Endpoint**:
  * The waitpoint approval handling is in [page.tsx](https://github.com/triggerdotdev/examples/blob/main/meme-generator-human-in-the-loop/src/app/endpoints/\[slug]/page.tsx), which processes:
    * User selections from Slack buttons
    * Waitpoint completion with the chosen meme variant
    * Success/failure feedback to the approver

## Learn more

To learn more, take a look at the following resources:

* [Waitpoint tokens](/wait-for-token) - learn about waitpoint tokens in Trigger.dev and human-in-the-loop flows
* [OpenAI DALL-E API](https://platform.openai.com/docs/guides/images) - learn about the DALL-E image generation API
* [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
* [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks) - learn about integrating with Slack

---

## OpenAI Agents SDK for Python guardrails

This example project demonstrates how to implement different types of guardrails using the OpenAI Agent SDK for Python with Trigger.dev.

## Overview

This demo is a practical guide that demonstrates:

* **Three types of AI guardrails**: Input validation, output checking, and real-time streaming monitoring
* Integration of the [OpenAI Agent SDK for Python](https://openai.github.io/openai-agents-python/) with [Trigger.dev](https://trigger.dev) for production AI workflows
* Triggering Python scripts from tasks using our [Python build extension](/config/extensions/pythonExtension)
* **Educational examples** of implementing guardrails for AI safety and control mechanisms
* Real-world scenarios like math tutoring agents with content validation and complexity monitoring

Guardrails are safety mechanisms that run alongside AI agents to validate input, check output, monitor streaming content in real-time, and prevent unwanted or harmful behavior.

## GitHub repo

<Card title="View the OpenAI Agent SDK Guardrails repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/openai-agent-sdk-guardrails-examples">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

### Trigger.dev Tasks

* **[inputGuardrails.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/trigger/inputGuardrails.ts)** - Passes user prompts to Python script and handles `InputGuardrailTripwireTriggered` exceptions
* **[outputGuardrails.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/trigger/outputGuardrails.ts)** - Runs agent generation and catches `OutputGuardrailTripwireTriggered` exceptions with detailed error info
* **[streamingGuardrails.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/trigger/streamingGuardrails.ts)** - Executes streaming Python script and parses JSON output containing guardrail metrics

### Python Implementations

* **[input-guardrails.py](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/python/input-guardrails.py)** - Agent with `@input_guardrail` decorator that validates user input before processing (example: math tutor that only responds to math questions)
* **[output-guardrails.py](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/python/output-guardrails.py)** - Agent with `@output_guardrail` decorator that validates generated responses using a separate guardrail agent
* **[streaming-guardrails.py](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/src/python/streaming-guardrails.py)** - Processes `ResponseTextDeltaEvent` streams with async guardrail checks at configurable intervals (example: stops streaming if language is too complex for a 10-year-old)

### Configuration

* **[trigger.config.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agent-sdk-guardrails-examples/trigger.config.ts)** - Uses the Trigger.dev Python extension

### Learn more

* [OpenAI Agent SDK documentation](https://openai.github.io/openai-agents-python/)
* [OpenAI Agent SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/)
* Our [Python build extension](/config/extensions/pythonExtension#python)

---

## OpenAI Agents SDK for Typescript + Trigger.dev playground

Build production-ready AI agents with OpenAI Agents SDK for Typescript and Trigger.dev. Explore 7 examples covering streaming, multi-agent systems, and tool integration.

## Overview

7 production-ready patterns built with the OpenAI Agents SDK and Trigger.dev. Clone this repo to experiment with everything from basic calls to workflows with tools, streaming, guardrails, handoffs, and more.

By combining the OpenAI Agents SDK with Trigger.dev, you can create durable agents that can be deployed to production and scaled to any size, with retries, queues, and full observability built-in.

## Video

<video />

## Tech stack

* [Node.js](https://nodejs.org) runtime environment
* [OpenAI Agents SDK for Typescript](https://openai.github.io/openai-agents-js/) for creating and managing AI agents
* [Trigger.dev](https://trigger.dev) for task orchestration, batching, scheduling, and workflow management
* [Zod](https://zod.dev) for payload validation

## GitHub repo

<Card title="View the OpenAI Agents SDK TypeScript playground repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/openai-agents-sdk-with-trigger-playground">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Agent tasks

* **Basic Agent Chat**: Personality-based conversations with strategic model selection
* **Agent with Tools**: A simple agent that can call tools to get weather data
* **Streaming Agent**: Real-time content generation with progress tracking
* **Agent Handoffs**: True multi-agent collaboration using the [handoff pattern](https://openai.github.io/openai-agents-js/guides/handoffs/) where agents can dynamically transfer control to specialists
* **Parallel Agents**: Concurrent agent processing for complex analysis tasks
* **Scheduled Agent**: Time-based agent workflows for continuous monitoring
* **Agent with Guardrails**: Input guardrails for safe AI interactions

## Relevant code

* **[basicAgentChat.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/basicAgentChat.ts)** - Strategic model selection (GPT-4, o1-preview, o1-mini, gpt-4o-mini) mapped to personality types with Trigger.dev task orchestration
* **[agentWithTools.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/agentWithTools.ts)** - OpenAI tool calling with Zod validation integrated into Trigger.dev's retry and error handling mechanisms
* **[streamingAgent.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/streamingAgent.ts)** - Native OpenAI streaming responses with real-time progress tracking via Trigger.dev metadata
* **[scheduledAgent.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/scheduledAgent.ts)** - Cron-scheduled OpenAI agents running every 6 hours with automatic trend analysis
* **[parallelAgents.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/parallelAgents.ts)** - Concurrent OpenAI agent execution using Trigger.dev batch operations (`batch.triggerByTaskAndWait`) for scalable text analysis
* **[agentWithGuardrails.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/agentWithGuardrails.ts)** - OpenAI classification agents as input guardrails with structured validation and exception handling
* **[agentHandoff.ts](https://github.com/triggerdotdev/examples/blob/main/openai-agents-sdk-with-trigger-playground/src/trigger/agentHandoff.ts)** - OpenAI Agents SDK handoff pattern with specialist delegation orchestrated through Trigger.dev workflows

## Learn more

* [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-js/) - learn about creating and managing AI agents
* [OpenAI Agents SDK handoffs](https://openai.github.io/openai-agents-js/guides/handoffs/) - learn about agent-to-agent delegation patterns
* [Batch triggering](/triggering#batch-trigger) - learn about parallel task execution
* [Scheduled tasks (cron)](/tasks/scheduled#scheduled-tasks-cron) - learn about cron-based task scheduling

---

## Product image generator using Replicate and Trigger.dev

AI-powered product image generator that transforms basic product photos into professional marketing shots using Replicate's image generation models

## Overview

This project demonstrates how to build an AI-powered product image generator that transforms basic product photos into professional marketing shots. Users upload a product image and receive three professionally styled variations: clean product shots, lifestyle scenes, and hero shots with dramatic lighting.

## Video

<video />

## GitHub repo

Clone this repo and follow the instructions in the `README.md` file to get started.

<Card title="View the product image generator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/product-image-generator">
  Click here to view the full code in our examples repository on GitHub. You can fork it and use it
  as a starting point for your project.
</Card>

## Tech stack

* [**Next.js**](https://nextjs.org/) – frontend React framework
* [**Replicate**](https://replicate.com/docs) – AI image generation using the `google/nano-banana` image-to-image model
* [**UploadThing**](https://uploadthing.com/) – file upload management and server callbacks
* [**Cloudflare R2**](https://developers.cloudflare.com/r2/) – scalable image storage with public URLs

## How it works

The application orchestrates image generation through two main tasks: [`generateImages`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/trigger/generate-images.ts) coordinates batch processing, while [`generateImage`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/trigger/generate-images.ts) handles individual style generation.

Each generation task enhances prompts with style-specific instructions, calls Replicate's `google/nano-banana` image-to-image model, creates waitpoint tokens for async webhook handling, and uploads results to Cloudflare R2. The frontend displays real-time progress updates via React hooks as tasks complete.

Style presets include clean product shots (white background), lifestyle scenes (person holding product), and hero shots (dramatic lighting).

## Relevant code

* **Image generation tasks** – batch processing with waitpoints for Replicate webhook callbacks ([`app/trigger/generate-images.ts`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/trigger/generate-images.ts))
* **Upload handler** – UploadThing integration that triggers batch generation ([`app/api/uploadthing/core.ts`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/api/uploadthing/core.ts))
* **Real-time progress UI** – live task updates using React hooks ([`app/components/GeneratedCard.tsx`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/components/GeneratedCard.tsx))
* **Custom prompt interface** – user-defined style generation ([`app/components/CustomPromptCard.tsx`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/components/CustomPromptCard.tsx))
* **Main app component** – layout and state management ([`app/ProductImageGenerator.tsx`](https://github.com/triggerdotdev/examples/blob/main/product-image-generator/app/ProductImageGenerator.tsx))

## Learn more

* [**Waitpoints**](/wait-for-token) – pause tasks for async webhook callbacks
* [**React hooks**](/realtime/react-hooks/overview) – real-time task updates and frontend integration
* [**Batch operations**](/triggering#tasks-batchtrigger) – parallel task execution patterns
* [**Replicate API**](https://replicate.com/docs/get-started/nextjs) – AI model integration
* [**UploadThing**](https://docs.uploadthing.com/) – file upload handling and server callbacks

---

## Next.js Realtime CSV Importer

This example Next.js project demonstrates how to use Trigger.dev Realtime to build a CSV Uploader with progress updates streamed to the frontend.

## Overview

The frontend is a Next.js app that allows users to upload a CSV file, which is then processed in the background using Trigger.dev tasks. The progress of the task is streamed back to the frontend in real-time using Trigger.dev Realtime.

* A [Next.js](https://nextjs.org/) app with [Trigger.dev](https://trigger.dev/) for the background tasks.
* [UploadThing](https://uploadthing.com/) to handle CSV file uploads
* Trigger.dev [Realtime](https://trigger.dev/launchweek/0/realtime) to stream updates to the frontend.

## GitHub repo

<Card title="View the Realtime CSV Importer repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/blob/main/realtime-csv-importer/README.md">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* View the Trigger.dev task code in the [src/trigger/csv.ts](https://github.com/triggerdotdev/examples/blob/main/realtime-csv-importer/src/trigger/csv.ts) file.
* The parent task `csvValidator` downloads the CSV file, parses it, and then splits the rows into multiple batches. It then does a `batch.triggerAndWait` to distribute the work the `handleCSVRow` task.
* The `handleCSVRow` task "simulates" checking the row for a valid email address and then updates the progress of the parent task using `metadata.parent`. See the [Trigger.dev docs](/runs/metadata#parent-and-root-updates) for more information on how to use the `metadata.parent` object.
* The `useRealtimeCSVValidator` hook in the [src/hooks/useRealtimeCSVValidator.ts](https://github.com/triggerdotdev/examples/blob/main/realtime-csv-importer/src/hooks/useRealtimeCSVValidator.ts) file handles the call to `useRealtimeRun` to get the progress of the parent task.
* The `CSVProcessor` component in the [src/components/CSVProcessor.tsx](https://github.com/triggerdotdev/examples/blob/main/realtime-csv-importer/src/components/CSVProcessor.tsx) file handles the file upload and displays the progress bar, and uses the `useRealtimeCSVValidator` hook to get the progress updates.

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Image generation with Fal.ai and Trigger.dev Realtime

This example Next.js project generates an image from a prompt using Fal.ai and shows the progress of the task on the frontend using Trigger.dev Realtime.

## Overview

This full stack Next.js project showcases the following:

* A Trigger.dev task which [generates an image from a prompt using Fal.ai](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/trigger/realtime-generate-image.ts)
* When a [form is submitted](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/page.tsx) in the UI, triggering the task using a [server action](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/actions/process-image.ts)
* Showing the [progress of the task](https://github.com/triggerdotdev/examples/blob/main/realtime-fal-ai-image-generation/src/app/processing/%5Bid%5D/ProcessingContent.tsx) on the frontend using Trigger.dev Realtime. This also includes error handling and a fallback UI
* Once the task is completed, showing the generated image on the frontend next to the original image

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Walkthrough video

This video walks through the process of creating this task in a Next.js project.

<iframe title="Trigger.dev walkthrough" />

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Smart Spreadsheet

An AI-powered company enrichment tool that uses Exa search and Claude to extract verified company data with source attribution.

## Overview

Smart Spreadsheet is an AI-powered tool that enriches company data on demand. Input a company name or website URL and get verified information including industry, headcount, and funding details; each with source attribution. Results appear in the frontend in real-time as each task completes.

* A [Next.js](https://nextjs.org/) app with [Trigger.dev](https://trigger.dev/) for background tasks
* [Exa](https://exa.ai/) – an AI-native search engine that returns clean, structured content ready for LLM extraction
* [Claude](https://anthropic.com/) via the [Vercel AI SDK](https://sdk.vercel.ai/) for data extraction
* [Supabase](https://supabase.com/) PostgreSQL database for persistence
* Trigger.dev [Realtime](/realtime/overview) for live updates to the frontend

## Video

<video />

## GitHub repo

<Card title="View the Smart Spreadsheet repo" icon="github" href="https://github.com/triggerdotdev/examples/tree/main/smart-spreadsheet">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## How it works

The enrichment workflow:

1. **Trigger enrichment** – User enters a company name or URL in the spreadsheet UI
2. **Parallel data gathering** – Four subtasks run concurrently to fetch basic info, industry, employee count, and funding details
3. **AI extraction** – Each subtask uses Exa search + Claude to extract structured data with source URLs
4. **Real-time updates** – Results appear in the frontend as each subtask completes
5. **Persist results** – Enriched data is saved to Supabase with source attribution

## Features

* **Parallel processing** – All four enrichment categories run simultaneously using [batch.triggerByTaskAndWait](/triggering#batch-trigger-by-task-and-wait)
* **Source attribution** – Every data point includes the URL it was extracted from
* **Live updates** – Results appear in the UI as each task completes using [Realtime](/realtime/overview)
* **Structured extraction** – Zod schemas ensure consistent data output from Claude

## Key code patterns

### Parallel task execution

The main task triggers all four enrichment subtasks simultaneously using `batch.triggerByTaskAndWait`:

```ts src/trigger/enrich-company.ts theme={"theme":"css-variables"}
const { runs } = await batch.triggerByTaskAndWait([
  { task: getBasicInfo, payload: { companyName, companyUrl } },
  { task: getIndustry, payload: { companyName, companyUrl } },
  { task: getEmployeeCount, payload: { companyName, companyUrl } },
  { task: getFundingRound, payload: { companyName, companyUrl } },
]);
```

### Live updates from child tasks

Each subtask uses `metadata.parent.set()` to update the parent's metadata as soon as data is extracted:

```ts src/trigger/get-basic-info.ts theme={"theme":"css-variables"}
// After Claude extracts the data, update the parent task's metadata
metadata.parent.set("website", object.website);
metadata.parent.set("description", object.description);
```

The frontend subscribes to these metadata updates using [Realtime](/realtime/overview), so users see each field populate as it's discovered.

## Relevant code

| File                                                                                                                                           | Description                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [`src/trigger/enrich-company.ts`](https://github.com/triggerdotdev/examples/blob/main/smart-spreadsheet/src/trigger/enrich-company.ts)         | Main orchestrator that triggers parallel subtasks and persists results |
| [`src/trigger/get-basic-info.ts`](https://github.com/triggerdotdev/examples/blob/main/smart-spreadsheet/src/trigger/get-basic-info.ts)         | Extracts company website and description                               |
| [`src/trigger/get-industry.ts`](https://github.com/triggerdotdev/examples/blob/main/smart-spreadsheet/src/trigger/get-industry.ts)             | Classifies company industry                                            |
| [`src/trigger/get-employee-count.ts`](https://github.com/triggerdotdev/examples/blob/main/smart-spreadsheet/src/trigger/get-employee-count.ts) | Finds employee headcount                                               |
| [`src/trigger/get-funding-round.ts`](https://github.com/triggerdotdev/examples/blob/main/smart-spreadsheet/src/trigger/get-funding-round.ts)   | Discovers latest funding information                                   |

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Turborepo monorepo with Prisma

Two example projects demonstrating how to use Prisma and Trigger.dev in a Turborepo monorepo setup.

## Overview

These examples demonstrate two different ways of using Prisma and Trigger.dev in a Turborepo monorepo. In both examples, a task is triggered from a Next.js app using a server action, which uses Prisma to add a user to a database table. The examples differ in how Trigger.dev is installed and configured.

* Example 1: Turborepo monorepo demo with Trigger.dev and Prisma packages
* Example 2: Turborepo monorepo demo with a Prisma package and Trigger.dev installed in a Next.js app

<Note>
  You can either fork the repos below, or simply check out the project structures and code to get an idea of how to set up Trigger.dev in your own monorepos.
</Note>

## Example 1: Turborepo monorepo demo with Trigger.dev and Prisma packages

This simple example demonstrates how to use Trigger.dev and Prisma as packages inside a monorepo created with Turborepo. The Trigger.dev task is triggered by a button click in a Next.js app which triggers the task via a server action.

### GitHub repo

Fork the GitHub repo below to get started with this example project.

<Card title="Check out the Turborepo monorepo demo with Trigger.dev and Prisma packages" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

### Features

* This monorepo has been created using the [Turborepo CLI](https://turbo.build/repo), following the official [Prisma and Turborepo docs](https://www.prisma.io/docs/guides/turborepo), and then adapted for use with Trigger.dev.
* [pnpm](https://pnpm.io/) has been used as the package manager.
* A tasks package (`@repo/tasks`) using [Trigger.dev](https://trigger.dev) is used to create and execute tasks from an app inside the monorepo.
* A database package (`@repo/db`) using [Prisma ORM](https://www.prisma.io/docs/orm/) is used to interact with the database. You can use any popular Postgres database supported by Prisma, e.g. [Supabase](https://supabase.com/), [Neon](https://neon.tech/), etc.
* A [Next.js](https://nextjs.org/) example app (`apps/web`) to show how to trigger the task via a server action.

### Project structure

Simplified project structure for this example:

```
|
| — apps/
|   | — web/                    # Next.js frontend application
|   |   | — app/                # Next.js app router
|   |   |   | — api/
|   |   |   |   | — actions.ts  # Server actions for triggering tasks
|   |   |   | — page.tsx        # Main page with "Add new user" button
|   |   |   | — layout.tsx      # App layout
|   |   | — package.json        # Dependencies including @repo/db and @repo/tasks
|   |
|   | — docs/                   # Documentation app (not fully implemented)
|
| — packages/
|   | — database/               # Prisma database package (@repo/db)
|   |   | — prisma/
|   |   |   | — schema.prisma   # Database schema definition
|   |   | — generated/          # Generated Prisma client (gitignored)
|   |   | — src/
|   |   |   | — index.ts        # Exports from the database package
|   |   | — package.json        # Database package dependencies
|   |
|   | — tasks/                  # Trigger.dev tasks package (@repo/tasks)
|   |   | — src/
|   |   |   | — index.ts        # Exports from the tasks package
|   |   |   | — trigger/
|   |   |       | — index.ts    # Exports the tasks
|   |   |       | — addNewUser.ts # Task implementation for adding users
|   |   | — trigger.config.ts   # Trigger.dev configuration
|   |   | — package.json        # Tasks package dependencies
|   |
|   | — ui/                     # UI components package (referenced but not detailed)
|
| — turbo.json                  # Turborepo configuration
| — package.json                # Root package.json with workspace config
```

### Relevant files and code

#### Database package

* Prisma is added as a package in [`/packages/database`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/database/) and exported as `@repo/db` in the [`package.json`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/database/package.json) file.
* The schema is defined in the [`prisma/schema.prisma`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/database/prisma/schema.prisma) file.

#### Tasks package

<Note>
  to run `pnpm dlx trigger.dev@latest init` in a blank packages folder, you have to add a `package.json` file first, otherwise it will attempt to add Trigger.dev files in the root of your monorepo.
</Note>

* Trigger.dev is added as a package in [`/packages/tasks`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks) and exported as `@repo/tasks` in the [`package.json`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/package.json) file.
* The [`addNewUser.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/src/trigger/addNewUser.ts) task adds a new user to the database.
* The [`packages/tasks/src/index.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/src/index.ts) file exports values and types from the Trigger.dev SDK, and is exported from the package via the [`package.json`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/package.json) file.
* The [`packages/tasks/src/trigger/index.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/src/trigger/index.ts) file exports the task from the package. Every task must be exported from the package like this.
* The [`trigger.config.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/packages/tasks/trigger.config.ts) file configures the Trigger.dev project settings. This is where the Trigger.dev [Prisma build extension](https://trigger.dev/docs/config/extensions/prismaExtension) is added, which is required to use Prisma in the Trigger.dev task.

<Info>
  You must include the version of Prisma you are using in the `trigger.config.ts` file, otherwise the Prisma build extension will not work. Learn more about our [Prisma build extension](/config/extensions/prismaExtension).
</Info>

#### The Next.js app `apps/web`

* The app is a simple Next.js app using the App Router, that uses the `@repo/db` package to interact with the database and the `@repo/tasks` package to trigger the task. These are both added as dependencies in the [`package.json`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/apps/web/package.json) file.
* The task is triggered from a button click in the app in [`page.tsx`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/apps/web/app/page.tsx), which uses a server action in [`/app/api/actions.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/apps/web/app/api/actions.ts) to trigger the task with an example payload.

### Running the example

To run this example, check out the full instructions [in the GitHub repo README file](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package/README.md).

## Example 2: Turborepo monorepo demo with a Prisma package and Trigger.dev installed in a Next.js app

This example demonstrates how to use Trigger.dev and Prisma in a monorepo created with Turborepo. Prisma has been added as a package, and Trigger.dev has been installed in a Next.js app. The task is triggered by a button click in the app via a server action.

### GitHub repo

Fork the GitHub repo below to get started with this example project.

<Card title="Check out the Turborepo monorepo demo with a Prisma package and Trigger.dev installed in a Next.js app" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

### Features

* This monorepo has been created using the [Turborepo CLI](https://turbo.build/repo), following the official [Prisma and Turborepo docs](https://www.prisma.io/docs/guides/turborepo), and then adapted for use with Trigger.dev.
* [pnpm](https://pnpm.io/) has been used as the package manager.
* A database package (`@repo/db`) using [Prisma ORM](https://www.prisma.io/docs/orm/) is used to interact with the database. You can use any popular Postgres database supported by Prisma, e.g. [Supabase](https://supabase.com/), [Neon](https://neon.tech/), etc.
* A [Next.js](https://nextjs.org/) example app (`apps/web`) to show how to trigger the task via a server action.
* Trigger.dev initialized and an `addNewUser` task created in the `web` app.

### Project structure

Simplified project structure for this example:

```
|
| — apps/
|   | — web/                       # Next.js frontend application
|   |   | — app/                   # Next.js app router
|   |   |   | — api/
|   |   |   |   | — actions.ts     # Server actions for triggering tasks
|   |   |   | — page.tsx           # Main page with "Add new user" button
|   |   | — src/
|   |   |   | — trigger/
|   |   |       | — addNewUser.ts  # Task implementation for adding users
|   |   | — trigger.config.ts      # Trigger.dev configuration
|   |   | — package.json           # Dependencies including @repo/db
|   |
|   | — docs/                      # Documentation app
|       | — app/
|           | — page.tsx           # Docs landing page
|
| — packages/
|   | — database/                  # Prisma database package (@repo/db)
|   |   | — prisma/
|   |   |   | — schema.prisma      # Database schema definition
|   |
|   | — ui/                        # UI components package
|
| — turbo.json                     # Turborepo configuration
| — package.json                   # Root package.json with workspace config
```

## Relevant files and code

### Database package (`@repo/db`)

* Located in [`/packages/database/`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/packages/database/) and exported as `@repo/db`
* Schema defined in [`schema.prisma`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/packages/database/prisma/schema.prisma)
* Provides database access to other packages and apps

### Next.js app (`apps/web`)

* Contains Trigger.dev configuration in [`trigger.config.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/apps/web/trigger.config.ts)
* Trigger.dev tasks are defined in [`src/trigger/`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/apps/web/src/trigger/) (e.g., [`addNewUser.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/apps/web/src/trigger/addNewUser.ts))
* Demonstrates triggering tasks via server actions in [`app/api/actions.ts`](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/apps/web/app/api/actions.ts)

### Running the example

To run this example, check out the full instructions [in the GitHub repo README file](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-trigger/README.md).

---

## Deep research agent using Vercel's AI SDK

Deep research agent which generates comprehensive PDF reports using Vercel's AI SDK.

<Info title="Acknowledgements">
  Acknowledgements: This example project is derived from the brilliant [deep research
  guide](https://aie-feb-25.vercel.app/docs/deep-research) by [Nico
  Albanese](https://x.com/nicoalbanese10).
</Info>

## Overview

This full-stack project is an intelligent deep research agent that autonomously conducts multi-layered web research, generating comprehensive reports which are then converted to PDF and uploaded to storage.

<video />

**Tech stack:**

* **[Next.js](https://nextjs.org/)** for the web app
* **[Vercel's AI SDK](https://sdk.vercel.ai/)** for AI model integration and structured generation
* **[Trigger.dev](https://trigger.dev)** for task orchestration, execution and real-time progress updates
* **[OpenAI's GPT-4o model](https://openai.com/gpt-4)** for intelligent query generation, content analysis, and report creation
* **[Exa API](https://exa.ai/)** for semantic web search with live crawling
* **[LibreOffice](https://www.libreoffice.org/)** for PDF generation
* **[Cloudflare R2](https://developers.cloudflare.com/r2/)** to store the generated reports

**Features:**

* **Recursive research**: AI generates search queries, evaluates their relevance, asks follow-up questions and searches deeper based on initial findings.
* **Real-time progress**: Live updates are shown on the frontend using Trigger.dev Realtime as research progresses.
* **Intelligent source evaluation**: AI evaluates search result relevance before processing.
* **Research report generation**: The completed research is converted to a structured HTML report using a detailed system prompt.
* **PDF creation and uploading to Cloud storage**: The completed reports are then converted to PDF using LibreOffice and uploaded to Cloudflare R2.

## GitHub repo

<Card title="View the Vercel AI SDK deep research agent repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-deep-research-agent">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## How the deep research agent works

### Trigger.dev orchestration

The research process is orchestrated through three connected Trigger.dev tasks:

1. `deepResearchOrchestrator` - Main task that coordinates the entire research workflow.
2. `generateReport` - Processes research data into a structured HTML report using OpenAI's GPT-4o model
3. `generatePdfAndUpload` - Converts HTML to PDF using LibreOffice and uploads to R2 cloud storage

Each task uses `triggerAndWait()` to create a dependency chain, ensuring proper sequencing while maintaining isolation and error handling.

### The deep research recursive function

The core research logic uses a recursive depth-first search approach. A query is recursively expanded and the results are collected.

**Key parameters:**

* `depth`: Controls recursion levels (default: 2)
* `breadth`: Number of queries per level (default: 2, halved each recursion)

```
Level 0 (Initial Query): "AI safety in autonomous vehicles"
│
├── Level 1 (depth = 1, breadth = 2):
│   ├── Sub-query 1: "Machine learning safety protocols in self-driving cars"
│   │   ├── → Search Web → Evaluate Relevance → Extract Learnings
│   │   └── → Follow-up: "How do neural networks handle edge cases?"
│   │
│   └── Sub-query 2: "Regulatory frameworks for autonomous vehicle testing"
│       ├── → Search Web → Evaluate Relevance → Extract Learnings
│       └── → Follow-up: "What are current safety certification requirements?"
│
└── Level 2 (depth = 2, breadth = 1):
    ├── From Sub-query 1 follow-up:
    │   └── "Neural network edge case handling in autonomous systems"
    │       └── → Search Web → Evaluate → Extract → DEPTH LIMIT REACHED
    │
    └── From Sub-query 2 follow-up:
        └── "Safety certification requirements for self-driving vehicles"
            └── → Search Web → Evaluate → Extract → DEPTH LIMIT REACHED
```

**Process flow:**

1. **Query generation**: OpenAI's GPT-4o generates multiple search queries from the input
2. **Web search**: Each query searches the web via the Exa API with live crawling
3. **Relevance evaluation**: OpenAI's GPT-4o evaluates if results help answer the query
4. **Learning extraction**: Relevant results are analyzed for key insights and follow-up questions
5. **Recursive deepening**: Follow-up questions become new queries for the next depth level
6. **Accumulation**: All learnings, sources, and queries are accumulated across recursion levels

### Using Trigger.dev Realtime to trigger and subscribe to the deep research task

We use the [`useRealtimeTaskTrigger`](/realtime/react-hooks/triggering#userealtimetasktrigger) React hook to trigger the `deep-research` task and subscribe to it's updates.

**Frontend (React Hook)**:

```typescript theme={"theme":"css-variables"}
const triggerInstance = useRealtimeTaskTrigger<typeof deepResearchOrchestrator>("deep-research", {
  accessToken: triggerToken,
});
const { progress, label } = parseStatus(triggerInstance.run?.metadata);
```

As the research progresses, the metadata is set within the tasks and the frontend is kept updated with every new status:

**Task Metadata**:

```typescript theme={"theme":"css-variables"}
metadata.set("status", {
  progress: 25,
  label: `Searching the web for: "${query}"`,
});
```

## Relevant code

* **Deep research task**: Core logic in [src/trigger/deepResearch.ts](https://github.com/triggerdotdev/examples/blob/main/vercel-ai-sdk-deep-research-agent/src/trigger/deepResearch.ts) - orchestrates the recursive research process. Here you can change the model, the depth and the breadth of the research.
* **Report generation**: [src/trigger/generateReport.ts](https://github.com/triggerdotdev/examples/blob/main/vercel-ai-sdk-deep-research-agent/src/trigger/generateReport.ts) - creates structured HTML reports from research data. The system prompt is defined in the code - this can be updated to be more or less detailed.
* **PDF generation**: [src/trigger/generatePdfAndUpload.ts](https://github.com/triggerdotdev/examples/blob/main/vercel-ai-sdk-deep-research-agent/src/trigger/generatePdfAndUpload.ts) - converts reports to PDF and uploads to R2. This is a simple example of how to use LibreOffice to convert HTML to PDF.
* **Research agent UI**: [src/components/DeepResearchAgent.tsx](https://github.com/triggerdotdev/examples/blob/main/vercel-ai-sdk-deep-research-agent/src/components/DeepResearchAgent.tsx) - handles form submission and real-time progress display using the `useRealtimeTaskTrigger` hook.
* **Progress component**: [src/components/progress-section.tsx](https://github.com/triggerdotdev/examples/blob/main/deep-research-agent/src/components/progress-section.tsx) - displays live research progress.

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---

## Vercel AI SDK image generator

This example Next.js project uses the Vercel AI SDK to generate images from a prompt.

## Overview

This demo is a full stack example that uses the following:

* A [Next.js](https://nextjs.org/) app using [shadcn](https://ui.shadcn.com/) for the UI
* Our 'useRealtimeRun' [React hook](/realtime/react-hooks/subscribe#userealtimerun) to subscribe to the run and show updates on the frontend
* The [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction) to [generate images](https://sdk.vercel.ai/docs/ai-sdk-core/image-generation) using OpenAI's DALL-E models

## GitHub repo

<Card title="View the Vercel AI SDK image generator repo" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Video

<video />

## Relevant code

* View the Trigger.dev task code which generates the image using the Vercel AI SDK in [src/trigger/realtime-generate-image.ts](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator/src/trigger/realtime-generate-image.ts).
* We use a [useRealtimeRun](/realtime/react-hooks/subscribe#userealtimerun) hook to subscribe to the run in [src/app/processing/\[id\]/ProcessingContent.tsx](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator/src/app/processing/\[id]/ProcessingContent.tsx).

## Learn more about Trigger.dev Realtime

To learn more, take a look at the following resources:

* [Trigger.dev Realtime](/realtime) - learn more about how to subscribe to runs and get real-time updates
* [Realtime streaming](/realtime/react-hooks/streams) - learn more about streaming data from your tasks
* [Batch Triggering](/triggering#tasks-batchtrigger) - learn more about how to trigger tasks in batches
* [React hooks](/realtime/react-hooks) - learn more about using React hooks to interact with the Trigger.dev API

---
