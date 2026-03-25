# Create Test

## Overview

The Create Test endpoint allows you to establish a new agent response test via POST to `https://api.elevenlabs.io/v1/convai/agent-testing/create`.

## Endpoint Details

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/convai/agent-testing/create`
**Content-Type:** `application/json`

## Request Body

The request accepts a discriminated union of three test types, all requiring a `type` and `name` field:

### Test Types

1. **LLM Test** (`type: "llm"`)
   - Evaluates agent responses against success/failure criteria
   - Optional: `success_condition`, `success_examples`, `failure_examples`
   - Supports `dynamic_variables` and `chat_history`

2. **Tool Test** (`type: "tool"`)
   - Validates tool calls and parameters
   - Includes `tool_call_parameters` for evaluation configuration
   - Features `check_any_tool_matches` flag for flexible matching

3. **Simulation Test** (`type: "simulation"`)
   - Runs multi-turn conversation simulations
   - Configurable via `simulation_scenario`, `simulation_max_turns` (default: 5)
   - Optional `simulation_environment` parameter

All test types support:
- `from_conversation_metadata`: Reference to source conversation
- `dynamic_variables`: Custom variable substitution
- `chat_history`: Conversation context
- `parent_folder_id`: Optional folder organization

## Response

**Status 200:** Returns `CreateAgentTestResponseModel` containing the test's `id` string.

**Status 422:** Validation error with detailed error information.

## Server Endpoints

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
