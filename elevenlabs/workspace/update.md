# Update Settings API Documentation

## Overview
This endpoint allows you to modify Convai settings for your workspace using a PATCH request to `https://api.elevenlabs.io/v1/convai/settings`.

## Request Details

**HTTP Method:** PATCH
**Content-Type:** application/json
**Authentication:** Optional xi-api-key header

## Configurable Parameters

The request body supports the following optional fields:

- **conversation_initiation_client_data_webhook** - Configuration for webhook notifications during conversation initialization, including URL and custom request headers
- **webhooks** - Settings for post-call webhooks with event types (transcript, audio, call_initiation_failure)
- **can_use_mcp_servers** - Boolean flag enabling MCP server usage (default: false)
- **rag_retention_period_days** - Data retention window in days (default: 10)
- **conversation_embedding_retention_days** - Embedding retention period; null uses system default of 30 days
- **default_livekit_stack** - Stack type selection: "standard" or "static" (default: standard)

## Response

A successful 200 response returns a `GetConvAiSettingsResponseModel` containing your updated configuration with all the same fields listed above.

## Error Handling

A 422 response indicates validation errors with detailed error information about invalid parameters.

## SDK Examples

Multiple language implementations are provided (TypeScript, Python, Go, Ruby, Java, PHP, C#, Swift), all demonstrating how to call the update endpoint with an empty or minimal configuration object.
