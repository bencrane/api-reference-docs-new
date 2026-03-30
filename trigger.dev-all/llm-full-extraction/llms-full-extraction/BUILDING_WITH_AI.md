> Sources:
> - https://trigger.dev/docs/building-with-ai
> - https://trigger.dev/docs/mcp-introduction
> - https://trigger.dev/docs/mcp-tools
> - https://trigger.dev/docs/mcp-agent-rules
> - https://trigger.dev/docs/skills

# Building with AI

## Overview

Tools and resources for building Trigger.dev projects with AI coding assistants.

## Quick setup

We provide multiple tools to help AI coding assistants write correct Trigger.dev code. Use one or all of them for the best developer experience.

<Steps>
  <Step title="Install the MCP Server">
    Give your AI assistant direct access to Trigger.dev tools — search docs, trigger tasks, deploy projects, and monitor runs. Works with Claude Code, Cursor, Windsurf, VS Code (Copilot), and Zed.

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp
    ```

    [Learn more →](/mcp-introduction)
  </Step>

  <Step title="Install Skills">
    Portable instruction sets that teach any AI coding assistant Trigger.dev best practices. Works with Claude Code, Cursor, Windsurf, VS Code (Copilot), and any tool that supports the [Agent Skills standard](https://agentskills.io).

    ```bash theme={"theme":"css-variables"}
    npx skills add triggerdotdev/skills
    ```

    [Learn more →](/skills)
  </Step>

  <Step title="Install Agent Rules">
    Comprehensive rule sets installed directly into your AI client's config files. Works with Cursor, Claude Code, VS Code (Copilot), Windsurf, Gemini CLI, Cline, and more. Claude Code also gets a dedicated subagent for hands-on help.

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-rules
    ```

    [Learn more →](/mcp-agent-rules)
  </Step>
</Steps>

## Skills vs Agent Rules vs MCP

Not sure which tool to use? Here's how they compare:

|                   | **Skills**                                 | **Agent Rules**                                                                 | **MCP Server**                                      |
| :---------------- | :----------------------------------------- | :------------------------------------------------------------------------------ | :-------------------------------------------------- |
| **What it does**  | Drops skill files into your project        | Installs rule sets into client config                                           | Runs a live server your AI connects to              |
| **Installs to**   | `.claude/skills/`, `.cursor/skills/`, etc. | `.cursor/rules/`, `CLAUDE.md`, `AGENTS.md`, etc.                                | `mcp.json`, `~/.claude.json`, etc.                  |
| **Updates**       | Re-run `npx skills add`                    | Re-run `npx trigger.dev@latest install-rules` or auto-prompted on `trigger dev` | Always latest (uses `@latest`)                      |
| **Best for**      | Teaching patterns and best practices       | Comprehensive code generation guidance                                          | Live project interaction (deploy, trigger, monitor) |
| **Works offline** | Yes                                        | Yes                                                                             | No (calls Trigger.dev API)                          |

**Our recommendation:** Install all three. Skills and Agent Rules teach your AI *how* to write code. The MCP Server lets it *do things* in your project.

## Project-level context snippet

If you prefer a lightweight/passive approach, paste the snippet below into a context file at the root of your project. Different AI tools read different files:

| File                              | Read by                       |
| :-------------------------------- | :---------------------------- |
| `CLAUDE.md`                       | Claude Code                   |
| `AGENTS.md`                       | OpenAI Codex, Jules, OpenCode |
| `.cursor/rules/*.md`              | Cursor                        |
| `.github/copilot-instructions.md` | GitHub Copilot                |
| `CONVENTIONS.md`                  | Windsurf, Cline, and others   |

Create the file that matches your AI tool (or multiple files if your team uses different tools) and paste the snippet below. This gives the AI essential Trigger.dev context without installing anything.

