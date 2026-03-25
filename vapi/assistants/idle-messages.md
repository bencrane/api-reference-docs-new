# Idle Messages Documentation

## Overview

Idle messages are automatic prompts that engage users during conversation pauses. According to the documentation, they function through Assistant Hooks and "trigger on customer silence timeout" while supporting both exact messages and model-generated responses based on conversation history.

## Key Benefits

The feature addresses three main use cases:
- Re-engaging distracted users or those experiencing audio delays
- Reducing call abandonment during silent periods
- Providing proactive assistance when users hesitate

**Important note:** "Idle messages are automatically disabled during tool calls and warm transfers to avoid interrupting system processes."

## How It Works

The system operates in three stages:
1. **Detection** – Timer begins when user stops speaking
2. **Activation** – Retrieves an appropriate message for the user
3. **Reset** – Counter resets when user responds (optional)

## Configuration Parameters

| Setting | Range | Default |
|---------|-------|---------|
| Timeout | 1-1,000 seconds | 7.5 seconds |
| Max triggers per call | 1-10 | 3 |
| Reset mode | Never or on user speech | Never |

Messages can use exact strings or dynamic prompts. The `say.exact` field provides verbatim messages, while `say.prompt` generates responses using conversation context.

## Best Practices

**Recommended message tone:** Concise, encouraging language like "Are you still there?" or "I'm here whenever you're ready to continue."

**Timing guidelines:**
- Urgent transactions: 5-10 seconds
- Standard support: 10-20 seconds
- Complex discussions: 20-30 seconds

## Multilingual Support

The documentation suggests two approaches: creating language-specific assistants or using dynamic prompts that detect conversation language automatically.

## Troubleshooting

Common issues include messages not triggering (verify hook configuration), overly frequent messages (increase timeout duration), and max count reached too quickly (enable reset on user speech).
