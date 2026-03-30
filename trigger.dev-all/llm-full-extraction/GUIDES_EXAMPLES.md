> Sources:
> - https://trigger.dev/docs/guides/examples/dall-e3-generate-image
> - https://trigger.dev/docs/guides/examples/deepgram-transcribe-audio
> - https://trigger.dev/docs/guides/examples/fal-ai-image-to-cartoon
> - https://trigger.dev/docs/guides/examples/fal-ai-realtime
> - https://trigger.dev/docs/guides/examples/ffmpeg-video-processing
> - https://trigger.dev/docs/guides/examples/firecrawl-url-crawl
> - https://trigger.dev/docs/guides/examples/hookdeck-webhook
> - https://trigger.dev/docs/guides/examples/libreoffice-pdf-conversion
> - https://trigger.dev/docs/guides/examples/lightpanda
> - https://trigger.dev/docs/guides/examples/open-ai-with-retrying
> - https://trigger.dev/docs/guides/examples/pdf-to-image
> - https://trigger.dev/docs/guides/examples/puppeteer
> - https://trigger.dev/docs/guides/examples/react-email
> - https://trigger.dev/docs/guides/examples/react-pdf
> - https://trigger.dev/docs/guides/examples/replicate-image-generation
> - https://trigger.dev/docs/guides/examples/resend-email-sequence
> - https://trigger.dev/docs/guides/examples/satori
> - https://trigger.dev/docs/guides/examples/scrape-hacker-news
> - https://trigger.dev/docs/guides/examples/sentry-error-tracking
> - https://trigger.dev/docs/guides/examples/sharp-image-processing
> - https://trigger.dev/docs/guides/examples/stripe-webhook
> - https://trigger.dev/docs/guides/examples/supabase-database-operations
> - https://trigger.dev/docs/guides/examples/supabase-storage-upload
> - https://trigger.dev/docs/guides/examples/vercel-ai-sdk
> - https://trigger.dev/docs/guides/examples/vercel-sync-env-vars

# Code Examples

## Generate an image using DALL·E 3

This example will show you how to generate an image using DALL·E 3 and text using GPT-4o with Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to make reliable calls to AI APIs, specifically OpenAI's GPT-4o and DALL-E 3. It showcases automatic retrying with a maximum of 3 attempts, built-in error handling to avoid timeouts, and the ability to trace and monitor API calls.

## Task code

```ts trigger/generateContent.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

type Payload = {
  theme: string;
  description: string;
};

export const generateContent = task({
  id: "generate-content",
  retry: {
    maxAttempts: 3, // Retry up to 3 times
  },
  run: async ({ theme, description }: Payload) => {
    // Generate text
    const textResult = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: generateTextPrompt(theme, description),
    });

    if (!textResult.choices[0]) {
      throw new Error("No content, retrying…");
    }

    // Generate image
    const imageResult = await openai.images.generate({
      model: "dall-e-3",
      prompt: generateImagePrompt(theme, description),
    });

    if (!imageResult.data[0]) {
      throw new Error("No image, retrying…");
    }

    return {
      text: textResult.choices[0],
      image: imageResult.data[0].url,
    };
  },
});

function generateTextPrompt(theme: string, description: string): any {
  return `Theme: ${theme}\n\nDescription: ${description}`;
}

function generateImagePrompt(theme: string, description: string): any {
  return `Theme: ${theme}\n\nDescription: ${description}`;
}
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "theme": "A beautiful sunset",
  "description": "A sunset over the ocean with a tiny yacht in the distance."
}
```

---

## Transcribe audio using Deepgram

This example will show you how to transcribe audio using Deepgram's speech recognition API with Trigger.dev.

## Overview

