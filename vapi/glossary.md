# Vapi Voice AI Glossary

## Overview
This documentation provides definitions for essential terminology related to Vapi and voice AI applications, organized alphabetically from A-W.

## Key Definitions Summary

**Pricing & Costs:**
The platform charges "at-cost" (without markup) for STT, LLM, and TTS provider requests.

**Communication Concepts:**
- *Backchanneling* involves listener feedback like "yeah" or "hmm" during conversations
- *Speech Endpointing* detects where speech starts and ends using silence detection and machine learning
- *Voice-to-Voice* latency measures response time from user speech completion to AI agent's first audio output (ideal: <1 second)

**Call Types:**
- *Inbound calls* arrive at the assistant from external callers
- *Outbound calls* originate from the assistant to target numbers

**Technical Terms:**
- *STT* (Speech-to-text): Converting audio to transcript text
- *TTS* (Text-to-speech): Converting text to playable audio
- *LLM* (Large Language Model): Machine learning models generating text probabilistically
- *Inference*: Running prompts through an LLM for output
- *SDK*: Pre-packaged developer libraries and tools
- *Server URL*: Bidirectional endpoints receiving and responding with conversation data
- *Webhook*: Traditional unidirectional data-receiving endpoints

**Compliance:**
The Telemarketing Sales Rule (TSR) requires explicit consent before making outbound calls and carries potential civil or criminal penalties for violations.
