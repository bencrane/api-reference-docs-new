# Modal Examples Documentation Index

> A comprehensive collection of Modal examples organized by category. Each example demonstrates how to use Modal for various tasks, from deploying LLMs to processing data in parallel.

Source: [https://modal.com/docs/examples](https://modal.com/docs/examples)

---

## Getting Started

| Example | File | Description |
|---------|------|-------------|
| [Hello, world!](hello-world.md) | `hello-world.md` | Core features of Modal: running functions locally, remotely, and in parallel |
| [Simple web scraper](webscraper.md) | `webscraper.md` | Web scraping with Modal using Playwright |
| [Serving web endpoints](basic-web.md) | `basic-web.md` | Creating and serving web endpoints on Modal |

## Large Language Models (LLMs)

| Example | File | Description |
|---------|------|-------------|
| [Deploy an OpenAI-compatible LLM service with vLLM](llm-inference.md) | `llm-inference.md` | Deploy an OpenAI-compatible LLM inference service using vLLM |
| [Cut Ministral 3 cold start times by 10x with snapshots](ministral3-inference.md) | `ministral3-inference.md` | Use memory snapshots to dramatically reduce cold start times |
| [Maximize tokens per second in batch processing with vLLM](vllm-throughput.md) | `vllm-throughput.md` | High-throughput batch LLM inference with vLLM |
| [Serve an ultra-low-latency chatbot with SGLang](sglang-low-latency.md) | `sglang-low-latency.md` | Ultra-low-latency LLM serving with SGLang |
| [Efficient LLM Finetuning with Unsloth](unsloth-finetune.md) | `unsloth-finetune.md` | Fine-tune LLMs efficiently using Unsloth |
| [Run a multimodal RAG chatbot to answer questions about PDFs](chat-with-pdf-vision.md) | `chat-with-pdf-vision.md` | Multimodal RAG chatbot for PDF Q&A |
| [Fine-tune an LLM to replace your CEO](llm-finetuning.md) | `llm-finetuning.md` | Fine-tune an LLM on custom data using doppel-bot |
| [Deploy a stateless MCP with FastMCP](mcp-server-stateless.md) | `mcp-server-stateless.md` | Deploy a stateless Model Context Protocol server |

## Images, Video, & 3D

| Example | File | Description |
|---------|------|-------------|
| [Edit images with Flux Kontext](image-to-image.md) | `image-to-image.md` | Image-to-image editing with Flux Kontext |
| [Fine-tune Wan2.1 video models on your face](music-video-gen.md) | `music-video-gen.md` | Generate music videos with fine-tuned video models |
| [Run Flux fast with torch.compile](flux.md) | `flux.md` | Fast Flux inference using torch.compile optimization |
| [Fine-tune Flux with LoRA](diffusers-lora-finetune.md) | `diffusers-lora-finetune.md` | Fine-tune Flux/Stable Diffusion models with LoRA |
| [Animate images with LTX-Video](image-to-video.md) | `image-to-video.md` | Image-to-video generation with LTX-Video |
| [Generate video clips with LTX-Video](ltx.md) | `ltx.md` | Text-to-video generation with LTX-Video |
| [Run Stable Diffusion with a CLI, API, and web UI](text-to-image.md) | `text-to-image.md` | Full-featured Stable Diffusion deployment |

## Audio

| Example | File | Description |
|---------|------|-------------|
| [Deploy a Moshi voice chatbot](llm-voice-chat.md) | `llm-voice-chat.md` | Voice chatbot with Moshi (Quillman) |
| [Stream transcripts at the speed of speech using Kyutai STT](streaming-kyutai-stt.md) | `streaming-kyutai-stt.md` | Real-time speech-to-text streaming |
| [Make music with ACE-Step](generate-music.md) | `generate-music.md` | AI music generation with ACE-Step |
| [Generate speech with Chatterbox](chatterbox-tts.md) | `chatterbox-tts.md` | Text-to-speech with Chatterbox TTS |
| [Run high throughput batched transcription with Whisper](batched-whisper.md) | `batched-whisper.md` | High-throughput batch audio transcription |
| [Fine-tune Whisper to recognize new words](fine-tune-asr.md) | `fine-tune-asr.md` | Fine-tune Whisper ASR models |

## Real-time Communication (WebRTC)

| Example | File | Description |
|---------|------|-------------|
| [Serverless WebRTC](webrtc-yolo.md) | `webrtc-yolo.md` | WebRTC video processing with YOLO object detection |
| [WebRTC quickstart with FastRTC](fastrtc-flip-webcam.md) | `fastrtc-flip-webcam.md` | Quick WebRTC setup with FastRTC |

## Computational Biology

| Example | File | Description |
|---------|------|-------------|
| [Fold proteins with Chai-1](chai1.md) | `chai1.md` | Protein folding with Chai-1 |
| [Build a protein-folding dashboard](esm3.md) | `esm3.md` | ESM3 protein-folding dashboard |
| [Fold proteins with Boltz-2](boltz-predict.md) | `boltz-predict.md` | Protein structure prediction with Boltz-2 |

## Modal Sandboxes

| Example | File | Description |
|---------|------|-------------|
| [Run a background coding agent with OpenCode](opencode-server.md) | `opencode-server.md` | Background coding agent with OpenCode |
| [Build a scalable AI coding platform](modal-vibe.md) | `modal-vibe.md` | Scalable AI coding platform (Modal Vibe) |
| [Create GIFs from Slack using the Claude Agent SDK](claude-slack-gif-creator.md) | `claude-slack-gif-creator.md` | Slack GIF creation with Claude Agent SDK |
| [Run a LangGraph agent's code in a secure GPU sandbox](agent.md) | `agent.md` | LangGraph agent with secure GPU sandbox |
| [Control a sandboxed computer with an LLM](anthropic-computer-use.md) | `anthropic-computer-use.md` | Anthropic computer use in sandboxes |
| [Build a stateful, sandboxed code interpreter](simple-code-interpreter.md) | `simple-code-interpreter.md` | Stateful sandboxed code interpreter |
| [Run Node.js, Ruby, and more in a Sandbox](safe-code-execution.md) | `safe-code-execution.md` | Multi-language safe code execution |
| [Speed up Sandbox starts with warm pools](sandbox-pool.md) | `sandbox-pool.md` | Warm pool pattern for fast sandbox starts |

## Reinforcement Learning

| Example | File | Description |
|---------|------|-------------|
| [Train a model to solve math problems using GRPO and verl](grpo-verl.md) | `grpo-verl.md` | GRPO training with verl framework |
| [Train a model to solve coding problems using GRPO and TRL](grpo-trl.md) | `grpo-trl.md` | GRPO training with TRL framework |

## Embeddings

| Example | File | Description |
|---------|------|-------------|
| [Embed millions of documents with TEI](amazon-embeddings.md) | `amazon-embeddings.md` | High-throughput document embedding |
| [Turn satellite images into vectors and store them in MongoDB](mongodb-search.md) | `mongodb-search.md` | Image embedding and MongoDB vector search |

## Parallel Processing and Job Scheduling

| Example | File | Description |
|---------|------|-------------|
| [Deploy a Hacker News Slackbot](hackernews-alerts.md) | `hackernews-alerts.md` | Scheduled Hacker News monitoring Slackbot |
| [Run a Document OCR job queue](doc-ocr-jobs.md) | `doc-ocr-jobs.md` | Document OCR processing with job queues |
| [Serve a Document OCR web app](doc-ocr-webapp.md) | `doc-ocr-webapp.md` | Document OCR web application |

## Training Models from Scratch

| Example | File | Description |
|---------|------|-------------|
| [Train an SLM with early-stopping grid search over hyperparameters](hp-sweep-gpt.md) | `hp-sweep-gpt.md` | Hyperparameter sweep for GPT-style model training |
| [Run long, resumable training jobs](long-training.md) | `long-training.md` | Long-running training with checkpointing |

## Hosting Popular Libraries

| Example | File | Description |
|---------|------|-------------|
| [YOLO: Fine-tune and serve computer vision models](finetune-yolo.md) | `finetune-yolo.md` | Fine-tune and deploy YOLO models |
| [Blender: Build a 3D render farm](blender-video.md) | `blender-video.md` | Distributed 3D rendering with Blender |
| [Streamlit: Run and deploy Streamlit apps](serve-streamlit.md) | `serve-streamlit.md` | Deploy Streamlit applications |
| [SQLite: Publish explorable data with Datasette](cron-datasette.md) | `cron-datasette.md` | Datasette deployment with cron data updates |
| [Algolia: Build docsearch with a crawler](algolia-indexer.md) | `algolia-indexer.md` | Algolia search index crawler |

## Connecting to Other APIs

| Example | File | Description |
|---------|------|-------------|
| [Discord: Deploy and run a Discord Bot](discord-bot.md) | `discord-bot.md` | Discord bot deployment |
| [Google Sheets: Sync databases and APIs to a Google Sheet](db-to-sheet.md) | `db-to-sheet.md` | Database to Google Sheets synchronization |
| [OpenAI: Run a RAG Q&A chatbot](potus-speech-qanda.md) | `potus-speech-qanda.md` | RAG Q&A chatbot with OpenAI |
| [Tailscale: Add Modal Apps to your VPN](modal-tailscale.md) | `modal-tailscale.md` | Tailscale VPN integration |
| [Prometheus: Publish custom metrics with Pushgateway](pushgateway.md) | `pushgateway.md` | Prometheus metrics publishing |

## Managing Data

| Example | File | Description |
|---------|------|-------------|
| [Mount S3 buckets in Modal apps](s3-bucket-mount.md) | `s3-bucket-mount.md` | S3 bucket mounting |
| [Build your own data warehouse with DuckDB, DBT, and Modal](dbt-duckdb.md) | `dbt-duckdb.md` | Data warehouse with DuckDB and DBT |
| [Create a LoRA Playground with Modal, Gradio, and S3](cloud-bucket-mount-loras.md) | `cloud-bucket-mount-loras.md` | LoRA model playground with cloud bucket mounts |

## Miscellaneous

| Example | File | Description |
|---------|------|-------------|
| [Serving very large models](very-large-models.md) | `very-large-models.md` | Techniques for deploying very large models |

---

*60 examples total. Generated from [modal.com/docs/examples](https://modal.com/docs/examples).*
