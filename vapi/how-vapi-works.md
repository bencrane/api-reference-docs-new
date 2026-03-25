# Orchestration Models

## Overview

Vapi implements a sophisticated orchestration layer on top of speech-to-text, language models, and text-to-speech. This layer includes several real-time models that enhance conversational quality:

- **Endpointing** – Identifies when users finish speaking
- **Interruptions** – Enables users to cut in and interrupt the assistant
- **Background noise filtering** – Removes ambient noise in real-time
- **Background voice filtering** – Filters out speech from TVs, echoes, or other speakers
- **Backchanneling** – Inserts affirmations like "yeah" or "got it" naturally
- **Emotion detection** – Recognizes user tone and conveys it to the LLM
- **Filler injection** – Adds natural speech patterns like "um" and "like"

## Key Components

**Endpointing**: Rather than relying on silence detection, Vapi employs "a custom fusion audio-text model to know when a user has completed their turn." This approach achieves sub-second response times while avoiding premature user interruption.

**Interruptions**: The system uses proprietary technology to differentiate genuine interruptions from backchannel responses, while tracking where the assistant was cut off.

**Background Voice Filtering**: Vapi developed "proprietary audio filtering model that's able to focus in on the primary speaker and block everything else out."

**Backchanneling**: A proprietary model determines optimal timing and selection of affirmations during user speech.

**Emotion Detection**: Real-time audio analysis extracts emotional nuance to inform LLM behavior adjustments.

**Filler Injection**: A custom model converts streaming output in real-time, adding natural conversational elements without additional latency.