Transcribe audio using [Deepgram's](https://developers.deepgram.com/docs/introduction) speech recognition API.

## Key Features

* Transcribe audio from a URL
* Use the Nova 2 model for transcription

## Task code

```ts trigger/deepgramTranscription.ts theme={"theme":"css-variables"}
import { createClient } from "@deepgram/sdk";
import { logger, task } from "@trigger.dev/sdk";

// Initialize the Deepgram client, using your Deepgram API key (you can find this in your Deepgram account settings).
const deepgram = createClient(process.env.DEEPGRAM_SECRET_KEY);

export const deepgramTranscription = task({
  id: "deepgram-transcribe-audio",
  run: async (payload: { audioUrl: string }) => {
    const { audioUrl } = payload;

    logger.log("Transcribing audio from URL", { audioUrl });

    // Transcribe the audio using Deepgram
    const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
      {
        url: audioUrl,
      },
      {
        model: "nova-2", // Use the Nova 2 model for the transcription
        smart_format: true, // Automatically format transcriptions to improve readability
        diarize: true, // Recognize speaker changes and assign a speaker to each word in the transcript
      }
    );

    if (error) {
      logger.error("Failed to transcribe audio", { error });
      throw error;
    }

    console.dir(result, { depth: null });

    // Extract the transcription from the result
    const transcription = result.results.channels[0].alternatives[0].paragraphs?.transcript;

    logger.log(`Generated transcription: ${transcription}`);

    return {
      result,
    };
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "audioUrl": "https://dpgr.am/spacewalk.wav"
}
```

---

## Convert an image to a cartoon using Fal.ai

This example task generates an image from a URL using Fal.ai and uploads it to Cloudflare R2.

## Walkthrough

This video walks through the process of creating this task in a Next.js project.

<iframe title="Trigger.dev walkthrough" />

## Prerequisites

* An existing project
* A [Trigger.dev account](https://cloud.trigger.dev) with Trigger.dev [initialized in your project](/quick-start)
* A [Fal.ai](https://fal.ai/) account
* A [Cloudflare](https://developers.cloudflare.com/r2/) account with an R2 bucket setup

## Task code

This task converts an image to a cartoon using Fal.ai, and uploads the result to Cloudflare R2.

```ts trigger/fal-ai-image-to-cartoon.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import * as fal from "@fal-ai/serverless-client";
import fetch from "node-fetch";
import { z } from "zod";

// Initialize fal.ai client
fal.config({
  credentials: process.env.FAL_KEY, // Get this from your fal.ai dashboard
});

// Initialize S3-compatible client for Cloudflare R2
const s3Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const FalResult = z.object({
  images: z.tuple([z.object({ url: z.string() })]),
});

export const falAiImageToCartoon = task({
  id: "fal-ai-image-to-cartoon",
  run: async (payload: { imageUrl: string; fileName: string }) => {
    logger.log("Converting image to cartoon", payload);

    // Convert image to cartoon using fal.ai
    const result = await fal.subscribe("fal-ai/flux/dev/image-to-image", {
      input: {
        prompt: "Turn the image into a cartoon in the style of a Pixar character",
        image_url: payload.imageUrl,
      },
      onQueueUpdate: (update) => {
        logger.info("Fal.ai processing update", { update });
      },
    });

    const $result = FalResult.parse(result);
    const [{ url: cartoonImageUrl }] = $result.images;

    // Download the cartoon image
    const imageResponse = await fetch(cartoonImageUrl);
    const imageBuffer = await imageResponse.arrayBuffer().then(Buffer.from);

    // Upload to Cloudflare R2
    const r2Key = `cartoons/${payload.fileName}`;
    const uploadParams = {
      Bucket: process.env.R2_BUCKET, // Create a bucket in your Cloudflare dashboard
      Key: r2Key,
      Body: imageBuffer,
      ContentType: "image/png",
    };

    logger.log("Uploading cartoon to R2", { key: r2Key });
    await s3Client.send(new PutObjectCommand(uploadParams));

    logger.log("Cartoon uploaded to R2", { key: r2Key });

    return {
      originalUrl: payload.imageUrl,
      cartoonUrl: `File uploaded to storage at: ${r2Key}`,
    };
  },
});
```

### Testing your task

You can test your task by triggering it from the Trigger.dev dashboard.

```json theme={"theme":"css-variables"}
"imageUrl": "<image-url>", // Replace with the URL of the image you want to convert to a cartoon
"fileName": "<file-name>" // Replace with the name you want to save the file as in Cloudflare R2
```

---

## Generate an image from a prompt using Fal.ai and Trigger.dev Realtime

This example task generates an image from a prompt using Fal.ai and shows the progress of the task on the frontend using Trigger.dev Realtime.

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Walkthrough

This video walks through the process of creating this task in a Next.js project.

<iframe title="Trigger.dev walkthrough" />

## Prerequisites

* An existing project
* A [Trigger.dev account](https://cloud.trigger.dev) with Trigger.dev [initialized in your project](/quick-start)
* A [Fal.ai](https://fal.ai/) account

## Task code

This task generates an image from a prompt using Fal.ai.

```ts trigger/fal-ai-image-from-prompt-realtime.ts theme={"theme":"css-variables"}
import * as fal from "@fal-ai/serverless-client";
import { logger, schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const FalResult = z.object({
  images: z.tuple([z.object({ url: z.string() })]),
});

export const payloadSchema = z.object({
  imageUrl: z.string().url(),
  prompt: z.string(),
});

export const realtimeImageGeneration = schemaTask({
  id: "realtime-image-generation",
  schema: payloadSchema,
  run: async (payload) => {
    const result = await fal.subscribe("fal-ai/flux/dev/image-to-image", {
      input: {
        image_url: payload.imageUrl,
        prompt: payload.prompt,
      },
      onQueueUpdate: (update) => {
        logger.info("Fal.ai processing update", { update });
      },
    });

    const $result = FalResult.parse(result);
    const [{ url: cartoonUrl }] = $result.images;

    return {
      imageUrl: cartoonUrl,
    };
  },
});
```

### Testing your task

You can test your task by triggering it from the Trigger.dev dashboard. Here's an example payload:

```json theme={"theme":"css-variables"}
{
  "imageUrl": "https://static.vecteezy.com/system/resources/previews/005/857/332/non_2x/funny-portrait-of-cute-corgi-dog-outdoors-free-photo.jpg",
  "prompt": "Dress this dog for Christmas"
}
```

---

## Video processing with FFmpeg

These examples show you how to process videos in various ways using FFmpeg with Trigger.dev.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [FFmpeg](https://www.ffmpeg.org/download.html) installed on your machine

### Adding the FFmpeg build extension

To use these example tasks, you'll first need to add our FFmpeg extension to your project configuration like this:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { ffmpeg } from "@trigger.dev/build/extensions/core";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [ffmpeg()],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

You'll also need to add `@trigger.dev/build` to your `package.json` file under `devDependencies` if you don't already have it there.

If you are modifying this example and using popular FFmpeg libraries like `fluent-ffmpeg` you'll also need to add them to [`external`](/config/config-file#external) in your `trigger.config.ts` file.

## Compress a video using FFmpeg

This task demonstrates how to use FFmpeg to compress a video, reducing its file size while maintaining reasonable quality, and upload the compressed video to R2 storage.

### Key Features

* Fetches a video from a given URL
* Compresses the video using FFmpeg with various compression settings
* Uploads the compressed video to R2 storage

### Task code

```ts trigger/ffmpeg-compress-video.ts theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { logger, task } from "@trigger.dev/sdk";
import ffmpeg from "fluent-ffmpeg";
import fs from "fs/promises";
import fetch from "node-fetch";
import { Readable } from "node:stream";
import os from "os";
import path from "path";

// Initialize S3 client
const s3Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const ffmpegCompressVideo = task({
  id: "ffmpeg-compress-video",
  run: async (payload: { videoUrl: string }) => {
    const { videoUrl } = payload;

    // Generate temporary file names
    const tempDirectory = os.tmpdir();
    const outputPath = path.join(tempDirectory, `output_${Date.now()}.mp4`);

    // Fetch the video
    const response = await fetch(videoUrl);

    // Compress the video
    await new Promise((resolve, reject) => {
      if (!response.body) {
        return reject(new Error("Failed to fetch video"));
      }

      ffmpeg(Readable.from(response.body))
        .outputOptions([
          "-c:v libx264", // Use H.264 codec
          "-crf 28", // Higher CRF for more compression (28 is near the upper limit for acceptable quality)
          "-preset veryslow", // Slowest preset for best compression
          "-vf scale=iw/2:ih/2", // Reduce resolution to 320p width (height auto-calculated)
          "-c:a aac", // Use AAC for audio
          "-b:a 64k", // Reduce audio bitrate to 64k
          "-ac 1", // Convert to mono audio
        ])
        .output(outputPath)
        .on("end", resolve)
        .on("error", reject)
        .run();
    });

    // Read the compressed video
    const compressedVideo = await fs.readFile(outputPath);
    const compressedSize = compressedVideo.length;

    // Log compression results
    logger.log(`Compressed video size: ${compressedSize} bytes`);
    logger.log(`Temporary compressed video file created`, { outputPath });

    // Create the r2Key for the extracted audio, using the base name of the output path
    const r2Key = `processed-videos/${path.basename(outputPath)}`;

    const uploadParams = {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
      Body: compressedVideo,
    };

    // Upload the video to R2 and get the URL
    await s3Client.send(new PutObjectCommand(uploadParams));
    logger.log(`Compressed video saved to your r2 bucket`, { r2Key });

    // Delete the temporary compressed video file
    await fs.unlink(outputPath);
    logger.log(`Temporary compressed video file deleted`, { outputPath });

    // Return the compressed video buffer and r2 key
    return {
      Bucket: process.env.R2_BUCKET,
      r2Key,
    };
  },
});
```

### Testing your task

To test this task, use this payload structure:

```json theme={"theme":"css-variables"}
{
  "videoUrl": "<video-url>" // Replace <a-video-url> with the URL of the video you want to upload
}
```

## Extract audio from a video using FFmpeg

This task demonstrates how to use FFmpeg to extract audio from a video, convert it to WAV format, and upload it to R2 storage.

### Key Features

* Fetches a video from a given URL
* Extracts the audio from the video using FFmpeg
* Converts the extracted audio to WAV format
* Uploads the extracted audio to R2 storage

### Task code

```ts trigger/ffmpeg-extract-audio.ts theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { logger, task } from "@trigger.dev/sdk";
import ffmpeg from "fluent-ffmpeg";
import fs from "fs/promises";
import fetch from "node-fetch";
import { Readable } from "node:stream";
import os from "os";
import path from "path";

// Initialize S3 client
const s3Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const ffmpegExtractAudio = task({
  id: "ffmpeg-extract-audio",
  run: async (payload: { videoUrl: string }) => {
    const { videoUrl } = payload;

    // Generate temporary file names
    const tempDirectory = os.tmpdir();
    const outputPath = path.join(tempDirectory, `audio_${Date.now()}.wav`);

    // Fetch the video
    const response = await fetch(videoUrl);

    // Extract the audio
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

    // Read the extracted audio
    const audioBuffer = await fs.readFile(outputPath);
    const audioSize = audioBuffer.length;

    // Log audio extraction results
    logger.log(`Extracted audio size: ${audioSize} bytes`);
    logger.log(`Temporary audio file created`, { outputPath });

    // Create the r2Key for the extracted audio, using the base name of the output path
    const r2Key = `extracted-audio/${path.basename(outputPath)}`;

    const uploadParams = {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
      Body: audioBuffer,
    };

    // Upload the audio to R2 and get the URL
    await s3Client.send(new PutObjectCommand(uploadParams));
    logger.log(`Extracted audio saved to your R2 bucket`, { r2Key });

    // Delete the temporary audio file
    await fs.unlink(outputPath);
    logger.log(`Temporary audio file deleted`, { outputPath });

    // Return the audio file path, size, and R2 URL
    return {
      Bucket: process.env.R2_BUCKET,
      r2Key,
    };
  },
});
```

### Testing your task

To test this task, use this payload structure:

<Warning>
  Make sure to provide a video URL that contains audio. If the video does not have audio, the task
  will fail.
</Warning>

```json theme={"theme":"css-variables"}
{
  "videoUrl": "<video-url>" // Replace <a-video-url> with the URL of the video you want to upload
}
```

## Generate a thumbnail from a video using FFmpeg

This task demonstrates how to use FFmpeg to generate a thumbnail from a video at a specific time and upload the generated thumbnail to R2 storage.

### Key Features

* Fetches a video from a given URL
* Generates a thumbnail from the video at the 5-second mark
* Uploads the generated thumbnail to R2 storage

### Task code

```ts trigger/ffmpeg-generate-thumbnail.ts theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { logger, task } from "@trigger.dev/sdk";
import ffmpeg from "fluent-ffmpeg";
import fs from "fs/promises";
import fetch from "node-fetch";
import { Readable } from "node:stream";
import os from "os";
import path from "path";

// Initialize S3 client
const s3Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const ffmpegGenerateThumbnail = task({
  id: "ffmpeg-generate-thumbnail",
  run: async (payload: { videoUrl: string }) => {
    const { videoUrl } = payload;

    // Generate output file name
    const tempDirectory = os.tmpdir();
    const outputPath = path.join(tempDirectory, `thumbnail_${Date.now()}.jpg`);

    // Fetch the video
    const response = await fetch(videoUrl);

    // Generate the thumbnail
    await new Promise((resolve, reject) => {
      if (!response.body) {
        return reject(new Error("Failed to fetch video"));
      }
      ffmpeg(Readable.from(response.body))
        .screenshots({
          count: 1,
          folder: "/tmp",
          filename: path.basename(outputPath),
          size: "320x240",
          timemarks: ["5"], // 5 seconds
        })
        .on("end", resolve)
        .on("error", reject);
    });

    // Read the generated thumbnail
    const thumbnail = await fs.readFile(outputPath);

    // Create the r2Key for the extracted audio, using the base name of the output path
    const r2Key = `thumbnails/${path.basename(outputPath)}`;

    const uploadParams = {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
      Body: thumbnail,
    };

    // Upload the thumbnail to R2 and get the URL
    await s3Client.send(new PutObjectCommand(uploadParams));
    const r2Url = `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com/${process.env.R2_BUCKET}/${r2Key}`;
    logger.log("Thumbnail uploaded to R2", { url: r2Url });

    // Delete the temporary file
    await fs.unlink(outputPath);

    // Log thumbnail generation results
    logger.log(`Thumbnail uploaded to S3: ${r2Url}`);

    // Return the thumbnail buffer, path, and R2 URL
    return {
      thumbnailBuffer: thumbnail,
      thumbnailPath: outputPath,
      r2Url,
    };
  },
});
```

### Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "videoUrl": "<video-url>" // Replace <a-video-url> with the URL of the video you want to upload
}
```

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

---

## Crawl a URL using Firecrawl

This example demonstrates how to crawl a URL using Firecrawl with Trigger.dev.

## Overview

Firecrawl is a tool for crawling websites and extracting clean markdown that's structured in an LLM-ready format.

Here are two examples of how to use Firecrawl with Trigger.dev:

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* A [Firecrawl](https://firecrawl.dev/) account

## Example 1: crawl an entire website with Firecrawl

This task crawls a website and returns the `crawlResult` object. You can set the `limit` parameter to control the number of URLs that are crawled.

```ts trigger/firecrawl-url-crawl.ts theme={"theme":"css-variables"}
import Firecrawl from "@mendable/firecrawl-js";
import { task } from "@trigger.dev/sdk";

// Initialize the Firecrawl client with your API key
const firecrawlClient = new Firecrawl({
  apiKey: process.env.FIRECRAWL_API_KEY, // Get this from your Firecrawl dashboard
});

export const firecrawlCrawl = task({
  id: "firecrawl-crawl",
  run: async (payload: { url: string }) => {
    const { url } = payload;

    // Crawl: scrapes all the URLs of a web page and return content in LLM-ready format
    const crawlResult = await firecrawlClient.crawl(url, {
      limit: 100, // Limit the number of URLs to crawl
      scrapeOptions: {
        formats: ["markdown", "html"],
      },
    });

    if (crawlResult.status === "failed") {
      throw new Error(`Failed to crawl: ${url}`);
    }

    return {
      data: crawlResult,
    };
  },
});
```

### Testing your task

You can test your task by triggering it from the Trigger.dev dashboard.

```json theme={"theme":"css-variables"}
"url": "<url-to-crawl>" // Replace with the URL you want to crawl
```

## Example 2: scrape a single URL with Firecrawl

This task scrapes a single URL and returns the `scrapeResult` object.

```ts trigger/firecrawl-url-scrape.ts theme={"theme":"css-variables"}
import Firecrawl from "@mendable/firecrawl-js";
import { task } from "@trigger.dev/sdk";

// Initialize the Firecrawl client with your API key
const firecrawlClient = new Firecrawl({
  apiKey: process.env.FIRECRAWL_API_KEY, // Get this from your Firecrawl dashboard
});

export const firecrawlScrape = task({
  id: "firecrawl-scrape",
  run: async (payload: { url: string }) => {
    const { url } = payload;

    // Scrape: scrapes a URL and get its content in LLM-ready format (markdown, structured data via LLM Extract, screenshot, html)
    const scrapeResult = await firecrawlClient.scrape(url, {
      formats: ["markdown", "html"],
    });

    return {
      data: scrapeResult,
    };
  },
});
```

### Testing your task

You can test your task by triggering it from the Trigger.dev dashboard.

```json theme={"theme":"css-variables"}
"url": "<url-to-scrape>" // Replace with the URL you want to scrape
```

---

## Trigger tasks from Hookdeck webhooks

This example demonstrates how to use Hookdeck to receive webhooks and trigger Trigger.dev tasks.

## Overview

This example shows how to use [Hookdeck](https://hookdeck.com) as your webhook infrastructure to trigger Trigger.dev tasks. Hookdeck receives webhooks from external services, and forwards them directly to the Trigger.dev API. This gives you the best of both worlds: Hookdeck's webhook management, logging, and replay capabilities, combined with Trigger.dev's reliable task execution.

## Key features

* Use Hookdeck as your webhook endpoint for external services
* Hookdeck forwards webhooks directly to Trigger.dev tasks via the API
* All webhooks are logged and replayable in Hookdeck

## Setting up Hookdeck

You'll configure everything in the [Hookdeck dashboard](https://dashboard.hookdeck.com). No code changes needed in your app.

### 1. Create a destination

In Hookdeck, create a new [destination](https://hookdeck.com/docs/destinations) with the following settings:

* **URL**: `https://api.trigger.dev/api/v1/tasks/<task-id>/trigger` (replace `<task-id>` with your task ID)
* **Method**: POST
* **Authentication**: Bearer token (use your `TRIGGER_SECRET_KEY` from Trigger.dev)

### 2. Add a transformation

Create a [transformation](https://hookdeck.com/docs/transformations) to wrap the webhook body in the `payload` field that Trigger.dev expects:

```javascript theme={"theme":"css-variables"}
addHandler("transform", (request, context) => {
  request.body = { payload: { ...request.body } };
  return request;
});
```

### 3. Create a connection

Create a [connection](https://hookdeck.com/docs/connections) that links your source (where webhooks come from) to the destination and transformation you created above.

## Task code

This task will be triggered when Hookdeck forwards a webhook to the Trigger.dev API.

```ts trigger/webhook-handler.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const webhookHandler = task({
  id: "webhook-handler",
  run: async (payload: Record<string, unknown>) => {
    // The payload contains the original webhook data from the external service
    console.log("Received webhook:", payload);

    // Add your custom logic here
  },
});
```

## Testing your setup

To test everything is working:

1. Set up your destination, transformation, and connection in [Hookdeck](https://dashboard.hookdeck.com)
2. Send a test webhook to your Hookdeck source URL (use the Hookdeck Console or cURL)
3. Check the Hookdeck dashboard to verify the webhook was received and forwarded
4. Check the [Trigger.dev dashboard](https://cloud.trigger.dev) to see the successful run of your task

For more information on setting up Hookdeck, refer to the [Hookdeck Documentation](https://hookdeck.com/docs).

---

## Convert documents to PDF using LibreOffice

This example demonstrates how to convert documents to PDF using LibreOffice with Trigger.dev.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [LibreOffice](https://www.libreoffice.org/download/libreoffice-fresh/) installed on your machine
* A [Cloudflare R2](https://developers.cloudflare.com) account and bucket

### Using our `aptGet` build extension to add the LibreOffice package

To deploy this task, you'll need to add LibreOffice to your project configuration, like this:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { aptGet } from "@trigger.dev/build/extensions/core";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [
      aptGet({
        packages: ["libreoffice"],
      }),
    ],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

You'll also need to add `@trigger.dev/build` to your `package.json` file under `devDependencies` if you don't already have it there.

## Convert a document to PDF using LibreOffice and upload to R2

This task demonstrates how to use LibreOffice to convert a document (.doc or .docx) to PDF and upload the PDF to an R2 storage bucket.

### Key Features

* Fetches a document from a given URL
* Converts the document to PDF
* Uploads the PDF to R2 storage

### Task code

```ts trigger/libreoffice-pdf-convert.ts theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { task } from "@trigger.dev/sdk";
import libreoffice from "libreoffice-convert";
import { promisify } from "node:util";
import path from "path";
import fs from "fs";

const convert = promisify(libreoffice.convert);

// Initialize S3 client
const s3Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const libreOfficePdfConvert = task({
  id: "libreoffice-pdf-convert",
  run: async (payload: { documentUrl: string }, { ctx }) => {
    // Set LibreOffice path for production environment
    if (ctx.environment.type !== "DEVELOPMENT") {
      process.env.LIBREOFFICE_PATH = "/usr/bin/libreoffice";
    }

    try {
      // Create temporary file paths
      const inputPath = path.join(process.cwd(), `input_${Date.now()}.docx`);
      const outputPath = path.join(process.cwd(), `output_${Date.now()}.pdf`);

      // Download file from URL
      const response = await fetch(payload.documentUrl);
      const buffer = Buffer.from(await response.arrayBuffer());
      fs.writeFileSync(inputPath, buffer);

      const inputFile = fs.readFileSync(inputPath);
      // Convert to PDF using LibreOffice
      const pdfBuffer = await convert(inputFile, ".pdf", undefined);
      fs.writeFileSync(outputPath, pdfBuffer);

      // Upload to R2
      const key = `converted-pdfs/output_${Date.now()}.pdf`;
      await s3Client.send(
        new PutObjectCommand({
          Bucket: process.env.R2_BUCKET,
          Key: key,
          Body: fs.readFileSync(outputPath),
        })
      );

      // Cleanup temporary files
      fs.unlinkSync(inputPath);
      fs.unlinkSync(outputPath);

      return { pdfLocation: key };
    } catch (error) {
      console.error("Error converting PDF:", error);
      throw error;
    }
  },
});
```

### Testing your task

To test this task, use this payload structure:

```json theme={"theme":"css-variables"}
{
  "documentUrl": "<a-document-url>" // Replace <a-document-url> with the URL of the document you want to convert
}
```

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

---

## Lightpanda

These examples demonstrate how to use Lightpanda with Trigger.dev.

## Overview

Lightpanda is a purpose-built browser for AI and automation workflows. It is 10x faster, uses 10x less RAM than Chrome headless.

Here are a few examples of how to use Lightpanda with Trigger.dev.

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

## Limitations

* Lightpanda does not support the `puppeteer` screenshot feature.

## Using Lightpanda Cloud

### Prerequisites

* A [Lightpanda](https://lightpanda.io/) cloud token

### Get links from a website

In this task we use Lightpanda browser to get links from a provided URL. You will have to pass the URL as a payload when triggering the task.

Make sure to add `LIGHTPANDA_TOKEN` to your Trigger.dev dashboard on the Environment Variables page:

```bash theme={"theme":"css-variables"}
LIGHTPANDA_TOKEN="<your-token>"
```

```ts trigger/lightpanda-cloud-puppeteer.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import puppeteer from "puppeteer-core";

export const lightpandaCloudPuppeteer = task({
  id: "lightpanda-cloud-puppeteer",
  machine: {
    preset: "micro",
  },
  run: async (payload: { url: string }, { ctx }) => {
    logger.log("Lets get a page's links with Lightpanda!", { payload, ctx });

    if (!payload.url) {
      logger.warn("Please define the payload url");
      throw new Error("payload.url is undefined");
    }

    const token = process.env.LIGHTPANDA_TOKEN;
    if (!token) {
      logger.warn("Please define the env variable LIGHTPANDA_TOKEN");
      throw new Error("LIGHTPANDA_TOKEN is undefined");
    }

    // Connect to Lightpanda's cloud
    const browser = await puppeteer.connect({
      browserWSEndpoint: `wss://cloud.lightpanda.io/ws?browser=lightpanda&token=${token}`,
    });
    const context = await browser.createBrowserContext();
    const page = await context.newPage();

    // Dump all the links from the page.
    await page.goto(payload.url);

    const links = await page.evaluate(() => {
      return Array.from(document.querySelectorAll("a")).map((row) => {
        return row.getAttribute("href");
      });
    });

    logger.info("Processing done, shutting down…");

    await page.close();
    await context.close();
    await browser.disconnect();

    logger.info("✅ Completed");

    return {
      links,
    };
  },
});
```

### Proxies

Proxies can be used with your browser via the proxy query string parameter. By default, the proxy used is "datacenter" which is a pool of shared datacenter IPs.
`datacenter` accepts an optional `country` query string parameter which is an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.

```bash theme={"theme":"css-variables"}
# This example will use a German IP
wss://cloud.lightpanda.io/ws?proxy=datacenter&country=de&token=${token}
```

### Session

A session is alive until you close it or the connection is closed. The max duration of a session is 15 minutes.

## Using Lightpanda browser directly

### Prerequisites

* Setup the [Lightpanda build extension](/config/extensions/lightpanda)

### Get the HTML of a webpage

This task will dump the HTML of a provided URL using the Lightpanda browser binary. You will have to pass the URL as a payload when triggering the task.

```ts trigger/lightpanda-fetch.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { execSync } from "node:child_process";

export const lightpandaFetch = task({
  id: "lightpanda-fetch",
  machine: {
    preset: "micro",
  },
  run: async (payload: { url: string }, { ctx }) => {
    logger.log("Lets get a page's content with Lightpanda!", { payload, ctx });

    if (!payload.url) {
      logger.warn("Please define the payload url");
      throw new Error("payload.url is undefined");
    }

    const buffer = execSync(`lightpanda fetch --dump ${payload.url}`);

    logger.info("✅ Completed");

    return {
      message: buffer.toString(),
    };
  },
});
```

### Lightpanda CDP with Puppeteer

This task initializes a Lightpanda CDP server and uses it with `puppeteer-core` to scrape a provided URL.

```ts trigger/lightpanda-cdp.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { spawn, type ChildProcessWithoutNullStreams } from "node:child_process";
import puppeteer from "puppeteer-core";

const spawnLightpanda = async (host: string, port: string) =>
  new Promise<ChildProcessWithoutNullStreams>((resolve, reject) => {
    const child = spawn("lightpanda", [
      "serve",
      "--host",
      host,
      "--port",
      port,
      "--log_level",
      "info",
    ]);

    child.on("spawn", async () => {
      logger.info("Running Lightpanda's CDP server…", {
        pid: child.pid,
      });

      await new Promise((resolve) => setTimeout(resolve, 250));
      resolve(child);
    });
    child.on("error", (e) => reject(e));
  });

export const lightpandaCDP = task({
  id: "lightpanda-cdp",
  machine: {
    preset: "micro",
  },
  run: async (payload: { url: string }, { ctx }) => {
    logger.log("Lets get a page's links with Lightpanda!", { payload, ctx });

    if (!payload.url) {
      logger.warn("Please define the payload url");
      throw new Error("payload.url is undefined");
    }

    const host = process.env.LIGHTPANDA_CDP_HOST ?? "127.0.0.1";
    const port = process.env.LIGHTPANDA_CDP_PORT ?? "9222";

    // Launch Lightpanda's CDP server
    const lpProcess = await spawnLightpanda(host, port);

    const browser = await puppeteer.connect({
      browserWSEndpoint: `ws://${host}:${port}`,
    });
    const context = await browser.createBrowserContext();
    const page = await context.newPage();

    // Dump all the links from the page.
    await page.goto(payload.url);

    const links = await page.evaluate(() => {
      return Array.from(document.querySelectorAll("a")).map((row) => {
        return row.getAttribute("href");
      });
    });

    logger.info("Processing done");
    logger.info("Shutting down…");

    // Close Puppeteer instance
    await browser.close();

    // Stop Lightpanda's CDP Server
    lpProcess.kill();

    logger.info("✅ Completed");

    return {
      links,
    };
  },
});
```

---

## Call OpenAI with retrying

This example will show you how to call OpenAI with retrying using Trigger.dev.

## Overview

Sometimes OpenAI calls can take a long time to complete, or they can fail. This task will retry if the API call fails completely or if the response is empty.

## Task code

```ts trigger/openai.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export const openaiTask = task({
  id: "openai-task",
  //specifying retry options overrides the defaults defined in your trigger.config file
  retry: {
    maxAttempts: 10,
    factor: 1.8,
    minTimeoutInMs: 500,
    maxTimeoutInMs: 30_000,
    randomize: false,
  },
  run: async (payload: { prompt: string }) => {
    //if this fails, it will throw an error and retry
    const chatCompletion = await openai.chat.completions.create({
      messages: [{ role: "user", content: payload.prompt }],
      model: "gpt-3.5-turbo",
    });

    if (chatCompletion.choices[0]?.message.content === undefined) {
      //sometimes OpenAI returns an empty response, let's retry by throwing an error
      throw new Error("OpenAI call failed");
    }

    return chatCompletion.choices[0].message.content;
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "prompt": "What is the meaning of life?"
}
```

---

## Turn a PDF into an image using MuPDF

This example will show you how to turn a PDF into an image using MuPDF and Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to turn a PDF into a series of images using MuPDF and upload them to Cloudflare R2.

## Update your build configuration

To use this example, add these build settings below to your `trigger.config.ts` file. They ensure that the `mutool` and `curl` packages are installed when you deploy your task. You can learn more about this and see more build settings [here](/config/extensions/aptGet).

```ts trigger.config.ts theme={"theme":"css-variables"}
export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [aptGet({ packages: ["mupdf-tools", "curl"] })],
  },
});
```

## Task code

```ts trigger/pdfToImage.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { execSync } from "child_process";
import fs from "fs";
import path from "path";

// Initialize S3 client
const s3Client = new S3Client({
  region: "auto",
  endpoint: process.env.S3_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const pdfToImage = task({
  id: "pdf-to-image",
  run: async (payload: { pdfUrl: string; documentId: string }) => {
    logger.log("Converting PDF to images", payload);

    const pdfPath = `/tmp/${payload.documentId}.pdf`;
    const outputDir = `/tmp/${payload.documentId}`;

    // Download PDF and convert to images using MuPDF
    execSync(`curl -s -o ${pdfPath} ${payload.pdfUrl}`);
    fs.mkdirSync(outputDir, { recursive: true });
    execSync(`mutool convert -o ${outputDir}/page-%d.png ${pdfPath}`);

    // Upload images to R2
    const uploadedUrls = [];
    for (const file of fs.readdirSync(outputDir)) {
      const s3Key = `images/${payload.documentId}/${file}`;
      const uploadParams = {
        Bucket: process.env.S3_BUCKET,
        Key: s3Key,
        Body: fs.readFileSync(path.join(outputDir, file)),
        ContentType: "image/png",
      };

      logger.log("Uploading to R2", uploadParams);

      await s3Client.send(new PutObjectCommand(uploadParams));
      const s3Url = `https://${process.env.S3_BUCKET}.r2.cloudflarestorage.com/${s3Key}`;
      uploadedUrls.push(s3Url);
      logger.log("Image uploaded to R2", { url: s3Url });
    }

    // Clean up
    fs.rmSync(outputDir, { recursive: true, force: true });
    fs.unlinkSync(pdfPath);

    logger.log("All images uploaded to R2", { urls: uploadedUrls });

    return {
      imageUrls: uploadedUrls,
    };
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "pdfUrl": "https://pdfobject.com/pdf/sample.pdf",
  "documentId": "unique-document-id"
}
```

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

---

## Puppeteer

These examples demonstrate how to use Puppeteer with Trigger.dev.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Puppeteer](https://pptr.dev/guides/installation) installed on your machine

## Overview

There are 3 example tasks to follow on this page:

1. [Basic example](/guides/examples/puppeteer#basic-example)
2. [Generate a PDF from a web page](/guides/examples/puppeteer#generate-a-pdf-from-a-web-page)
3. [Scrape content from a web page](/guides/examples/puppeteer#scrape-content-from-a-web-page)

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

## Build configuration

To use all examples on this page, you'll first need to add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    // This is required to use the Puppeteer library
    extensions: [puppeteer()],
  },
});
```

Learn more about the [trigger.config.ts](/config/config-file) file including setting default retry settings, customizing the build environment, and more.

## Set an environment variable

Set the following environment variable in your [Trigger.dev dashboard](/deploy-environment-variables) or [using the SDK](/deploy-environment-variables#in-your-code):

```bash theme={"theme":"css-variables"}
PUPPETEER_EXECUTABLE_PATH: "/usr/bin/google-chrome-stable",
```

## Basic example

### Overview

In this example we use [Puppeteer](https://pptr.dev/) to log out the title of a web page, in this case from the [Trigger.dev](https://trigger.dev) landing page.

### Task code

```ts trigger/puppeteer-basic-example.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import puppeteer from "puppeteer";

export const puppeteerTask = task({
  id: "puppeteer-log-title",
  run: async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto("https://trigger.dev");

    const content = await page.title();
    logger.info("Content", { content });

    await browser.close();
  },
});
```

### Testing your task

There's no payload required for this task so you can just click "Run test" from the Test page in the dashboard. Learn more about testing tasks [here](/run-tests).

## Generate a PDF from a web page

### Overview

In this example we use [Puppeteer](https://pptr.dev/) to generate a PDF from the [Trigger.dev](https://trigger.dev) landing page and upload it to [Cloudflare R2](https://developers.cloudflare.com/r2/).

### Task code

```ts trigger/puppeteer-generate-pdf.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import puppeteer from "puppeteer";
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";

// Initialize S3 client
const s3Client = new S3Client({
  region: "auto",
  endpoint: process.env.S3_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const puppeteerWebpageToPDF = task({
  id: "puppeteer-webpage-to-pdf",
  run: async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const response = await page.goto("https://trigger.dev");
    const url = response?.url() ?? "No URL found";

    // Generate PDF from the web page
    const generatePdf = await page.pdf();

    logger.info("PDF generated from URL", { url });

    await browser.close();

    // Upload to R2
    const s3Key = `pdfs/test.pdf`;
    const uploadParams = {
      Bucket: process.env.S3_BUCKET,
      Key: s3Key,
      Body: generatePdf,
      ContentType: "application/pdf",
    };

    logger.log("Uploading to R2 with params", uploadParams);

    // Upload the PDF to R2 and return the URL.
    await s3Client.send(new PutObjectCommand(uploadParams));
    const s3Url = `https://${process.env.S3_BUCKET}.s3.amazonaws.com/${s3Key}`;
    logger.log("PDF uploaded to R2", { url: s3Url });
    return { pdfUrl: s3Url };
  },
});
```

### Testing your task

There's no payload required for this task so you can just click "Run test" from the Test page in the dashboard. Learn more about testing tasks [here](/run-tests).

## Scrape content from a web page

### Overview

In this example we use [Puppeteer](https://pptr.dev/) with a [BrowserBase](https://www.browserbase.com/) proxy to scrape the GitHub stars count from the [Trigger.dev](https://trigger.dev) landing page and log it out. See [this list](/guides/examples/puppeteer#proxying) for more proxying services we recommend.

<Warning>
  When web scraping, you MUST use the technique below which uses a proxy with Puppeteer. Direct
  scraping without using `browserWSEndpoint` is prohibited and will result in account suspension.
  Screenshots are also prohibited when scraping.
</Warning>

### Task code

```ts trigger/scrape-website.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import puppeteer from "puppeteer-core";

export const puppeteerScrapeWithProxy = task({
  id: "puppeteer-scrape-with-proxy",
  run: async () => {
    const browser = await puppeteer.connect({
      browserWSEndpoint: `wss://connect.browserbase.com?apiKey=${process.env.BROWSERBASE_API_KEY}`,
    });

    const page = await browser.newPage();

    try {
      // Navigate to the target website
      await page.goto("https://trigger.dev", { waitUntil: "networkidle0" });

      // Scrape the GitHub stars count
      const starCount = await page.evaluate(() => {
        const starElement = document.querySelector(".github-star-count");
        const text = starElement?.textContent ?? "0";
        const numberText = text.replace(/[^0-9]/g, "");
        return parseInt(numberText);
      });

      logger.info("GitHub star count", { starCount });

      return { starCount };
    } catch (error) {
      logger.error("Error during scraping", {
        error: error instanceof Error ? error.message : String(error),
      });
      throw error;
    } finally {
      await browser.close();
    }
  },
});
```

### Testing your task

There's no payload required for this task so you can just click "Run test" from the Test page in the dashboard. Learn more about testing tasks [here](/run-tests).

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

## Proxying

If you're using Trigger.dev Cloud and Puppeteer or any other tool to scrape content from websites you don't own, you'll need to proxy your requests. **If you don't you'll risk getting our IP address blocked and we will ban you from our service. You must always have permission from the website owner to scrape their content.**

Here are a list of proxy services we recommend:

* [Browserbase](https://www.browserbase.com/)
* [Brightdata](https://brightdata.com/)
* [Browserless](https://browserless.io/)
* [Oxylabs](https://oxylabs.io/)
* [ScrapingBee](https://scrapingbee.com/)
* [Smartproxy](https://smartproxy.com/)

---

## Send emails using React Email

Learn how to send beautiful emails using React Email and Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to send emails using [React Email](https://react.email/).

<Note>
  This example uses [Resend](https://resend.com) as the email provider. You can use other email
  providers like [Loops](https://loops.so) or [SendGrid](https://sendgrid.com) etc. Full list of
  their integrations can be found [here](https://react.email/docs/introduction#integrations).
</Note>

## Task code

<Warning>
  This email is built using React components. To use React components in your task, it must be a
  .tsx file.
</Warning>

```tsx trigger/sendReactEmail.tsx theme={"theme":"css-variables"}
import { Body, Button, Container, Head, Heading, Html, Preview } from "@react-email/components";
import { logger, task } from "@trigger.dev/sdk";
import { Resend } from "resend";

// Initialize Resend client
const resend = new Resend(process.env.RESEND_API_KEY);

// React Email template component
const EmailTemplate = ({ name, message }: { name: string; message: string }) => (
  <Html lang="en">
    <Head />
    <Preview>New message from {name}</Preview>
    <Body style={{ fontFamily: "Arial, sans-serif", margin: "0", padding: "0" }}>
      <Container style={{ padding: "20px", maxWidth: "600px" }}>
        <Heading>Hello from Acme Inc.</Heading>
        <p>Hi {name},</p>
        <p>{message}</p>
        <Button
          href="https://trigger.dev"
          style={{
            backgroundColor: "#0070f3",
            color: "white",
            padding: "12px 20px",
            borderRadius: "8px",
          }}
        >
          Go to Acme Inc.
        </Button>
      </Container>
    </Body>
  </Html>
);

export const sendEmail = task({
  id: "send-react-email",
  run: async (payload: {
    to: string;
    name: string;
    message: string;
    subject: string;
    from?: string;
  }) => {
    try {
      logger.info("Sending email using React.email and Resend", {
        to: payload.to,
      });

      // Send the email using Resend
      const { data, error } = await resend.emails.send({
        // The from address needs to be a verified email address you own
        from: payload.from || "email@acmeinc.com", // Default from address
        to: payload.to,
        subject: payload.subject,
        react: <EmailTemplate name={payload.name} message={payload.message} />,
      });

      if (error) {
        logger.error("Failed to send email", { error });
        throw new Error(`Failed to send email: ${error.message}`);
      }

      logger.info("Email sent successfully", { emailId: data?.id });

      // Return the response from Resend
      return {
        id: data?.id,
        status: "sent",
      };
    } catch (error) {
      logger.error("Unexpected error sending email", { error });
      throw error;
    }
  },
});
```

## The email

This example email should look like this:

<img alt="React Email" />

This is just a simple implementation, you can customize the email to be as complex as you want. Check out the [React email templates](https://react.email/templates) for more inspiration.

## Testing your task

To test this task in the [dashboard](https://cloud.trigger.dev), you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "to": "recipient@example.com",
  "name": "Jane Doe",
  "message": "Thank you for signing up for our service!",
  "subject": "Welcome to Acme Inc."
}
```

## Deploying your task

Deploy the task to production using the Trigger.dev CLI `deploy` command.

## Using Cursor / AI to build your emails

In this video you can see how we use Cursor to build a welcome email.

We recommend using our [Cursor rules](https://trigger.dev/changelog/cursor-rules-writing-tasks/) to help you build your tasks and emails.

#### Video: creating a new email template using Cursor

<video />

#### The generated email template

<img alt="Cursor" />

#### The generated code

```tsx emails/trigger-welcome-email.tsx theme={"theme":"css-variables"}
import {
  Body,
  Button,
  Container,
  Head,
  Heading,
  Hr,
  Html,
  Img,
  Link,
  Preview,
  Section,
  Text,
} from "@react-email/components";

const baseUrl = process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : "";

export interface TriggerWelcomeEmailProps {
  name: string;
}

export const TriggerWelcomeEmail = ({ name }: TriggerWelcomeEmailProps) => (
  <Html>
    <Head />
    <Preview>Welcome to Trigger.dev - Your background jobs platform!</Preview>
    <Body style={main}>
      <Container style={container}>
        <Section style={box}>
          <Img
            src="https://trigger.dev/assets/triggerdev-lockup--light.svg"
            width="150"
            height="40"
            alt="Trigger.dev"
          />
          <Hr style={hr} />
          <Heading>Welcome, {name}!</Heading>
          <Text style={paragraph}>
            Thanks for signing up for Trigger.dev! You're now ready to start creating powerful
            background jobs and workflows.
          </Text>
          <Text style={paragraph}>
            You can monitor your jobs, view runs, and manage your projects right from your
            dashboard.
          </Text>
          <Button style={button} href="https://cloud.trigger.dev/dashboard">
            View your Trigger.dev Dashboard
          </Button>
          <Hr style={hr} />
          <Text style={paragraph}>
            To help you get started, check out our{" "}
            <Link style={anchor} href="https://trigger.dev/docs">
              documentation
            </Link>{" "}
            and{" "}
            <Link style={anchor} href="https://trigger.dev/docs/quickstart">
              quickstart guide
            </Link>
            .
          </Text>
          <Text style={paragraph}>
            You can create your first job using our SDK, set up integrations, and configure triggers
            to automate your workflows. Take a look at our{" "}
            <Link style={anchor} href="https://trigger.dev/docs/examples">
              examples
            </Link>{" "}
            for inspiration.
          </Text>
          <Text style={paragraph}>
            Join our{" "}
            <Link style={anchor} href="https://discord.gg/kA47vcd8Qr">
              Discord community
            </Link>{" "}
            to connect with other developers and get help when you need it.
          </Text>
          <Text style={paragraph}>
            We're here to help you build amazing things. If you have any questions, check out our{" "}
            <Link style={anchor} href="https://trigger.dev/docs">
              documentation
            </Link>{" "}
            or reach out to us on Discord.
          </Text>
          <Text style={paragraph}>— The Trigger.dev team</Text>
          <Hr style={hr} />
          <Text style={footer}>Trigger.dev Inc.</Text>
        </Section>
      </Container>
    </Body>
  </Html>
);

export default TriggerWelcomeEmail;

const main = {
  backgroundColor: "#0E0C15",
  fontFamily:
    '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
};

const container = {
  backgroundColor: "#1D1B27",
  margin: "0 auto",
  padding: "20px 0 48px",
  marginBottom: "64px",
};

const box = {
  padding: "0 48px",
};

const hr = {
  borderColor: "#2D2B3B",
  margin: "20px 0",
};

const paragraph = {
  color: "#E1E1E3",
  fontSize: "16px",
  lineHeight: "24px",
  textAlign: "left" as const,
};

const anchor = {
  color: "#A78BFA",
};

const button = {
  backgroundColor: "#7C3AED",
  borderRadius: "6px",
  color: "#fff",
  fontSize: "16px",
  fontWeight: "bold",
  textDecoration: "none",
  textAlign: "center" as const,
  display: "block",
  width: "100%",
  padding: "12px",
};

const footer = {
  color: "#9CA3AF",
  fontSize: "12px",
  lineHeight: "16px",
};
```

And then to trigger the email, you can use the following task:

```tsx trigger/triggerWelcomeEmail.tsx theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { Resend } from "resend";
import TriggerWelcomeEmail from "emails/trigger-welcome-email";

// Initialize Resend client
const resend = new Resend(process.env.RESEND_API_KEY);

export const sendEmail = task({
  id: "trigger-welcome-email",
  run: async (payload: { to: string; name: string; subject: string; from?: string }) => {
    try {
        to: payload.to,
      });

      const { data, error } = await resend.emails.send({
        // The from address needs to be a verified email address
        from: payload.from || "email@acmeinc.com", // Default from address
        to: payload.to,
        subject: payload.subject,
        react: <TriggerWelcomeEmail name={payload.name} />,
      });

      if (error) {
        logger.error("Failed to send email", { error });
        throw new Error(`Failed to send email: ${error.message}`);
      }

      logger.info("Email sent successfully", { emailId: data?.id });

      return {
        id: data?.id,
        status: "sent",
      };
    } catch (error) {
      logger.error("Unexpected error sending email", { error });
      throw error;
    }
  },
});
```

## Troubleshooting

If you see this error when using `react-email` packages:

```
reactDOMServer.renderToPipeableStream is not a function
```

See our [common problems guide](/troubleshooting#reactdomserver-rendertopipeablestream-is-not-a-function-when-using-react-email) for more information.

## Learn more

### React Email docs

Check out the [React Email docs](https://react.email/docs) and learn how to set up and use React Email, including how to preview your emails locally.

<CardGroup>
  <Card title="Components" icon="puzzle-piece" href="https://react.email/components">
    Pre-built components you can copy and paste into your emails.
  </Card>

  <Card title="Templates" icon="rectangle-list" href="https://react.email/templates">
    Extensive pre-built templates ready to use.
  </Card>
</CardGroup>

---

## Generate a PDF using react-pdf and save it to R2

This example will show you how to generate a PDF using Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to generate a PDF using [react-pdf](https://react-pdf.org/) and save it to Cloudflare R2.

## Task code

<Info> This example must be a .tsx file to use React components.</Info>

```ts trigger/generateResumePDF.tsx theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { renderToBuffer, Document, Page, Text, View } from "@react-pdf/renderer";
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";

// Initialize R2 client
const r2Client = new S3Client({
  // How to authenticate to R2: https://developers.cloudflare.com/r2/api/s3/tokens/
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const generateResumePDF = task({
  id: "generate-resume-pdf",
  run: async (payload: { text: string }) => {
    // Log the payload
    logger.log("Generating PDF resume", payload);

    // Render the ResumeDocument component to a PDF buffer
    const pdfBuffer = await renderToBuffer(
      <Document>
        <Page size="A4">
          <View>
            <Text>{payload.text}</Text>
          </View>
        </Page>
      </Document>
    );

    // Generate a unique filename based on the text and current timestamp
    const filename = `${payload.text.replace(/\s+/g, "-").toLowerCase()}-${Date.now()}.pdf`;

    // Set the R2 key for the PDF file
    const r2Key = `resumes/${filename}`;

    // Set the upload parameters for R2
    const uploadParams = {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
      Body: pdfBuffer,
      ContentType: "application/pdf",
    };

    // Log the upload parameters
    logger.log("Uploading to R2 with params", uploadParams);

    // Upload the PDF to R2
    await r2Client.send(new PutObjectCommand(uploadParams));

    // Return the Bucket and R2 key for the uploaded PDF
    return {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
    };
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "text": "Hello, world!"
}
```

---

## Image-to-image generation using Replicate and nano-banana

Learn how to generate images from source image URLs using Replicate and Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to generate images from source image URLs using [Replicate](https://replicate.com/), the [nano-banana-image-to-image](https://replicate.com/meta/nano-banana-image-to-image) model.

## Task code

```tsx trigger/generateImage.tsx theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { task, wait } from "@trigger.dev/sdk";
import Replicate, { Prediction } from "replicate";

// Initialize clients
const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

const s3Client = new S3Client({
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

const model = "google/nano-banana";

export const generateImageAndUploadToR2 = task({
  id: "generate-image-and-upload-to-r2",
  run: async (payload: { prompt: string; imageUrl: string }) => {
    const { prompt, imageUrl } = payload;

    const token = await wait.createToken({
      timeout: "10m",
    });

    // Use Flux with structured prompt
    const output = await replicate.predictions.create({
      model: model,
      input: { prompt, image_input: [imageUrl] },
      // pass the provided URL to Replicate's webhook, so they can "callback"
      webhook: token.url,
      webhook_events_filter: ["completed"],
    });

    const result = await wait.forToken<Prediction>(token).unwrap();
    // unwrap() throws a timeout error or returns the result 👆

    if (!result.ok) {
      throw new Error("Failed to create prediction");
    }

    const generatedImageUrl = result.output.output;

    const image = await fetch(generatedImageUrl);
    const imageBuffer = Buffer.from(await image.arrayBuffer());

    const base64Image = Buffer.from(imageBuffer).toString("base64");

    const timestamp = Date.now();
    const filename = `generated-${timestamp}.png`;

    // Generate unique key for R2
    const sanitizedFileName = filename.replace(/[^a-zA-Z0-9.-]/g, "_");
    const r2Key = `uploaded-images/${timestamp}-${sanitizedFileName}`;

    const uploadParams = {
      Bucket: process.env.R2_BUCKET,
      Key: r2Key,
      Body: imageBuffer,
      ContentType: "image/png",
      // Add cache control for better performance
      CacheControl: "public, max-age=31536000", // 1 year
    };

    const uploadResult = await s3Client.send(new PutObjectCommand(uploadParams));

    // Construct the public URL using the R2_PUBLIC_URL env var
    const publicUrl = `${process.env.R2_PUBLIC_URL}/${r2Key}`;

    return {
      success: true,
      publicUrl,
      originalPrompt: prompt,
      sourceImageUrl: imageUrl,
    };
  },
});
```

## Environment variables

You will need to set the following environment variables:

```
TRIGGER_SECRET_KEY=<your-trigger-secret-key>
REPLICATE_API_TOKEN=<your-replicate-api-token>
R2_ENDPOINT=<your-r2-endpoint>
R2_ACCESS_KEY_ID=<your-r2-access-key-id>
R2_SECRET_ACCESS_KEY=<your-r2-secret-access-key>
R2_BUCKET=<your-r2-bucket>
R2_PUBLIC_URL=<your-r2-public-url>
```

---

## Send a sequence of emails using Resend

This example will show you how to send a sequence of emails over several days using Resend with Trigger.dev.

## Overview

Each email is wrapped in retry.onThrow. This will retry the block of code if an error is thrown. This is useful when you don’t want to retry the whole task, but just a part of it. The entire task will use the default retrying, so can also retry.

Additionally this task uses wait.for to wait for a certain amount of time before sending the next email. During the waiting time, the task will be paused and will not consume any resources.

## Task code

```ts trigger/email-sequence.ts theme={"theme":"css-variables"}
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_ASP_KEY);

export const emailSequence = task({
  id: "email-sequence",
  run: async (payload: { userId: string; email: string; name: string }) => {
    console.log(`Start email sequence for user ${payload.userId}`, payload);

    // Send the first email immediately
    const firstEmailResult = await retry.onThrow(
      async ({ attempt }) => {
        const { data, error } = await resend.emails.send({
          from: "hello@trigger.dev",
          to: payload.email,
          subject: "Welcome to Trigger.dev",
          html: `<p>Hello ${payload.name},</p><p>Welcome to Trigger.dev</p>`,
        });

        if (error) {
          // Throwing an error will trigger a retry of this block
          throw error;
        }

        return data;
      },
      { maxAttempts: 3 }
    );

    // Then wait 3 days
    await wait.for({ days: 3 });

    // Send the second email
    const secondEmailResult = await retry.onThrow(
      async ({ attempt }) => {
        const { data, error } = await resend.emails.send({
          from: "hello@trigger.dev",
          to: payload.email,
          subject: "Some tips for you",
          html: `<p>Hello ${payload.name},</p><p>Here are some tips for you…</p>`,
        });

        if (error) {
          // Throwing an error will trigger a retry of this block
          throw error;
        }

        return data;
      },
      { maxAttempts: 3 }
    );

    //etc...
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "userId": "123",
  "email": "<your-test-email>", // Replace with your test email
  "name": "Alice Testington"
}
```

---

## Generate OG Images using Satori

Learn how to generate dynamic Open Graph images using Satori and Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to generate dynamic Open Graph (OG) images using Vercel's [Satori](https://github.com/vercel/satori). The task takes a title and image URL as input and generates a beautiful OG image with text overlay.

This can be customized and extended however you like, full list of options can be found [here](https://github.com/vercel/satori).

## Task code

```tsx trigger/generateOgImage.ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";
import satori from "satori";
import sharp from "sharp";
import { join } from "path";
import fs from "fs/promises";

export const generateOgImage = schemaTask({
  id: "generate-og-image",
  schema: z.object({
    width: z.number().optional(),
    height: z.number().optional(),
    title: z.string(),
    imageUrl: z.string().url(),
  }),
  run: async (payload) => {
    // Load font
    const fontResponse = await fetch(
      "https://github.com/googlefonts/roboto/raw/main/src/hinted/Roboto-Regular.ttf"
    ).then((res) => res.arrayBuffer());

    // Fetch and convert image to base64
    const imageResponse = await fetch(payload.imageUrl);
    const imageBuffer = await imageResponse.arrayBuffer();
    const imageBase64 = `data:${
      imageResponse.headers.get("content-type") || "image/jpeg"
    };base64,${Buffer.from(imageBuffer).toString("base64")}`;

    const markup = (
      <div
        style={{
          width: payload.width ?? 1200,
          height: payload.height ?? 630,
          display: "flex",
          backgroundColor: "#121317",
          position: "relative",
          fontFamily: "Roboto",
        }}
      >
        <img
          src={imageBase64}
          width={payload.width ?? 1200}
          height={payload.height ?? 630}
          style={{
            objectFit: "cover",
          }}
        />
        <h1
          style={{
            fontSize: "60px",
            fontWeight: "bold",
            color: "#fff",
            margin: 0,
            position: "absolute",
            top: "50%",
            transform: "translateY(-50%)",
            left: "48px",
            maxWidth: "60%",
            textShadow: "0 2px 4px rgba(0,0,0,0.5)",
          }}
        >
          {payload.title}
        </h1>
      </div>
    );

    const svg = await satori(markup, {
      width: payload.width ?? 1200,
      height: payload.height ?? 630,
      fonts: [
        {
          name: "Roboto",
          data: fontResponse,
          weight: 400,
          style: "normal",
        },
      ],
    });

    const fileName = `og-${Date.now()}.jpg`;
    const tempDir = join(process.cwd(), "tmp");
    await fs.mkdir(tempDir, { recursive: true });
    const outputPath = join(tempDir, fileName);

    await sharp(Buffer.from(svg))
      .jpeg({
        quality: 90,
        mozjpeg: true,
      })
      .toFile(outputPath);

    return {
      filePath: outputPath,
      width: payload.width,
      height: payload.height,
    };
  },
});
```

## Image example

This image was generated using the above task.

<img alt="OG Image" />

## Testing your task

To test this task in the [dashboard](https://cloud.trigger.dev), you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "title": "My Awesome OG image",
  "imageUrl": "<your-image-url>",
  "width": 1200, // optional, defaults to 1200
  "height": 630 // optional, defaults to 630
}
```

---

## Scrape the top 3 articles from Hacker News and email yourself a summary every weekday

This example demonstrates how to scrape the top 3 articles from Hacker News using BrowserBase and Puppeteer, summarize them with ChatGPT and send a nicely formatted email summary to yourself every weekday using Resend.

<iframe title="YouTube video player" />

## Overview

In this example we'll be using a number of different tools and features to:

1. Scrape the content of the top 3 articles from Hacker News
2. Summarize each article
3. Email the summaries to yourself

And we'll be using the following tools and features:

* [Schedules](/tasks/scheduled) to run the task every weekday at 9 AM
* [Batch Triggering](/triggering#yourtask-batchtriggerandwait) to run separate child tasks for each article while the parent task waits for them all to complete
* [idempotencyKey](/triggering#idempotencykey) to prevent tasks being triggered multiple times
* [BrowserBase](https://browserbase.com/) to proxy the scraping of the Hacker News articles
* [Puppeteer](https://pptr.dev/) to scrape the articles linked from Hacker News
* [OpenAI](https://platform.openai.com/docs/overview) to summarize the articles
* [Resend](https://resend.com/) to send a nicely formatted email summary

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Puppeteer](https://pptr.dev/guides/installation) installed on your machine
* A [BrowserBase](https://browserbase.com/) account
* An [OpenAI](https://platform.openai.com/docs/overview) account
* A [Resend](https://resend.com/) account

## Build configuration

First up, add these build settings to your `trigger.config.ts` file:

```tsx trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    // This is required to use the Puppeteer library
    extensions: [puppeteer()],
  },
});
```

Learn more about the [trigger.config.ts](/config/config-file) file including setting default retry settings, customizing the build environment, and more.

### Environment variables

Set the following environment variable in your local `.env` file to run this task locally. And before deploying your task, set them in the [Trigger.dev dashboard](/deploy-environment-variables) or [using the SDK](/deploy-environment-variables#in-your-code):

```bash theme={"theme":"css-variables"}
BROWSERBASE_API_KEY: "<your BrowserBase API key>"
OPENAI_API_KEY: "<your OpenAI API key>"
RESEND_API_KEY: "<your Resend API key>"
```

### Task code

```ts trigger/scrape-hacker-news.ts theme={"theme":"css-variables"}
import { render } from "@react-email/render";
import { logger, schedules, task, wait } from "@trigger.dev/sdk";
import { OpenAI } from "openai";
import puppeteer from "puppeteer-core";
import { Resend } from "resend";
import { HNSummaryEmail } from "./summarize-hn-email";

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const resend = new Resend(process.env.RESEND_API_KEY);

// Parent task (scheduled to run 9AM every weekday)
export const summarizeHackerNews = schedules.task({
  id: "summarize-hacker-news",
  cron: {
    pattern: "0 9 * * 1-5",
    timezone: "Europe/London",
  }, // Run at 9 AM, Monday to Friday
  run: async () => {
    // Connect to BrowserBase to proxy the scraping of the Hacker News articles
    const browser = await puppeteer.connect({
      browserWSEndpoint: `wss://connect.browserbase.com?apiKey=${process.env.BROWSERBASE_API_KEY}`,
    });
    logger.info("Connected to Browserbase");

    const page = await browser.newPage();

    // Navigate to Hacker News and scrape top 3 articles
    await page.goto("https://news.ycombinator.com/news", {
      waitUntil: "networkidle0",
    });
    logger.info("Navigated to Hacker News");

    const articles = await page.evaluate(() => {
      const items = document.querySelectorAll(".athing");
      return Array.from(items)
        .slice(0, 3)
        .map((item) => {
          const titleElement = item.querySelector(".titleline > a");
          const link = titleElement?.getAttribute("href");
          const title = titleElement?.textContent;
          return { title, link };
        });
    });
    logger.info("Scraped top 3 articles", { articles });

    await browser.close();
    await wait.for({ seconds: 5 });

    // Use batchTriggerAndWait to process articles
    const summaries = await scrapeAndSummarizeArticle
      .batchTriggerAndWait(
        articles.map((article) => ({
          payload: { title: article.title!, link: article.link! },
        }))
      )
      .then((batch) => batch.runs.filter((run) => run.ok).map((run) => run.output));

    // Send email using Resend
    await resend.emails.send({
      from: "Hacker News Summary <hi@demo.tgr.dev>",
      to: ["james@trigger.dev"],
      subject: "Your morning HN summary",
      html: render(<HNSummaryEmail articles={summaries} />),
    });

    logger.info("Email sent successfully");
  },
});

// Child task for scraping and summarizing individual articles
export const scrapeAndSummarizeArticle = task({
  id: "scrape-and-summarize-articles",
  retry: {
    maxAttempts: 3,
    minTimeoutInMs: 5000,
    maxTimeoutInMs: 10000,
    factor: 2,
    randomize: true,
  },
  run: async ({ title, link }: { title: string; link: string }) => {
    logger.info(`Summarizing ${title}`);

    const browser = await puppeteer.connect({
      browserWSEndpoint: `wss://connect.browserbase.com?apiKey=${process.env.BROWSERBASE_API_KEY}`,
    });
    const page = await browser.newPage();

    // Prevent all assets from loading, images, stylesheets etc
    await page.setRequestInterception(true);
    page.on("request", (request) => {
      if (["script", "stylesheet", "image", "media", "font"].includes(request.resourceType())) {
        request.abort();
      } else {
        request.continue();
      }
    });

    await page.goto(link, { waitUntil: "networkidle0" });
    logger.info(`Navigated to article: ${title}`);

    // Extract the main content of the article
    const content = await page.evaluate(() => {
      const articleElement = document.querySelector("article") || document.body;
      return articleElement.innerText.trim().slice(0, 1500); // Limit to 1500 characters
    });

    await browser.close();

    logger.info(`Extracted content for article: ${title}`, { content });

    // Summarize the content using ChatGPT
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [
        {
          role: "user",
          content: `Summarize this article in 2-3 concise sentences:\n\n${content}`,
        },
      ],
    });

    logger.info(`Generated summary for article: ${title}`);

    return {
      title,
      link,
      summary: response.choices[0].message.content,
    };
  },
});
```

## Create your email template using React Email

To prevent the main example from becoming too cluttered, we'll create a separate file for our email template. It's formatted using [React Email](https://react.email/docs/introduction) components so you'll need to install the package to use it.

Notice how this file is imported into the main task code and passed to Resend to send the email.

```tsx summarize-hn-email.tsx theme={"theme":"css-variables"}
import { Html, Head, Body, Container, Section, Heading, Text, Link } from "@react-email/components";

interface Article {
  title: string;
  link: string;
  summary: string | null;
}

export const HNSummaryEmail: React.FC<{ articles: Article[] }> = ({ articles }) => (
  <Html>
    <Head />
    <Body style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <Container>
        <Heading as="h1">Your Morning HN Summary</Heading>
        {articles.map((article, index) => (
          <Section key={index} style={{ marginBottom: "20px" }}>
            <Heading as="h3">
              <Link href={article.link}>{article.title}</Link>
            </Heading>
            <Text>{article.summary || "No summary available"}</Text>
          </Section>
        ))}
      </Container>
    </Body>
  </Html>
);
```

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

## Testing your task

To test this task in the dashboard, use the Test page and set the schedule date to "Now" to ensure the task triggers immediately. Then click "Run test" and wait for the task to complete.

---

## Track errors with Sentry

This example demonstrates how to track errors with Sentry using Trigger.dev.

## Overview

Automatically send errors and source maps to your Sentry project from your Trigger.dev tasks. Sending source maps to Sentry allows for more detailed stack traces when errors occur, as Sentry can map the minified code back to the original source code.

## Prerequisites

* A [Sentry](https://sentry.io) account and project
* A [Trigger.dev](https://trigger.dev) account and project

## Setup

This setup involves two files:

1. **`trigger.config.ts`** - Configures the build to upload source maps to Sentry during deployment
2. **`trigger/init.ts`** - Initializes Sentry and registers the error tracking hook at runtime

<Note>
  You will need to set the `SENTRY_AUTH_TOKEN` and `SENTRY_DSN` environment variables. You can find
  the `SENTRY_AUTH_TOKEN` in your Sentry dashboard, in settings -> developer settings -> auth tokens
  and the `SENTRY_DSN` in your Sentry dashboard, in settings -> projects -> your project -> client
  keys (DSN). Add these to your `.env` file, and in your [Trigger.dev
  dashboard](https://cloud.trigger.dev), under environment variables in your project's sidebar.
</Note>

### Build configuration

Add this build configuration to your `trigger.config.ts` file. This uses the Sentry esbuild plugin to upload source maps every time you deploy your project.

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { esbuildPlugin } from "@trigger.dev/build/extensions";
import { sentryEsbuildPlugin } from "@sentry/esbuild-plugin";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [
      esbuildPlugin(
        sentryEsbuildPlugin({
          org: "<your-sentry-org>",
          project: "<your-sentry-project>",
          // Find this auth token in settings -> developer settings -> auth tokens
          authToken: process.env.SENTRY_AUTH_TOKEN,
        }),
        { placement: "last", target: "deploy" }
      ),
    ],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

### Runtime initialization

Create a `trigger/init.ts` file to initialize Sentry and register the global `onFailure` hook. This file is automatically loaded when your tasks execute.

```ts trigger/init.ts theme={"theme":"css-variables"}
import { tasks } from "@trigger.dev/sdk";
import * as Sentry from "@sentry/node";

// Initialize Sentry
Sentry.init({
  defaultIntegrations: false,
  // The Data Source Name (DSN) is a unique identifier for your Sentry project.
  dsn: process.env.SENTRY_DSN,
  // Update this to match the environment you want to track errors for
  environment: process.env.NODE_ENV === "production" ? "production" : "development",
});

// Register a global onFailure hook to capture errors
tasks.onFailure(({ payload, error, ctx }) => {
  Sentry.captureException(error, {
    extra: {
      payload,
      ctx,
    },
  });
});
```

<Note>
  Learn more about [global lifecycle hooks](/tasks/overview#global-lifecycle-hooks) and the
  [`init.ts` file](/tasks/overview#init-ts).
</Note>

## Testing that errors are being sent to Sentry

To test that errors are being sent to Sentry, you need to create a task that will fail.

This task takes no payload, and will throw an error.

```ts trigger/sentry-error-test.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";

export const sentryErrorTest = task({
  id: "sentry-error-test",
  retry: {
    // Only retry once
    maxAttempts: 1,
  },
  run: async () => {
    const error = new Error("This is a custom error that Sentry will capture");
    error.cause = { additionalContext: "This is additional context" };
    throw error;
  },
});
```

After creating the task, deploy your project.

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

Once deployed, navigate to the `test` page in the sidebar of your [Trigger.dev dashboard](https://cloud.trigger.dev), click on your `prod` environment, and select the `sentryErrorTest` task.

Run a test task with an empty payload by clicking the `Run test` button.

Your run should then fail, and if everything is set up correctly, you will see an error in the Sentry project dashboard shortly after.

---

## Process images using Sharp

This example demonstrates how to process images using the Sharp library with Trigger.dev.

## Overview

This task processes and watermarks an image using the Sharp library, and then uploads it to R2 storage.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* The [Sharp](https://sharp.pixelplumbing.com/install) library installed on your machine
* An R2-compatible object storage service, such as [Cloudflare R2](https://developers.cloudflare.com/r2)

## Adding the build configuration

To use this example, you'll first need to add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    // This is required to use the Sharp library
    external: ["sharp"],
  },
});
```

<Note>
  Any packages that install or build a native binary should be added to external, as native binaries
  cannot be bundled.
</Note>

## Key features

* Resizes a JPEG image to 800x800 pixels
* Adds a watermark to the image, positioned in the bottom-right corner, using a PNG image
* Uploads the processed image to R2 storage

## Task code

```ts trigger/sharp-image-processing.ts theme={"theme":"css-variables"}
import { S3Client } from "@aws-sdk/client-s3";
import { Upload } from "@aws-sdk/lib-storage";
import { logger, task } from "@trigger.dev/sdk";
import fs from "fs/promises";
import os from "os";
import path from "path";
import sharp from "sharp";

// Initialize R2 client using your R2 account details
const r2Client = new S3Client({
  region: "auto",
  endpoint: process.env.R2_ENDPOINT,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY ?? "",
  },
});

export const sharpProcessImage = task({
  id: "sharp-process-image",
  retry: { maxAttempts: 1 },
  run: async (payload: { imageUrl: string; watermarkUrl: string }) => {
    const { imageUrl, watermarkUrl } = payload;
    const outputPath = path.join(os.tmpdir(), `output_${Date.now()}.jpg`);

    const [imageResponse, watermarkResponse] = await Promise.all([
      fetch(imageUrl),
      fetch(watermarkUrl),
    ]);
    const imageBuffer = await imageResponse.arrayBuffer();
    const watermarkBuffer = await watermarkResponse.arrayBuffer();

    await sharp(Buffer.from(imageBuffer))
      .resize(800, 800) // Resize the image to 800x800px
      .composite([
        {
          input: Buffer.from(watermarkBuffer),
          gravity: "southeast", // Position the watermark in the bottom-right corner
        },
      ])
      .jpeg() // Convert to jpeg
      .toBuffer() // Convert to buffer
      .then(async (outputBuffer) => {
        await fs.writeFile(outputPath, outputBuffer); // Write the buffer to file

        const r2Key = `processed-images/${path.basename(outputPath)}`;
        const uploadParams = {
          Bucket: process.env.R2_BUCKET,
          Key: r2Key,
          Body: await fs.readFile(outputPath),
        };

        const upload = new Upload({
          client: r2Client,
          params: uploadParams,
        });

        await upload.done();
        logger.log("Image uploaded to R2 storage.", {
          path: `/${process.env.R2_BUCKET}/${r2Key}`,
        });

        await fs.unlink(outputPath); // Clean up the temporary file
        return { r2Key };
      });
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "imageUrl": "<an-image-url.jpg>", // Replace with a URL to a JPEG image
  "watermarkUrl": "<an-image-url.png>" // Replace with a URL to a PNG watermark image
}
```

## Local development

To test this example task locally, be sure to install any packages from the build extensions you added to your `trigger.config.ts` file to your local machine. In this case, you need to install .

---

## Trigger a task from Stripe webhook events

This example demonstrates how to handle Stripe webhook events using Trigger.dev.

## Overview

This example shows how to set up a webhook handler in your existing app for incoming Stripe events. The handler triggers a task when a `checkout.session.completed` event is received. This is easily customisable to handle other Stripe events.

## Key features

* Shows how to create a Stripe webhook handler in your app
* Triggers a task from your backend when a `checkout.session.completed` event is received

## Environment variables

You'll need to configure the following environment variables for this example to work:

* `STRIPE_WEBHOOK_SECRET` The secret key used to verify the Stripe webhook signature.
* `TRIGGER_API_URL` Your Trigger.dev API url: `https://api.trigger.dev`
* `TRIGGER_SECRET_KEY` Your Trigger.dev secret key

## Setting up the Stripe webhook handler

First you'll need to create a [Stripe webhook](https://stripe.com/docs/webhooks) handler route that listens for POST requests and verifies the Stripe signature.

Here are examples of how you can set up a handler using different frameworks:

<CodeGroup>
  ```ts Next.js theme={"theme":"css-variables"}
  // app/api/stripe-webhook/route.ts
  import { NextResponse } from "next/server";
  import { tasks } from "@trigger.dev/sdk";
  import Stripe from "stripe";
  import type { stripeCheckoutCompleted } from "@/trigger/stripe-checkout-completed";
  //     👆 **type-only** import

  export async function POST(request: Request) {
    const signature = request.headers.get("stripe-signature");
    const payload = await request.text();

    if (!signature || !payload) {
      return NextResponse.json(
        { error: "Invalid Stripe payload/signature" },
        {
          status: 400,
        }
      );
    }

    const event = Stripe.webhooks.constructEvent(
      payload,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET as string
    );

    // Perform the check based on the event type
    switch (event.type) {
      case "checkout.session.completed": {
        // Trigger the task only if the event type is "checkout.session.completed"
        const { id } = await tasks.trigger<typeof stripeCheckoutCompleted>(
          "stripe-checkout-completed",
          event.data.object
        );
        return NextResponse.json({ runId: id });
      }
      default: {
        // Return a response indicating that the event is not handled
        return NextResponse.json(
          { message: "Event not handled" },
          {
            status: 200,
          }
        );
      }
    }
  }
  ```

  ```ts Remix theme={"theme":"css-variables"}
  // app/webhooks.stripe.ts
  import { type ActionFunctionArgs, json } from "@remix-run/node";
  import type { stripeCheckoutCompleted } from "src/trigger/stripe-webhook";
  //     👆 **type-only** import
  import { tasks } from "@trigger.dev/sdk";
  import Stripe from "stripe";

  export async function action({ request }: ActionFunctionArgs) {
    // Validate the Stripe webhook payload
    const signature = request.headers.get("stripe-signature");
    const payload = await request.text();

    if (!signature || !payload) {
      return json({ error: "Invalid Stripe payload/signature" }, { status: 400 });
    }

    const event = Stripe.webhooks.constructEvent(
      payload,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET as string
    );

    // Perform the check based on the event type
    switch (event.type) {
      case "checkout.session.completed": {
        // Trigger the task only if the event type is "checkout.session.completed"
        const { id } = await tasks.trigger<typeof stripeCheckoutCompleted>(
          "stripe-checkout-completed",
          event.data.object
        );
        return json({ runId: id });
      }
      default: {
        // Return a response indicating that the event is not handled
        return json({ message: "Event not handled" }, { status: 200 });
      }
    }
  }
  ```
</CodeGroup>

## Task code

This task is triggered when a `checkout.session.completed` event is received from Stripe.

```ts trigger/stripe-checkout-completed.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import type stripe from "stripe";

export const stripeCheckoutCompleted = task({
  id: "stripe-checkout-completed",
  run: async (payload: stripe.Checkout.Session) => {
    // Add your custom logic for handling the checkout.session.completed event here
  },
});
```

## Testing your task locally

To test everything is working you can use the Stripe CLI to send test events to your endpoint:

1. Install the [Stripe CLI](https://stripe.com/docs/stripe-cli#install), and login
2. Follow the instructions to [test your handler](https://docs.stripe.com/webhooks#test-webhook). This will include a temporary `STRIPE_WEBHOOK_SECRET` that you can use for testing.
3. When triggering the event, use the `checkout.session.completed` event type. With the Stripe CLI: `stripe trigger checkout.session.completed`
4. If your endpoint is set up correctly, you should see the Stripe events logged in your console with a status of `200`.
5. Then, check the [Trigger.dev](https://cloud.trigger.dev) dashboard and you should see the successful run of the `stripe-webhook` task.

For more information on setting up and testing Stripe webhooks, refer to the [Stripe Webhook Documentation](https://stripe.com/docs/webhooks).

---

## Supabase database operations using Trigger.dev

These examples demonstrate how to run basic CRUD operations on a table in a Supabase database using Trigger.dev.

## Add a new user to a table in a Supabase database

This is a basic task which inserts a new row into a table from a Trigger.dev task.

### Key features

* Shows how to set up a Supabase client using the `@supabase/supabase-js` library
* Shows how to add a new row to a table using `insert`

### Prerequisites

* A [Supabase account](https://supabase.com/dashboard/) and a project set up
* In your Supabase project, create a table called `user_subscriptions`.
* In your `user_subscriptions` table, create a new column:
  * `user_id`, with the data type: `text`

### Task code

```ts trigger/supabase-database-insert.ts theme={"theme":"css-variables"}
import { createClient } from "@supabase/supabase-js";
import { task } from "@trigger.dev/sdk";
import jwt from "jsonwebtoken";
// Generate the Typescript types using the Supabase CLI: https://supabase.com/docs/guides/api/rest/generating-types
import { Database } from "database.types";

export const supabaseDatabaseInsert = task({
  id: "add-new-user",
  run: async (payload: { userId: string }) => {
    const { userId } = payload;

    // Get JWT secret from env vars
    const jwtSecret = process.env.SUPABASE_JWT_SECRET;
    if (!jwtSecret) {
      throw new Error("SUPABASE_JWT_SECRET is not defined in environment variables");
    }

    // Create JWT token for the user
    const token = jwt.sign({ sub: userId }, jwtSecret, { expiresIn: "1h" });

    // Initialize Supabase client with JWT
    const supabase = createClient<Database>(
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

    // Insert a new row into the user_subscriptions table with the provided userId
    const { error } = await supabase.from("user_subscriptions").insert({
      user_id: userId,
    });

    // If there was an error inserting the new user, throw an error
    if (error) {
      throw new Error(`Failed to insert new user: ${error.message}`);
    }

    return {
      message: `New user added successfully: ${userId}`,
    };
  },
});
```

<Note>
  To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
  our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
  how to use JWT authentication for user-specific operations or your service role key for
  admin-level access.
</Note>

### Testing your task

To test this task in the [Trigger.dev dashboard](https://cloud.trigger.dev), you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "userId": "user_12345"
}
```

If the task completes successfully, you will see a new row in your `user_subscriptions` table with the `user_id` set to `user_12345`.

## Update a user's subscription on a table in a Supabase database

This task shows how to update a user's subscription on a table. It checks if the user already has a subscription and either inserts a new row or updates an existing row with the new plan.

This type of task is useful for managing user subscriptions, updating user details, or performing other operations you might need to do on a database table.

### Key features

* Shows how to set up a Supabase client using the `@supabase/supabase-js` library
* Adds a new row to the table if the user doesn't exist using `insert`
* Checks if the user already has a plan, and if they do updates the existing row using `update`
* Demonstrates how to use [AbortTaskRunError](https://trigger.dev/docs/errors-retrying#using-aborttaskrunerror) to stop the task run without retrying if an invalid plan type is provided

### Prerequisites

* A [Supabase account](https://supabase.com/dashboard/) and a project set up
* In your Supabase project, create a table called `user_subscriptions` (if you haven't already)
* In your `user_subscriptions` table, create these columns (if they don't already exist):

  * `user_id`, with the data type: `text`
  * `plan`, with the data type: `text`
  * `updated_at`, with the data type: `timestamptz`

### Task code

```ts trigger/supabase-update-user-subscription.ts theme={"theme":"css-variables"}
import { createClient } from "@supabase/supabase-js";
import { AbortTaskRunError, task } from "@trigger.dev/sdk";
// Generate the Typescript types using the Supabase CLI: https://supabase.com/docs/guides/api/rest/generating-types
import { Database } from "database.types";

// Define the allowed plan types
type PlanType = "hobby" | "pro" | "enterprise";

// Create a single Supabase client for interacting with your database
// 'Database' supplies the type definitions to supabase-js
const supabase = createClient<Database>(
  // These details can be found in your Supabase project settings under `API`
  process.env.SUPABASE_PROJECT_URL as string, // e.g. https://abc123.supabase.co - replace 'abc123' with your project ID
  process.env.SUPABASE_SERVICE_ROLE_KEY as string // Your service role secret key
);

export const supabaseUpdateUserSubscription = task({
  id: "update-user-subscription",
  run: async (payload: { userId: string; newPlan: PlanType }) => {
    const { userId, newPlan } = payload;

    // Abort the task run without retrying if the new plan type is invalid
    if (!["hobby", "pro", "enterprise"].includes(newPlan)) {
      throw new AbortTaskRunError(
        `Invalid plan type: ${newPlan}. Allowed types are 'hobby', 'pro', or 'enterprise'.`
      );
    }

    // Query the user_subscriptions table to check if the user already has a subscription
    const { data: existingSubscriptions } = await supabase
      .from("user_subscriptions")
      .select("user_id")
      .eq("user_id", userId);

    if (!existingSubscriptions || existingSubscriptions.length === 0) {
      // If there are no existing users with the provided userId and plan, insert a new row
      const { error: insertError } = await supabase.from("user_subscriptions").insert({
        user_id: userId,
        plan: newPlan,
        updated_at: new Date().toISOString(),
      });

      // If there was an error inserting the new subscription, throw an error
      if (insertError) {
        throw new Error(`Failed to insert user subscription: ${insertError.message}`);
      }
    } else {
      // If the user already has a subscription, update their existing row
      const { error: updateError } = await supabase
        .from("user_subscriptions")
        // Set the plan to the new plan and update the timestamp
        .update({ plan: newPlan, updated_at: new Date().toISOString() })
        .eq("user_id", userId);

      // If there was an error updating the subscription, throw an error
      if (updateError) {
        throw new Error(`Failed to update user subscription: ${updateError.message}`);
      }
    }

    // Return an object with the userId and newPlan
    return {
      userId,
      newPlan,
    };
  },
});
```

<Note>
  This task uses your service role secret key to bypass Row Level Security. There are different ways
  of configuring your [RLS
  policies](https://supabase.com/docs/guides/database/postgres/row-level-security), so always make
  sure you have the correct permissions set up for your project.
</Note>

### Testing your task

To test this task in the [Trigger.dev dashboard](https://cloud.trigger.dev), you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "userId": "user_12345",
  "newPlan": "pro"
}
```

If the task completes successfully, you will see a new row in your `user_subscriptions` table with the `user_id` set to `user_12345`, the `plan` set to `pro`, and the `updated_at` timestamp updated to the current time.

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

## Uploading files to Supabase Storage

This example demonstrates how to upload files to Supabase Storage using Trigger.dev.

## Overview

This example shows how to upload a video file to Supabase Storage using two different methods.

* [Upload to Supabase Storage using the Supabase client](/guides/examples/supabase-storage-upload#example-1-upload-to-supabase-storage-using-the-supabase-storage-client)
* [Upload to Supabase Storage using the AWS S3 client](/guides/examples/supabase-storage-upload#example-2-upload-to-supabase-storage-using-the-aws-s3-client)

## Upload to Supabase Storage using the Supabase client

This task downloads a video from a provided URL and uploads it to Supabase Storage using the Supabase client.

### Task code

```ts trigger/supabase-storage-upload.ts theme={"theme":"css-variables"}
import { createClient } from "@supabase/supabase-js";
import { logger, task } from "@trigger.dev/sdk";
import fetch from "node-fetch";

// Initialize Supabase client
const supabase = createClient(
  process.env.SUPABASE_PROJECT_URL ?? "",
  process.env.SUPABASE_SERVICE_ROLE_KEY ?? ""
);

export const supabaseStorageUpload = task({
  id: "supabase-storage-upload",
  run: async (payload: { videoUrl: string }) => {
    const { videoUrl } = payload;

    const bucket = "my_bucket"; // Replace "my_bucket" with your bucket name
    const objectKey = `video_${Date.now()}.mp4`;

    // Download video data as a buffer
    const response = await fetch(videoUrl);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const videoBuffer = await response.buffer();

    // Upload the video directly to Supabase Storage
    const { error } = await supabase.storage.from(bucket).upload(objectKey, videoBuffer, {
      contentType: "video/mp4",
      upsert: true,
    });

    if (error) {
      throw new Error(`Error uploading video: ${error.message}`);
    }

    logger.log(`Video uploaded to Supabase Storage bucket`, { objectKey });

    // Return the video object key and bucket
    return {
      objectKey,
      bucket: bucket,
    };
  },
});
```

### Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "videoUrl": "<a-video-url>" // Replace <a-video-url> with the URL of the video you want to upload
}
```

## Upload to Supabase Storage using the AWS S3 client

This task downloads a video from a provided URL, saves it to a temporary file, and then uploads the video file to Supabase Storage using the AWS S3 client.

### Key features

* Fetches a video from a provided URL
* Uploads the video file to Supabase Storage using S3

### Task code

```ts trigger/supabase-storage-upload-s3.ts theme={"theme":"css-variables"}
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { logger, task } from "@trigger.dev/sdk";
import fetch from "node-fetch";

// Initialize S3 client for Supabase Storage
const s3Client = new S3Client({
  region: process.env.SUPABASE_REGION, // Your Supabase project's region e.g. "us-east-1"
  endpoint: `https://${process.env.SUPABASE_PROJECT_ID}.supabase.co/storage/v1/s3`,
  credentials: {
    // These credentials can be found in your supabase storage settings, under 'S3 access keys'
    accessKeyId: process.env.SUPABASE_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.SUPABASE_SECRET_ACCESS_KEY ?? "",
  },
});

export const supabaseStorageUploadS3 = task({
  id: "supabase-storage-upload-s3",
  run: async (payload: { videoUrl: string }) => {
    const { videoUrl } = payload;

    // Fetch the video as an ArrayBuffer
    const response = await fetch(videoUrl);
    const videoArrayBuffer = await response.arrayBuffer();
    const videoBuffer = Buffer.from(videoArrayBuffer);

    const bucket = "my_bucket"; // Replace "my_bucket" with your bucket name
    const objectKey = `video_${Date.now()}.mp4`;

    // Upload the video directly to Supabase Storage
    await s3Client.send(
      new PutObjectCommand({
        Bucket: bucket,
        Key: objectKey,
        Body: videoBuffer,
      })
    );
    logger.log(`Video uploaded to Supabase Storage bucket`, { objectKey });

    // Return the video object key
    return {
      objectKey,
      bucket: bucket,
    };
  },
});
```

<Note>
  To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
  our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
  how to use JWT authentication for user-specific operations or your service role key for
  admin-level access.
</Note>

### Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "videoUrl": "<a-video-url>" // Replace <a-video-url> with the URL of the video you want to upload
}
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

## Using the Vercel AI SDK

This example demonstrates how to use the Vercel AI SDK with Trigger.dev.

## Overview

The [Vercel AI SDK](https://www.npmjs.com/package/ai) is a simple way to use AI models from many different providers, including OpenAI, Microsoft Azure, Google Generative AI, Anthropic, Amazon Bedrock, Groq, Perplexity and [more](https://sdk.vercel.ai/providers/ai-sdk-providers).

It provides a consistent interface to interact with the different AI models, so you can easily switch between them without needing to change your code.

## Generate text using OpenAI

This task shows how to use the Vercel AI SDK to generate text from a prompt with OpenAI.

### Task code

```ts trigger/vercel-ai-sdk-openai.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { generateText } from "ai";
// Install the package of the AI model you want to use, in this case OpenAI
import { openai } from "@ai-sdk/openai"; // Ensure OPENAI_API_KEY environment variable is set

export const openaiTask = task({
  id: "openai-text-generate",

  run: async (payload: { prompt: string }) => {
    const chatCompletion = await generateText({
      model: openai("gpt-4-turbo"),
      // Add a system message which will be included with the prompt
      system: "You are a friendly assistant!",
      // The prompt passed in from the payload
      prompt: payload.prompt,
    });

    // Log the generated text
    logger.log("chatCompletion text:" + chatCompletion.text);

    return chatCompletion;
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json theme={"theme":"css-variables"}
{
  "prompt": "What is the meaning of life?"
}
```

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

## Syncing environment variables from your Vercel projects

This example demonstrates how to sync environment variables from your Vercel project to Trigger.dev.

<Warning>
  **Deprecated when using the Vercel integration.** If you are using the [Vercel
  integration](/vercel-integration), do not use `syncVercelEnvVars` — the integration handles env
  var syncing natively and using both together can cause env vars to be incorrectly populated.

  If you are **not** using the Vercel integration, `syncVercelEnvVars` is still supported. Continue
  with the configuration below.
</Warning>

## Build configuration

If you are not using the [Vercel integration](/vercel-integration), you can sync environment variables manually by adding the `syncVercelEnvVars` build extension to your `trigger.config.ts` file. This extension will run automatically every time you deploy your Trigger.dev project.

<Note>
  You need to set the `VERCEL_ACCESS_TOKEN` and `VERCEL_PROJECT_ID` environment variables, or pass
  in the token and project ID as arguments to the `syncVercelEnvVars` build extension. If you're
  working with a team project, you'll also need to set `VERCEL_TEAM_ID`, which can be found in your
  team settings. You can find / generate the `VERCEL_ACCESS_TOKEN` in your Vercel
  [dashboard](https://vercel.com/account/settings/tokens). Make sure the scope of the token covers
  the project with the environment variables you want to sync.
</Note>

<Note>
  When running the build from a Vercel build environment (e.g., during a Vercel deployment), the
  environment variable values will be read from `process.env` instead of fetching them from the
  Vercel API. This is determined by checking if the `VERCEL` environment variable is present. The
  API is still used to determine which environment variables are configured for your project, but
  the actual values come from the local environment.
</Note>

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncVercelEnvVars } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    // Add the syncVercelEnvVars build extension
    extensions: [
      syncVercelEnvVars({
        // A personal access token created in your Vercel account settings
        // Used to authenticate API requests to Vercel
        // Generate at: https://vercel.com/account/tokens
        vercelAccessToken: process.env.VERCEL_ACCESS_TOKEN,
        // The unique identifier of your Vercel project
        // Found in Project Settings > General > Project ID
        projectId: process.env.VERCEL_PROJECT_ID,
        // Optional: The ID of your Vercel team
        // Only required for team projects
        // Found in Team Settings > General > Team ID
        vercelTeamId: process.env.VERCEL_TEAM_ID,
      }),
    ],
  },
});
```

<Note>
  [Build extensions](/config/extensions/overview) allow you to hook into the build system and
  customize the build process or the resulting bundle and container image (in the case of
  deploying). You can use pre-built extensions or create your own.
</Note>

## Running the sync operation

To sync the environment variables, all you need to do is run our `deploy` command. You should see some output in the console indicating that the environment variables have been synced, and they should now be available in your Trigger.dev dashboard.

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

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
