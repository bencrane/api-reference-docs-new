# Frequently Asked Questions

## Overview
Vapi is a voice AI platform designed for developers building conversational applications. The FAQ addresses common questions about suitability, customization, costs, setup, and enterprise features.

## Key Topics Covered

**Use Case Suitability**
Vapi targets developers creating "voice AI applications simulating human conversation" using LLMs, ranging from turn-based scenarios like appointment booking to complex agentic assistants.

**Customization & Flexibility**
The platform supports custom models across its pipeline (text-to-speech, LLM, speech-to-text). Users can either integrate hosted models through provider keys or deploy external models via custom LLM endpoints.

**Cost Considerations**
While building in-house is possible, Vapi emphasizes the substantial engineering challenges in real-time voice applications. The platform charges minimal fees above provider costs (Deepgram, OpenAI, ElevenLabs), focusing on orchestration rather than model provision.

**Implementation**
Setup is straightforward—minutes via dashboard or single-line code with client SDKs. Advanced features like function calling require a server URL.

**Performance & Enterprise Features**
- Latency: ~800 milliseconds end-to-end
- Concurrency: Supports 1000+ concurrent sessions
- Compliance: HIPAA, SOC 2 Type II, GDPR
- Security: Encryption in transit/at rest, access controls, audit logging
- Options: White-labeling (API-first), on-premise deployment, multi-tenancy support

**Differentiation**
Vapi emphasizes low latency, high reliability, and developer-focused tooling compared to competing voice AI platforms.
