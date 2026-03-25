# Delete Test API Documentation

## Endpoint Overview

The ElevenLabs API provides a DELETE endpoint for removing agent response tests: `DELETE https://api.elevenlabs.io/v1/convai/agent-testing/{test_id}`

This operation removes "an agent response test by ID."

## Key Parameters

The endpoint requires a single path parameter:
- **test_id**: A string identifier for the test to be deleted, which is provided upon test creation

An optional header parameter `xi-api-key` can be included for authentication.

## API Response

- **Success (200)**: Returns a successful response with JSON content
- **Error (422)**: Validation errors are returned with detailed error information including location, message, and error type

## Implementation Examples

The documentation provides code samples across multiple programming languages:

**TypeScript/JavaScript** uses the ElevenLabs SDK: `client.conversationalAi.tests.delete("TeaqRRdTcIfIu2i7BYfT")`

**Python** implementation: `client.conversational_ai.tests.delete(test_id="TeaqRRdTcIfIu2i7BYfT")`

Additional examples are provided for Go, Ruby, Java, PHP, C#, and Swift, all demonstrating standard HTTP DELETE requests to the specified endpoint with the test ID embedded in the URL path.