<Accordion title="Copy the snippet">
  ````markdown theme={"theme":"css-variables"}
  # Trigger.dev rules

  ## Imports

  Always import from `@trigger.dev/sdk` — never from `@trigger.dev/sdk/v3` or use the deprecated `client.defineJob` pattern.

  ## Task pattern

  Every task must be exported. Use `task()` from `@trigger.dev/sdk`:

  ```ts
  import { task } from "@trigger.dev/sdk";

  export const myTask = task({
    id: "my-task",
    retry: {
      maxAttempts: 3,
      factor: 1.8,
      minTimeoutInMs: 500,
      maxTimeoutInMs: 30_000,
    },
    run: async (payload: { url: string }) => {
      // No timeouts — runs can take as long as needed
      return { success: true };
    },
  });
  ```

  ## Triggering tasks

  From your backend (Next.js route, Express handler, etc.):

  ```ts
  import type { myTask } from "./trigger/my-task";
  import { tasks } from "@trigger.dev/sdk";

  // Fire and forget
  const handle = await tasks.trigger<typeof myTask>("my-task", { url: "https://example.com" });

  // Batch trigger (up to 1,000 items)
  const batchHandle = await tasks.batchTrigger<typeof myTask>("my-task", [
    { payload: { url: "https://example.com/1" } },
    { payload: { url: "https://example.com/2" } },
  ]);
  ```

  ### From inside other tasks

  ```ts
  export const parentTask = task({
    id: "parent-task",
    run: async (payload) => {
      // Fire and forget
      await childTask.trigger({ data: "value" });

      // Wait for result — returns a Result object, NOT the output directly
      const result = await childTask.triggerAndWait({ data: "value" });
      if (result.ok) {
        console.log(result.output); // The actual return value
      } else {
        console.error(result.error);
      }

      // Or use .unwrap() to get output directly (throws on failure)
      const output = await childTask.triggerAndWait({ data: "value" }).unwrap();
    },
  });
  ```

  > Never wrap `triggerAndWait` or `batchTriggerAndWait` in `Promise.all` — this is not supported.

  ## Error handling

  ```ts
  import { task, retry, AbortTaskRunError } from "@trigger.dev/sdk";

  export const resilientTask = task({
    id: "resilient-task",
    retry: { maxAttempts: 5 },
    run: async (payload) => {
      // Permanent error — skip retrying
      if (!payload.isValid) {
        throw new AbortTaskRunError("Invalid payload, will not retry");
      }

      // Retry a specific block (not the whole task)
      const data = await retry.onThrow(
        async () => await fetchExternalApi(payload),
        { maxAttempts: 3 }
      );

      return data;
    },
  });
  ```

  ## Schema validation

  Use `schemaTask` with Zod for payload validation:

  ```ts
  import { schemaTask } from "@trigger.dev/sdk";
  import { z } from "zod";

  export const processVideo = schemaTask({
    id: "process-video",
    schema: z.object({ videoUrl: z.string().url() }),
    run: async (payload) => {
      // payload is typed and validated
    },
  });
  ```

  ## Waits

  Use `wait.for` for delays, `wait.until` for dates, and `wait.forToken` for external callbacks:

  ```ts
  import { wait } from "@trigger.dev/sdk";
  await wait.for({ seconds: 30 });
  await wait.until({ date: new Date("2025-01-01") });
  ```

  ## Configuration

  `trigger.config.ts` lives at the project root:

  ```ts
  import { defineConfig } from "@trigger.dev/sdk/build";

  export default defineConfig({
    project: "<your-project-ref>",
    dirs: ["./trigger"],
  });
  ```

  ## Common mistakes

  1. **Forgetting to export tasks** — every task must be a named export
  2. **Importing from `@trigger.dev/sdk/v3`** — this is the old v3 path; always use `@trigger.dev/sdk`
  3. **Using `client.defineJob()`** — this is the deprecated v2 API
  4. **Calling `task.trigger()` directly** — use `tasks.trigger<typeof myTask>("task-id", payload)` from your backend
  5. **Using `triggerAndWait` result as output** — it returns a `Result` object; check `result.ok` then access `result.output`, or use `.unwrap()`
  6. **Wrapping waits/triggerAndWait in `Promise.all`** — not supported in Trigger.dev tasks
  7. **Adding timeouts to tasks** — tasks have no built-in timeout; use `maxDuration` in config if needed
  ````
</Accordion>

## llms.txt

We also publish machine-readable documentation for LLM consumption:

