# Introduction to Vapi

## Overview
Vapi is described as "the developer platform for building voice AI agents," handling infrastructure complexity so developers can create quality voice experiences. The platform enables natural conversations, phone call capabilities, system integration, and complex workflows like scheduling and support.

## Core Technology Stack
Voice agents combine three technologies: speech-to-text (converting spoken language to text), large language models (processing conversations and generating responses), and text-to-speech (converting responses back to speech). The platform supports numerous providers including OpenAI, Anthropic, Google, Gladia, Deepgram, and ElevenLabs.

## Building Approaches

**Assistants** work best for most applications, using a single system prompt with tools and structured outputs. They suit customer support, lead qualification, and booking scenarios.

**Squads** orchestrate multiple specialized assistants with context-preserving transfers, ideal for medical triage, e-commerce routing, and property management.

## Key Features
- Sub-600ms response times for real-time conversations
- Inbound and outbound calling capabilities
- Web application embedding
- API and database connectivity
- Multi-assistant orchestration

## Getting Started Options

The platform offers two primary paths: phone call integration for customer support and sales automation, or web integration for embedding voice into existing applications. The Vapi CLI tool provides terminal-based access to platform features, installable via: `curl -sSL https://vapi.ai/install.sh | bash`

## Common Applications
Popular use cases include customer support automation, sales and lead qualification, appointment scheduling, medical triage, and e-commerce order management, with detailed examples available in the documentation.
