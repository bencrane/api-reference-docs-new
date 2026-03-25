# Get Conversation Details

This API endpoint retrieves detailed information about a specific conversation from the ElevenLabs Conversational AI service.

## Endpoint Overview

**Request Method:** GET
**URL:** `https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}`

The endpoint is designed to fetch comprehensive conversation data, including transcripts, metadata, analysis results, and call metrics.

## Required Parameters

- **conversation_id** (path parameter): The identifier for the conversation being retrieved

## Optional Parameters

- **xi-api-key** (header): API authentication key

## Response Structure

A successful request returns a `GetConversationResponseModel` containing:

- **agent_id**: Identifier of the agent used
- **agent_name**: Human-readable agent name
- **status**: Current conversation state (initiated, in-progress, processing, done, or failed)
- **conversation_id**: Unique conversation identifier
- **metadata**: Comprehensive call information including duration, timestamps, costs, and deletion settings
- **analysis**: Evaluation criteria results, data collection outputs, and call summaries
- **transcript**: Array of conversation turns with messages, tool calls, and feedback
- **has_audio/has_user_audio/has_response_audio**: Audio availability flags
- **environment**: Deployment environment (default: production)

## Implementation Examples

The documentation provides code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for straightforward GET request implementation across multiple programming languages and frameworks.

## Error Handling

Status code 422 indicates validation errors with detailed error information provided in the response body.
