# Voice Fallback Configuration

## Overview

The documentation explains that voice fallback configuration enables calls to continue if the primary voice provider fails. As stated: "Your assistant will sequentially fallback to only the voices you configure within your plan, in the exact order you specify."

Without a configured fallback plan, calls terminate with an error when the chosen voice provider fails.

## How It Works

When voice failures occur, the system detects the problem and automatically switches to the first fallback voice in your configured sequence. If additional failures happen, it progresses through your list until either a voice succeeds or all configured options are exhausted.

## Configuration Methods

**Dashboard Setup**: Navigate to the Voice tab, locate the Fallback Voices section, and add fallbacks by selecting providers and voices from available options. Provider-specific settings like stability and speed can be configured through Additional Configuration.

**API Setup**: Add a `fallbackPlan` property containing a `voices` array with valid JSON configurations for each fallback voice. Order matters—Vapi processes fallbacks sequentially from the beginning.

## Provider Support

The system supports 20+ voice providers, each with unique configuration options including:
- ElevenLabs (stability, similarity boost, style controls)
- Cartesia (emotion configurations, speed control)
- Azure, OpenAI, LMNT, Rime AI, PlayHT, Deepgram, and others

Each provider offers distinct parameters for customizing voice characteristics.

## Recommendations

Use different providers to prevent provider-wide outages, select voices with similar characteristics to maintain consistency, and test configurations for smooth transitions. The system supports unlimited fallbacks, though 2-3 from different providers is recommended.

## Pricing & User Experience

Fallback activation incurs no additional fees. Users may notice brief pauses and voice changes when switching, which similar-sounding voices help minimize.
