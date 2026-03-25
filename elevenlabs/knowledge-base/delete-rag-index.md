# Delete RAG Index

## Endpoint Overview

The Delete RAG Index endpoint removes a RAG (Retrieval-Augmented Generation) index associated with a knowledge base document in ElevenLabs' Conversational AI system.

**Endpoint:** `DELETE https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index/{rag_index_id}`

## Path Parameters

- **documentation_id** (required, string): "The id of a document from the knowledge base. This is returned on document addition."
- **rag_index_id** (required, string): "The id of RAG index of document from the knowledge base."

## Optional Headers

- **xi-api-key** (optional, string): API authentication key

## Response Schema

A successful deletion returns a `RagDocumentIndexResponseModel` containing:

- **id** (string): Index identifier
- **model** (EmbeddingModelEnum): One of `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`, or `qwen3_embedding_4b`
- **status** (RagIndexStatus): Current state (new, created, processing, failed, succeeded, rag_limit_exceeded, document_too_small, or cannot_index_folder)
- **progress_percentage** (number): Completion percentage
- **document_model_index_usage** (object): Contains `used_bytes` metric

## HTTP Status Codes

- **200**: Successful deletion
- **422**: Validation error

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

The documentation includes SDK implementations for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
