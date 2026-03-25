# Get Test Invocation

## Endpoint Overview

The Get Test Invocation endpoint retrieves detailed information about a specific test invocation using its ID. This endpoint is part of the ElevenLabs Conversational AI testing suite.

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/test-invocations/{test_invocation_id}`

## Key Parameters

- **test_invocation_id** (path, required): The identifier for a test invocation, which is provided when tests are executed
- **xi-api-key** (header, optional): Your API authentication key

## Response Structure

The endpoint returns a `GetTestSuiteInvocationResponseModel` containing:

- **id**: The test invocation identifier
- **agent_id**: Associated agent identifier
- **branch_id**: Optional branch identifier
- **created_at**: Unix timestamp of creation
- **folder_id**: Optional folder organization identifier
- **test_runs**: Array of `UnitTestRunResponseModel` objects with comprehensive test execution data

## Test Run Details

Each test run includes:
- Test status (pending, passed, failed)
- Agent responses with conversation history
- Tool calls and their results
- Test condition evaluations with detailed rationale
- Dynamic variables used during testing
- Performance metrics and timestamps

## Available Servers

The API is accessible through multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
