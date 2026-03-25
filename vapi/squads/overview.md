# Introduction to Squads (Multi-Assistant Conversations)

## Overview

Squads enable developers to decompose intricate workflows by distributing tasks across specialized assistants that seamlessly transition between one another. This architecture allows each assistant to focus on discrete responsibilities—such as initial lead qualification followed by appointment scheduling—while maintaining conversation continuity.

## Key Advantages

The documentation emphasizes three primary benefits:

- **Reduced hallucination** - Focused prompts with specific instructions minimize model confusion
- **Lower token consumption** - Shorter contexts decrease API costs per interaction
- **Faster response times** - Streamlined processing reduces overall latency

## Implementation

Squads are configured by defining a `squad` object with a `members` array containing persistent or transient assistants. The first member initiates the conversation. The system leverages [Handoff Tools](/tools/handoff) to manage transitions between squad members.

### Basic Configuration Example

```json
{
    "squad": {
        "members": [
            {
                "assistantId": "information-gathering-assistant-id"
            },
            {
                "assistant": {
                    "name": "Appointment Booking",
                    "model": {
                        "provider": "openai",
                        "model": "gpt-4o"
                    }
                }
            }
        ]
    }
}
```

## Customization Strategies

### Assistant-Level Adjustments

Use `assistantOverrides` to modify individual squad members without altering their base configuration. This proves valuable when standardizing voice characteristics across members or appending handoff-specific tools.

### Squad-Wide Modifications

Apply `memberOverrides` to establish uniform settings across all assistants simultaneously, such as consistent voice parameters.

## Recommended Practices

1. **Single responsibility principle** - Limit each assistant to 1-3 focused goals with minimal tool sets
2. **Compact team structure** - Reduce squad size; split responsibilities only at functional boundaries
3. **Explicit transition logic** - Document handoff triggers with precise conditions and required information
4. **Strategic context management** - Employ context engineering to control historical data passed between assistants, leveraging variable extraction for efficiency
