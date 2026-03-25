# Speechmatics Documentation

## Overview

Speechmatics is an enterprise speech recognition platform offering accurate, fast speech-to-text for voice AI applications. It utilizes advanced self-supervised learning to handle diverse accents, dialects, and challenging acoustic environments effectively.

## Key Advantages on Vapi

**Real-time Accuracy**: The platform delivers transcripts in under one second while maintaining high precision—essential for natural voice agent interactions.

**Extensive Language Support**: Coverage spans 55+ languages with support for regional variants like Brazilian Portuguese and Canadian French without needing separate configurations.

**Speaker Diarization**: Unique among Vapi's transcribers, this capability identifies speakers in multi-party conversations by labeling each word with a speaker identifier. (Note: This feature is currently rolling out.)

**Custom Vocabulary**: Users can supply domain-specific terms, acronyms, and proper nouns to enhance accuracy for specialized applications.

## Setup Instructions

1. Navigate to the **Assistants** tab
2. Create or select a voice assistant
3. Access the **Transcriber** tab
4. Select **Speechmatics** from the Provider dropdown

A demonstration video is available for additional guidance.

## Recommended Settings

- **Operating Point**: Use the **Enhanced** model for optimal real-time performance
- **Region**: Select the geographically closest region to minimize latency
- **Custom Vocabulary**: Add critical terminology and utilize the *Sounds Like* feature for pronunciation clarity
