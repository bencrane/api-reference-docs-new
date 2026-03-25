# Custom Voices Documentation

## Overview

This page explains how to implement custom voices through supported providers in your assistant configuration.

## Configuration

To use a custom voice, set the `voice` property in your assistant configuration with your preferred provider:

```json
{
  "voice": {
    "provider": "deepgram",
    "voiceId": "your-voice-id"
  }
}
```

## Available Resources

The documentation provides setup guides for two primary voice providers:

- **ElevenLabs**: Instructions for configuring a custom ElevenLabs voice within Vapi
- **PlayHT**: Instructions for configuring a custom PlayHT voice within Vapi

Each provider has dedicated documentation covering their specific setup procedures and requirements.
