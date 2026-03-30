> Sources:
> - https://trigger.dev/docs/guides/ai-agents/overview
> - https://trigger.dev/docs/guides/ai-agents/claude-code-trigger
> - https://trigger.dev/docs/guides/ai-agents/generate-translate-copy
> - https://trigger.dev/docs/guides/ai-agents/respond-and-check-content
> - https://trigger.dev/docs/guides/ai-agents/route-question
> - https://trigger.dev/docs/guides/ai-agents/translate-and-refine
> - https://trigger.dev/docs/guides/ai-agents/verify-news-article

# AI Agent Guides

## AI agents overview

Real world AI agent example tasks using Trigger.dev

## Example projects using AI agents

<CardGroup>
  <Card icon="scroll" title="Claude changelog generator" href="/guides/example-projects/claude-changelog-generator">
    Automatically generate professional changelogs from git commits using Claude.
  </Card>

  <Card icon="book" title="Claude GitHub wiki agent" href="/guides/example-projects/claude-github-wiki">
    Generate and maintain GitHub wiki documentation with Claude-powered analysis.
  </Card>

  <Card icon="hand" title="Human-in-the-loop workflow" href="/guides/example-projects/human-in-the-loop-workflow">
    Create audio summaries of newspaper articles using a human-in-the-loop workflow built with
    ReactFlow and Trigger.dev waitpoint tokens.
  </Card>

  <Card title="Mastra agents with memory" icon="database" href="/guides/example-projects/mastra-agents-with-memory">
    Use Mastra to create a weather agent that can collect live weather data and generate clothing
    recommendations.
  </Card>

  <Card title="OpenAI Agent Python SDK guardrails" icon="snake" href="/guides/example-projects/openai-agent-sdk-guardrails">
    Use the OpenAI Agent SDK to create a guardrails system for your AI agents.
  </Card>

  <Card title="OpenAI Agent TypeScript SDK playground" icon="rocket" href="/guides/example-projects/openai-agents-sdk-typescript-playground">
    A playground containing 7 AI agents using the OpenAI Agent SDK for TypeScript with Trigger.dev.
  </Card>

  <Card title="Vercel AI SDK deep research agent" icon="triangle" href="/guides/example-projects/vercel-ai-sdk-deep-research">
    Use the Vercel AI SDK to generate comprehensive PDF reports using a deep research agent.
  </Card>

  <Card title="Smart Spreadsheet" icon="table" href="/guides/example-projects/smart-spreadsheet">
    Enrich company data using Exa search and Claude with real-time streaming results.
  </Card>
</CardGroup>

## Agent fundamentals

These guides will show you how to set up different types of AI agent workflows with Trigger.dev. The examples take inspiration from Anthropic's blog post on [building effective agents](https://www.anthropic.com/research/building-effective-agents).

<CardGroup>
  <Card title="Prompt chaining" href="/guides/ai-agents/generate-translate-copy">
    Chain prompts together to generate and translate marketing copy automatically
  </Card>

  <Card title="Routing" href="/guides/ai-agents/route-question">
    Send questions to different AI models based on complexity analysis
  </Card>

  <Card title="Parallelization" href="/guides/ai-agents/respond-and-check-content">
    Simultaneously check for inappropriate content while responding to customer inquiries
  </Card>

  <Card title="Orchestrator" href="/guides/ai-agents/verify-news-article">
    Coordinate multiple AI workers to verify news article accuracy
  </Card>

  <Card title="Evaluator-optimizer" href="/guides/ai-agents/translate-and-refine">
    Translate text and automatically improve quality through feedback loops
  </Card>
</CardGroup>

---

## Claude Agent SDK setup guide

Build AI agents that can read files, run commands, and edit code using the Claude Agent SDK and Trigger.dev.

The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) gives you the same tools, agent loop, and context management that power Claude Code. Combined with Trigger.dev, you get durable execution, automatic retries, and full observability for your agents.

## Setup

