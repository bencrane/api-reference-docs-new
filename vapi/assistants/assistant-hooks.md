# Assistant Hooks Documentation

## Overview

Assistant hooks automate actions during calls by responding to specific events. These include call endings, speech interruptions, timeouts, and low-confidence transcripts. Hooks support combining multiple actions with optional filters to control triggering behavior.

## Supported Events

The documentation lists five event types:

- **call.ending**: Triggered when a call concludes
- **assistant.speech.interrupted**: Occurs when customer interrupts the assistant
- **customer.speech.interrupted**: Occurs when assistant interrupts customer
- **customer.speech.timeout**: Triggered when customer remains silent beyond a threshold
- **assistant.transcriber.endpointedSpeechLowConfidence**: Occurs for low-confidence transcripts

## Hook Structure

Each hook contains:

- `on`: The triggering event
- `do`: Actions to execute (supports "tool" and "say" types)
- `filters`: Optional conditions for triggering
- `options`: Configuration for specific hook types
- `name`: Optional identifier

## Action Types

**Say**: Produces speech using either `exact` (predetermined text) or `prompt` (AI-generated responses).

**Tool**: Executes functions including call transfers, function invocations, and call termination.

## Key Configuration Examples

The documentation provides templates for: transferring calls on pipeline errors, combining multiple actions, handling interruptions, managing customer timeouts, and processing low-confidence transcripts.

For `customer.speech.timeout` hooks, configurable options include timeout duration (1-1000 seconds), maximum trigger count (1-10), and reset behavior.

## Low Confidence Transcript Handling

The `assistant.transcriber.endpointedSpeechLowConfidence` hook addresses borderline transcripts. It supports confidence range configuration via `confidenceMin` and `confidenceMax` parameters, with shorthand syntax available: `[confidence=min:max]`.

Multiple hooks can target different confidence ranges for tailored responses.

## Practical Use Cases

Common applications include: agent escalation on errors, graceful interruption handling, unresponsiveness detection, error logging, and Slack integration for call failure notifications.
