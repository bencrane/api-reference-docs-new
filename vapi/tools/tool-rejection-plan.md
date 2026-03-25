# Tool Rejection Plan

## Overview

A rejection plan is a mechanism to prevent tool execution based on conversation state conditions. When all specified conditions match, the tool call is rejected using AND logic. To implement OR logic at the top level, use a single group condition with `operator: "OR"`. An empty or omitted conditions array means the tool always executes.

## Core Condition Types

**RegexCondition** matches message content against patterns:
- `type`: "regex"
- `regex`: Pattern string with RegExp.test-style matching
- `target` (optional): Specifies which message to inspect by role and position
- `negate` (optional): Inverts the match result

**LiquidCondition** evaluates Liquid templates outputting "true" or "false":
- `type`: "liquid"
- `liquid`: Template accessing messages, now, and variables

**GroupCondition** combines multiple conditions:
- `type`: "group"
- `operator`: AND or OR
- `conditions`: Nested condition array supporting recursion

## Practical Applications

### Preventing Premature Call Termination

Block endCall unless the user explicitly says goodbye. "Match message content with a regex" to check for farewell keywords, negating the condition so rejection occurs when these phrases are absent.

### Guarding Against Accidental Transfers

Reject transfer requests containing question marks, ensuring users aren't transferred mid-inquiry. This prevents the tool from executing when a "?" appears in the most recent user message.

### Verifying Recent Context

Use Liquid templates to examine the last several messages, confirming users mentioned "transfer," "connect," or "representative" before allowing the tool to proceed.

### Complex Logic with Groups

Combine multiple regex patterns using OR logic within a group to reject based on several exclusion criteria simultaneously, then add AND conditions for additional safety checks.

## Implementation Notes

- Escape backslashes in JSON regex patterns (e.g., `\\b` represents word boundaries)
- Use `position: -1` for the most recent message; negative indices count backward
- Omit `role` to evaluate messages regardless of sender
- Attach rejectionPlan directly to tool definitions in assistant configuration