<Note>
  This guide assumes you are working with an existing [Trigger.dev](https://trigger.dev) project.
  Follow our [quickstart](/quick-start) to get set up if you don't have a project yet.
</Note>

<Steps>
  <Step title="Install the Claude Agent SDK">
    ```bash npm theme={"theme":"css-variables"}
    npm install @anthropic-ai/claude-agent-sdk
    ```
  </Step>

  <Step title="Configure trigger.config.ts">
    Add the SDK to the `external` array so it's not bundled:

    ```ts trigger.config.ts theme={"theme":"css-variables"}
    import { defineConfig } from "@trigger.dev/sdk";

    export default defineConfig({
      project: process.env.TRIGGER_PROJECT_REF!,
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
  </Step>

  <Step title="Set your API key">
    Add your Anthropic API key to your environment variables. The SDK reads it automatically.

    ```bash theme={"theme":"css-variables"}
    ANTHROPIC_API_KEY=sk-ant-...
    ```

    You can set this in the [Trigger.dev dashboard](https://cloud.trigger.dev) under **Environment Variables**, or in your `.env` file for local development.
  </Step>

  <Step title="Create your first agent task">
    This example creates a task where Claude generates code in an empty workspace. The agent will create files based on your prompt:

    ```ts trigger/claude-agent.ts theme={"theme":"css-variables"}
    import { query } from "@anthropic-ai/claude-agent-sdk";
    import { schemaTask, logger } from "@trigger.dev/sdk";
    import { mkdtemp, rm, readdir } from "node:fs/promises";
    import { tmpdir } from "node:os";
    import { join } from "node:path";
    import { z } from "zod";

    export const codeGenerator = schemaTask({
      id: "code-generator",
      schema: z.object({
        prompt: z.string(),
      }),
      run: async ({ prompt }, { signal }) => {
        const abortController = new AbortController();
        signal.addEventListener("abort", () => abortController.abort());

        // Create an empty workspace for the agent
        // The agent will create files here based on the prompt
        const workDir = await mkdtemp(join(tmpdir(), "claude-agent-"));
        logger.info("Created workspace", { workDir });

        try {
          const result = query({
            prompt,
            options: {
              model: "claude-sonnet-4-20250514",
              abortController,
              cwd: workDir,
              maxTurns: 10,
              permissionMode: "acceptEdits",
              allowedTools: ["Read", "Edit", "Write", "Glob"],
            },
          });

          for await (const message of result) {
            logger.info("Agent message", { type: message.type });
          }

          // See what files Claude created
          const files = await readdir(workDir, { recursive: true });
          logger.info("Files created", { files });

          return { filesCreated: files };
        } finally {
          await rm(workDir, { recursive: true, force: true });
        }
      },
    });
    ```
  </Step>

  <Step title="Run the dev server">
    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest dev
    ```
  </Step>

  <Step title="Test your agent">
    Go to the Trigger.dev dashboard, find your `code-generator` task, and trigger it with a test payload:

    ```json theme={"theme":"css-variables"}
    {
      "prompt": "Create a Node.js project with a fibonacci.ts file containing a function to calculate fibonacci numbers, and a fibonacci.test.ts file with tests."
    }
    ```
  </Step>
</Steps>

## How it works

The `query()` function runs Claude in an agentic loop where it can:

1. **Read files** - Explore codebases with `Read`, `Grep`, and `Glob` tools
2. **Edit files** - Modify code with `Edit` and `Write` tools
3. **Run commands** - Execute shell commands with `Bash` tool (if enabled)
4. **Think step by step** - Use extended thinking for complex problems

The agent continues until it completes the task or reaches `maxTurns`.

### Permission modes

| Mode                  | What it does                                          |
| --------------------- | ----------------------------------------------------- |
| `"default"`           | Asks for approval on potentially dangerous operations |
| `"acceptEdits"`       | Auto-approves file operations, asks for bash/network  |
| `"bypassPermissions"` | Skips all safety checks (not recommended)             |

### Available tools

```ts theme={"theme":"css-variables"}
allowedTools: [
  "Task", // Planning and task management
  "Glob", // Find files by pattern
  "Grep", // Search file contents
  "Read", // Read file contents
  "Edit", // Edit existing files
  "Write", // Create new files
  "Bash", // Run shell commands
  "TodoRead", // Read todo list
  "TodoWrite", // Update todo list
];
```

## GitHub repo

<Card title="View the Claude Agent SDK + Trigger.dev example" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/claude-agent-sdk-trigger">
  A complete example with two agent patterns: basic safe code generation and advanced with bash
  execution.
</Card>

## Example projects using the Claude Agent SDK

<CardGroup>
  <Card title="Claude changelog generator" icon="scroll" href="/guides/example-projects/claude-changelog-generator">
    Generate changelogs from git commits using custom MCP tools.
  </Card>

  <Card title="Claude GitHub wiki agent" icon="book" href="/guides/example-projects/claude-github-wiki">
    Analyze repositories and answer questions with real-time streaming.
  </Card>
</CardGroup>

## Learn more

* [Claude Agent SDK docs](https://platform.claude.com/docs/en/agent-sdk/overview) – Official Anthropic documentation
* [Trigger.dev Realtime](/realtime/overview) – Stream agent progress to your frontend
* [Waitpoints](/wait) – Add human-in-the-loop approval steps

---

## Generate and translate copy

Create an AI agent workflow that generates and translates copy

## Overview

**Prompt chaining** is an AI workflow pattern that decomposes a complex task into a sequence of steps, where each LLM call processes the output of the previous one. This approach trades off latency for higher accuracy by making each LLM call an easier, more focused task, with the ability to add programmatic checks between steps to ensure the process remains on track.

<img alt="Generating and translating copy" />

## Example task

In this example, we'll create a workflow that generates and translates copy. This approach is particularly effective when tasks require different models or approaches for different inputs.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` to provide LLM logs
* Generates marketing copy based on subject and target word count
* Validates the generated copy meets word count requirements (±10 words)
* Translates the validated copy to the target language while preserving tone

```typescript theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { task } from "@trigger.dev/sdk";
import { generateText } from "ai";

export interface TranslatePayload {
  marketingSubject: string;
  targetLanguage: string;
  targetWordCount: number;
}

export const generateAndTranslateTask = task({
  id: "generate-and-translate-copy",
  maxDuration: 300, // Stop executing after 5 mins of compute
  run: async (payload: TranslatePayload) => {
    // Step 1: Generate marketing copy
    const generatedCopy = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: "You are an expert copywriter.",
        },
        {
          role: "user",
          content: `Generate as close as possible to ${payload.targetWordCount} words of compelling marketing copy for ${payload.marketingSubject}`,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-and-translate-copy",
      },
    });

    // Gate: Validate the generated copy meets the word count target
    const wordCount = generatedCopy.text.split(/\s+/).length;

    if (
      wordCount < payload.targetWordCount - 10 ||
      wordCount > payload.targetWordCount + 10
    ) {
      throw new Error(
        `Generated copy length (${wordCount} words) is outside acceptable range of ${
          payload.targetWordCount - 10
        }-${payload.targetWordCount + 10} words`
      );
    }

    // Step 2: Translate to target language
    const translatedCopy = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: `You are an expert translator specializing in marketing content translation into ${payload.targetLanguage}.`,
        },
        {
          role: "user",
          content: `Translate the following marketing copy to ${payload.targetLanguage}, maintaining the same tone and marketing impact:\n\n${generatedCopy.text}`,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-and-translate-copy",
      },
    });

    return {
      englishCopy: generatedCopy,
      translatedCopy,
    };
  },
});
```

## Run a test

On the Test page in the dashboard, select the `generate-and-translate-copy` task and include a payload like the following:

```json theme={"theme":"css-variables"}
{
  marketingSubject: "The controversial new Jaguar electric concept car",
  targetLanguage: "Spanish",
  targetWordCount: 100,
}
```

This example payload generates copy and then translates it using sequential LLM calls. The translation only begins after the generated copy has been validated against the word count requirements.

<video />

---

## Respond to customer inquiry and check for inappropriate content

Create an AI agent workflow that responds to customer inquiries while checking if their text is inappropriate

## Overview

**Parallelization** is a workflow pattern where multiple tasks or processes run simultaneously instead of sequentially, allowing for more efficient use of resources and faster overall execution. It's particularly valuable when different parts of a task can be handled independently, such as running content analysis and response generation at the same time.

<img alt="Parallelization" />

## Example task

In this example, we'll create a workflow that simultaneously checks content for issues while responding to customer inquiries. This approach is particularly effective when tasks require multiple perspectives or parallel processing streams, with the orchestrator synthesizing the results into a cohesive output.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` to provide LLM logs
* Uses [`batch.triggerByTaskAndWait`](/triggering#batch-triggerbytaskandwait) to run customer response and content moderation tasks in parallel
* Generates customer service responses using an AI model
* Simultaneously checks for inappropriate content while generating responses

```typescript theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { batch, task } from "@trigger.dev/sdk";
import { generateText } from "ai";

// Task to generate customer response
export const generateCustomerResponse = task({
  id: "generate-customer-response",
  run: async (payload: { question: string }) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: "You are a helpful customer service representative.",
        },
        { role: "user", content: payload.question },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-customer-response",
      },
    });

    return response.text;
  },
});

// Task to check for inappropriate content
export const checkInappropriateContent = task({
  id: "check-inappropriate-content",
  run: async (payload: { text: string }) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "You are a content moderator. Respond with 'true' if the content is inappropriate or contains harmful, threatening, offensive, or explicit content, 'false' otherwise.",
        },
        { role: "user", content: payload.text },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "check-inappropriate-content",
      },
    });

    return response.text.toLowerCase().includes("true");
  },
});

// Main task that coordinates the parallel execution
export const handleCustomerQuestion = task({
  id: "handle-customer-question",
  run: async (payload: { question: string }) => {
    const {
      runs: [responseRun, moderationRun],
    } = await batch.triggerByTaskAndWait([
      {
        task: generateCustomerResponse,
        payload: { question: payload.question },
      },
      {
        task: checkInappropriateContent,
        payload: { text: payload.question },
      },
    ]);

    // Check moderation result first
    if (moderationRun.ok && moderationRun.output === true) {
      return {
        response:
          "I apologize, but I cannot process this request as it contains inappropriate content.",
        wasInappropriate: true,
      };
    }

    // Return the generated response if everything is ok
    if (responseRun.ok) {
      return {
        response: responseRun.output,
        wasInappropriate: false,
      };
    }

    // Handle any errors
    throw new Error("Failed to process customer question");
  },
});
```

## Run a test

On the Test page in the dashboard, select the `handle-customer-question` task and include a payload like the following:

```json theme={"theme":"css-variables"}
{
  "question": "Can you explain 2FA?"
}
```

When triggered with a question, the task simultaneously generates a response while checking for inappropriate content using two parallel LLM calls. The main task waits for both operations to complete before delivering the final response.

<video />

---

## Route a question to a different AI model

Create an AI agent workflow that routes a question to a different AI model depending on its complexity

## Overview

**Routing** is a workflow pattern that classifies an input and directs it to a specialized followup task. This pattern allows for separation of concerns and building more specialized prompts, which is particularly effective when there are distinct categories that are better handled separately. Without routing, optimizing for one kind of input can hurt performance on other inputs.

<img alt="Routing" />

## Example task

In this example, we'll create a workflow that routes a question to a different AI model depending on its complexity. This approach is particularly effective when tasks require different models or approaches for different inputs.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` in the source verification and historical analysis tasks to provide LLM logs
* Routes questions using a lightweight model (`o1-mini`) to classify complexity
* Directs simple questions to `gpt-4o` and complex ones to `gpt-o3-mini`
* Returns both the answer and metadata about the routing decision

````typescript theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { task } from "@trigger.dev/sdk";
import { generateText } from "ai";
import { z } from "zod";

// Schema for router response
const routingSchema = z.object({
  model: z.enum(["gpt-4o", "gpt-o3-mini"]),
  reason: z.string(),
});

// Router prompt template
const ROUTER_PROMPT = `You are a routing assistant that determines the complexity of questions.
Analyze the following question and route it to the appropriate model:

- Use "gpt-4o" for simple, common, or straightforward questions
- Use "gpt-o3-mini" for complex, unusual, or questions requiring deep reasoning

Respond with a JSON object in this exact format:
{"model": "gpt-4o" or "gpt-o3-mini", "reason": "your reasoning here"}

Question: `;

export const routeAndAnswerQuestion = task({
  id: "route-and-answer-question",
  run: async (payload: { question: string }) => {
    // Step 1: Route the question
    const routingResponse = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "You must respond with a valid JSON object containing only 'model' and 'reason' fields. No markdown, no backticks, no explanation.",
        },
        {
          role: "user",
          content: ROUTER_PROMPT + payload.question,
        },
      ],
      temperature: 0.1,
      experimental_telemetry: {
        isEnabled: true,
        functionId: "route-and-answer-question",
      },
    });

    // Add error handling and cleanup
    let jsonText = routingResponse.text.trim();
    if (jsonText.startsWith("```")) {
      jsonText = jsonText.replace(/```json\n|\n```/g, "");
    }

    const routingResult = routingSchema.parse(JSON.parse(jsonText));

    // Step 2: Get the answer using the selected model
    const answerResult = await generateText({
      model: openai(routingResult.model),
      messages: [{ role: "user", content: payload.question }],
    });

    return {
      answer: answerResult.text,
      selectedModel: routingResult.model,
      routingReason: routingResult.reason,
    };
  },
});
````

