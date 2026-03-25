# Data Flow Documentation

## Overview
Vapi's data architecture separates customer-accessible call data from internal operational logs. Understanding this distinction is crucial for organizations prioritizing data control and compliance.

## Key Data Classification

The platform generates two log categories:

**System Logs** remain "strictly internal to Vapi and are never shared with customers or uploaded to custom storage buckets." These support infrastructure monitoring only.

**Call Logs** encompass conversation transcripts, recordings, and metadata—all accessible via API and dashboard, with optional custom bucket upload.

## Pipeline Architecture

Vapi orchestrates voice conversations through modular, configurable components:

1. **Transport Layer** - Audio streaming via SIP, Telephony, WebSocket, or WebRTC
2. **Speech-to-Text** - Real-time transcription (supports custom integrations)
3. **Orchestration** - Proprietary endpointing, interruption detection, emotion analysis, and backchanneling (non-customizable, runs on Vapi infrastructure)
4. **Language Model** - Response generation via configurable providers
5. **Text-to-Speech** - Audio synthesis with bring-your-own-key support

## Storage Options

**Default Configuration:** Recordings, transcripts, and call logs stored on Vapi infrastructure.

**Custom Storage:** Call artifacts upload to AWS S3, GCP, Cloudflare R2, Supabase, or Azure Blob Storage, while system logs and usage metrics persist on Vapi's servers.

## Bring-Your-Own Infrastructure

- Transcriber: ✅ (via WebSocket or API keys)
- LLM: ✅ (OpenAI-compatible endpoints)
- Voice: ✅ (audio streaming endpoints)
- Orchestration: ❌ (Vapi exclusive)
- Storage: ✅ (multiple cloud providers)

## HIPAA Considerations

When enabling HIPAA mode without custom storage, "Vapi will **not store** call recordings or transcripts." Organizations must configure custom buckets to retain sensitive data post-call.

## Ephemeral Processing

Orchestration models process audio in real-time without persistence. Only final transcripts and call logs are retained—unless HIPAA mode prevents even this storage.
