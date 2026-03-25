# Get Settings API Documentation

## Endpoint Overview

The "Get settings" endpoint retrieves Convai settings for a workspace via a GET request to `https://api.elevenlabs.io/v1/convai/settings`.

## Request Details

**HTTP Method:** GET

**Base URL:** https://api.elevenlabs.io (with regional alternatives available)

**Optional Header:**
- `xi-api-key` (header parameter, not required)

## Response Structure

A successful 200 response returns a `GetConvAiSettingsResponseModel` object containing:

- **conversation_initiation_client_data_webhook** - webhook configuration for conversation initiation
- **webhooks** - post-call webhook settings including event types (transcript, audio, call_initiation_failure)
- **can_use_mcp_servers** - boolean indicating MCP server availability (defaults to false)
- **rag_retention_period_days** - retention period for RAG data (defaults to 10)
- **conversation_embedding_retention_days** - retention duration for conversation embeddings
- **default_livekit_stack** - either "standard" or "static" (defaults to standard)

## Error Response

A 422 response indicates validation errors with detailed error information.

## SDK Implementation

Official SDKs support this endpoint across multiple languages:
- **TypeScript:** `client.conversationalAi.settings.get()`
- **Python:** `client.conversational_ai.settings.get()`
- **Go, Ruby, Java, PHP, C#, Swift:** Raw HTTP implementations provided
