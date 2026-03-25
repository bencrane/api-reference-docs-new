# Flush Syntax Documentation

## Overview

The flush syntax is a VAPI audio control mechanism that "forces immediate transmission of LLM output to voice providers, eliminating buffering delays for real-time voice interactions."

Use flush syntax when you need to acknowledge requests immediately, provide feedback during long operations, create natural conversation pauses, or support custom LLM integrations with processing delays.

## How It Works

VAPI processes flush syntax through four steps:

1. **Detection** - The system scans LLM output using regex pattern matching
2. **Split** - Text divides at the flush position
3. **Immediate Send** - Content before flush transmits instantly to the voice provider
4. **Continue** - Remaining text follows standard buffering

## Syntax Formats

Three formats are supported with case-insensitive matching:

- `<flush />` (self-closing, recommended)
- `<flush>` (opening tag)
- `</flush>` (closing tag)

The regex pattern allows whitespace variations: `/<\s*flush\s*\/?>|<\s*\/\s*flush\s*>/i`

## Configuration Requirements

Flush requires this voice configuration:

```json
{
  "voice": {
    "chunkPlan": {
      "enabled": true
    }
  }
}
```

**Critical**: Flush will not function when `chunkPlan.enabled: false`—tags will appear in voice output instead of being processed.

## Usage Examples

- **Basic acknowledgment**: "I'm processing your request... <flush /> Let me check that for you."
- **Tool feedback**: "Looking up that information... <flush /> This may take a moment."
- **Conversation flow**: "That's a great question. <flush /> Based on the data I have..."

## Best Practices

**Use flush for:**
- Request acknowledgments
- Long-running operations feedback
- Natural conversation pauses
- Custom delays in external integrations

**Avoid flush for:**
- Every response (causes audio fragmentation)
- Mid-sentence placement (disrupts speech flow)
- Short responses (normal buffering suffices)
- Multiple instances per response (creates choppy audio)

## Troubleshooting

**Tags appearing in output**: Verify `chunkPlan.enabled: true` in configuration

**Unrecognized syntax**: Use exact formats without extra parameters or typos

**Choppy audio**: Reduce flush frequency and place only at sentence boundaries

## Related Resources

- Voice Formatting Plan - Control voice output formatting
- Background Messages - Send messages during conversations
- Custom Tools - Build tools leveraging flush feedback