* [trigger.dev/docs/llms.txt](https://trigger.dev/docs/llms.txt) — concise overview
* [trigger.dev/docs/llms-full.txt](https://trigger.dev/docs/llms-full.txt) — full documentation

These follow the [llms.txt standard](https://llmstxt.org) and can be fed directly into any LLM context window.

## Troubleshooting

<AccordionGroup>
  <Accordion title="AI keeps generating old v2/v3 code">
    Install [Agent Rules](/mcp-agent-rules) or [Skills](/skills) — they override the outdated patterns in the AI's training data. The [context snippet](#project-level-context-snippet) above is a quick alternative.
  </Accordion>

  <Accordion title="MCP server won't connect">
    1. Make sure you've restarted your AI client after adding the config
    2. Run `npx trigger.dev@latest install-mcp` again — it will detect and fix common issues
    3. Check that `npx trigger.dev@latest mcp` runs without errors in your terminal
    4. See the [MCP introduction](/mcp-introduction) for client-specific config details
  </Accordion>

  <Accordion title="Which tool should I install?">
    All three if possible. If you can only pick one:

    * **Agent Rules** if you want the broadest code generation improvement
    * **Skills** if you use multiple AI tools and want a single install
    * **MCP Server** if you need to trigger tasks, deploy, and search docs from your AI
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup>
  <Card title="MCP Server" icon="sparkles" href="/mcp-introduction">
    Install and configure the MCP Server for live project interaction.
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/skills">
    Portable instruction sets for any AI coding assistant.
  </Card>

  <Card title="Agent Rules" icon="scroll" href="/mcp-agent-rules">
    Comprehensive rule sets installed into your AI client.
  </Card>

  <Card title="Writing tasks" icon="code" href="/tasks/overview">
    Learn the task patterns your AI assistant will follow.
  </Card>
</CardGroup>

---

## MCP Introduction

Learn how to install and configure the Trigger.dev MCP Server

## What is the Trigger.dev MCP Server?

The Trigger.dev MCP (Model Context Protocol) Server enables AI assistants to interact directly with your Trigger.dev projects. It provides a comprehensive set of tools to:

* Search Trigger.dev documentation
* Initialize new Trigger.dev projects
* List and manage your projects and organizations
* Get task information and trigger task runs
* Deploy projects to different environments
* Monitor run details and list runs with filtering options

## Installation

The quickest way to get set up is the interactive installer:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest install-mcp
```

It will detect your installed clients and configure them automatically. You can also copy-paste the config for your client below.

## Client Configuration

Each client has a slightly different config format. Copy the snippet for your client into the appropriate file.

<Tabs>
  <Tab title="Claude Code">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client claude-code
    ```

    Or add this configuration to `~/.claude.json` (user) or `.mcp.json` (project):

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Claude Code MCP docs ↗](https://code.claude.com/docs/en/mcp)
  </Tab>

  <Tab title="Cursor">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client cursor
    ```

    Or add this configuration to `~/.cursor/mcp.json` (user) or `.cursor/mcp.json` (project):

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Cursor MCP docs ↗](https://cursor.com/docs/context/mcp)
  </Tab>

  <Tab title="Windsurf">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client windsurf
    ```

    Or add this configuration to `~/.codeium/windsurf/mcp_config.json`:

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Windsurf MCP docs ↗](https://docs.windsurf.com/windsurf/cascade/mcp)
  </Tab>

  <Tab title="VS Code">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client vscode
    ```

    Or add this configuration to `.vscode/mcp.json` (project) or `~/Library/Application Support/Code/User/mcp.json` (user, macOS):

    ```json theme={"theme":"css-variables"}
    {
      "servers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    <Note>VS Code uses `servers` instead of `mcpServers`.</Note>

    [View VS Code MCP docs ↗](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
  </Tab>

  <Tab title="Zed">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client zed
    ```

    Or add this configuration to `~/.config/zed/settings.json`:

    ```json theme={"theme":"css-variables"}
    {
      "context_servers": {
        "trigger": {
          "source": "custom",
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Zed context servers docs ↗](https://zed.dev/docs/ai/mcp)
  </Tab>

  <Tab title="Cline">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client cline
    ```

    Or add this configuration to `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`:

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Cline MCP docs ↗](https://docs.cline.bot/mcp/configuring-mcp-servers)
  </Tab>

  <Tab title="Gemini CLI">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client gemini-cli
    ```

    Or add this configuration to `~/.gemini/settings.json` (user) or `.gemini/settings.json` (project):

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="AMP">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client amp
    ```

    Or add this configuration to `~/.config/amp/settings.json`:

    ```json theme={"theme":"css-variables"}
    {
      "amp.mcpServers": {
        "trigger": {
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Sourcegraph AMP MCP docs ↗](https://ampcode.com/manual#mcp)
  </Tab>

  <Tab title="Codex CLI">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client openai-codex
    ```

    Or add this configuration to `~/.codex/config.toml`:

    ```toml theme={"theme":"css-variables"}
    [mcp_servers.trigger]
    command = "npx"
    args = ["trigger.dev@latest", "mcp"]
    ```
  </Tab>

  <Tab title="Crush">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client crush
    ```

    Or add this configuration to `.crush.json` (project), `crush.json`, or `~/.config/crush/crush.json` (user). Files are loaded in priority order: `.crush.json` → `crush.json` → `$HOME/.config/crush/crush.json`.

    ```json theme={"theme":"css-variables"}
    {
      "mcp": {
        "trigger": {
          "type": "stdio",
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```

    [View Charm MCP docs ↗](https://github.com/charmbracelet/crush)
  </Tab>

  <Tab title="opencode">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client opencode
    ```

    Or add this configuration to `~/.config/opencode/opencode.json` (user) or `./opencode.json` (project):

    ```json theme={"theme":"css-variables"}
    {
      "mcp": {
        "trigger": {
          "type": "local",
          "command": ["npx", "trigger.dev@latest", "mcp"],
          "enabled": true
        }
      }
    }
    ```

    [View opencode MCP docs ↗](https://opencode.ai/docs/mcp-servers/)
  </Tab>

  <Tab title="Ruler">
    Install using the command line:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest install-mcp --client ruler
    ```

    Or add this configuration to `.ruler/mcp.json`:

    ```json theme={"theme":"css-variables"}
    {
      "mcpServers": {
        "trigger": {
          "type": "stdio",
          "command": "npx",
          "args": ["trigger.dev@latest", "mcp"]
        }
      }
    }
    ```
  </Tab>
</Tabs>

After adding the config, restart your client. You should see a server named **trigger** connect automatically.

## Authentication

The `search_docs` tool works without authentication. All other tools require you to be logged in via the [Trigger.dev CLI](/cli-login-commands). The first time you use an authenticated tool, your MCP client will prompt you to log in.

<Accordion title="CLI Options">
  The `install-mcp` command supports these options:

  **Core Options**

  * `-p, --project-ref <project ref>` — Scope the MCP server to a specific project
  * `-t, --tag <package tag>` — CLI package version to use (default: latest)
  * `--dev-only` — Restrict to the dev environment only
  * `--yolo` — Install into all supported clients automatically
  * `--scope <scope>` — `user`, `project`, or `local`
  * `--client <clients...>` — Install into specific client(s)

  **Configuration Options**

  * `--log-file <log file>` — Write logs to a file
  * `-a, --api-url <value>` — Custom Trigger.dev API URL
  * `-l, --log-level <level>` — Log level (debug, info, log, warn, error, none)

  **Examples**

  Install for all supported clients:

  ```bash theme={"theme":"css-variables"}
  npx trigger.dev@latest install-mcp --yolo
  ```

  Install for specific clients:

  ```bash theme={"theme":"css-variables"}
  npx trigger.dev@latest install-mcp --client claude-code cursor --scope user
  ```

  Restrict to dev environment for a specific project:

  ```bash theme={"theme":"css-variables"}
  npx trigger.dev@latest install-mcp --dev-only --project-ref proj_abc123
  ```

  To add these options to a manual config, append them to the `args` array:

  ```json theme={"theme":"css-variables"}
  {
    "args": ["trigger.dev@latest", "mcp", "--dev-only", "--project-ref", "proj_abc123"]
  }
  ```
</Accordion>

## Getting Started

Once installed, you can start using the MCP server by asking your AI assistant questions like:

* `"Search the trigger docs for a ffmpeg example"`
* `"Initialize trigger.dev in my project"`
* `"Get all tasks in my project"`
* `"Trigger my foobar task with a sample payload"`
* `"Get the details of the latest run for my foobar task"`
* `"List all runs for my foobar task"`
* `"Deploy my project to staging"`
* `"Deploy my project to production"`

## Next Steps

<CardGroup>
  <Card title="MCP Tools" icon="wrench" href="/mcp-tools">
    Explore all available MCP tools for managing your projects.
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/skills">
    Portable instruction sets that teach AI assistants Trigger.dev patterns.
  </Card>

  <Card title="Agent Rules" icon="scroll" href="/mcp-agent-rules">
    Install comprehensive rule sets directly into your AI client.
  </Card>
</CardGroup>

---

## MCP Tools

Learn about how to use the tools available in the Trigger.dev MCP Server

## Documentation and Search Tools

### search\_docs

Search the Trigger.dev documentation for guides, examples, and API references.

**Example usage:**

* `"How do I create a scheduled task?"`
* `"Show me webhook examples"`
* `"What are the deployment options?"`

## Project Management Tools

### list\_orgs

List all organizations you have access to.

**Example usage:**

* `"What organizations do I have?"`
* `"Show me my orgs"`

### list\_projects

List all projects in your Trigger.dev account.

**Example usage:**

* `"What projects do I have?"`
* `"List my Trigger.dev projects"`

### create\_project\_in\_org

Create a new project in an organization.

**Example usage:**

* `"Create a new project called 'my-app'"`
* `"Set up a new Trigger.dev project"`

### initialize\_project

Initialize Trigger.dev in your project with automatic setup and configuration.

**Example usage:**

* `"Set up Trigger.dev in this project"`
* `"Add Trigger.dev to my app"`

## Task Management Tools

### get\_current\_worker

Get the current worker for a project, including the worker version, SDK version, and registered tasks with their payload schemas.

**Example usage:**

* `"What tasks are available?"`
* `"Show me the tasks in dev"`

### trigger\_task

Trigger a task to run with a specific payload. You can add a delay, set tags, configure retries, choose a machine size, set a TTL, or use an idempotency key.

**Example usage:**

* `"Run the email-notification task"`
* `"Trigger my-task with userId 123"`
* `"Execute the sync task in production"`

## Run Monitoring Tools

### get\_run\_details

Get detailed information about a specific task run, including logs and status. Enable debug mode to get the full trace with all logs and spans.

**Example usage:**

* `"Show me details for run run_abc123"`
* `"Why did this run fail?"`

### list\_runs

List runs for a project. Filter by status, task, tags, version, machine size, or time period.

**Example usage:**

* `"Show me recent runs"`
* `"List failed runs from the last 7 days"`
* `"What runs are currently executing?"`

### wait\_for\_run\_to\_complete

Wait for a specific run to finish and return the result.

**Example usage:**

* `"Wait for run run_abc123 to complete"`

### cancel\_run

Cancel a running or queued run.

**Example usage:**

* `"Cancel run run_abc123"`
* `"Stop that task"`

## Deployment Tools

### deploy

Deploy your project to staging or production.

**Example usage:**

* `"Deploy to production"`
* `"Deploy to staging"`

### list\_deploys

List deployments for a project. Filter by status or time period.

**Example usage:**

* `"Show me recent deployments"`
* `"What's deployed to production?"`

### list\_preview\_branches

List all preview branches in the project.

**Example usage:**

* `"What preview branches exist?"`
* `"Show me preview deployments"`

<Callout type="warning">
  The deploy and list\_preview\_branches tools are not available when the MCP server is running with the `--dev-only` flag.
</Callout>

---

## Agent rules

Install Trigger.dev agent rules to guide AI assistants toward correct, up-to-date code patterns.

## What are Trigger.dev agent rules?

Trigger.dev agent rules are comprehensive instruction sets that guide AI assistants to write optimal Trigger.dev code. These rules ensure your AI assistant understands best practices, current APIs, and recommended patterns when working with Trigger.dev projects.

<Note>
  Agent Rules are one of three AI tools we provide. You can also install [Skills](/skills) for portable cross-editor instruction sets or the [MCP Server](/mcp-introduction) for live project interaction. See the [comparison table](/building-with-ai#skills-vs-agent-rules-vs-mcp) for details.
</Note>

## Installation

Install the agent rules with the following command:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest install-rules
```

## Available rule sets

We provide five specialized rule sets, each optimized for different aspects of Trigger.dev development:

| Rule set            | Tokens | Description                                                                                  | GitHub                                                                                        |
| :------------------ | :----- | :------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Basic tasks**     | 1,200  | Essential rules for writing basic Trigger.dev tasks and fundamental patterns                 | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/basic-tasks.md)     |
| **Advanced tasks**  | 3,000  | Comprehensive rules for complex workflows, error handling, and advanced task patterns        | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/advanced-tasks.md)  |
| **Scheduled tasks** | 780    | Specialized guidance for cron jobs, scheduled workflows, and time-based triggers             | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/scheduled-tasks.md) |
| **Configuration**   | 1,900  | Complete guide for trigger.config.ts setup, environment configuration, and project structure | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/config.md)          |
| **Realtime**        | 1,700  | Using Trigger.dev Realtime features and frontend integration patterns                        | [View](https://github.com/triggerdotdev/trigger.dev/blob/main/rules/4.0.0/realtime.md)        |

## Claude Code subagent

For Claude Code users, we provide a subagent called `trigger-dev-expert` that's an expert at writing well-structured Trigger.dev code.

### Installation

The subagent is available as an option when running the rules installation command. Select "Claude Code" as your client and choose to include the subagent when prompted.

<img alt="Claude Code subagent installation" />

### Usage

Activate the subagent in your prompts by requesting it explicitly:

```markdown theme={"theme":"css-variables"}
use the trigger-dev-expert subagent to create a trigger.dev job that accepts a video url, processes it with ffmpeg to extract the audio, runs the audio through a text-to-speech API like openai, and then uploads both the transcription and the audio to s3
```

The subagent works best when combined with the appropriate rule sets installed alongside it, providing both high-level architectural guidance and detailed implementation knowledge.

## Supported AI clients

The Trigger.dev rules work across a wide range of AI coding assistants and editors:

| Client              | Rule activation                                          | Docs                                                              |
| :------------------ | :------------------------------------------------------- | :---------------------------------------------------------------- |
| **Cursor**          | Automatic when working in trigger directories            | [Link](https://docs.cursor.com/en/context/rules#rules/)           |
| **Claude Code**     | Context-aware activation + custom subagent               | [Link](https://docs.anthropic.com/en/docs/claude-code)            |
| **VSCode Copilot**  | Integration with GitHub Copilot chat                     | [Link](https://code.visualstudio.com/docs/copilot/overview)       |
| **Windsurf**        | Automatic activation in Trigger.dev projects             | [Link](https://docs.windsurf.com/windsurf/cascade/memories#rules) |
| **Gemini CLI**      | Command-line integration                                 | [Link](https://ai.google.dev/gemini-api/docs)                     |
| **Cline**           | Automatic context detection                              | [Link](https://github.com/cline/cline)                            |
| **Sourcegraph AMP** | Code intelligence integration                            | [Link](https://sourcegraph.com/docs)                              |
| **Kilo**            | Custom rule integration                                  | [Link](https://kilocode.ai/docs/advanced-usage/custom-rules)      |
| **Ruler**           | Rule management                                          | [Link](https://github.com/intellectronica/ruler)                  |
| **AGENTS.md**       | Universal format for OpenAI Codex, Jules, OpenCode, etc. |                                                                   |

### Rule activation behavior

Different AI tools handle rules differently:

* **Automatic Activation**: Cursor, Windsurf, VSCode Copilot, and Cline automatically apply relevant rules when working in Trigger.dev projects or when `trigger.config.ts` is detected
* **Context-Aware**: Claude Code intelligently applies rules based on the current context and file types
* **Manual Integration**: AGENTS.md clients and others append rules to configuration files for manual activation

## Keeping rules updated

Trigger.dev rules are regularly updated to reflect new features, API changes, and best practices. The CLI includes automatic update detection.

### Automatic update notifications

When running `npx trigger.dev@latest dev`, you'll receive notifications when newer rule versions are available with a simple update command.

### Manual updates

Update rules anytime with:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest install-rules
```

The update process replaces existing rules without creating duplicates, keeping your configuration files clean and organized.

### Why updates matter

* **Current API patterns**: Access the latest Trigger.dev APIs and features
* **Performance optimizations**: Benefit from improved patterns and practices
* **Deprecated pattern avoidance**: Prevent AI assistants from generating outdated code
* **New feature support**: Immediate access to newly released capabilities

## Getting started

1. Install the rules:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest install-rules
```

2. Follow the prompts to install the rules for your AI client.

3. Consider installing the `trigger-dev-expert` subagent if using Claude Code.

## Next steps

<CardGroup>
  <Card title="Skills" icon="wand-magic-sparkles" href="/skills">
    Portable instruction sets that work across all AI coding assistants.
  </Card>

  <Card title="MCP Server" icon="sparkles" href="/mcp-introduction">
    Give your AI assistant direct access to Trigger.dev tools and APIs.
  </Card>

  <Card title="Complete AI setup" icon="layer-group" href="/building-with-ai">
    See all AI tools and how they compare.
  </Card>

  <Card title="Writing tasks" icon="code" href="/tasks/overview">
    Learn the task patterns that agent rules teach your AI assistant.
  </Card>
</CardGroup>

---

## Skills

Install Trigger.dev skills to teach any AI coding assistant best practices for writing tasks, agents, and workflows.

## What are agent skills?

Skills are portable instruction sets that teach AI coding assistants how to use Trigger.dev effectively. Unlike vendor-specific config files (`.cursor/rules`, `CLAUDE.md`), skills use an open standard that works across all major AI assistants. For example, Cursor users and Claude Code users can get the same knowledge from a single install.

<Note>
  Skills are one of three AI tools we provide. You can also install [Agent Rules](/mcp-agent-rules) for client-specific rule sets or the [MCP Server](/mcp-introduction) for live project interaction. See the [comparison table](/building-with-ai#skills-vs-agent-rules-vs-mcp) for details.
</Note>

Skills are installed as directories containing a `SKILL.md` file. Each `SKILL.md` includes YAML frontmatter (name, description) and markdown instructions with patterns, examples, and best practices that AI assistants automatically discover and follow.

## Installation

When you run `npx skills add triggerdotdev/skills`, the CLI detects your installed AI tools and copies the appropriate files to each tool's expected location. For example, `.claude/skills/`, `.cursor/skills/`, `.github/skills/`, etc.

```bash theme={"theme":"css-variables"}
npx skills add triggerdotdev/skills
```

<Note>`skills` is an open-source CLI by Vercel. Learn more at [skills.sh](https://skills.sh).</Note>

The result: your AI assistant understands Trigger.dev's specific patterns for exports, schema validation, error handling, retries, and more.

## Available skills

Install all skills at once, or pick the ones relevant to your current work:

```bash theme={"theme":"css-variables"}
# Install all Trigger.dev skills
npx skills add triggerdotdev/skills

# Or install individual skills
npx skills add triggerdotdev/skills --skill trigger-tasks
npx skills add triggerdotdev/skills --skill trigger-agents
npx skills add triggerdotdev/skills --skill trigger-config
npx skills add triggerdotdev/skills --skill trigger-realtime
npx skills add triggerdotdev/skills --skill trigger-setup
```

| Skill              | Use for                                                    | Covers                                                       |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| `trigger-setup`    | First time setup, new projects                             | SDK install, `npx trigger init`, project structure           |
| `trigger-tasks`    | Writing background tasks, async workflows, scheduled tasks | Triggering, waits, queues, retries, cron, metadata           |
| `trigger-agents`   | LLM workflows, orchestration, multi-step AI agents         | Prompt chaining, routing, parallelization, human-in-the-loop |
| `trigger-realtime` | Live updates, progress indicators, streaming               | React hooks, progress bars, streaming AI responses           |
| `trigger-config`   | Project setup, build configuration                         | `trigger.config.ts`, extensions (Prisma, FFmpeg, Playwright) |

Not sure which skill to install? Install `trigger-tasks`; it covers the most common patterns for writing Trigger.dev tasks.

## Supported AI assistants

Skills work with any AI coding assistant that supports the [Agent Skills standard](https://agentskills.io), including:

* [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
* [Cursor](https://cursor.com)
* [Windsurf](https://codeium.com/windsurf)
* [GitHub Copilot](https://github.com/features/copilot)
* [Cline](https://github.com/cline/cline)
* [Codex CLI](https://github.com/openai/codex)
* [Gemini CLI](https://github.com/google-gemini/gemini-cli)
* [OpenCode](https://opencode.ai)
* [View all →](https://skills.sh)

## Next steps

<CardGroup>
  <Card title="Agent Rules" icon="scroll" href="/mcp-agent-rules">
    Install comprehensive rule sets directly into your AI client.
  </Card>

  <Card title="MCP Server" icon="sparkles" href="/mcp-introduction">
    Give your AI assistant direct access to Trigger.dev tools and APIs.
  </Card>

  <Card title="Writing tasks" icon="code" href="/tasks/overview">
    Learn the task patterns that skills teach your AI assistant.
  </Card>

  <Card title="skills.sh" icon="box" href="https://skills.sh">
    Browse the full Agent Skills ecosystem.
  </Card>
</CardGroup>

---
