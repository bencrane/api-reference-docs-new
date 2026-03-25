# Stream Simulate Conversation

## Overview

The **Stream Simulate Conversation** endpoint allows you to run a conversation between an agent and a simulated user, with responses streamed back in real-time.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/simulate-conversation/stream`

## Key Characteristics

- Streams partial message lists that should be concatenated
- Sends a final message containing conversation analysis upon completion
- Requires an `agent_id` path parameter
- Accepts optional `xi-api-key` header for authentication

## Request Parameters

### Required Fields

**simulation_specification** (ConversationSimulationSpecification)
Specifies how the conversation should be simulated, including the simulated user configuration.

### Optional Fields

- **extra_evaluation_criteria** (array): Additional evaluation criteria to assess the conversation
- **new_turns_limit** (integer, default: 10000): Maximum number of conversation turns to generate

## Response Format

The API returns streamed responses as:
1. Partial message lists (concatenate these as they arrive)
2. A final message containing complete conversation analysis

## Usage Examples

### TypeScript/JavaScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const client = new ElevenLabsClient();
await client.conversationalAi.agents.simulateConversationStream(
  "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
  {
    simulationSpecification: {
      simulatedUserConfig: {
        firstMessage: "Hello, how can I help you today?",
        language: "en",
        disableFirstMessageInterruptions: false,
      },
    },
  }
);
```

### Python
```python
from elevenlabs import ElevenLabs, ConversationSimulationSpecification, AgentConfig

client = ElevenLabs()
client.conversational_ai.agents.simulate_conversation_stream(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    simulation_specification=ConversationSimulationSpecification(
        simulated_user_config=AgentConfig(
            first_message="Hello, how can I help you today?",
            language="en",
            disable_first_message_interruptions=False,
        ),
    ),
)
```

## Configuration Options

The `SimulationSpecification` supports:
- **simulated_user_config**: Agent configuration for the simulated user
- **tool_mock_config**: Mock configurations for tools (per-tool basis)
- **partial_conversation_history**: Existing conversation to build upon
- **dynamic_variables**: Variable values for simulation context

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
