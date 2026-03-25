# Fine-tuned OpenAI Models

## Overview

Vapi enables integration with any OpenAI-compatible endpoint as your language model, supporting services such as OpenRouter, AnyScale, Together AI, and self-hosted servers.

## When to Use Custom LLMs

According to the documentation, custom LLMs are beneficial for:
- Deploying open-source models like Mixtral
- Modifying context mid-conversation
- Pre-processing messages before LLM transmission

## LLM Provider Setup

To integrate a third-party LLM provider, first submit your credentials:

```json
{
  "provider": "openrouter",
  "apiKey": "<YOUR OPENROUTER KEY>"
}
```

Then configure your assistant:

```json
{
  "name": "My Assistant",
  "model": {
    "provider": "openrouter",
    "model": "cognitivecomputations/dolphin-mixtral-8x7b",
    "messages": [
      {
        "role": "system",
        "content": "You are an assistant."
      }
    ],
    "temperature": 0.7
  }
}
```

## Fine-Tuned OpenAI Model Configuration

Implementation requires:
1. Setting the custom LLM URL to `https://api.openai.com/v1`
2. Using your OpenAI API key
3. Specifying your fine-tuned model identifier
4. Sending a PATCH request with `model.metadataSendMode` disabled

## Self-Hosted Server Implementation

Your endpoint must align with OpenAI's API specifications and ideally support streaming. For authenticated servers, register credentials via the `/credential` endpoint:

```json
{
  "provider": "custom-llm",
  "apiKey": "<YOUR SERVER API KEY>"
}
```

Create your assistant configuration:

```json
{
  "name": "My Assistant",
  "model": {
    "provider": "custom-llm",
    "url": "<YOUR OPENAI COMPATIBLE ENDPOINT BASE URL>",
    "model": "my-cool-model",
    "messages": [
      {
        "role": "system",
        "content": "You are an assistant."
      }
    ],
    "temperature": 0.7
  }
}
```
