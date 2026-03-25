# OpenAI Realtime API Documentation

## Overview
The OpenAI Realtime API enables developers to build voice assistants using native speech-to-speech models. Unlike traditional Vapi configurations that combine separate transcription, language, and voice services, this API "natively processes audio in and audio out."

## Available Models

Three production and preview models are offered:

| Model | Status | Use Case |
|-------|--------|----------|
| `gpt-realtime-2025-08-28` | Production | Production workloads |
| `gpt-4o-realtime-preview-2024-12-17` | Preview | Development & testing |
| `gpt-4o-mini-realtime-preview-2024-12-17` | Preview | Cost-sensitive apps |

## Voice Options

**Standard voices** (all models): alloy, echo, shimmer

**Realtime-exclusive voices**: marin, cedar

**Unsupported voices**: ash, ballad, coral, fable, onyx, nova

## Key Implementation Points

- System messages are automatically converted to session instructions during WebSocket initialization
- Function calling configurations remain unchanged from traditional models
- Configuration supports temperature (0.5-0.7 recommended) and token limits (200-300 suggested)

## Prompting Best Practices

Effective prompts should use:
- Bullet points over lengthy paragraphs
- Clear, concise sections (Role, Personality, Instructions, Tools, Safety)
- Specific pacing and personality guidance
- Conversation flow structures

## Current Limitations

Knowledge bases, custom voice cloning, and transcription customization are not supported with the Realtime API.

## Migration Steps

1. Update model provider to realtime variant
2. Verify voice compatibility
3. Remove transcriber configuration
4. Retain existing function calling setup
5. Optimize prompts for realtime processing
