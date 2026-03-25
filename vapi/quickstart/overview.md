# Core Models

## Overview

Vapi operates as "an orchestration layer over three modules: the **transcriber**, the **model**, and the **voice**."

The platform enables developers to select providers independently—OpenAI, Groq, Deepgram, ElevenLabs, PlayHT, or custom servers—for each component. Vapi then optimizes latency, manages scaling and streaming, and orchestrates conversation flow for natural-sounding interactions.

## Three-Step Pipeline

**Listen (Intake Raw Audio)**
The client device records raw audio, which is either transcribed locally or sent to a server for conversion to text.

**Run an LLM**
The transcript feeds into a language model prompt for inference, providing the conversational intelligence.

**Speak (Text to Raw Audio)**
The LLM's text output converts back to playable audio, processed either on-device or via server.

## Performance Goals

The system targets real-time performance with sensitivity to 50-100ms intervals, streaming between each layer. The complete voice-to-voice cycle aims for under 500-700ms latency.

Vapi integrates these components while providing straightforward management tools for developers.
