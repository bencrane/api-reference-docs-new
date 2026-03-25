# Update test

## Endpoint Overview

The **Update test** endpoint allows you to modify an existing agent response test using a PUT request to `https://api.elevenlabs.io/v1/convai/agent-testing/{test_id}`.

## Request Details

**Method:** PUT
**Content-Type:** application/json
**Path Parameter:** `test_id` (string, required) - The identifier of the chat response test returned upon creation

**Optional Header:**
- `xi-api-key` - API authentication key

## Request Body

The request accepts three discriminated test types via the `type` field:

### LLM Test Type
Evaluates agent responses against success criteria:
- `type`: "llm" (required)
- `name`: string (required)
- `dynamic_variables`: object with string/number/integer/boolean values
- `chat_history`: array of conversation transcripts
- `success_condition`: prompt evaluating True/False responses
- `success_examples`: non-empty array of successful response examples
- `failure_examples`: non-empty array of failure response examples
- `from_conversation_metadata`: optional metadata including conversation_id and agent_id

### Tool Test Type
Validates tool call execution:
- `type`: "tool" (required)
- `name`: string (required)
- `tool_call_parameters`: evaluation criteria for tool invocation
- `check_any_tool_matches`: boolean to match any tool call against criteria
- Supports dynamic variables and chat history configuration

### Simulation Test Type
Runs multi-turn conversation simulations:
- `type`: "simulation" (required)
- `name`: string (required)
- `simulation_scenario`: scenario and user persona description
- `simulation_max_turns`: integer (default: 5)
- `simulation_environment`: defaults to 'production' if not provided
- `success_condition`: evaluation prompt

## Response

**Success Status:** 200 OK

Returns the updated test object containing:
- `id`: test identifier
- `type`: the test type (llm, tool, or simulation)
- `name`: test name
- All submitted configuration fields
- Complete conversation history with metadata

**Error Status:** 422 Unprocessable Entity

Returns validation errors with details about malformed requests.

## Code Examples

Multiple SDK implementations are available across TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
