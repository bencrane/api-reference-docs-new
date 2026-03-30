> Sources:
> - https://trigger.dev/docs/guides/use-cases/overview
> - https://trigger.dev/docs/guides/use-cases/data-processing-etl
> - https://trigger.dev/docs/guides/use-cases/marketing
> - https://trigger.dev/docs/guides/use-cases/media-generation
> - https://trigger.dev/docs/guides/use-cases/media-processing

# Use Cases

## Use cases

Explore common use cases for Trigger.dev including data processing, media workflows, marketing automation, and AI generation

Trigger.dev handles workflows that traditional platforms struggle with: long-running operations, unpredictable API latencies, multi-hour processing, and complex orchestration patterns. Our platform provides no timeout limits, automatic retries, and real-time progress tracking built in.

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

---

## Data processing & ETL workflows

Learn how to use Trigger.dev for data processing and ETL (Extract, Transform, Load), including web scraping, database synchronization, batch enrichment and more.

## Overview

Build complex data pipelines that process large datasets without timeouts. Handle streaming analytics, batch enrichment, web scraping, database sync, and file processing with automatic retries and progress tracking.

## Featured examples

<CardGroup>
  <Card title="Realtime CSV importer" icon="book" href="/guides/example-projects/realtime-csv-importer">
    Import CSV files with progress streamed live to frontend.
  </Card>

  <Card title="Web scraper with BrowserBase" icon="book" href="/guides/examples/scrape-hacker-news">
    Scrape websites using BrowserBase and Puppeteer.
  </Card>

  <Card title="Supabase database webhooks" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Trigger tasks from Supabase database webhooks.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for data processing & ETL workflows

**Process datasets for hours without timeouts:** Handle multi-hour transformations, large file processing, or complete database exports. No execution time limits.

**Parallel processing with built-in rate limiting:** Process thousands of records simultaneously while respecting API rate limits. Scale efficiently without overwhelming downstream services.

**Stream progress to your users in real-time:** Show row-by-row processing status updating live in your dashboard. Users see exactly where processing is and how long remains.

## Production use cases

<CardGroup>
  <Card title="MagicSchool AI customer story" href="https://trigger.dev/customers/magicschool-ai-customer-story">
    Read how MagicSchool AI uses Trigger.dev to generate insights from millions of student interactions.
  </Card>

  <Card title="Comp AI customer story" href="https://trigger.dev/customers/comp-ai-customer-story">
    Read how Comp AI uses Trigger.dev to automate evidence collection at scale, powering their open source, AI-driven compliance platform.
  </Card>

  <Card title="Midday customer story" href="https://trigger.dev/customers/midday-customer-story">
    Read how Midday use Trigger.dev to sync large volumes of bank transactions in their financial management platform.
  </Card>
</CardGroup>

## Example workflow patterns

<Tabs>
  <Tab title="CSV file import">
    Simple CSV import pipeline. Receives file upload, parses CSV rows, validates data, imports to database with progress tracking.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[importCSV] --> B[parseCSVFile]
          B --> C[validateRows]
          C --> D[bulkInsertToDB]
          D --> E[notifyCompletion]
      ```
    </div>
  </Tab>

  <Tab title="Multi-source ETL pipeline">
    **Coordinator pattern with parallel extraction**. Batch triggers parallel extraction from multiple sources (APIs, databases, S3), transforms and validates data, loads to data warehouse with monitoring.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[runETLPipeline] --> B[coordinateExtraction]
          B --> C[batchTriggerAndWait]

          C --> D[extractFromAPI]
          C --> E[extractFromDatabase]
          C --> F[extractFromS3]

          D --> G[transformData]
          E --> G
          F --> G

          G --> H[validateData]
          H --> I[loadToWarehouse]
      ```
    </div>
  </Tab>

  <Tab title="Parallel web scraping">
    **Coordinator pattern with browser automation**. Launches headless browsers in parallel to scrape multiple pages, extracts structured data, cleans and normalizes content, stores in database.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[scrapeSite] --> B[coordinateScraping]
          B --> C[batchTriggerAndWait]

          C --> D[scrapePage1]
          C --> E[scrapePage2]
          C --> F[scrapePageN]

          D --> G[cleanData]
          E --> G
          F --> G

          G --> H[normalizeData]
          H --> I[storeInDatabase]
      ```
    </div>
  </Tab>

  <Tab title="Batch data enrichment">
    **Coordinator pattern with rate limiting**. Fetches records needing enrichment, batch triggers parallel API calls with configurable concurrency to respect rate limits, validates enriched data, updates database.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[enrichRecords] --> B[fetchRecordsToEnrich]
          B --> C[coordinateEnrichment]
          C --> D[batchTriggerAndWait]

          D --> E[enrichRecord1]
          D --> F[enrichRecord2]
          D --> G[enrichRecordN]

          E --> H[validateEnrichedData]
          F --> H
          G --> H

          H --> I[updateDatabase]
      ```
    </div>
  </Tab>
