# Self-Hosting: Run Your Own LLM with DiscoGen

Run your own LLM for DiscoGen on your hardware. This guide sets up a **proof-of-concept** inference stack on a single GPU using Docker: [Ollama](https://github.com/ollama/ollama) for inference, [LiteLLM](https://github.com/BerriAI/litellm) as an API proxy, and [Cloudflared](https://github.com/cloudflare/cloudflared) for tunnel access.

## Why self-host?

| Feature | Cloud LLM (OpenAI, Anthropic) | Self-hosted |
|---------|-------------------------------|-------------|
| **Cost** | Pay per token. Scales linearly with volume. | Fixed GPU cost. Process unlimited tokens for a flat hourly rate. |
| **Data privacy** | Prompts and domain data sent to third-party APIs | Everything stays on your network |
| **Latency** | Depends on provider load and rate limits | Dedicated GPU, no queue, no throttling |
| **Model control** | Limited to provider's model catalog | Run any open-source model, swap anytime |

> **PoC scope**
>
> This guide covers a single-GPU setup for evaluation and testing. A production deployment with multiple GPUs, model sharding across nodes, or high-throughput serving (vLLM, TGI, etc.) is beyond this scope. For multi-GPU setups, consider [vLLM](https://docs.vllm.ai/) or [TGI](https://huggingface.co/docs/text-generation-inference/) for tensor-parallel inference across nodes.

## Prerequisites

- **GPU:** NVIDIA with 96GB+ VRAM recommended (16GB minimum for smaller models). Don't have one? Rent on-demand from [Lambda](https://lambda.ai/) (used in this guide), [RunPod](https://www.runpod.io/), [Vast.ai](https://vast.ai/), or [CoreWeave](https://www.coreweave.com/). Most providers come with NVIDIA drivers pre-installed.
- **Docker** with [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). The setup script installs both if missing.

## Pick a model

The setup script detects your VRAM and offers these defaults:

| VRAM | Model | |
|------|-------|-|
| 80GB+ | **Llama 4 Scout** | MoE, 17B active params. Best single-GPU option for structured output |
| 40-80GB | **Llama 3.1 70B** | Dense 70B. Reliable JSON generation, well-tested |
| 20-40GB | **Qwen3 32B** | Comparable to 72B models at half the VRAM |
| 8-20GB | **Llama 3.1 8B** | Lightweight. Good for testing the pipeline |

Or select **Custom model** to enter any model name from [ollama.com/library](https://ollama.com/library).

> **Model choice matters**
>
> This guide uses **Llama 4 Scout** on a single GPU as an example. Scout handles firmographic enrichment and basic DiscoGen tasks well, but complex use cases (contact research, multi-step reasoning, nuanced classification) may need a more capable model. For frontier-level quality comparable to GPT-5, look at **DeepSeek-V3.2** (671B) or **Qwen3.5 397B**, both of which require multi-GPU setups.
>
> **Watch your quantization.** Ollama defaults to Q4 to fit models in less VRAM. Heavily quantized models (Q2, Q3) produce worse structured output: hallucinated fields, inconsistent formatting, lower accuracy. **Q4\_K\_M is the practical minimum** for DiscoGen. If a model only fits at Q3 or below, pick a smaller model at Q4 instead.

## Setting up

```bash
mkdir discolike-self-hosting && cd discolike-self-hosting
curl -LO https://api.discolike.com/v1/docs/self-hosting/docker-compose.yml
curl -LO https://api.discolike.com/v1/docs/self-hosting/setup.sh
chmod +x setup.sh && ./setup.sh
```

The script detects your GPU and lets you pick a model that fits.

It then generates API keys, starts the Docker stack, pulls the model (this can take a while depending on your connection), and verifies inference end-to-end.

When complete, you get your tunnel URL, model name, and API key.

> **About the tunnel URL**
>
> The setup creates an instant `*.trycloudflare.com` URL via Docker. It works immediately but changes on restart. For a permanent subdomain, see [Named tunnels](#setting-up-a-named-tunnel) below.

## Connecting to DiscoLike

### Adding your model

1. Go to **Settings → Integrations → AI Providers → Add**

2. Fill in the form:

| Field | Value |
|-------|-------|
| Provider | **Bring Your Own Model** |
| Integration Name | e.g. **`llama4_scout`** |
| Base URL | Your tunnel URL, **without** the `/v1` suffix |
| Model Name | **`openai/llama4:scout`** |
| API Key | The LiteLLM key from setup |

3. Click **Save**. DiscoLike sends a test prompt to validate the connection.

> **The model name must start with `openai/`**
>
> This is the most common setup issue. DiscoLike uses LiteLLM to route requests, and the `openai/` prefix tells it to use the OpenAI-compatible protocol your LiteLLM proxy speaks. Without it, validation will fail.
>
> **`openai/llama4:scout`** ✓    `llama4:scout` ✗
>
> Same for other models: **`openai/llama3.1:70b`**, **`openai/qwen3:32b`**, etc.

### Adding web search (optional)

Serper gives DiscoGen access to live web results alongside your domain data. Useful for enriching companies with recent news, funding rounds, or hiring signals.

1. Grab an API key from [serper.dev](https://serper.dev). A paid plan is recommended as the free tier has strict rate limits that will slow down DiscoGen batch processing.

2. Go to **Settings → Integrations → Search Providers → Add**

| Field | Value |
|-------|-------|
| Provider | **Serper** |
| Integration Name | e.g. **`serper`** |
| API Key | Your Serper key |
| Search Model | **`serper/search`** (auto-populated) |

3. Click **Save**. DiscoLike validates with a test search.

### Running DiscoGen

Open **DiscoGen** and select your self-hosted model from the **Model** dropdown. If you added Serper, toggle **Enable web search**, pick a **Search Depth**, and select your provider under **Search Source**.

Hit **Submit**. DiscoGen sends each domain through your model and streams results into the table.

## Setting up a named tunnel

For a persistent subdomain that survives restarts, replace the quick tunnel with a named one:

```bash
cloudflared tunnel login
cloudflared tunnel create discolike-llm
cloudflared tunnel route dns discolike-llm llm.yourdomain.com
cloudflared tunnel run --url http://localhost:4000 discolike-llm
```

Then update your **Base URL** in the DiscoLike integration to `https://llm.yourdomain.com`.

## Managing your stack

```bash
docker compose up -d                # Start everything
docker compose down                  # Stop everything
docker compose logs -f               # Follow logs
docker compose logs cloudflared      # Get current tunnel URL
docker exec ollama ollama list       # List installed models
docker exec ollama ollama pull qwen3:32b  # Pull another model
```

Switching models? Edit `litellm-config.yaml`, run `docker compose restart litellm`, and update the **Model Name** in DiscoLike (with the `openai/` prefix).

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Validation fails | Model name must start with **`openai/`**. Base URL must **not** end with `/v1` |
| Model won't load | `nvidia-smi`. If VRAM is full, re-run `./setup.sh` and pick a smaller model |
| LiteLLM returns 500 | `docker compose logs litellm --tail 50`. Usually Ollama is still loading |
| Tunnel unreachable | `docker compose logs cloudflared`. If the URL changed, update DiscoLike |

Quick validation test from your terminal:

```bash
curl https://your-tunnel-url/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "llama4:scout", "messages": [{"role": "user", "content": "hi"}], "max_tokens": 5}'
```

If this returns a response, the stack is working. Check your DiscoLike configuration if validation still fails.