## Run a test

Triggering our task with a simple question shows it routing to the gpt-4o model and returning the answer with reasoning:

```json theme={"theme":"css-variables"}
{
  "question": "How many planets are there in the solar system?"
}
```

<video />

---

## Translate text and refine it based on feedback

This guide will show you how to create a task that translates text and refines it based on feedback.

## Overview

This example is based on the **evaluator-optimizer** pattern, where one LLM generates a response while another provides evaluation and feedback in a loop. This is particularly effective for tasks with clear evaluation criteria where iterative refinement provides better results.

<img alt="Evaluator-optimizer" />

## Example task

This example task translates text into a target language and refines the translation over a number of iterations based on feedback provided by the LLM.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to generate the translation
* Uses `experimental_telemetry` to provide LLM logs on the Run page in the dashboard
* Runs for a maximum of 10 iterations
* Uses `generateText` again to evaluate the translation
* Recursively calls itself to refine the translation based on the feedback

```typescript theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

interface TranslationPayload {
  text: string;
  targetLanguage: string;
  previousTranslation?: string;
  feedback?: string;
  rejectionCount?: number;
}

export const translateAndRefine = task({
  id: "translate-and-refine",
  run: async (payload: TranslationPayload) => {
    const rejectionCount = payload.rejectionCount || 0;

    // Bail out if we've hit the maximum attempts
    if (rejectionCount >= 10) {
      return {
        finalTranslation: payload.previousTranslation,
        iterations: rejectionCount,
        status: "MAX_ITERATIONS_REACHED",
      };
    }

    // Generate translation (or refinement if we have previous feedback)
    const translationPrompt = payload.feedback
      ? `Previous translation: "${payload.previousTranslation}"\n\nFeedback received: "${payload.feedback}"\n\nPlease provide an improved translation addressing this feedback.`
      : `Translate this text into ${payload.targetLanguage}, preserving style and meaning: "${payload.text}"`;

    const translation = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: `You are an expert literary translator into ${payload.targetLanguage}.
                   Focus on accuracy first, then style and natural flow.`,
        },
        {
          role: "user",
          content: translationPrompt,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "translate-and-refine",
      },
    });

    // Evaluate the translation
    const evaluation = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: `You are an expert literary critic and translator focused on practical, high-quality translations.
                 Your goal is to ensure translations are accurate and natural, but not necessarily perfect.
                 This is iteration ${
                   rejectionCount + 1
                 } of a maximum 5 iterations.
                 
                 RESPONSE FORMAT:
                 - If the translation meets 90%+ quality: Respond with exactly "APPROVED" (nothing else)
                 - If improvements are needed: Provide only the specific issues that must be fixed
                 
                 Evaluation criteria:
                 - Accuracy of meaning (primary importance)
                 - Natural flow in the target language
                 - Preservation of key style elements
                 
                 DO NOT provide detailed analysis, suggestions, or compliments.
                 DO NOT include the translation in your response.
                 
                 IMPORTANT RULES:
                 - First iteration MUST receive feedback for improvement
                 - Be very strict on accuracy in early iterations
                 - After 3 iterations, lower quality threshold to 85%`,
        },
        {
          role: "user",
          content: `Original: "${payload.text}"
                 Translation: "${translation.text}"
                 Target Language: ${payload.targetLanguage}
                 Iteration: ${rejectionCount + 1}
                 Previous Feedback: ${
                   payload.feedback ? `"${payload.feedback}"` : "None"
                 }
                 
                 ${
                   rejectionCount === 0
                     ? "This is the first attempt. Find aspects to improve."
                     : 'Either respond with exactly "APPROVED" or provide only critical issues that must be fixed.'
                 }`,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "translate-and-refine",
      },
    });

    // If approved, return the final result
    if (evaluation.text.trim() === "APPROVED") {
      return {
        finalTranslation: translation.text,
        iterations: rejectionCount,
        status: "APPROVED",
      };
    }

    // If not approved, recursively call the task with feedback
    await translateAndRefine
      .triggerAndWait({
        text: payload.text,
        targetLanguage: payload.targetLanguage,
        previousTranslation: translation.text,
        feedback: evaluation.text,
        rejectionCount: rejectionCount + 1,
      })
      .unwrap();
  },
});
```