</Tabs>

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

---

## Marketing workflows

Learn how to use Trigger.dev for marketing workflows, including drip campaigns, behavioral triggers, personalization engines, and AI-powered content workflows

## Overview

Build marketing workflows from email drip sequences to orchestrating full multi-channel campaigns. Handle multi-day sequences, behavioral triggers, dynamic content generation, and build live analytics dashboards.

## Featured examples

<CardGroup>
  <Card title="Email sequences with Resend" icon="book" href="/guides/examples/resend-email-sequence">
    Send multi-day email sequences with wait delays between messages.
  </Card>

  <Card title="Product image generator" icon="book" href="/guides/example-projects/product-image-generator">
    Transform product photos into professional marketing images using Replicate.
  </Card>

  <Card title="Human-in-the-loop workflow" icon="book" href="/guides/example-projects/human-in-the-loop-workflow">
    Approve marketing content using a human-in-the-loop workflow.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for marketing workflows

**Delays without idle costs:** Wait hours or weeks between steps. Waits over 5 seconds are automatically checkpointed and don't count towards compute usage. Perfect for drip campaigns and scheduled follow-ups.

**Guaranteed delivery:** Messages send exactly once, even after retries. Personalized content isn't regenerated on failure.

**Scale without limits:** Process thousands in parallel while respecting rate limits. Send to entire segments without overwhelming APIs.

## Production use cases

<Card title="Icon customer story" href="https://trigger.dev/customers/icon-customer-story">
  Read how Icon uses Trigger.dev to process and generate thousands of videos per month for their AI-driven video creation platform.
</Card>

## Example workflow patterns

<Tabs>
  <Tab title="Drip email campaign">
    Simple drip campaign. User signs up, waits specified delay, sends personalized email, tracks engagement.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[userCreateAccount] --> B[sendWelcomeEmail]
          B --> C[wait.for 24h]
          C --> D[sendProductTipsEmail]
          D --> E[wait.for 7d]
          E --> F[sendFeedbackEmail]

      ```
    </div>
  </Tab>

  <Tab title="Multi-channel campaigns">
    **Router pattern with delay orchestration**. User action triggers campaign, router selects channel based on preferences (email/SMS/push), coordinates multi-day sequence with delays between messages, tracks engagement across channels.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[startCampaign] --> B[fetchUserProfile]
          B --> C[selectChannel]
          C --> D{Preferred<br/>Channel?}

          D -->|Email| E[sendEmail1]
          D -->|SMS| F[sendSMS1]
          D -->|Push| G[sendPush1]

          E --> H[wait.for 2d]
          F --> H
          G --> H

          H --> I[sendFollowUp]
          I --> J[trackConversion]
      ```
    </div>
  </Tab>

  <Tab title="AI content with approval">
    **Supervisor pattern with approval gate**. Generates AI marketing content (images, copy, assets), pauses with wait.forToken for human review, applies revisions if needed, publishes to channels after approval.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[createCampaignAssets] --> B[generateAIContent]
          B --> C[wait.forToken approval]
          C --> D{Approved?}

          D -->|Yes| E[publishToChannels]
          D -->|Needs revision| F[applyFeedback]
          F --> B
      ```
    </div>
  </Tab>

  <Tab title="Survey response enrichment">
    **Coordinator pattern with enrichment**. User completes survey, batch triggers parallel enrichment from CRM/analytics, analyzes and scores responses, updates customer profiles, triggers personalized follow-up campaigns.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processSurveyResponse] --> B[coordinateEnrichment]
          B --> C[batchTriggerAndWait]

          C --> D[fetchCRMData]
          C --> E[fetchAnalytics]
          C --> F[fetchBehaviorData]

          D --> G[analyzeAndScore]
          E --> G
          F --> G

          G --> H[updateCRMProfile]
          H --> I[triggerFollowUp]
      ```
    </div>
  </Tab>
</Tabs>

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

---

