# Compute RAG Index

## Endpoint Overview

The Compute RAG Index endpoint is a POST request to `https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index`. This API triggers indexing for documents lacking RAG processing or returns current status for those already indexed.

## Key Parameters

**Path Parameter:**
- `documentation_id` (required): The document identifier returned upon knowledge base document addition

**Request Body:**
- `model` (required): Embedding model selection with options including `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`, and `qwen3_embedding_4b`

**Optional Header:**
- `xi-api-key`: API authentication key

## Response Schema

Success responses (HTTP 200) return a `RagDocumentIndexResponseModel` containing:
- Document identifier
- Selected embedding model
- Processing status (new, created, processing, failed, succeeded, or various error states)
- Progress percentage as a numeric value
- Usage metrics tracking indexed byte consumption

## Available Embedding Models

Three embedding options are provided:
- `e5_mistral_7b_instruct` (default)
- `multilingual_e5_large_instruct`
- `qwen3_embedding_4b`

## Status Values

The response includes one of eight possible status indicators: new, created, processing, failed, succeeded, rag_limit_exceeded, document_too_small, or cannot_index_folder.