## Run a test

On the Test page in the dashboard, select the `translate-and-refine` task and include a payload like the following:

```json theme={"theme":"css-variables"}
{
  "text": "In the twilight of his years, the old clockmaker's hands, once steady as the timepieces he crafted, now trembled like autumn leaves in the wind.",
  "targetLanguage": "French"
}
```

This example payload translates the text into French and should be suitably difficult to require a few iterations, depending on the model used and the prompt criteria you set.

<video />

---

## Verify a news article

Create an AI agent workflow that verifies the facts in a news article

## Overview

This example demonstrates the **orchestrator-workers** pattern, where a central AI agent dynamically breaks down complex tasks and delegates them to specialized worker agents. This pattern is particularly effective when tasks require multiple perspectives or parallel processing streams, with the orchestrator synthesizing the results into a cohesive output.

<img alt="Orchestrator" />

## Example task

Our example task uses multiple LLM calls to extract claims from a news article and analyze them in parallel, combining source verification and historical context to assess their credibility.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` to provide LLM logs
* Uses [`batch.triggerByTaskAndWait`](/triggering#batch-triggerbytaskandwait) to orchestrate parallel processing of claims
* Extracts factual claims from news articles using the `o1-mini` model
* Evaluates claims against recent sources and analyzes historical context in parallel
* Combines results into a structured analysis report

```typescript theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { batch, logger, task } from "@trigger.dev/sdk";
import { CoreMessage, generateText } from "ai";

