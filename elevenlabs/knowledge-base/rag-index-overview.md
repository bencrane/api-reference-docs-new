# Get RAG Index Overview

## Endpoint Details

The API provides a GET endpoint at `https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index` that "Provides total size and other information of RAG indexes used by knowledgebase documents."

## Request Parameters

The endpoint accepts an optional header parameter:
- **xi-api-key** (header, optional): API authentication key

## Response Schema

Successful responses (HTTP 200) return a `RagIndexOverviewResponseModel` containing:

| Field | Type | Description |
|-------|------|-------------|
| total_used_bytes | integer | Total bytes currently used |
| total_max_bytes | integer | Maximum bytes available |
| models | array | Embedding model information array |

Each model object in the array includes:
- **model**: One of three embedding options (e5_mistral_7b_instruct, multilingual_e5_large_instruct, or qwen3_embedding_4b)
- **used_bytes**: Storage consumed by that specific model

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Implementation Examples

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call this endpoint across different programming languages and frameworks.
