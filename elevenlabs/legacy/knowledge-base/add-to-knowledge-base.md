# Add To Knowledge Base API Documentation

## Endpoint Overview

This endpoint enables uploading files or webpage URLs to create knowledge base documents for ElevenLabs conversational AI agents.

**URL:** `POST https://api.elevenlabs.io/v1/convai/knowledge-base`

**Content-Type:** `multipart/form-data`

## Key Details

The documentation notes that "After creating the document, update the agent's knowledge base by calling Update agent."

## Request Parameters

**Query Parameters:**
- `agent_id` (optional): string identifier for the target agent

**Headers:**
- `xi-api-key` (optional): authentication key

**Form Data:**
- `name` (string): human-readable label for the document
- `url` (string): webpage URL containing documentation the agent can access
- `file` (binary): documentation file the agent will reference

## Response

Success returns HTTP 200 with schema containing:
- `id`: document identifier
- `name`: the provided name
- `folder_path`: array of folder segments from root to parent

Validation errors return HTTP 422.

## SDK Examples

Implementations provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating multipart form submission patterns across various programming languages and HTTP client libraries.
