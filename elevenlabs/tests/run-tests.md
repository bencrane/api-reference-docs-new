# Run Tests on Agent

## Endpoint Overview

**POST** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/run-tests`

This endpoint executes selected tests on a conversational AI agent, with optional configuration overrides.

## Purpose

"Run selected tests on the agent with provided configuration. If the agent configuration is provided, it will be used to override default agent configuration."

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `agent_id` | string | Yes | The identifier of the agent returned upon creation |

## Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `xi-api-key` | string | No | API authentication key |

## Request Body

The request accepts a JSON object with the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tests` | array | Yes | List of test configurations to execute |
| `agent_config_override` | object | No | Configuration modifications for testing purposes |
| `branch_id` | string | No | Branch identifier; uses default if omitted |

### Tests Array Schema

Each test object requires:
- `test_id` (string, required): Identifier of the test
- `workflow_node_id` (string, optional): Target workflow node
- `root_folder_id` (string, optional): Target folder by ID
- `root_folder_name` (string, optional): Target folder by name

## Response

**Status 200:** Returns a `GetTestSuiteInvocationResponseModel` containing test execution results.

**Status 422:** Returns validation error details.

## API Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
