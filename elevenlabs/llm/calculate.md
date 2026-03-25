# Calculate Expected LLM Usage

## Overview
The ElevenLabs API provides an endpoint to calculate expected costs for different LLM models based on specific parameters.

## Endpoint Details

**POST** `https://api.elevenlabs.io/v1/convai/llm-usage/calculate`

This endpoint "Returns a list of LLM models and the expected cost for using them based on the provided values."

## Request Parameters

The request body requires three fields:

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt_length` | integer | Length of the prompt in characters |
| `number_of_pages` | integer | Pages of content in PDF documents or URLs in knowledge base |
| `rag_enabled` | boolean | Whether RAG is enabled |

## Response

The endpoint returns an object containing:
- `llm_prices`: An array of objects, each with:
  - `llm`: The model identifier
  - `price_per_minute`: Numerical cost value

## Supported LLM Models

The API supports numerous models including:
- GPT series (GPT-4o, GPT-4, GPT-4-Turbo, GPT-5 variants)
- Claude series (Sonnet, Haiku variants)
- Gemini series (various versions and variants)
- Specialized models (Qwen, Grok, custom LLMs)

## Regional Endpoints

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Support

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
