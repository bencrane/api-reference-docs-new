> Sources:
> - https://trigger.dev/docs/guides/introduction
> - https://trigger.dev/docs/guides/frameworks/nextjs
> - https://trigger.dev/docs/guides/frameworks/nextjs-webhooks
> - https://trigger.dev/docs/guides/frameworks/nodejs
> - https://trigger.dev/docs/guides/frameworks/remix
> - https://trigger.dev/docs/guides/frameworks/remix-webhooks
> - https://trigger.dev/docs/guides/frameworks/bun
> - https://trigger.dev/docs/guides/frameworks/prisma
> - https://trigger.dev/docs/guides/frameworks/drizzle
> - https://trigger.dev/docs/guides/frameworks/sequin
> - https://trigger.dev/docs/guides/frameworks/supabase-guides-overview
> - https://trigger.dev/docs/guides/frameworks/supabase-edge-functions-basic
> - https://trigger.dev/docs/guides/frameworks/supabase-edge-functions-database-webhooks
> - https://trigger.dev/docs/guides/frameworks/supabase-authentication
> - https://trigger.dev/docs/guides/frameworks/webhooks-guides-overview

# Framework Guides

## Frameworks, guides and examples

A growing list of guides and examples to get the most out of Trigger.dev.

## Frameworks

<CardGroup>
  <Card title="Bun" href="/guides/frameworks/bun" />

  <Card title="Next.js" href="/guides/frameworks/nextjs" />

  <Card title="Node.js" href="/guides/frameworks/nodejs" />

  <Card title="Remix" href="/guides/frameworks/remix" />

  <Card title="SvelteKit" href="/guides/community/sveltekit" />
</CardGroup>

## Guides

Get set up fast using our detailed walk-through guides.

| Guide                                                                                      | Description                                                            |
| :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [AI Agent: Content moderation](/guides/ai-agents/respond-and-check-content)                | Parallel check content while responding to customers                   |
| [AI Agent: Generate and translate copy](/guides/ai-agents/generate-translate-copy)         | Chain prompts to generate and translate content                        |
| [AI Agent: News verification](/guides/ai-agents/verify-news-article)                       | Orchestrate fact checking of news articles                             |
| [AI Agent: Route questions](/guides/ai-agents/route-question)                              | Route questions to different models based on complexity                |
| [AI Agent: Translation refinement](/guides/ai-agents/translate-and-refine)                 | Evaluate and refine translations with feedback                         |
| [Claude Agent SDK](/guides/ai-agents/claude-code-trigger)                                  | Build AI agents that read files, run commands, and edit code           |
| [Cursor rules](/guides/cursor-rules)                                                       | Use Cursor rules to help write Trigger.dev tasks                       |
| [Prisma](/guides/frameworks/prisma)                                                        | How to setup Prisma with Trigger.dev                                   |
| [Python image processing](/guides/python/python-image-processing)                          | Use Python and Pillow to process images                                |
| [Python document to markdown](/guides/python/python-doc-to-markdown)                       | Use Python and MarkItDown to convert documents to markdown             |
| [Python PDF form extractor](/guides/python/python-pdf-form-extractor)                      | Use Python, PyMuPDF and Trigger.dev to extract data from a PDF form    |
| [Python web crawler](/guides/python/python-crawl4ai)                                       | Use Python, Crawl4AI and Playwright to create a headless web crawler   |
| [Sequin database triggers](/guides/frameworks/sequin)                                      | Trigger tasks from database changes using Sequin                       |
| [Stripe webhooks](/guides/examples/stripe-webhook)                                         | Trigger tasks from incoming Stripe webhook events                      |
| [Hookdeck webhooks](/guides/examples/hookdeck-webhook)                                     | Use Hookdeck to receive webhooks and forward them to Trigger.dev tasks |
| [Supabase database webhooks](/guides/frameworks/supabase-edge-functions-database-webhooks) | Trigger tasks using Supabase database webhooks                         |
| [Supabase edge function hello world](/guides/frameworks/supabase-edge-functions-basic)     | Trigger tasks from Supabase edge function                              |
| [Using webhooks in Next.js](/guides/frameworks/nextjs-webhooks)                            | Trigger tasks from a webhook in Next.js                                |
| [Using webhooks in Remix](/guides/frameworks/remix-webhooks)                               | Trigger tasks from a webhook in Remix                                  |

## Featured use cases

<CardGroup>
  <Card title="Data processing & ETL workflows" icon="database" href="/guides/use-cases/data-processing-etl">
    Build complex data pipelines that process large datasets without timeouts.
  </Card>

  <Card title="Media processing workflows" icon="film" href="/guides/use-cases/media-processing">
    Batch process videos, images, audio, and documents with no execution time limits.
  </Card>

  <Card title="AI media generation workflows" icon="wand-magic-sparkles" href="/guides/use-cases/media-generation">
    Generate images, videos, audio, documents and other media using AI models.
  </Card>

  <Card title="Marketing workflows" icon="bullhorn" href="/guides/use-cases/marketing">
    Build drip campaigns, create marketing content, and orchestrate multi-channel campaigns.
  </Card>
</CardGroup>

## Example projects

Example projects are full projects with example repos you can fork and use. These are a great way of learning how to use Trigger.dev in your projects.

| Example project                                                                                                 | Description                                                                                                                            | Framework | GitHub                                                                                                         |
| :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| [Anchor Browser web scraper](/guides/example-projects/anchor-browser-web-scraper)                               | Monitor a website and find the cheapest tickets for a show.                                                                            | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper)                |
| [Batch LLM Evaluator](/guides/example-projects/batch-llm-evaluator)                                             | Evaluate multiple LLM models and stream the results to the frontend.                                                                   | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/batch-llm-evaluator)                       |
| [Claude changelog generator](/guides/example-projects/claude-changelog-generator)                               | Automatically generate professional changelogs from git commits using Claude.                                                          | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/changelog-generator)                       |
| [Claude GitHub wiki agent](/guides/example-projects/claude-github-wiki)                                         | Generate and maintain GitHub wiki documentation with Claude-powered analysis.                                                          | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/claude-agent-github-wiki)                  |
| [Claude thinking chatbot](/guides/example-projects/claude-thinking-chatbot)                                     | Use Vercel's AI SDK and Anthropic's Claude 3.7 model to create a thinking chatbot.                                                     | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/claude-thinking-chatbot)                   |
| [Cursor background agent](/guides/example-projects/cursor-background-agent)                                     | Run Cursor's headless CLI agent as a background task, streaming live output to the browser.                                            | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/cursor-cli-demo)                           |
| [Human-in-the-loop workflow](/guides/example-projects/human-in-the-loop-workflow)                               | Create audio summaries of newspaper articles using a human-in-the-loop workflow built with ReactFlow and Trigger.dev waitpoint tokens. | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/article-summary-workflow)                  |
| [Mastra agents with memory](/guides/example-projects/mastra-agents-with-memory)                                 | Use Mastra to create a weather agent that can collect live weather data and generate clothing recommendations.                         | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/mastra-agents)                             |
| [OpenAI Agents SDK for Python guardrails](/guides/example-projects/openai-agent-sdk-guardrails)                 | Use the OpenAI Agents SDK for Python to create a guardrails system for your AI agents.                                                 | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/openai-agent-sdk-guardrails-examples)      |
| [OpenAI Agents SDK for TypeScript playground](/guides/example-projects/openai-agents-sdk-typescript-playground) | A playground containing 7 AI agents using the OpenAI Agents SDK for TypeScript with Trigger.dev.                                       | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/openai-agents-sdk-with-trigger-playground) |
| [Product image generator](/guides/example-projects/product-image-generator)                                     | Transform basic product photos into professional marketing shots using Replicate's image generation models.                            | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/product-image-generator)                   |
| [Python web crawler](/guides/python/python-crawl4ai)                                                            | Use Python, Crawl4AI and Playwright to create a headless web crawler with Trigger.dev.                                                 | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/python-crawl4ai)                           |
| [Realtime CSV Importer](/guides/example-projects/realtime-csv-importer)                                         | Upload a CSV file and see the progress of the task streamed to the frontend.                                                           | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/realtime-csv-importer)                     |
| [Realtime Fal.ai image generation](/guides/example-projects/realtime-fal-ai)                                    | Generate an image from a prompt using Fal.ai and show the progress of the task on the frontend using Realtime.                         | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation)          |
| [Smart Spreadsheet](/guides/example-projects/smart-spreadsheet)                                                 | Enrich company data using Exa search and Claude with real-time streaming results.                                                      | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/smart-spreadsheet)                         |
| [Turborepo monorepo with Prisma](/guides/example-projects/turborepo-monorepo-prisma)                            | Use Prisma in a Turborepo monorepo with Trigger.dev.                                                                                   | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package)  |
| [Vercel AI SDK image generator](/guides/example-projects/vercel-ai-sdk-image-generator)                         | Use the Vercel AI SDK to generate images from a prompt.                                                                                | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator)             |
| [Vercel AI SDK deep research agent](/guides/example-projects/vercel-ai-sdk-deep-research)                       | Use the Vercel AI SDK to generate comprehensive PDF reports using a deep research agent.                                               | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-deep-research-agent)         |

## Example tasks

Task code you can copy and paste to use in your project. They can all be extended and customized to fit your needs.

| Example task                                                                  | Description                                                                                                                                          |
| :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DALL·E 3 image generation](/guides/examples/dall-e3-generate-image)          | Use OpenAI's GPT-4o and DALL·E 3 to generate an image and text.                                                                                      |
| [Deepgram audio transcription](/guides/examples/deepgram-transcribe-audio)    | Transcribe audio using Deepgram's speech recognition API.                                                                                            |
| [Fal.ai image to cartoon](/guides/examples/fal-ai-image-to-cartoon)           | Convert an image to a cartoon using Fal.ai, and upload the result to Cloudflare R2.                                                                  |
| [Fal.ai with Realtime](/guides/examples/fal-ai-realtime)                      | Generate an image from a prompt using Fal.ai and show the progress of the task on the frontend using Realtime.                                       |
| [FFmpeg video processing](/guides/examples/ffmpeg-video-processing)           | Use FFmpeg to process a video in various ways and save it to Cloudflare R2.                                                                          |
| [Firecrawl URL crawl](/guides/examples/firecrawl-url-crawl)                   | Learn how to use Firecrawl to crawl a URL and return LLM-ready markdown.                                                                             |
| [LibreOffice PDF conversion](/guides/examples/libreoffice-pdf-conversion)     | Convert a document to PDF using LibreOffice.                                                                                                         |
| [Lightpanda](/guides/examples/lightpanda)                                     | Use Lightpanda browser (or cloud version) to get a webpage's content.                                                                                |
| [OpenAI with retrying](/guides/examples/open-ai-with-retrying)                | Create a reusable OpenAI task with custom retry options.                                                                                             |
| [PDF to image](/guides/examples/pdf-to-image)                                 | Use `MuPDF` to turn a PDF into images and save them to Cloudflare R2.                                                                                |
| [Puppeteer](/guides/examples/puppeteer)                                       | Use Puppeteer to generate a PDF or scrape a webpage.                                                                                                 |
| [React email](/guides/examples/react-email)                                   | Send an email using React Email.                                                                                                                     |
| [React to PDF](/guides/examples/react-pdf)                                    | Use `react-pdf` to generate a PDF and save it to Cloudflare R2.                                                                                      |
| [Resend email sequence](/guides/examples/resend-email-sequence)               | Send a sequence of emails over several days using Resend with Trigger.dev.                                                                           |
| [Replicate image generation](/guides/examples/replicate-image-generation)     | Learn how to generate images from source image URLs using Replicate and Trigger.dev.                                                                 |
| [Satori](/guides/examples/satori)                                             | Generate OG images using React Satori.                                                                                                               |
| [Scrape Hacker News](/guides/examples/scrape-hacker-news)                     | Scrape Hacker News using BrowserBase and Puppeteer, summarize the articles with ChatGPT and send an email of the summary every weekday using Resend. |
| [Sentry error tracking](/guides/examples/sentry-error-tracking)               | Automatically send errors to Sentry from your tasks.                                                                                                 |
| [Sharp image processing](/guides/examples/sharp-image-processing)             | Use Sharp to process an image and save it to Cloudflare R2.                                                                                          |
| [Supabase database operations](/guides/examples/supabase-database-operations) | Run basic CRUD operations on a table in a Supabase database using Trigger.dev.                                                                       |
| [Supabase Storage upload](/guides/examples/supabase-storage-upload)           | Download a video from a URL and upload it to Supabase Storage using S3.                                                                              |
| [Vercel AI SDK](/guides/examples/vercel-ai-sdk)                               | Use Vercel AI SDK to generate text using OpenAI.                                                                                                     |
| [Vercel sync environment variables](/guides/examples/vercel-sync-env-vars)    | Automatically sync environment variables from your Vercel projects to Trigger.dev.                                                                   |