// Define types for our workers' outputs
interface Claim {
  id: number;
  text: string;
}

interface SourceVerification {
  claimId: number;
  isVerified: boolean;
  confidence: number;
  explanation: string;
}

interface HistoricalAnalysis {
  claimId: number;
  feasibility: number;
  historicalContext: string;
}

// Worker 1: Claim Extractor
export const extractClaims = task({
  id: "extract-claims",
  run: async ({ article }: { article: string }) => {
    try {
      const messages: CoreMessage[] = [
        {
          role: "system",
          content:
            "Extract distinct factual claims from the news article. Format as numbered claims.",
        },
        {
          role: "user",
          content: article,
        },
      ];

      const response = await generateText({
        model: openai("o1-mini"),
        messages,
      });

      const claims = response.text
        .split("\n")
        .filter((line: string) => line.trim())
        .map((claim: string, index: number) => ({
          id: index + 1,
          text: claim.replace(/^\d+\.\s*/, ""),
        }));

      logger.info("Extracted claims", { claimCount: claims.length });
      return claims;
    } catch (error) {
      logger.error("Error in claim extraction", {
        error: error instanceof Error ? error.message : "Unknown error",
      });
      throw error;
    }
  },
});

// Worker 2: Source Verifier
export const verifySource = task({
  id: "verify-source",
  run: async (claim: Claim) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "Verify this claim by considering recent news sources and official statements. Assess reliability.",
        },
        {
          role: "user",
          content: claim.text,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "verify-source",
      },
    });

    return {
      claimId: claim.id,
      isVerified: false,
      confidence: 0.7,
      explanation: response.text,
    };
  },
});