## AI media generation workflows

Learn how to use Trigger.dev for AI media generation including image creation, video synthesis, audio generation, and multi-modal content workflows

## Overview

Build AI media generation pipelines that handle unpredictable API latencies and long-running operations. Generate images, videos, audio, and multi-modal content with automatic retries, progress tracking, and no timeout limits.

## Featured examples

<CardGroup>
  <Card title="Product image generator" icon="book" href="/guides/example-projects/product-image-generator">
    Transform product photos into professional marketing images using Replicate.
  </Card>

  <Card title="Meme generator (human-in-the-loop)" icon="book" href="/guides/example-projects/meme-generator-human-in-the-loop">
    Generate memes with DALL·E 3 and add human approval steps.
  </Card>

  <Card title="Vercel AI SDK image generation" icon="book" href="/guides/example-projects/vercel-ai-sdk-image-generator">
    Generate images from text prompts using the Vercel AI SDK.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for AI media generation workflows

**Pay only for active compute, not AI inference time:** Checkpoint-resume pauses during AI API calls. Generate content that takes minutes or hours without paying for idle inference time.

**No timeout limits for long generations:** Handle generations that take minutes or hours without execution limits. Perfect for high-quality video synthesis and complex multi-modal workflows.

**Human approval gates for brand safety:** Add review steps before publishing AI-generated content. Pause workflows for human approval using waitpoint tokens.

## Production use cases

<CardGroup>
  <Card title="Icon customer story" href="https://trigger.dev/customers/icon-customer-story">
    Read how Icon uses Trigger.dev to process and generate thousands of videos per month for their AI-driven video creation platform.
  </Card>

  <Card title="Papermark customer story" href="https://trigger.dev/customers/papermark-customer-story">
    Read how Papermark process thousands of documents per month using Trigger.dev.
  </Card>
</CardGroup>

## Example workflow patterns

<Tabs>
  <Tab title="AI content with approval">
    **Supervisor pattern with approval gate**. Generates AI content, pauses execution with wait.forToken to allow human review, applies feedback if needed, publishes approved content.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[generateContent] --> B[createWithAI]
          B --> C[wait.forToken approval]
          C --> D{Approved?}

          D -->|Yes| E[publishContent]
          D -->|Needs revision| F[applyFeedback]
          F --> B
      ```
    </div>
  </Tab>

  <Tab title="AI image generation">
    Simple AI image generation. Receives prompt and parameters, calls OpenAI DALL·E 3, post-processes result, uploads to storage.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[generateImage] --> B[optimizeImage]
          B --> C[uploadToStorage]
          C --> D[updateDatabase]
      ```
    </div>
  </Tab>

  <Tab title="Batch image generation">
    **Coordinator pattern with rate limiting**. Receives batch of generation requests, coordinates parallel processing with configurable concurrency to respect API rate limits, validates outputs, stores results.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processBatch] --> B[coordinateGeneration]
          B --> C[batchTriggerAndWait]

          C --> D[generateImage1]
          C --> E[generateImage2]
          C --> F[generateImageN]

          D --> G[validateResults]
          E --> G
          F --> G

          G --> H[storeResults]
          H --> I[notifyCompletion]
      ```
    </div>
  </Tab>

  <Tab title="Multi-step image enhancement">
    **Coordinator pattern with sequential processing**. Generates initial content with AI, applies style transfer or enhancement, upscales resolution, optimizes and compresses for delivery.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processCreative] --> B[generateWithAI]
          B --> C[applyStyleTransfer]
          C --> D[upscaleResolution]
          D --> E[optimizeAndCompress]
          E --> F[uploadToStorage]
      ```
    </div>
  </Tab>
</Tabs>

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

---

## Media processing workflows

Learn how to use Trigger.dev for media processing including video transcoding, image optimization, audio transformation, and document conversion.

## Overview

Build media processing pipelines that handle large files and long-running operations. Process videos, images, audio, and documents with automatic retries, progress tracking, and no timeout limits.

## Featured examples

<CardGroup>
  <Card title="FFmpeg video processing" icon="book" href="/guides/examples/ffmpeg-video-processing">
    Process videos and upload results to R2 storage using FFmpeg.
  </Card>

  <Card title="Product image generator" icon="book" href="/guides/example-projects/product-image-generator">
    Transform product photos into professional marketing images using Replicate.
  </Card>

  <Card title="LibreOffice PDF conversion" icon="book" href="/guides/examples/libreoffice-pdf-conversion">
    Convert documents to PDF using LibreOffice.
  </Card>
