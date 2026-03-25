# Silent Handoffs

## Overview

Silent handoffs enable seamless transitions between AI assistants without interrupting the caller experience. Rather than announcing transfers verbally, the conversation continues naturally across multiple agents.

## The Core Problem and Solution

**Issue**: Traditional AI call flows announce handoffs verbally, which disrupts the conversation flow and may confuse callers.

**Resolution**: Silent handoffs maintain continuity by keeping transfers invisible to the user, creating "one continuous conversation" even when multiple assistants are involved.

## Implementation Steps

### 1. Configure the Destination Assistant's First Message
- Set `firstMessage` to an empty string
- Set `firstMessageMode` to `assistant-speaks-first-with-model-generated-message`

### 2. Adjust Squad Handoff Messages
- For all `members[*].model.tools/toolIds`, unset or null the `messages` property

### 3. Initiate Transfer from Source Assistant
Include in the source assistant's prompt: "trigger the 'handoff' tool with '[Assistant Name]' Assistant"

### 4. Guide the Destination Assistant
Add instruction to the destination assistant's prompt: "Proceed directly to the Task section without any greetings or small talk"

## Example Workflow

A practical scenario demonstrates the flow:
- **HPMA** (Main Assistant) confirms order details, then hands off invisibly
- **HPPA** (Payment Assistant) collects payment without announcing the transition
- **HPMA-SA** (Sub Assistant) arranges shipping silently
- The customer perceives one unified interaction throughout

## JSON Configuration Example

```json
{
  "members": [
    {
      "name": "HPMA (Main Assistant)",
      "model": {
        "provider": "openai",
        "model": "gpt-4o",
        "tools": [
          {
            "type": "handoff",
            "destinations": [
              {
                "type": "assistant",
                "assistantName": "HPPA"
              }
            ],
            "messages": []
          }
        ]
      }
    }
  ],
  "name": "HP Payment Squad With SubAgent"
}
```

**Critical Note**: Ensure all `members[*].model.tools.messages` properties are null or empty arrays.

## Assistant Configuration Details

### HPMA (Main Assistant)
- Voice provider: Cartesia
- Model: GPT-4o with 50 token limit
- Temperature: 0.3
- Transcriber: Deepgram Nova-2
- Key setting: Empty `firstMessage` with model-generated mode enabled

### HPPA (Payment Assistant)
Handles secure payment collection with similar configuration, transitions to HPMA-SA upon completion.

### HPMA-SA (Sub Assistant)
Manages final shipping details and closes the interaction professionally.

## Prompt Guidelines

Each assistant's system prompt includes:
- **Identity**: Role and purpose definition
- **Context**: Relevant operational boundaries
- **Style**: Tone and communication approach
- **Response Guidelines**: Behavioral constraints (avoid mentioning "functions," "tools," "transferring," or call endings)
- **Task**: Step-by-step workflow with handoff triggers

Key instruction for non-initial assistants: "proceed to the Task section without any greetings or small talk" prevents awkward greeting repetition.

## Benefits

Silent handoffs deliver:
- Uninterrupted customer experience
- Enhanced satisfaction through natural conversation flow
- Seamless multi-agent coordination
- Professional call handling without technical jargon exposure
