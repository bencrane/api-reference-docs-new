# HIPAA Compliance Documentation Summary

## Key Overview

Vapi provides privacy protections for voice assistant users handling sensitive health information. The platform allows organizations to enable HIPAA compliance through a simple configuration setting.

## Core Compliance Features

**Enabling HIPAA Mode:** Organizations can set `hipaaEnabled: true` in their assistant configuration to prevent storage of call logs, recordings, and transcriptions. As the documentation states, this approach ensures "no call logs, recordings, or transcriptions are stored during or after your calls."

## Provider Requirements

When HIPAA compliance is active, only certified providers may be used:
- **LLM Models:** OpenAI, Azure OpenAI, Anthropic, Google, Together AI
- **Voice (TTS):** Vapi, ElevenLabs, Cartesia, Rime AI, Deepgram, Azure
- **Transcription (STT):** Azure, Deepgram

## PHI Usage Guidelines

Protected health information can only pass through the `/call` endpoint during voice processing. The documentation emphasizes that "you should not put PHI in an `/assistant` prompt or in a `/phone-number` label."

## Structured Output Handling

Organizations can selectively store non-sensitive structured outputs (like appointment confirmations or satisfaction scores) using the `forceStoreOnHipaaEnabled` setting, but must never store actual protected health data this way.

## Organizational Responsibility

Under the Business Associate Agreement, organizations remain responsible for not introducing PHI through prohibited channels and ensuring all third-party provider accounts maintain HIPAA compliance.