</CardGroup>

## Benefits of using Trigger.dev for media processing workflows

**Process multi-hour videos without timeouts:** Transcode videos, extract frames, or run CPU-intensive operations for hours. No execution time limits.

**Stream progress to users in real-time:** Show processing status updating live in your UI. Users see exactly where encoding is and how long remains.

**Parallel processing with resource control:** Process hundreds of files simultaneously with configurable concurrency limits. Control resource usage without overwhelming infrastructure.

## Example workflow patterns

<Tabs>
  <Tab title="Video transcode">
    Simple video transcoding pipeline. Downloads video from storage, batch triggers parallel transcoding to multiple formats and thumbnail extraction, uploads all results.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processVideo] --> B[downloadFromStorage]
          B --> C[batchTriggerAndWait]

          C --> D[transcodeToHD]
          C --> E[transcodeToSD]
          C --> F[extractThumbnail]

          D --> G[uploadToStorage]
          E --> G
          F --> G
      ```
    </div>
  </Tab>

  <Tab title="Adaptive video processing">
    **Router + Coordinator pattern**. Analyzes video metadata to determine source resolution, routes to appropriate transcoding preset, batch triggers parallel post-processing for thumbnails, preview clips, and chapter detection.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processVideoUpload] --> B[analyzeMetadata]
          B --> C{Source<br/>Resolution?}

          C -->|4K Source| D[transcode4K]
          C -->|HD Source| E[transcodeHD]
          C -->|SD Source| F[transcodeSD]

          D --> G[coordinatePostProcessing]
          E --> G
          F --> G

          G --> H[batchTriggerAndWait]
          H --> I[extractThumbnails]
          H --> J[generatePreview]
          H --> K[detectChapters]

          I --> L[uploadToStorage]
          J --> L
          K --> L

          L --> M[notifyComplete]
      ```
    </div>
  </Tab>

  <Tab title="Smart image optimization">
    **Router + Coordinator pattern**. Analyzes image content to detect type, routes to specialized processing (background removal for products, face detection for portraits, scene analysis for landscapes), upscales with AI, batch triggers parallel variant generation.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processImageUpload] --> B[analyzeContent]
          B --> C{Content<br/>Type?}

          C -->|Product| D[removeBackground]
          C -->|Portrait| E[detectFaces]
          C -->|Landscape| F[analyzeScene]

          D --> G[upscaleWithAI]
          E --> G
          F --> G

          G --> H[batchTriggerAndWait]
          H --> I[generateWebP]
          H --> J[generateThumbnails]
          H --> K[generateSocialCrops]

          I --> L[uploadToStorage]
          J --> L
          K --> L
      ```
    </div>
  </Tab>

  <Tab title="Podcast production">
    **Coordinator pattern**. Pre-processes raw audio with noise reduction and speaker diarization, batch triggers parallel tasks for transcription (Deepgram), audio enhancement, and chapter detection, aggregates results to generate show notes and publish.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processAudioUpload] --> B[cleanAudio]
          B --> C[coordinateProcessing]

          C --> D[batchTriggerAndWait]
          D --> E[transcribeWithDeepgram]
          D --> F[enhanceAudio]
          D --> G[detectChapters]

          E --> H[generateShowNotes]
          F --> H
          G --> H

          H --> I[publishToPlatforms]
      ```
    </div>
  </Tab>

  <Tab title="Document extraction with approval">
    **Router pattern with human-in-the-loop**. Detects file type and routes to appropriate processor, classifies document with AI to determine type (invoice/contract/receipt), extracts structured data fields, optionally pauses with wait.forToken for human approval.

    <div>
      ```mermaid theme={"theme":"css-variables"}
      graph TB
          A[processDocumentUpload] --> B[detectFileType]

          B -->|PDF| C[extractText]
          B -->|Word/Excel| D[convertToPDF]
          B -->|Image| E[runOCR]

          C --> F[classifyDocument]
          D --> F
          E --> F

          F -->|Invoice| G[extractLineItems]
          F -->|Contract| H[extractClauses]
          F -->|Receipt| I[extractExpenses]

          G --> J{Needs<br/>Review?}
          H --> J
          I --> J

          J -->|Yes| K[wait.forToken approval]
          J -->|No| L[processAndIntegrate]
          K --> L
      ```
    </div>
  </Tab>
</Tabs>

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

---
