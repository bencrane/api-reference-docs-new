# Handoff Tool Documentation

## Overview

The handoff tool enables seamless call transfers between assistants in multi-agent systems. According to the documentation, you can "Transfer to a specific assistant by ID or by name (within a squad)" and "Determine the destination dynamically at runtime via a webhook."

## Key Configuration Patterns

### Single Destination Handoff

The tool supports two reference methods:
- **By Assistant ID**: Direct reference using a unique identifier
- **By Assistant Name**: References squad members by their assigned name

### Multiple Destination Approaches

The documentation distinguishes two recommended patterns:

1. **OpenAI Recommended**: "creates separate tool definitions for each destination"
2. **Anthropic Recommended**: "single tool with multiple destination options"

## Context Engineering Options

Four context transfer types are available:

- **All**: Transfers entire conversation history
- **Last N Messages**: Limits to most recent N messages for performance
- **User and Assistant Messages Only**: Filters out system messages and tool details
- **None**: Starts destination with blank conversation

## Advanced Features

### Variable Extraction

Variables can be extracted through two methods:
1. `variableExtractionPlan` in destinations using structured output
2. `tool.function` parameters for custom extraction

Extracted variables use Liquid template syntax (e.g., `{{variableName}}`) for access.

### Dynamic Handoffs

The system supports runtime destination determination via webhook. The server responds with destination configuration and can reject handoffs with custom error messages.

### Squad Destinations

Handoffs can transfer entire conversations to multi-agent squads, either by saved squad ID or transient inline definition.

## Tool Messages Configuration

Four message types control caller experience:
- `request-start`: Triggers when handoff begins
- `request-complete`: Triggers on successful transfer
- `request-failed`: Triggers on transfer failure
- `request-response-delayed`: Triggers during server delays

## Rejection Planning

Handoffs can be prevented based on conversation state using:
- **Regex conditions**: Match message content patterns
- **Liquid conditions**: Complex template-based logic
- **Group conditions**: Combined AND/OR logic across conditions

## Best Practices Summary

Key recommendations include: writing specific destination descriptions, limiting context size for performance, optimizing for model type, extracting key data before handoff, customizing tool messages, thorough testing of edge cases, and enabling artifact capture for monitoring.