<Note>
  If you would like to see a guide for your framework, or an example task for your use case, please
  request it in our [Discord server](https://trigger.dev/discord) and we'll add it to the list.
</Note>

---

## Next.js setup guide

This guide will show you how to setup Trigger.dev in your existing Next.js project, test an example task, and view the run.

<Note>This guide can be followed for both App and Pages router as well as Server Actions.</Note>

## Prerequisites

* Setup a project in&#x20;
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Initial setup

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

<Tip>
  Instead of running your Next.js app and Trigger.dev dev server in separate terminals, you can run them concurrently. First, add these scripts to your `package.json`:

  ```json theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  {
    "scripts": {
      "trigger:dev": "npx trigger.dev@latest dev",
      "dev": "npx concurrently --kill-others --names \"next,trigger\" --prefix-colors \"yellow,blue\" \"next dev\" \"npm run trigger:dev\""
    }
  }
  ```

  Then, in your terminal, you can start both servers with a single command:

  ```bash theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  npm run dev
  ```

  This will run both your Next.js app and Trigger.dev dev server in the same terminal window, with color-coded output to distinguish between them.
</Tip>

## Set your secret key locally

Set your `TRIGGER_SECRET_KEY` environment variable in your `.env.local` file if using the Next.js App router or `.env` file if using Pages router. This key is used to authenticate with Trigger.dev, so you can trigger runs from your Next.js app. Visit the API Keys page in the dashboard and select the DEV secret key.

<img alt="How to find your secret key" />

For more information on authenticating with Trigger.dev, see the [API keys page](/apikeys).

## Triggering your task in Next.js

Here are the steps to trigger your task in the Next.js App and Pages router and Server Actions.

<Tabs>
  <Tab title="App Router">
    <Steps>
      <Step title="Create a Route Handler">
        Add a Route Handler by creating a `route.ts` file (or `route.js` file) in the `app/api` directory like this: `app/api/hello-world/route.ts`.
      </Step>

      <Step title="Add your task">
        Add this code to your `route.ts` file which imports your task along with `NextResponse` to handle the API route response:

        ```ts app/api/hello-world/route.ts theme={"theme":"css-variables"}
        // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
        import type { helloWorldTask } from "@/trigger/example";
        import { tasks } from "@trigger.dev/sdk";
        import { NextResponse } from "next/server";

        //tasks.trigger also works with the edge runtime
        //export const runtime = "edge";

        export async function GET() {
          const handle = await tasks.trigger<typeof helloWorldTask>(
            "hello-world",
            "James"
          );

          return NextResponse.json(handle);
        }
        ```
      </Step>

      <Step title="Trigger your task">
        Run your Next.js app:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          npm run dev
          ```

          ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          pnpm run dev
          ```

          ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          yarn dev
          ```
        </CodeGroup>

        Run the dev server from Step 2. of the [Initial Setup](/guides/frameworks/nextjs#initial-setup) section above if it's not already running:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          npx trigger.dev@latest dev
          ```

          ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          pnpm dlx trigger.dev@latest dev
          ```

          ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          yarn dlx trigger.dev@latest dev
          ```
        </CodeGroup>

        Now visit the URL in your browser to trigger the task. Ensure the port number is the same as the one you're running your Next.js app on. For example, if you're running your Next.js app on port 3000, visit:

        ```bash theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
        http://localhost:3000/api/hello-world
        ```

        You should see the CLI log the task run with a link to view the logs in the dashboard.

        <img alt="Trigger.dev CLI showing a successful run" />

        Visit the [Trigger.dev dashboard](https://cloud.trigger.dev) to see your run.
      </Step>
    </Steps>
  </Tab>

  <Tab title="App Router (Server Actions)">
    <Steps>
      <Step title="Create an `actions.ts` file">
        Create an `actions.ts` file in the `app/api` directory and add this code which imports your `helloWorldTask()` task. Make sure to include `"use server";` at the top of the file.

        ```ts app/api/actions.ts theme={"theme":"css-variables"}
          "use server";

          import type { helloWorldTask } from "@/trigger/example";
          import { tasks } from "@trigger.dev/sdk";

          export async function myTask() {
            try {
              const handle = await tasks.trigger<typeof helloWorldTask>(
                "hello-world",
                "James"
              );

              return { handle };
            } catch (error) {
              console.error(error);
              return {
                error: "something went wrong",
              };
            }
          }
        ```
      </Step>

      <Step title="Create a button to trigger your task">
        For the purposes of this guide, we'll create a button with an `onClick` event that triggers your task. We'll add this to the `page.tsx` file so we can trigger the task by clicking the button. Make sure to import your task and include `"use client";` at the top of your file.

        ```ts app/page.tsx theme={"theme":"css-variables"}
        "use client";

        import { myTask } from "./actions";

        export default function Home() {
          return (
            <main className="flex min-h-screen flex-col items-center justify-center p-24">
              <button
                onClick={async () => {
                  await myTask();
                }}
              >
                Trigger my task
              </button>
            </main>
          );
        }
        ```
      </Step>

      <Step title="Trigger your task">
        Run your Next.js app:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"}
          npm run dev
          ```

          ```bash pnpm theme={"theme":"css-variables"}
          pnpm run dev
          ```

          ```bash yarn theme={"theme":"css-variables"}
          yarn dev
          ```
        </CodeGroup>

        Open your app in a browser, making sure the port number is the same as the one you're running your Next.js app on. For example, if you're running your Next.js app on port 3000, visit:

        ```bash theme={"theme":"css-variables"}
        http://localhost:3000
        ```

        Run the dev server from Step 2. of the [Initial Setup](/guides/frameworks/nextjs#initial-setup) section above if it's not already running:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"}
          npx trigger.dev@latest dev
          ```

          ```bash pnpm theme={"theme":"css-variables"}
          pnpm dlx trigger.dev@latest dev
          ```

          ```bash yarn theme={"theme":"css-variables"}
          yarn dlx trigger.dev@latest dev
          ```
        </CodeGroup>

        Then click the button we created in your app to trigger the task. You should see the CLI log the task run with a link to view the logs.

        <img alt="Trigger.dev CLI showing a successful run" />

        Visit the [Trigger.dev dashboard](https://cloud.trigger.dev) to see your run.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Pages Router">
    <Steps>
      <Step title="Create an API route">
        Create an API route in the `pages/api` directory. Then create a `hello-world .ts` (or `hello-world.js`) file for your task and copy this code example:

        ```ts pages/api/hello-world.ts theme={"theme":"css-variables"}
        // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
        import { helloWorldTask } from "@/trigger/example";
        import { tasks } from "@trigger.dev/sdk";
        import type { NextApiRequest, NextApiResponse } from "next";

        export default async function handler(
          req: NextApiRequest,
          res: NextApiResponse<{ id: string }>
        ) {
          const handle = await tasks.trigger<typeof helloWorldTask>(
          "hello-world",
          "James"
          );

          res.status(200).json(handle);
        }
        ```
      </Step>

      <Step title="Trigger your task">
        Run your Next.js app:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          npm run dev
          ```

          ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          pnpm run dev
          ```

          ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          yarn dev
          ```
        </CodeGroup>

        Run the dev server from Step 2. of the [Initial Setup](/guides/frameworks/nextjs#initial-setup) section above if it's not already running:

        <CodeGroup>
          ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          npx trigger.dev@latest dev
          ```

          ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          pnpm dlx trigger.dev@latest dev
          ```

          ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
          yarn dlx trigger.dev@latest dev
          ```
        </CodeGroup>

        Now visit the URL in your browser to trigger the task. Ensure the port number is the same as the one you're running your Next.js app on. For example, if you're running your Next.js app on port 3000, visit:

        ```bash theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
        http://localhost:3000/api/hello-world
        ```

        You should see the CLI log the task run with a link to view the logs in the dashboard.

        <img alt="Trigger.dev CLI showing a successful run" />

        Visit the [Trigger.dev dashboard](https://cloud.trigger.dev) to see your run.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Automatically sync environment variables from your Vercel project (optional)

If you want to automatically sync environment variables from your Vercel project to Trigger.dev, you can add our `syncVercelEnvVars` build extension to your `trigger.config.ts` file.

<Note>
  You need to set the `VERCEL_ACCESS_TOKEN` and `VERCEL_PROJECT_ID` environment variables, or pass
  in the token and project ID as arguments to the `syncVercelEnvVars` build extension. If you're
  working with a team project, you'll also need to set `VERCEL_TEAM_ID`, which can be found in your
  team settings. You can find / generate the `VERCEL_ACCESS_TOKEN` in your Vercel
  [dashboard](https://vercel.com/account/settings/tokens). Make sure the scope of the token covers
  the project with the environment variables you want to sync.
</Note>

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncVercelEnvVars } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [syncVercelEnvVars()],
  },
});
```

<Note>
  For more information, see our [Vercel sync environment
  variables](/guides/examples/vercel-sync-env-vars) guide.
</Note>

## Manually add your environment variables (optional)

If you have any environment variables in your tasks, be sure to add them in the dashboard so deployed code runs successfully. In Node.js, these environment variables are accessed in your code using `process.env.MY_ENV_VAR`.

In the sidebar select the "Environment Variables" page, then press the "New environment variable"
button. <img alt="Environment variables page" />

You can add values for your local dev environment, staging and prod. <img alt="Environment variables
page" />

You can also add environment variables in code by following the steps on the [Environment Variables page](/deploy-environment-variables#in-your-code).

## Deploying your task to Trigger.dev

For this guide, we'll manually deploy your task by running the [CLI deploy command](/cli-deploy) below. Other ways to deploy are listed in the next section.

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

### Other ways to deploy

<Tabs>
  <Tab title="GitHub Actions">
    Use GitHub Actions to automatically deploy your tasks whenever new code is pushed and when the `trigger` directory has changes in it. Follow [this guide](/github-actions) to set up GitHub Actions.
  </Tab>

  <Tab title="Vercel Integration">
    We're working on adding an official [Vercel integration](/vercel-integration) which you can follow the progress of [here](https://feedback.trigger.dev/p/vercel-integration-3).
  </Tab>
</Tabs>

## Troubleshooting & extra resources

### Revalidation from your Trigger.dev tasks

[Revalidation](https://vercel.com/docs/incremental-static-regeneration/quickstart#on-demand-revalidation) allows you to purge the cache for an ISR route. To revalidate an ISR route from a Trigger.dev task, you have to set up a handler for the `revalidate` event. This is an API route that you can add to your Next.js app.

This handler will run the `revalidatePath` function from Next.js, which purges the cache for the given path.

The handlers are slightly different for the App and Pages router:

#### Revalidation handler: App Router

If you are using the App router, create a new revalidation route at `app/api/revalidate/path/route.ts`:

```ts app/api/revalidate/path/route.ts theme={"theme":"css-variables"}
import { NextRequest, NextResponse } from "next/server";
import { revalidatePath } from "next/cache";

export async function POST(request: NextRequest) {
  try {
    const { path, type, secret } = await request.json();
    // Create a REVALIDATION_SECRET and set it in your environment variables
    if (secret !== process.env.REVALIDATION_SECRET) {
      return NextResponse.json({ message: "Invalid secret" }, { status: 401 });
    }

    if (!path) {
      return NextResponse.json({ message: "Path is required" }, { status: 400 });
    }

    revalidatePath(path, type);

    return NextResponse.json({ revalidated: true });
  } catch (err) {
    console.error("Error revalidating path:", err);
    return NextResponse.json({ message: "Error revalidating path" }, { status: 500 });
  }
}
```

#### Revalidation handler: Pages Router

If you are using the Pages router, create a new revalidation route at `pages/api/revalidate/path.ts`:

```ts pages/api/revalidate/path.ts theme={"theme":"css-variables"}
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    if (req.method !== "POST") {
      return res.status(405).json({ message: "Method not allowed" });
    }

    const { path, secret } = req.body;

    if (secret !== process.env.REVALIDATION_SECRET) {
      return res.status(401).json({ message: "Invalid secret" });
    }

    if (!path) {
      return res.status(400).json({ message: "Path is required" });
    }

    await res.revalidate(path);

    return res.json({ revalidated: true });
  } catch (err) {
    console.error("Error revalidating path:", err);
    return res.status(500).json({ message: "Error revalidating path" });
  }
}
```

#### Revalidation task

This task takes a `path` as a payload and will revalidate the path you specify, using the handler you set up previously.

<Note>
  To run this task locally you will need to set the `REVALIDATION_SECRET` environment variable in your `.env.local` file (or `.env` file if using Pages router).

  To run this task in production, you will need to set the `REVALIDATION_SECRET` environment variable in Vercel, in your project settings, and also in your environment variables in the Trigger.dev dashboard.
</Note>

```ts trigger/revalidate-path.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";

