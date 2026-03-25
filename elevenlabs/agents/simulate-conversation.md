# Simulate Conversation API Documentation

## Endpoint Overview

The Simulate Conversation endpoint allows you to run a conversation between an agent and a simulated user for testing purposes.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation`

## Request Parameters

### Path Parameters
- **agent_id** (required, string): The identifier of the agent returned upon creation

### Header Parameters
- **xi-api-key** (optional, string): API authentication key

### Request Body

The request accepts a JSON payload with the following structure:

**simulation_specification** (required): Details how the conversation should be simulated, including:
- `simulated_user_config`: Agent configuration for the simulated user
- `tool_mock_config`: Mock configurations for tools (optional)
- `partial_conversation_history`: Starting conversation context (optional)
- `dynamic_variables`: Variable values for the simulation (optional)

**extra_evaluation_criteria** (optional, array): List of evaluation criteria to test the agent's performance

**new_turns_limit** (optional, integer, default: 10000): Maximum conversation turns to generate

## Response Format

A successful response (HTTP 200) returns an `AgentSimulatedChatTestResponseModel` containing the complete simulation results.

## Error Handling

The API returns validation errors (HTTP 422) for malformed requests with detailed error information.

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Key Configuration Options

**Simulated User Configuration** includes:
- First message prompt
- Language selection
- Dynamic variable assignments
- Interruption behavior settings

**Evaluation Criteria** allows testing whether conversations achieve specific goals using prompt-based evaluation.
