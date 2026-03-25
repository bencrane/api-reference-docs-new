# Custom Transcriber Documentation

## Overview
The guide explains how to integrate your own transcription service with Vapi instead of relying on built-in providers. This approach enables developers to "stream audio from Vapi to your server" and "forward audio to Deepgram for transcription," returning real-time transcripts back.

## Key Benefits
According to the documentation, custom transcribers offer several advantages:
- **Flexibility** to work with preferred services
- **Control** for specialized processing unavailable with standard providers
- **Cost efficiency** by leveraging existing infrastructure
- **Customization** of audio handling and formatting

## Implementation Workflow

The process involves four main steps:

1. **Connection initialization** — Vapi establishes a WebSocket connection and sends a JSON message specifying audio encoding (linear16), sample rate (16000 Hz), and channel count

2. **Audio streaming** — Binary PCM audio data flows continuously to your server

3. **Transcription processing** — Your server forwards audio to Deepgram, which processes it and returns transcript events with channel identification

4. **Response** — Transcripts return to Vapi as JSON with fields for transcription text, channel identification ("customer" or "assistant"), and transcript type ("final" or "partial")

## Technical Setup Requirements

The implementation requires Node.js with dependencies including WebSocket support, Express, and the Deepgram SDK. The code demonstrates handling multi-channel audio with debouncing (3-second delays) to manage partial and final transcripts separately.

## Authentication & Security

The documentation notes that secure endpoints should use Custom Credentials with credential IDs for managing "Bearer Token, OAuth 2.0, or HMAC authentication." A legacy `secret` field sends values as HTTP headers for backward compatibility.

## Important Limitations

The service requires streaming support, proper stereo PCM validation, and channel detection using Deepgram's response format. Partial transcripts can update progressively until final confirmation arrives.
