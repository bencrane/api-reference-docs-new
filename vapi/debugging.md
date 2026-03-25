# Debugging Voice Agents Documentation

## Overview

Voice assistants integrate multiple AI systems—speech recognition, language models, and voice synthesis. When issues arise, systematic debugging helps identify and resolve root causes quickly.

Common problems fall into two categories:
- **Speech & Understanding**: Comprehension errors, inappropriate responses, unnatural-sounding output
- **Technical & Integration**: Audio quality problems, tool failures, workflow logic issues

## Quick Diagnostics

The documentation recommends starting with these immediate checks:

**1. Dashboard Testing**
"Test your voice agent directly in the dashboard" by using the "Talk to Assistant" or "Call" features. This eliminates network variables and provides real-time transcript visibility.

**2. Review Logs**
Access the Observe section to review Call Logs (transcripts and errors), API Logs (integration issues), and Webhook Logs (delivery verification).

**3. Component Testing**
Use Voice Test Suites for automated assistant testing and Tool Testing for individual tool validation with sample data.

**4. Provider Status Verification**
Check status pages for Vapi, OpenAI, Anthropic, ElevenLabs, Deepgram, and Gladia for service outages.

## Debugging Categories

### Speech and Language Issues
Address transcription accuracy through transcriber selection, improve intent recognition with more specific prompts, and enhance response quality by adjusting temperature settings and model configuration.

### Tool and Workflow Problems
Debug tool execution through Call Logs, resolve variable extraction by using clearer descriptions and distinct enum values, and trace workflow logic issues using conversation path analysis.

### Common Error Patterns

| Issue | Cause | Solution |
|-------|-------|----------|
| Misinterpreted speech | Recognition problems | Verify transcriber model |
| Irrelevant responses | Weak prompting | Refine system prompt specificity |
| Immediate call drops | Configuration errors | Validate all required fields |
| Tool failures | API integration issues | Test tools individually |
| Extended silence | Processing delays | Use faster models |

## Support Resources

The documentation directs users to the Vapi Discord community, API reference documentation, and the status page for ongoing assistance.