const NEXTJS_APP_URL = process.env.NEXTJS_APP_URL; // e.g. "http://localhost:3000" or "https://my-nextjs-app.vercel.app"
const REVALIDATION_SECRET = process.env.REVALIDATION_SECRET; // Create a REVALIDATION_SECRET and set it in your environment variables

export const revalidatePath = task({
  id: "revalidate-path",
  run: async (payload: { path: string }) => {
    const { path } = payload;

    try {
      const response = await fetch(`${NEXTJS_APP_URL}/api/revalidate/path`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          path: `${NEXTJS_APP_URL}/${path}`,
          secret: REVALIDATION_SECRET,
        }),
      });

      if (response.ok) {
        logger.log("Path revalidation successful", { path });
        return { success: true };
      } else {
        logger.error("Path revalidation failed", {
          path,
          statusCode: response.status,
          statusText: response.statusText,
        });
        return {
          success: false,
          error: `Revalidation failed with status ${response.status}: ${response.statusText}`,
        };
      }
    } catch (error) {
      logger.error("Path revalidation encountered an error", {
        path,
        error: error instanceof Error ? error.message : String(error),
      });
      return {
        success: false,
        error: `Failed to revalidate path due to an unexpected error`,
      };
    }
  },
});
```

#### Testing the revalidation task

You can test your revalidation task in the Trigger.dev dashboard on the testing page, using the following payload.

```json theme={"theme":"css-variables"}
{
  "path": "<path-to-revalidate>" // e.g. "blog"
}
```

### Next.js build failing due to missing API key in GitHub CI

This issue occurs during the Next.js app build process on GitHub CI where the Trigger.dev SDK is expecting the TRIGGER\_SECRET\_KEY environment variable to be set at build time. Next.js attempts to compile routes and creates static pages, which can cause issues with SDKs that require runtime environment variables. The solution is to mark the relevant pages as dynamic to prevent Next.js from trying to make them static. You can do this by adding the following line to the route file:

```ts theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
export const dynamic = "force-dynamic";
```

### Correctly passing event handlers to React components

An issue can sometimes arise when you try to pass a function directly to the `onClick` prop. This is because the function may require specific arguments or context that are not available when the event occurs. By wrapping the function call in an arrow function, you ensure that the handler is called with the correct context and any necessary arguments. For example:

This works:

```tsx theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
<Button onClick={() => myTask()}>Trigger my task</Button>
```

Whereas this does not work:

```tsx theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
<Button onClick={myTask}>Trigger my task</Button>
```

## Realtime updates with React hooks

The `@trigger.dev/react-hooks` package lets you subscribe to task runs from your React components. Show progress bars, stream AI responses, or display run status in real time.

<CardGroup>
  <Card title="React hooks" icon="react" href="/realtime/react-hooks/overview">
    Hooks for subscribing to runs, streaming data, and triggering tasks from the frontend.
  </Card>

  <Card title="Streams" icon="wave-pulse" href="/tasks/streams">
    Pipe continuous data (like AI completions) from your tasks to the client while they run.
  </Card>
</CardGroup>

## Learn more about Next.js and Trigger.dev

### Walk-through guides from development to deployment

<CardGroup>
  <Card title="Next.js - setup guide" icon="N" href="/guides/frameworks/nextjs">
    Learn how to setup Trigger.dev with Next.js, using either the pages or app router.
  </Card>

  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/guides/frameworks/nextjs-webhooks">
    Learn how to create a webhook handler for incoming webhooks in a Next.js app, and trigger a task from it.
  </Card>
</CardGroup>

### Task examples

<CardGroup>
  <Card title="Fal.ai with Realtime in Next.js" href="/guides/examples/fal-ai-realtime">
    Generate an image from a prompt using Fal.ai and Trigger.dev Realtime.
  </Card>

  <Card title="Generate a cartoon using Fal.ai in Next.js" href="/guides/examples/fal-ai-image-to-cartoon">
    Convert an image to a cartoon using Fal.ai.
  </Card>

  <Card title="Vercel sync environment variables" icon="code" href="/guides/examples/vercel-sync-env-vars">
    Learn how to automatically sync environment variables from your Vercel projects to Trigger.dev.
  </Card>

  <Card title="Vercel AI SDK" icon="code" href="/guides/examples/vercel-ai-sdk">
    Learn how to use the Vercel AI SDK, which is a simple way to use AI models from different
    providers, including OpenAI, Anthropic, Amazon Bedrock, Groq, Perplexity etc.
  </Card>
</CardGroup>

## Useful next steps

<CardGroup>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>

---

## Triggering tasks with webhooks in Next.js

Learn how to trigger a task from a webhook in a Next.js app.

## Prerequisites

* [A Next.js project, set up with Trigger.dev](/guides/frameworks/nextjs)
* [cURL](https://curl.se/) installed on your local machine. This will be used to send a POST request to your webhook handler.

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/nextjs-webhooks/my-app">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Adding the webhook handler

The webhook handler in this guide will be an API route.

This will be different depending on whether you are using the Next.js pages router or the app router.

### Pages router: creating the webhook handler

Create a new file `pages/api/webhook-handler.ts` or `pages/api/webhook-hander.js`.

In your new file, add the following code:

```ts /pages/api/webhook-handler.ts theme={"theme":"css-variables"}
import { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  // Parse the webhook payload
  const payload = req.body;

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  res.status(200).json({ message: "OK" });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

### App router: creating the webhook handler

Create a new file in the `app/api/webhook-handler/route.ts` or `app/api/webhook-handler/route.js`.

In your new file, add the following code:

```ts /app/api/webhook-handler/route.ts theme={"theme":"css-variables"}
import type { helloWorldTask } from "@/trigger/example";
import { tasks } from "@trigger.dev/sdk";
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  // Parse the webhook payload
  const payload = await req.json();

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  return NextResponse.json("OK", { status: 200 });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

## Triggering the task locally

Now that you have your webhook handler set up, you can trigger the 'Hello World' task from it. We will do this locally using cURL.

<Steps>
  <Step title="Run your Next.js app and the Trigger.dev dev server">
    First, run your Next.js app.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npm run dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm run dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dev
      ```
    </CodeGroup>

    Then, open up a second terminal window and start the Trigger.dev dev server:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Trigger the webhook with some dummy data">
    To send a POST request to your webhook handler, open up a terminal window on your local machine and run the following command:

    <Tip>
      If `http://localhost:3000` isn't the URL of your locally running Next.js app, replace the URL in
      the below command with that URL instead.
    </Tip>

    ```bash theme={"theme":"css-variables"}
    curl -X POST -H "Content-Type: application/json" -d '{"Name": "John Doe", "Age": "87"}' http://localhost:3000/api/webhook-handler
    ```

    This will send a POST request to your webhook handler, with a JSON payload.
  </Step>

  <Step title="Check the task ran successfully">
    After running the command, you should see a successful dev run and a 200 response in your terminals.

    If you now go to your [Trigger.dev dashboard](https://cloud.trigger.dev), you should also see a successful run for the 'Hello World' task, with the payload you sent, in this case; `{"name": "John Doe", "age": "87"}`.
  </Step>
</Steps>

## Learn more about Next.js and Trigger.dev

### Walk-through guides from development to deployment

<CardGroup>
  <Card title="Next.js - setup guide" icon="N" href="/guides/frameworks/nextjs">
    Learn how to setup Trigger.dev with Next.js, using either the pages or app router.
  </Card>

  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/guides/frameworks/nextjs-webhooks">
    Learn how to create a webhook handler for incoming webhooks in a Next.js app, and trigger a task from it.
  </Card>
</CardGroup>

### Task examples

<CardGroup>
  <Card title="Fal.ai with Realtime in Next.js" href="/guides/examples/fal-ai-realtime">
    Generate an image from a prompt using Fal.ai and Trigger.dev Realtime.
  </Card>

  <Card title="Generate a cartoon using Fal.ai in Next.js" href="/guides/examples/fal-ai-image-to-cartoon">
    Convert an image to a cartoon using Fal.ai.
  </Card>

  <Card title="Vercel sync environment variables" icon="code" href="/guides/examples/vercel-sync-env-vars">
    Learn how to automatically sync environment variables from your Vercel projects to Trigger.dev.
  </Card>

  <Card title="Vercel AI SDK" icon="code" href="/guides/examples/vercel-ai-sdk">
    Learn how to use the Vercel AI SDK, which is a simple way to use AI models from different
    providers, including OpenAI, Anthropic, Amazon Bedrock, Groq, Perplexity etc.
  </Card>
</CardGroup>

---

## Node.js setup guide

This guide will show you how to setup Trigger.dev in your existing Node.js project, test an example task, and view the run.

## Prerequisites

* Setup a project in&#x20;
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Initial setup

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Useful next steps

<CardGroup>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>

---

## Remix setup guide

This guide will show you how to setup Trigger.dev in your existing Remix project, test an example task, and view the run.

## Prerequisites

* Setup a project in&#x20;
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Initial setup

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Set your secret key locally

Set your `TRIGGER_SECRET_KEY` environment variable in your `.env` file. This key is used to authenticate with Trigger.dev, so you can trigger runs from your Remix app. Visit the API Keys page in the dashboard and select the DEV secret key.

<img alt="How to find your secret key" />

For more information on authenticating with Trigger.dev, see the [API keys page](/apikeys).

## Triggering your task in Remix

<Steps>
  <Step title="Create an API route">
    Create a new file called `api.hello-world.ts` (or `api.hello-world.js`) in the `app/routes` directory like this: `app/routes/api.hello-world.ts`.
  </Step>

  <Step title="Add your task">
    Add this code to your `api.hello-world.ts` file which imports your task:

    ```ts app/routes/api.hello-world.ts theme={"theme":"css-variables"}
    import type { helloWorldTask } from "../../src/trigger/example";
    import { tasks } from "@trigger.dev/sdk";

    export async function loader() {
      const handle = await tasks.trigger<typeof helloWorldTask>("hello-world", "James");

      return new Response(JSON.stringify(handle), {
        headers: { "Content-Type": "application/json" },
      });
    }
    ```
  </Step>

  <Step title="Trigger your task">
    Run your Remix app:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npm run dev
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm run dev
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dev
      ```
    </CodeGroup>

    Run the dev server from Step 2. of the [Initial Setup](/guides/frameworks/remix#initial-setup) section above if it's not already running:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>

    Now visit the URL in your browser to trigger the task. Ensure the port number is the same as the one you're running your Remix app on. For example, if you're running your Remix app on port 3000, visit:

    ```bash theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
    http://localhost:3000/api/trigger
    ```

    You should see the CLI log the task run with a link to view the logs in the dashboard.

    <img alt="Trigger.dev CLI showing a successful run" />

    Visit the [Trigger.dev dashboard](https://cloud.trigger.dev) to see your run.
  </Step>
</Steps>

## Manually add your environment variables (optional)

If you have any environment variables in your tasks, be sure to add them in the dashboard so deployed code runs successfully. In Node.js, these environment variables are accessed in your code using `process.env.MY_ENV_VAR`.

In the sidebar select the "Environment Variables" page, then press the "New environment variable"
button. <img alt="Environment variables page" />

You can add values for your local dev environment, staging and prod. <img alt="Environment variables
page" />

You can also add environment variables in code by following the steps on the [Environment Variables page](/deploy-environment-variables#in-your-code).

## Deploying your task to Trigger.dev

For this guide, we'll manually deploy your task by running the [CLI deploy command](/cli-deploy) below. Other ways to deploy are listed in the next section.

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

### Other ways to deploy

<Tabs>
  <Tab title="GitHub Actions">
    Use GitHub Actions to automatically deploy your tasks whenever new code is pushed and when the `trigger` directory has changes in it. Follow [this guide](/github-actions) to set up GitHub Actions.
  </Tab>

  <Tab title="Vercel Integration">
    We're working on adding an official [Vercel integration](/vercel-integration) which you can follow the progress of [here](https://feedback.trigger.dev/p/vercel-integration-3).
  </Tab>
</Tabs>

## Deploying to Vercel Edge Functions

Before we start, it's important to note that:

* We'll be using a type-only import for the task to ensure compatibility with the edge runtime.
* The `@trigger.dev/sdk` package supports the edge runtime out of the box.

There are a few extra steps to follow to deploy your `/api/hello-world` API endpoint to Vercel Edge Functions.

<Steps>
  <Step title="Update your API route">
    Update your API route to use the `runtime: "edge"` option and change it to an `action()` so we can trigger the task from a curl request later on.

    ```ts app/routes/api.hello-world.ts theme={"theme":"css-variables"}
    import { tasks } from "@trigger.dev/sdk";
    import type { helloWorldTask } from "../../src/trigger/example";
    //      👆 **type-only** import

    // include this at the top of your API route file
    export const config = {
      runtime: "edge",
    };
    export async function action({ request }: { request: Request }) {
      // This is where you'd authenticate the request
      const payload = await request.json();
      const handle = await tasks.trigger<typeof helloWorldTask>("hello-world", payload);
      return new Response(JSON.stringify(handle), {
        headers: { "Content-Type": "application/json" },
      });
    }
    ```
  </Step>

  <Step title="Update the Vercel configuration">
    Create or update the `vercel.json` file with the following:

    ```json vercel.json theme={"theme":"css-variables"}
    {
      "buildCommand": "npm run vercel-build",
      "devCommand": "npm run dev",
      "framework": "remix",
      "installCommand": "npm install",
      "outputDirectory": "build/client"
    }
    ```
  </Step>

  <Step title="Update package.json scripts">
    Update your `package.json` to include the following scripts:

    ```json package.json theme={"theme":"css-variables"}
    "scripts": {
        "build": "remix vite:build",
        "dev": "remix vite:dev",
        "lint": "eslint --ignore-path .gitignore --cache --cache-location ./node_modules/.cache/eslint .",
        "start": "remix-serve ./build/server/index.js",
        "typecheck": "tsc",
        "vercel-build": "remix vite:build && cp -r ./public ./build/client"
    },
    ```
  </Step>

  <Step title="Deploy to Vercel">
    Push your code to a Git repository and create a new project in the Vercel dashboard. Select your repository and follow the prompts to complete the deployment.
  </Step>

  <Step title="Add your Vercel environment variables">
    In the Vercel project settings, add your Trigger.dev secret key:

    ```bash theme={"theme":"css-variables"}
    TRIGGER_SECRET_KEY=your-secret-key
    ```

    You can find this key in the Trigger.dev dashboard under API Keys and select the environment key you want to use.

    <img alt="How to find your secret key" />
  </Step>

  <Step title="Deploy your project">
    Once you've added the environment variable, deploy your project to Vercel.

    <Note>
      Ensure you have also deployed your Trigger.dev task. See [deploy your task
      step](/guides/frameworks/remix#deploying-your-task-to-trigger-dev).
    </Note>
  </Step>

  <Step title="Test your task in production">
    After deployment, you can test your task in production by running this curl command:

    ```bash theme={"theme":"css-variables"}
    curl -X POST https://your-app.vercel.app/api/hello-world \
    -H "Content-Type: application/json" \
    -d '{"name": "James"}'
    ```

    This sends a POST request to your API endpoint with a JSON payload.
  </Step>
</Steps>

### Additional notes

The `vercel-build` script in `package.json` is specific to Remix projects on Vercel, ensuring that static assets are correctly copied to the build output.

The `runtime: "edge"` configuration in the API route allows for better performance on Vercel's Edge Network.

## Realtime updates with React hooks

The `@trigger.dev/react-hooks` package lets you subscribe to task runs from your React components. Show progress bars, stream AI responses, or display run status in real time.

<CardGroup>
  <Card title="React hooks" icon="react" href="/realtime/react-hooks/overview">
    Hooks for subscribing to runs, streaming data, and triggering tasks from the frontend.
  </Card>

  <Card title="Streams" icon="wave-pulse" href="/tasks/streams">
    Pipe continuous data (like AI completions) from your tasks to the client while they run.
  </Card>
</CardGroup>

## Additional resources for Remix

<Card title="Remix - triggering tasks using webhooks" icon="R" href="/guides/frameworks/remix-webhooks">
  How to create a webhook handler in a Remix app, and trigger a task from it.
</Card>

## Useful next steps

<CardGroup>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>

---

## Triggering tasks with webhooks in Remix

Learn how to trigger a task from a webhook in a Remix app.

## Prerequisites

* [A Remix project, set up with Trigger.dev](/guides/frameworks/remix)
* [cURL](https://curl.se/) installed on your local machine. This will be used to send a POST request to your webhook handler.

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/remix-webhooks">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Adding the webhook handler

The webhook handler in this guide will be an API route. Create a new file `app/routes/api.webhook-handler.ts` or `app/routes/api.webhook-handler.js`.

In your new file, add the following code:

```ts /api/webhook-handler.ts theme={"theme":"css-variables"}
import type { ActionFunctionArgs } from "@remix-run/node";
import { tasks } from "@trigger.dev/sdk";
import { helloWorldTask } from "src/trigger/example";

export async function action({ request }: ActionFunctionArgs) {
  const payload = await request.json();

  // Trigger the helloWorldTask with the webhook data as the payload
  await tasks.trigger<typeof helloWorldTask>("hello-world", payload);

  return new Response("OK", { status: 200 });
}
```

This code will handle the webhook payload and trigger the 'Hello World' task.

## Triggering the task locally

Now that you have a webhook handler set up, you can trigger the 'Hello World' task from it. We will do this locally using cURL.

<Steps>
  <Step title="Run your Remix app and the Trigger.dev dev server">
    First, run your Remix app.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npm run dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm run dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dev
      ```
    </CodeGroup>

    Then, open up a second terminal window and start the Trigger.dev dev server:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Trigger the webhook with some dummy data">
    To send a POST request to your webhook handler, open up a terminal window on your local machine and run the following command:

    <Tip>
      If `http://localhost:5173` isn't the URL of your locally running Remix app, replace the URL in the
      below command with that URL instead.
    </Tip>

    ```bash theme={"theme":"css-variables"}
    curl -X POST -H "Content-Type: application/json" -d '{"Name": "John Doe", "Age": "87"}' http://localhost:5173/api/webhook-handler
    ```

    This will send a POST request to your webhook handler, with a JSON payload.
  </Step>

  <Step title="Check the task ran successfully">
    After running the command, you should see a successful dev run and a 200 response in your terminals.

    If you now go to your [Trigger.dev dashboard](https://cloud.trigger.dev), you should also see a successful run for the 'Hello World' task, with the payload you sent, in this case; `{"name": "John Doe", "age": "87"}`.
  </Step>
</Steps>

---

## Bun guide

This guide will show you how to setup Trigger.dev in your existing Bun project, test an example task, and view the run.

<Warning>
  The trigger.dev CLI does not yet support Bun. So you will need to run the CLI using Node.js.
  Bun will still be used to execute your tasks, even in the `dev` environment.
</Warning>

<Note>
  **Supported Bun version:** Deployed tasks run on Bun 1.3.3. For local development, use Bun 1.3.x for compatibility.
</Note>

## Prerequisites

* Setup a project in&#x20;
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Known issues

* Certain OpenTelemetry instrumentation will not work with Bun, because Bun does not support Node's `register` hook. This means that some libraries that rely on this hook will not work with Bun.
* If Bun is installed via Homebrew (e.g. `/opt/homebrew/bin/bun`), you may see an `ENOENT: spawn /Users/<you>/.bun/bin/bun` error because the CLI expects Bun at the default install path. **Workaround:** create a symlink:
  ```bash theme={"theme":"css-variables"}
  mkdir -p ~/.bun/bin && ln -s $(which bun) ~/.bun/bin/bun
  ```

## Initial setup

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init --runtime bun
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init --runtime bun
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init --runtime bun
      ```
    </CodeGroup>

    It will do a few things:

    1. Log you into the CLI if you're not already logged in.
    2. Create a `trigger.config.ts` file in the root of your project.
    3. Ask where you'd like to create the `/trigger` directory.
    4. Create the `/src/trigger` directory with an example task, `/src/trigger/example.[ts/js]`.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Update example.ts to use Bun">
    Open the `/src/trigger/example.ts` file and replace the contents with the following:

    ```ts example.ts theme={"theme":"css-variables"}
    import { Database } from "bun:sqlite";
    import { task } from "@trigger.dev/sdk";

    export const bunTask = task({
      id: "bun-task",
      run: async (payload: { query: string }) => {
        const db = new Database(":memory:");
        const query = db.query("select 'Hello world' as message;");
        console.log(query.get()); // => { message: "Hello world" }

        return {
          message: "Query executed",
        };
      },
    });

    ```
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

---

## Prisma setup guide

This guide will show you how to set up Prisma with Trigger.dev

## Overview

This guide will show you how to set up [Prisma](https://www.prisma.io/) with Trigger.dev, test and view an example task run.

## Prerequisites

* An existing Node.js project with a `package.json` file
* Ensure TypeScript is installed
* A [PostgreSQL](https://www.postgresql.org/) database server running locally, or accessible via a connection string
* Prisma ORM [installed and initialized](https://www.prisma.io/docs/getting-started/quickstart) in your project
* A `DATABASE_URL` environment variable set in your `.env` file, pointing to your PostgreSQL database (e.g. `postgresql://user:password@localhost:5432/dbname`)

## Initial setup (optional)

Follow these steps if you don't already have Trigger.dev set up in your project.

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Creating a task using Prisma and deploying it to production

<Steps>
  <Step title="Writing the Prisma task">
    First, create a new task file in your `trigger` folder.

    This is a simple task that will add a new user to the database.

    <Note>
      For this task to work correctly, you will need to have a `user` model in your Prisma schema with
      an `id` field, a `name` field, and an `email` field.
    </Note>

    ```ts /trigger/prisma-add-new-user.ts theme={"theme":"css-variables"}
    import { PrismaClient } from "@prisma/client";
    import { task } from "@trigger.dev/sdk";

    // Initialize Prisma client
    const prisma = new PrismaClient();

    export const addNewUser = task({
      id: "prisma-add-new-user",
      run: async (payload: { name: string; email: string; id: number }) => {
        const { name, email, id } = payload;

        // This will create a new user in the database
        const user = await prisma.user.create({
          data: {
            name: name,
            email: email,
            id: id,
          },
        });

        return {
          message: `New user added successfully: ${user.id}`,
        };
      },
    });
    ```
  </Step>

  <Step title="Configuring the build extension">
    Next, configure the Prisma [build extension](https://trigger.dev/docs/config/extensions/overview) in the `trigger.config.js` file to include the Prisma client in the build.

    This will ensure that the Prisma client is available when the task runs.

    ```js /trigger.config.js theme={"theme":"css-variables"}
    export default defineConfig({
      project: "<project ref>", // Your project reference
      // Your other config settings...
      build: {
        extensions: [
          prismaExtension({
            mode: "legacy", // required
            version: "5.20.0", // optional, we'll automatically detect the version if not provided
            schema: "prisma/schema.prisma", // update this to the path of your Prisma schema file
          }),
        ],
      },
    });
    ```

    The `prismaExtension` requires a `mode` parameter. For standard Prisma setups, use `"legacy"`
    mode. See the [Prisma extension documentation](/config/extensions/prismaExtension) for other modes
    and full configuration options.

    <Note>
      [Build extensions](/config/extensions/overview) allow you to hook into the build system and
      customize the build process or the resulting bundle and container image (in the case of
      deploying). You can use pre-built extensions or create your own.
    </Note>
  </Step>

  <Step title="Optional: adding Prisma instrumentation">
    We use OpenTelemetry to [instrument](https://trigger.dev/docs/config/config-file#instrumentations) our tasks and collect telemetry data.

    If you want to automatically log all Prisma queries and mutations, you can use the Prisma instrumentation extension.

    ```js /trigger.config.js theme={"theme":"css-variables"}
    import { defineConfig } from "@trigger.dev/sdk";
    import { PrismaInstrumentation } from "@prisma/instrumentation";
    import { OpenAIInstrumentation } from "@traceloop/instrumentation-openai";

    export default defineConfig({
      //..other stuff
      instrumentations: [new PrismaInstrumentation(), new OpenAIInstrumentation()],
    });
    ```

    This provides much more detailed information about your tasks with minimal effort.
  </Step>

  <Step title="Deploying your task">
    With the build extension and task configured, you can now deploy your task using the Trigger.dev CLI.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest deploy
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest deploy
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest deploy
      ```
    </CodeGroup>
  </Step>

  <Step title="Adding your DATABASE_URL environment variable to Trigger.dev">
    In your Trigger.dev dashboard sidebar click "Environment Variables" <Icon icon="circle-1" />, and then the "New environment variable" button <Icon icon="circle-2" />.

    You can add values for your local dev environment, staging and prod. in this case we will add the `DATABASE_URL` for the production environment.

    <img
      alt="Environment variables
page"
    />
  </Step>

  <Step title="Running your task">
    To test this task, go to the 'test' page in the Trigger.dev dashboard and run the task with the following payload:

    ```json theme={"theme":"css-variables"}
    {
      "name": "<a-name>", // e.g. "John Doe"
      "email": "<a-email>", // e.g. "john@doe.test"
      "id": <a-number> // e.g. 12345
    }
    ```

    Congratulations! You should now see a new completed run, and a new user with the credentials you provided should be added to your database.
  </Step>
</Steps>

## Useful next steps

<CardGroup>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>

---

## Drizzle setup guide

This guide will show you how to set up Drizzle ORM with Trigger.dev

## Overview

This guide will show you how to set up [Drizzle ORM](https://orm.drizzle.team/) with Trigger.dev, test and view an example task run.

## Prerequisites

* An existing Node.js project with a `package.json` file
* Ensure TypeScript is installed
* A [PostgreSQL](https://www.postgresql.org/) database server running locally, or accessible via a connection string
* Drizzle ORM [installed and initialized](https://orm.drizzle.team/docs/get-started) in your project
* A `DATABASE_URL` environment variable set in your `.env` file, pointing to your PostgreSQL database (e.g. `postgresql://user:password@localhost:5432/dbname`)

## Initial setup (optional)

Follow these steps if you don't already have Trigger.dev set up in your project.

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Creating a task using Drizzle and deploying it to production

<Steps>
  <Step title="The task using Drizzle">
    First, create a new task file in your `trigger` folder.

    This is a simple task that will add a new user to your database, we will call it `drizzle-add-new-user`.

    <Note>
      For this task to work correctly, you will need to have a `users` table schema defined with Drizzle
      that includes `name`, `age` and `email` fields.
    </Note>

    ```ts /trigger/drizzle-add-new-user.ts theme={"theme":"css-variables"}
    import { eq } from "drizzle-orm";
    import { task } from "@trigger.dev/sdk";
    import { users } from "src/db/schema";
    import { drizzle } from "drizzle-orm/node-postgres";

    // Initialize Drizzle client
    const db = drizzle(process.env.DATABASE_URL!);

    export const addNewUser = task({
      id: "drizzle-add-new-user",
      run: async (payload: typeof users.$inferInsert) => {
        // Create new user
        const [user] = await db.insert(users).values(payload).returning();

        return {
          createdUser: user,
          message: "User created and updated successfully",
        };
      },
    });
    ```
  </Step>

  <Step title="Configuring the build">
    Next, in your `trigger.config.js` file, add `pg` to the `externals` array. `pg` is a non-blocking PostgreSQL client for Node.js.

    It is marked as an external to ensure that it is not bundled into the task's bundle, and instead will be installed and loaded from `node_modules` at runtime.

    ```js /trigger.config.js theme={"theme":"css-variables"}
    import { defineConfig } from "@trigger.dev/sdk";

    export default defineConfig({
      project: "<project ref>", // Your project reference
      // Your other config settings...
      build: {
        externals: ["pg"],
      },
    });
    ```
  </Step>

  <Step title="Deploying your task">
    Once the build configuration is added, you can now deploy your task using the Trigger.dev CLI.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest deploy
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest deploy
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest deploy
      ```
    </CodeGroup>
  </Step>

  <Step title="Adding your DATABASE_URL environment variable to Trigger.dev">
    In your Trigger.dev dashboard sidebar click "Environment Variables" <Icon icon="circle-1" />, and then the "New environment variable" button <Icon icon="circle-2" />.

    <img alt="Environment variables page" />

    You can add values for your local dev environment, staging and prod. in this case we will add the `DATABASE_URL` for the production environment.

    <img
      alt="Environment variables
page"
    />
  </Step>

  <Step title="Running your task">
    To test this task, go to the 'test' page in the Trigger.dev dashboard and run the task with the following payload:

    ```json theme={"theme":"css-variables"}
    {
      "name": "<a-name>", // e.g. "John Doe"
      "age": "<an-age>", // e.g. 25
      "email": "<an-email>" // e.g. "john@doe.test"
    }
    ```

    Congratulations! You should now see a new completed run, and a new user with the credentials you provided should be added to your database.
  </Step>
</Steps>

## Useful next steps

<CardGroup>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>

---

## Sequin database triggers

This guide will show you how to trigger tasks from database changes using Sequin

[Sequin](https://sequinstream.com) allows you to trigger tasks from database changes. Sequin captures every insert, update, and delete on a table and then ensures a task is triggered for each change.

Often, task runs coincide with database changes. For instance, you might want to use a Trigger.dev task to generate an embedding for each post in your database:

<img alt="Sequin and Trigger.dev Overview" />

In this guide, you'll learn how to use Sequin to trigger Trigger.dev tasks from database changes.

## Prerequisites

You are about to create a [regular Trigger.dev task](/tasks-regular) that you will execute when ever a post is inserted or updated in your database. Sequin will detect all the changes on the `posts` table and then send the payload of the post to an API endpoint that will call `tasks.trigger()` to create the embedding and update the database.

As long as you create an HTTP endpoint that Sequin can deliver webhooks to, you can use any web framework or edge function (e.g. Supabase Edge Functions, Vercel Functions, Cloudflare Workers, etc.) to invoke your Trigger.dev task. In this guide, we'll show you how to setup Trigger.dev tasks using Next.js API Routes.

You'll need the following to follow this guide:

* A Next.js project with [Trigger.dev](https://trigger.dev) installed
  <Info>
    If you don't have one already, follow [Trigger.dev's Next.js setup
    guide](/guides/frameworks/nextjs) to setup your project. You can return to this guide when
    you're ready to write your first Trigger.dev task.
  </Info>
* A [Sequin](https://console.sequinstream.com/register) account
* A Postgres database (Sequin works with any Postgres database version 12 and up) with a `posts` table.

## Create a Trigger.dev task

Start by creating a new Trigger.dev task that takes in a Sequin change event as a payload, creates an embedding, and then inserts the embedding into the database:

<Steps>
  <Step title="Create a `create-embedding-for-post` task">
    In your `src/trigger/tasks` directory, create a new file called `create-embedding-for-post.ts` and add the following code:

    <CodeGroup>
      ```ts trigger/create-embedding-for-post.ts theme={"theme":"css-variables"}
      import { task } from "@trigger.dev/sdk";
      import { OpenAI } from "openai";
      import { upsertEmbedding } from "../util";

      const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
      });

      export const createEmbeddingForPost = task({
        id: "create-embedding-for-post",
        run: async (payload: {
          record: {
            id: number;
            title: string;
            body: string;
            author: string;
            createdAt: string;
            embedding: string | null;
          },
          metadata: {
            table_schema: string,
            table_name: string,
            consumer: {
              id: string;
              name: string;
            };
          };
        }) => {
          // Create an embedding using the title and body of payload.record
          const content = `${payload.record.title}\n\n${payload.record.body}`;
          const embedding = (await openai.embeddings.create({
            model: "text-embedding-ada-002",
            input: content,
          })).data[0].embedding;

          // Upsert the embedding in the database. See utils.ts for the implementation -> ->
          await upsertEmbedding(embedding, payload.record.id);

          // Return the updated record
          return {
            ...payload.record,
            embedding: JSON.stringify(embedding),
          };
        }
      });
      ```

      ```ts utils.ts theme={"theme":"css-variables"}
      import pg from "pg";

      export async function upsertEmbedding(embedding: number[], id: number) {
        const client = new pg.Client({
          connectionString: process.env.DATABASE_URL,
        });
        await client.connect();

        try {
          const query = `
            INSERT INTO post_embeddings (id, embedding)
            VALUES ($2, $1)
            ON CONFLICT (id)
            DO UPDATE SET embedding = $1
          `;
          const values = [JSON.stringify(embedding), id];

          const result = await client.query(query, values);
          console.log(`Updated record in database. Rows affected: ${result.rowCount}`);

          return result.rowCount;
        } catch (error) {
          console.error("Error updating record in database:", error);
          throw error;
        } finally {
          await client.end();
        }
      }
      ```
    </CodeGroup>

    This task takes in a Sequin record event, creates an embedding, and then upserts the embedding into a `post_embeddings` table.
  </Step>

  <Step title="Add the task to your Trigger.dev project">
    Register the `create-embedding-for-post` task to your Trigger.dev cloud project by running the following command:

    ```bash theme={"theme":"css-variables"}
    npx trigger.dev@latest dev
    ```

    In the Trigger.dev dashboard, you should now see the `create-embedding-for-post` task:

    <Frame>
      <img alt="Task added" />
    </Frame>
  </Step>
</Steps>

<Check>
  You've successfully created a Trigger.dev task that will create an embedding for each post in your
  database. In the next step, you'll create an API endpoint that Sequin can deliver records to.
</Check>

## Setup API route

You'll now create an API endpoint that will receive posts from Sequin and then trigger the `create-embedding-for-post` task.

<Info>
  This guide covers how to setup an API endpoint using the Next.js App Router. You can find examples
  for Next.js Server Actions and Pages Router in the [Trigger.dev
  documentation](https://trigger.dev/docs/guides/frameworks/nextjs).
</Info>

<Steps>
  <Step title="Create a route handler">
    Add a route handler by creating a new `route.ts` file in a `/app/api/create-embedding-for-post` directory:

    ```ts app/api/create-embedding-for-post/route.ts theme={"theme":"css-variables"}
    import type { createEmbeddingForPost } from "@/trigger/create-embedding-for-post";
    import { tasks } from "@trigger.dev/sdk";
    import { NextResponse } from "next/server";

    export async function POST(req: Request) {
      const authHeader = req.headers.get("authorization");
      if (!authHeader || authHeader !== `Bearer ${process.env.SEQUIN_WEBHOOK_SECRET}`) {
        return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
      }
      const payload = await req.json();
      const handle = await tasks.trigger<typeof createEmbeddingForPost>(
        "create-embedding-for-post",
        payload
      );

      return NextResponse.json(handle);
    }
    ```

    This route handler will receive records from Sequin, parse them, and then trigger the `create-embedding-for-post` task.
  </Step>

  <Step title="Set secret keys">
    You'll need to set four secret keys in a `.env.local` file:

    ```bash theme={"theme":"css-variables"}
    SEQUIN_WEBHOOK_SECRET=your-secret-key
    TRIGGER_SECRET_KEY=secret-from-trigger-dev
    OPENAI_API_KEY=sk-proj-asdfasdfasdf
    DATABASE_URL=postgresql://
    ```

    The `SEQUIN_WEBHOOK_SECRET` ensures that only Sequin can access your API endpoint.

    The `TRIGGER_SECRET_KEY` is used to authenticate requests to Trigger.dev and can be found in the **API keys** tab of the Trigger.dev dashboard.

    The `OPENAI_API_KEY` and `DATABASE_URL` are used to create an embedding using OpenAI and connect to your database. Be sure to add these as [environment variables](https://trigger.dev/docs/deploy-environment-variables) in Trigger.dev as well.
  </Step>
</Steps>

<Check>
  You've successfully created an API endpoint that can receive record payloads from Sequin and
  trigger a Trigger.dev task. In the next step, you'll setup Sequin to trigger the endpoint.
</Check>

## Create Sequin consumer

You'll now configure Sequin to send every row in your `posts` table to your Trigger.dev task.

<Steps>
  <Step title="Connect Sequin to your database">
    1. Login to your Sequin account and click the **Add New Database** button.
    2. Enter the connection details for your Postgres database.

    <Info>
      If you need to connect to a local dev database, flip the **use localhost** switch and follow the instructions to create a tunnel using the [Sequin CLI](https://sequinstream.com/docs/cli).
    </Info>

    3. Follow the instructions to create a publication and a replication slot by running two SQL commands in your database:

    ```sql theme={"theme":"css-variables"}
    create publication sequin_pub for all tables;
    select pg_create_logical_replication_slot('sequin_slot', 'pgoutput');
    ```

    4. Name your database and click the **Connect Database** button.

    Sequin will connect to your database and ensure that it's configured properly.

    <Note>
      If you need step-by-step connection instructions to connect Sequin to your database, check out our [quickstart guide](https://sequinstream.com/docs/quickstart).
    </Note>
  </Step>

  <Step title="Tunnel to your local endpoint">
    Now, create a tunnel to your local endpoint so Sequin can deliver change payloads to your local API:

    1. In the Sequin console, open the **HTTP Endpoint** tab and click the **Create HTTP Endpoint** button.
    2. Enter a name for your endpoint (i.e. `local_endpoint`) and flip the **Use localhost** switch. Follow the instructions in the Sequin console to [install the Sequin CLI](https://sequinstream.com/docs/cli), then run:

    ```bash theme={"theme":"css-variables"}
    sequin tunnel --ports=3001:local_endpoint
    ```

    3. Now, click **Add encryption header** and set the key to `Authorization` and the value to `Bearer SEQUIN_WEBHOOK_SECRET`.
    4. Click **Create HTTP Endpoint**.
  </Step>

  <Step title="Create a Push Consumer">
    Create a push consumer that will capture posts from your database and deliver them to your local endpoint:

    1. Navigate to the **Consumers** tab and click the **Create Consumer** button.
    2. Select your `posts` table (i.e `public.posts`).
    3. You want to ensure that every post receives an embedding - and that embeddings are updated as posts are updated. To do this, select to process **Rows** and click **Continue**.

    <Note>
      You can also use **changes** for this particular use case, but **rows** comes with some nice replay and backfill features.
    </Note>

    4. You'll now set the sort and filter for the consumer. For this guide, we'll sort by `updated_at` and start at the beginning of the table. We won't apply any filters:

    <Frame>
      <img alt="Consumer Sort and Filter" />
    </Frame>

    5. On the next screen, select **Push** to have Sequin send the events to your webhook URL. Click **Continue**.
    6. Now, give your consumer a name (i.e. `posts_push_consumer`) and in the **HTTP Endpoint** section select the `local_endpoint` you created above. Add the exact API route you created in the previous step (i.e. `/api/create-embedding-for-post`):

    <Frame>
      <img alt="Consumer Endpoint" />
    </Frame>

    7. Click the **Create Consumer** button.
  </Step>
</Steps>

<Check>Your Sequin consumer is now created and ready to send events to your API endpoint.</Check>

## Test end-to-end

<Steps>
  <Step title="Spin up you dev environment">
    1. The Next.js app is running: `npm run dev`
    2. The Trigger.dev dev server is running `npx trigger.dev@latest dev`
    3. The Sequin tunnel is running: `sequin tunnel --ports=3001:local_endpoint`
  </Step>

  <Step title="Create a new post in your database">
    ```sql theme={"theme":"css-variables"}
    insert into
    posts (title, body, author)
    values
      (
        'The Future of AI',
        'An insightful look into how artificial intelligence is shaping the future of technology and society.',
        'Alice H Johnson'
      );
    ```
  </Step>

  <Step title="Trace the change in the Sequin dashboard">
    In the Sequin console, navigate to the [**Trace**](https://console.sequinstream.com/trace) tab and confirm that Sequin delivered the event to your local endpoint:

    <Frame>
      <img alt="Trace Event" />
    </Frame>
  </Step>

  <Step title="Confirm the event was received by your endpoint">
    In your local terminal, you should see a `200` response in your Next.js app:

    ```bash theme={"theme":"css-variables"}
    POST /api/create-embedding-for-post 200 in 262ms
    ```
  </Step>

  <Step title="Observe the task run in the Trigger.dev dashboard">
    Finally, in the [**Trigger.dev dashboard**](https://cloud.trigger.dev/), navigate to the Runs page and confirm that the task run completed successfully:

    <Frame>
      <img alt="Task run" />
    </Frame>
  </Step>
</Steps>

<Check>
  Every time a post is created or updated, Sequin will deliver the row payload to your API endpoint
  and Trigger.dev will run the `create-embedding-for-post` task.
</Check>

## Next steps

With Sequin and Trigger.dev, every post in your database will now have an embedding. This is a simple example of how you can trigger long-running tasks on database changes.

From here, add error handling and deploy to production:

* Add [retries](/errors-retrying) to your Trigger.dev task to ensure that any errors are captured and logged.
* Deploy to [production](/guides/frameworks/nextjs#deploying-your-task-to-trigger-dev) and update your Sequin consumer to point to your production database and endpoint.

---

## Supabase overview

Guides and examples for using Supabase with Trigger.dev.

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>

---

## Triggering tasks from Supabase edge functions

This guide will show you how to trigger a task from a Supabase edge function, and then view the run in our dashboard.

## Overview

Supabase edge functions allow you to trigger tasks either when an event is sent from a third party (e.g. when a new Stripe payment is processed, when a new user signs up to a service, etc), or when there are any changes or updates to your Supabase database.

This guide shows you how to set up and deploy a simple Supabase edge function example that triggers a task when an edge function URL is accessed.

## Prerequisites

* Ensure you have the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) installed
* Since Supabase CLI version 1.123.4, you must have [Docker Desktop installed](https://supabase.com/docs/guides/functions/deploy#deploy-your-edge-functions) to deploy Edge Functions
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/supabase-edge-functions">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Initial setup

<Steps>
  <Step title="Optional step 1: create a new Supabase project">
    <Info> If you already have a Supabase project on your local machine you can skip this step.</Info>

    You can create a new project by running the following command in your terminal using the Supabase CLI:

    ```bash theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
    supabase init
    ```

    <Note>
      If you are using VS Code, ensure to answer 'y' when asked to generate VS Code settings for Deno,
      and install any recommended extensions.
    </Note>
  </Step>

  <Step title="Optional step 2: create a package.json file">
    If your project does not already have `package.json` file (e.g. if you are using Deno), create it manually in your project's root folder.

    <Info> If your project has a `package.json` file you can skip this step.</Info>

    This is required for the Trigger.dev SDK to work correctly.

    ```ts package.json theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
    {
      "devDependencies": {
        "typescript": "^5.6.2"
      }
    }
    ```

    <Note> Update your Typescript version to the latest version available. </Note>
  </Step>

  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"} theme={"theme":"css-variables"} theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" />, view recent payloads <Icon icon="circle-4" />, and create run templates <Icon icon="circle-5" />.

    Press the "Run test" button <Icon icon="circle-6" />.

    <img alt="Test page" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

    <img alt="Run page" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

    <img alt="Terminal showing completed run" />
  </Step>
</Steps>

## Create a new Supabase edge function and deploy it

<Steps>
  <Step title="Create a new Supabase edge function">
    We'll call this example `edge-function-trigger`.

    In your project, run the following command in the terminal using the Supabase CLI:

    ```bash theme={"theme":"css-variables"}
    supabase functions new edge-function-trigger
    ```
  </Step>

  <Step title="Update the edge function code">
    Replace the placeholder code in your `edge-function-trigger/index.ts` file with the following:

    ```ts functions/edge-function-trigger/index.ts theme={"theme":"css-variables"}
    // Setup type definitions for built-in Supabase Runtime APIs
    import "jsr:@supabase/functions-js/edge-runtime.d.ts";
    // Import the Trigger.dev SDK - replace "<your-sdk-version>" with the version of the SDK you are using, e.g. "3.0.0". You can find this in your package.json file.
    import { tasks } from "npm:@trigger.dev/sdk@3.0.0";
    // Import your task type from your /trigger folder
    import type { helloWorldTask } from "../../../src/trigger/example.ts";
    //     👆 **type-only** import

    Deno.serve(async () => {
      await tasks.trigger<typeof helloWorldTask>(
        // Your task id
        "hello-world",
        // Your task payload
        "Hello from a Supabase Edge Function!"
      );
      return new Response("OK");
    });
    ```

    <Note>You can only import the `type` from the task.</Note>

    <Note>
      Tasks in the `trigger` folder use Node, so they must stay in there or they will not run,
      especially if you are using a different runtime like Deno. Also do not add "`npm:`" to imports
      inside your task files, for the same reason.
    </Note>
  </Step>

  <Step title="Deploy your edge function using the Supabase CLI">
    You can now deploy your edge function with the following command in your terminal:

    ```bash theme={"theme":"css-variables"}
    supabase functions deploy edge-function-trigger --no-verify-jwt
    ```

    <Warning>
      `--no-verify-jwt` removes the JSON Web Tokens requirement from the authorization header. By
      default this should be on, but it is not strictly required for this hello world example.
    </Warning>

    <Note>
      To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
      our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
      how to use JWT authentication for user-specific operations or your service role key for
      admin-level access.
    </Note>

    Follow the CLI instructions and once complete you should now see your new edge function deployment in your Supabase edge functions dashboard.

    There will be a link to the dashboard in your terminal output, or you can find it at this URL:

    `https://supabase.com/dashboard/project/<your-project-id>/functions`

    <Note>Replace `your-project-id` with your actual project ID.</Note>
  </Step>
</Steps>

## Set your Trigger.dev prod secret key in the Supabase dashboard

To trigger a task from your edge function, you need to set your Trigger.dev secret key in the Supabase dashboard.

To do this, first go to your Trigger.dev [project dashboard](https://cloud.trigger.dev) and copy the `prod` secret key from the API keys page.

<img alt="How to find your prod secret key" />

Then, in [Supabase](https://supabase.com/dashboard/projects), select your project, navigate to 'Project settings' <Icon icon="circle-1" />, click 'Edge functions' <Icon icon="circle-2" /> in the configurations menu, and then click the 'Add new secret' <Icon icon="circle-3" /> button.

Add `TRIGGER_SECRET_KEY` <Icon icon="circle-4" /> with the pasted value of your Trigger.dev `prod` secret key.

<img alt="Add secret key in Supabase" />

## Deploy your task and trigger it from your edge function

<Steps>
  <Step title="Deploy your 'Hello World' task">
    Next, deploy your `hello-world` task to [Trigger.dev cloud](https://cloud.trigger.dev).

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest deploy
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest deploy
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest deploy
      ```
    </CodeGroup>
  </Step>

  <Step title="Trigger a prod run from your deployed edge function">
    To do this all you need to do is simply open the `edge-function-trigger` URL.

    `https://supabase.com/dashboard/project/<your-project-id>/functions`

    <Note>Replace `your-project-id` with your actual project ID.</Note>

    In your Supabase project, go to your Edge function dashboard, find `edge-function-trigger`, copy the URL, and paste it into a new window in your browser.

    Once loaded you should see ‘OK’ on the new screen.

    <img alt="Edge function URL" />

    The task will be triggered when your edge function URL is accessed.

    Check your [cloud.trigger.dev](http://cloud.trigger.dev) dashboard and you should see a succesful `hello-world` task.

    **Congratulations, you have run a simple Hello World task from a Supabase edge function!**
  </Step>
</Steps>

### If you see a runtime error when calling tasks.trigger()

If you see `TypeError: Cannot read properties of undefined (reading 'toString')` when calling `tasks.trigger()` from your edge function, the SDK is hitting a dependency that expects Node-style APIs not available in the Supabase Edge (Deno) runtime. Use the [Tasks API](/management/tasks/trigger) with `fetch` instead of the SDK—that avoids loading the SDK in Deno:

```ts theme={"theme":"css-variables"}
const response = await fetch(
  `https://api.trigger.dev/api/v1/tasks/your-task-id/trigger`,
  {
    method: "POST",
    headers: {
      Authorization: `Bearer ${Deno.env.get("TRIGGER_SECRET_KEY")}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ payload: { your: "payload" } }),
  }
);
```

See [Trigger task via API](/management/tasks/trigger) for full request/response details and optional fields (e.g. `delay`, `idempotencyKey`).

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>

---

## Triggering tasks from Supabase Database Webhooks

This guide shows you how to trigger a transcribing task when a row is added to a table in a Supabase database, using a Database Webhook and Edge Function.

## Overview

Supabase and Trigger.dev can be used together to create powerful workflows triggered by real-time changes in your database tables:

* A Supabase Database Webhook triggers an Edge Function when a row including a video URL is inserted into a table
* The Edge Function triggers a Trigger.dev task, passing the `video_url` column data from the new table row as the payload
* The Trigger.dev task then:

  * Uses [FFmpeg](https://www.ffmpeg.org/) to extract the audio track from a video URL
  * Uses [Deepgram](https://deepgram.com) to transcribe the extracted audio
  * Updates the original table row using the `record.id` in Supabase with the new transcription using `update`

## Prerequisites

* Ensure you have the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) installed
* Since Supabase CLI version 1.123.4, you must have [Docker Desktop installed](https://supabase.com/docs/guides/functions/deploy#deploy-your-edge-functions) to deploy Edge Functions
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project
* [Create a new Deepgram account](https://deepgram.com/) and get your API key from the dashboard

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/supabase-edge-functions">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Initial setup

<Steps>
  <Step title="Optional step 1: create a new Supabase project">
    <Info> If you already have a Supabase project on your local machine you can skip this step.</Info>

    You can create a new project by running the following command in your terminal using the Supabase CLI:

    ```bash theme={"theme":"css-variables"}
    supabase init
    ```

    <Note>
      If you are using VS Code, ensure to answer 'y' when asked to generate VS Code settings for Deno,
      and install any recommended extensions.
    </Note>
  </Step>

  <Step title="Optional step 2: create a package.json file">
    If your project does not already have `package.json` file (e.g. if you are using Deno), create it manually in your project's root folder.

    <Info> If your project has a `package.json` file you can skip this step.</Info>

    This is required for the Trigger.dev SDK to work correctly.

    ```ts package.json theme={"theme":"css-variables"}
    {
      "devDependencies": {
        "typescript": "^5.6.2"
      }
    }
    ```

    <Note> Update your Typescript version to the latest version available. </Note>
  </Step>

  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    1. Log you into the CLI if you're not already logged in.
    2. Create a `trigger.config.ts` file in the root of your project.
    3. Ask where you'd like to create the `/trigger` directory.
    4. Create the `/trigger` directory with an example task, `/trigger/example.[ts/js]`.

    Choose "None" when prompted to install an example task. We will create a new task for this guide.
  </Step>
</Steps>

## Create a new table in your Supabase database

First, in the Supabase project dashboard, you'll need to create a new table to store the video URL and transcription.

To do this, click on 'Table Editor' <Icon icon="circle-1" /> in the left-hand menu and create a new table. <Icon icon="circle-2" />

<img alt="How to create a new Supabase table" />

Call your table `video_transcriptions`. <Icon icon="circle-1" />

Add two new columns, one called `video_url` with the type `text` <Icon icon="circle-2" />, and another called `transcription`, also with the type `text` <Icon icon="circle-3" />.

<img alt="How to create a new Supabase table 2" />

## Create and deploy the Trigger.dev task

### Generate the Database type definitions

To allow you to use TypeScript to interact with your table, you need to [generate the type definitions](https://supabase.com/docs/guides/api/rest/generating-types) for your Supabase table using the Supabase CLI.

```bash theme={"theme":"css-variables"}
supabase gen types --lang=typescript --project-id <project-ref> --schema public > database.types.ts
```

<Note> Replace `<project-ref>` with your Supabase project reference ID. This can be found in your Supabase project settings under 'General'. </Note>

### Create the transcription task

Create a new task file in your `/trigger` folder. Call it `videoProcessAndUpdate.ts`.

This task takes a video from a public video url, extracts the audio using FFmpeg and transcribes the audio using Deepgram. The transcription summary will then be updated back to the original row in the `video_transcriptions` table in Supabase.

You will need to install some additional dependencies for this task:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npm install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn install @deepgram/sdk @supabase/supabase-js fluent-ffmpeg
  ```
</CodeGroup>

These dependencies will allow you to interact with the Deepgram and Supabase APIs and extract audio from a video using FFmpeg.

<Warning>
  When updating your tables from a Trigger.dev task which has been triggered by a database change,
  be extremely careful to not cause an infinite loop. Ensure you have the correct conditions in
  place to prevent this.
</Warning>

```ts /trigger/videoProcessAndUpdate.ts theme={"theme":"css-variables"}
// Install any missing dependencies below
import { createClient as createDeepgramClient } from "@deepgram/sdk";
import { createClient as createSupabaseClient } from "@supabase/supabase-js";
import { logger, task } from "@trigger.dev/sdk";
import ffmpeg from "fluent-ffmpeg";
import fs from "fs";
import { Readable } from "node:stream";
import os from "os";
import path from "path";
import { Database } from "../../database.types";

// Create a single Supabase client for interacting with your database
// 'Database' supplies the type definitions to supabase-js
const supabase = createSupabaseClient<Database>(
  // These details can be found in your Supabase project settings under `API`
  process.env.SUPABASE_PROJECT_URL as string, // e.g. https://abc123.supabase.co - replace 'abc123' with your project ID
  process.env.SUPABASE_SERVICE_ROLE_KEY as string // Your service role secret key
);

// Your DEEPGRAM_SECRET_KEY can be found in your Deepgram dashboard
const deepgram = createDeepgramClient(process.env.DEEPGRAM_SECRET_KEY);

export const videoProcessAndUpdate = task({
  id: "video-process-and-update",
  run: async (payload: { videoUrl: string; id: number }) => {
    const { videoUrl, id } = payload;

    logger.log(`Processing video at URL: ${videoUrl}`);

    // Generate temporary file names
    const tempDirectory = os.tmpdir();
    const outputPath = path.join(tempDirectory, `audio_${Date.now()}.wav`);

    const response = await fetch(videoUrl);

    // Extract the audio using FFmpeg
    await new Promise((resolve, reject) => {
      if (!response.body) {
        return reject(new Error("Failed to fetch video"));
      }

      ffmpeg(Readable.from(response.body))
        .outputOptions([
          "-vn", // Disable video output
          "-acodec pcm_s16le", // Use PCM 16-bit little-endian encoding
          "-ar 44100", // Set audio sample rate to 44.1 kHz
          "-ac 2", // Set audio channels to stereo
        ])
        .output(outputPath)
        .on("end", resolve)
        .on("error", reject)
        .run();
    });

    logger.log(`Audio extracted from video`, { outputPath });

    // Transcribe the audio using Deepgram
    const { result, error } = await deepgram.listen.prerecorded.transcribeFile(
      fs.readFileSync(outputPath),
      {
        model: "nova-2", // Use the Nova 2 model
        smart_format: true, // Automatically format the transcription
        diarize: true, // Enable speaker diarization
      }
    );

    if (error) {
      throw error;
    }

    const transcription = result.results.channels[0].alternatives[0].paragraphs?.transcript;

    logger.log(`Transcription: ${transcription}`);

    // Delete the temporary audio file
    fs.unlinkSync(outputPath);
    logger.log(`Temporary audio file deleted`, { outputPath });

    const { error: updateError } = await supabase
      .from("video_transcriptions")
      // Update the transcription column
      .update({ transcription: transcription })
      // Find the row by its ID
      .eq("id", id);

    if (updateError) {
      throw new Error(`Failed to update transcription: ${updateError.message}`);
    }

    return {
      message: `Summary of the audio: ${transcription}`,
      result,
    };
  },
});
```

<Warning>
  This task uses your service role secret key to bypass Row Level Security. This is not recommended
  for production use as it has unlimited access and bypasses all security checks.
</Warning>

<Note>
  To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
  our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
  how to use JWT authentication for user-specific operations or your service role key for
  admin-level access.
</Note>

### Adding the FFmpeg build extension

Before you can deploy the task, you'll need to add the FFmpeg build extension to your `trigger.config.ts` file.

```ts trigger.config.ts theme={"theme":"css-variables"}
// Add this import
import { ffmpeg } from "@trigger.dev/build/extensions/core";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>", // Replace with your project ref
  // Your other config settings...
  build: {
    // Add the FFmpeg build extension
    extensions: [ffmpeg()],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

<Note>
  You'll also need to add `@trigger.dev/build` to your `package.json` file under `devDependencies`
  if you don't already have it there.
</Note>

If you are modifying this example and using popular FFmpeg libraries like `fluent-ffmpeg` you'll also need to add them to [`external`](/config/config-file#external) in your `trigger.config.ts` file.

### Add your Deepgram and Supabase environment variables to your Trigger.dev project

You will need to add your `DEEPGRAM_SECRET_KEY`, `SUPABASE_PROJECT_URL` and `SUPABASE_SERVICE_ROLE_KEY` as environment variables in your Trigger.dev project. This can be done in the 'Environment Variables' page in your project dashboard.

<img alt="Adding environment variables" />

### Deploying your task

Now you can now deploy your task using the following command:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

## Create and deploy the Supabase Edge Function

### Add your Trigger.dev prod secret key to the Supabase dashboard

Go to your Trigger.dev [project dashboard](https://cloud.trigger.dev) and copy the `prod` secret key from the API keys page.

<img alt="How to find your prod secret key" />

Then, in [Supabase](https://supabase.com/dashboard/projects), select the project you want to use, navigate to 'Project settings' <Icon icon="circle-1" />, click 'Edge Functions' <Icon icon="circle-2" /> in the configurations menu, and then click the 'Add new secret' <Icon icon="circle-3" /> button.

Add `TRIGGER_SECRET_KEY` <Icon icon="circle-4" /> with the pasted value of your Trigger.dev `prod` secret key.

<img alt="Add secret key in Supabase" />

### Create a new Edge Function using the Supabase CLI

Now create an Edge Function using the Supabase CLI. Call it `video-processing-handler`. This function will be triggered by the Database Webhook.

```bash theme={"theme":"css-variables"}
supabase functions new video-processing-handler
```

```ts functions/video-processing-handler/index.ts theme={"theme":"css-variables"}
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { tasks } from "npm:@trigger.dev/sdk@latest";
// Import the videoProcessAndUpdate task from the trigger folder
import type { videoProcessAndUpdate } from "../../../src/trigger/videoProcessAndUpdate.ts";
//     👆 type only import

// Sets up a Deno server that listens for incoming JSON requests
Deno.serve(async (req) => {
  const payload = await req.json();

  // This payload will contain the video url and id from the new row in the table
  const videoUrl = payload.record.video_url;
  const id = payload.record.id;

  // Trigger the videoProcessAndUpdate task with the videoUrl payload
  await tasks.trigger<typeof videoProcessAndUpdate>("video-process-and-update", { videoUrl, id });
  console.log(payload ?? "No name provided");

  return new Response("ok");
});
```

<Note>
  Tasks in the `trigger` folder use Node, so they must stay in there or they will not run,
  especially if you are using a different runtime like Deno. Also do not add "`npm:`" to imports
  inside your task files, for the same reason.
</Note>

### Deploy the Edge Function

Now deploy your new Edge Function with the following command:

```bash theme={"theme":"css-variables"}
supabase functions deploy video-processing-handler
```

Follow the CLI instructions, selecting the same project you added your `prod` secret key to, and once complete you should see your new Edge Function deployment in your Supabase Edge Functions dashboard.

There will be a link to the dashboard in your terminal output.

## Create the Database Webhook

In your Supabase project dashboard, click 'Project settings' <Icon icon="circle-1" />, then the 'API' tab <Icon icon="circle-2" />, and copy the `anon` `public` API key from the table <Icon icon="circle-3" />.

<img alt="How to find your Supabase API keys" />

Then, go to 'Database' <Icon icon="circle-1" /> click on 'Webhooks' <Icon icon="circle-2" />, and then click 'Create a new hook' <Icon icon="circle-3" />.

<img alt="How to create a new webhook" />

<Icon icon="circle-1" /> Call the hook `edge-function-hook`.

<Icon icon="circle-2" /> Select the new table you have created:
`public` `video_transcriptions`.

<Icon icon="circle-3" /> Choose the `insert` event.

<img alt="How to create a new webhook 2" />

<Icon icon="circle-4" /> Under 'Webhook configuration', select
'Supabase Edge Functions'

<Icon icon="circle-5" /> Under 'Edge Function', choose `POST`
and select the Edge Function you have created: `video-processing-handler`.

<Icon icon="circle-6" /> Under 'HTTP Headers', add a new header with the key `Authorization` and the value `Bearer <your-api-key>` (replace `<your-api-key>` with the `anon` `public` API key you copied earlier).

<Info>
  Supabase Edge Functions require a JSON Web Token [JWT](https://supabase.com/docs/guides/auth/jwts)
  in the authorization header. This is to ensure that only authorized users can access your edge
  functions.
</Info>

<Icon icon="circle-7" /> Click 'Create webhook'.

<img alt="How to create a new webhook 3" />

Your Database Webhook is now ready to use.

## Triggering the entire workflow

Your `video-processing-handler` Edge Function is now set up to trigger the `videoProcessAndUpdate` task every time a new row is inserted into your `video_transcriptions` table.

To do this, go back to your Supabase project dashboard, click on 'Table Editor' <Icon icon="circle-1" /> in the left-hand menu, click on the `video_transcriptions` table <Icon icon="circle-2" /> , and then click 'Insert', 'Insert Row' <Icon icon="circle-3" />.

<img alt="How to insert a new row 1" />

Add a new item under `video_url`, with a public video url. <Icon icon="circle-1" />.

You can use the following public video URL for testing: `https://content.trigger.dev/Supabase%20Edge%20Functions%20Quickstart.mp4`.

<img alt="How to insert a new row 2" />

Once the new table row has been inserted, check your [cloud.trigger.dev](http://cloud.trigger.dev) project 'Runs' list <Icon icon="circle-1" /> and you should see a processing `videoProcessAndUpdate` task <Icon icon="circle-2" /> which has been triggered when you added a new row with the video url to your `video_transcriptions` table.

<img alt="Supabase successful run" />

Once the run has completed successfully, go back to your Supabase `video_transcriptions` table, and you should see that in the row containing the original video URL, the transcription has now been added to the `transcription` column.

<img alt="Supabase successful table update" />

**Congratulations! You have completed the full workflow from Supabase to Trigger.dev and back again.**

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>

---

## Authenticating Supabase tasks: JWTs and service roles

Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role keys for admin access.

There are two ways to authenticate your Supabase client in Trigger.dev tasks:

### 1. Using JWT Authentication (Recommended for User-Specific Operations)

A JWT (JSON Web Token) is a string-formatted data container that typically stores user identity and permissions data. Row Level Security policies are based on the information present in JWTs. Supabase JWT docs can be found [here](https://supabase.com/docs/guides/auth/jwts).

To use JWTs with Supabase, you'll need to add the `SUPABASE_JWT_SECRET` environment variable in your project. This secret is used to sign the JWTs. This can be found in your Supabase project settings under `Data API`.

This example code shows how to create a JWT token for a user and initialize a Supabase client with that token for authentication, allowing the task to perform database operations as that specific user. You can adapt this code to fit your own use case.

```ts theme={"theme":"css-variables"}

// The rest of your task code
async run(payload: { user_id: string }) {
    const { user_id } = payload;

    // Optional error handling
    const jwtSecret = process.env.SUPABASE_JWT_SECRET;
    if (!jwtSecret) {
      throw new Error(
        "SUPABASE_JWT_SECRET is not defined in environment variables"
      );
    }

    // Create a JWT token for the user that expires in 1 hour
    const token = jwt.sign({ sub: user_id }, jwtSecret, { expiresIn: "1h" });

    // Initialize the Supabase client with the JWT token
    const supabase = createClient(
      // These details can be found in your Supabase project settings under `Data API`
      process.env.SUPABASE_URL as string,
      process.env.SUPABASE_ANON_KEY as string,
      {
        global: {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      }
    );
// The rest of your task code
```

Using JWTs to authenticate Supabase operations is more secure than using service role keys because it respects Row Level Security policies, maintains user-specific audit trails, and follows the principle of least privileged access.

### 2. Using Service Role Key (For Admin-Level Access)

<Warning>
  The service role key has unlimited access and bypasses all security checks. Only use it when you
  need admin-level privileges, and never expose it client-side.
</Warning>

This example code creates a Supabase client with admin-level privileges using a service role key, bypassing all Row Level Security policies to allow unrestricted database access.

```ts theme={"theme":"css-variables"}
// Create a single Supabase client for interacting with your database
// 'Database' supplies the type definitions to supabase-js
const supabase = createClient<Database>(
  // These details can be found in your Supabase project settings under `API`
  process.env.SUPABASE_PROJECT_URL as string, // e.g. https://abc123.supabase.co - replace 'abc123' with your project ID
  process.env.SUPABASE_SERVICE_ROLE_KEY as string // Your service role secret key
);

// Your task
```

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>

---

## Using webhooks with Trigger.dev

Guides for using webhooks with Trigger.dev.

## Overview

Webhooks are a way to send and receive events from external services. Triggering tasks using webhooks allow you to add real-time, event driven functionality to your app.

A webhook handler is code that executes in response to an event. They can be endpoints in your framework's routing which can be triggered by an external service.

## Webhook guides

<CardGroup>
  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/guides/frameworks/nextjs-webhooks">
    How to create a webhook handler in a Next.js app, and trigger a task from it.
  </Card>

  <Card title="Remix - triggering tasks using webhooks" icon="R" href="/guides/frameworks/remix-webhooks">
    How to create a webhook handler in a Remix app, and trigger a task from it.
  </Card>

  <Card title="Stripe webhooks" icon="webhook" href="/guides/examples/stripe-webhook">
    How to create a Stripe webhook handler and trigger a task when a 'checkout session completed'
    event is received.
  </Card>

  <Card title="Hookdeck webhooks" icon="webhook" href="/guides/examples/hookdeck-webhook">
    Use Hookdeck to receive webhooks and forward them to Trigger.dev tasks with logging and replay
    capabilities.
  </Card>

  <Card title="Supabase database webhooks guide" icon="webhook" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>
</CardGroup>

---