// Worker 3: Historical Context Analyzer
export const analyzeHistory = task({
  id: "analyze-history",
  run: async (claim: Claim) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "Analyze this claim in historical context, considering past announcements and technological feasibility.",
        },
        {
          role: "user",
          content: claim.text,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "analyze-history",
      },
    });

    return {
      claimId: claim.id,
      feasibility: 0.8,
      historicalContext: response.text,
    };
  },
});

// Orchestrator
export const newsFactChecker = task({
  id: "news-fact-checker",
  run: async ({ article }: { article: string }) => {
    // Step 1: Extract claims
    const claimsResult = await batch.triggerByTaskAndWait([
      { task: extractClaims, payload: { article } },
    ]);

    if (!claimsResult.runs[0].ok) {
      logger.error("Failed to extract claims", {
        error: claimsResult.runs[0].error,
        runId: claimsResult.runs[0].id,
      });
      throw new Error(
        `Failed to extract claims: ${claimsResult.runs[0].error}`
      );
    }

    const claims = claimsResult.runs[0].output;

    // Step 2: Process claims in parallel
    const parallelResults = await batch.triggerByTaskAndWait([
      ...claims.map((claim) => ({ task: verifySource, payload: claim })),
      ...claims.map((claim) => ({ task: analyzeHistory, payload: claim })),
    ]);

    // Split and process results
    const verifications = parallelResults.runs
      .filter(
        (run): run is typeof run & { ok: true } =>
          run.ok && run.taskIdentifier === "verify-source"
      )
      .map((run) => run.output as SourceVerification);

    const historicalAnalyses = parallelResults.runs
      .filter(
        (run): run is typeof run & { ok: true } =>
          run.ok && run.taskIdentifier === "analyze-history"
      )
      .map((run) => run.output as HistoricalAnalysis);

    return { claims, verifications, historicalAnalyses };
  },
});
```

## Run a test

On the Test page in the dashboard, select the `news-fact-checker` task and include a payload like the following:

```json theme={"theme":"css-variables"}
{
  "article": "Tesla announced a new breakthrough in battery technology today. The company claims their new batteries will have 50% more capacity and cost 30% less to produce. Elon Musk stated this development will enable electric vehicles to achieve price parity with gasoline cars by 2024. The new batteries are scheduled to enter production next quarter at the Texas Gigafactory."
}
```

This example payload verifies the claims in the news article and provides a report on the results.

<video />

---
