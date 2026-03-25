# Voicemail Detection Documentation

## Overview
Vapi's voicemail detection system enables outbound voice agents to handle voicemail events efficiently. The technology combines multiple detection methods to optimize for speed, accuracy, and cost-effectiveness.

## Key Benefits
The system addresses four primary concerns:
- **Time savings** through reduced wait times on unanswered calls
- **Cost reduction** by minimizing wasted call minutes
- **User experience** improvements via natural agent behavior during voicemail encounters
- **Higher engagement** through intentional, professional voicemail messages

## Detection Methods Comparison

Five detection approaches are available, each with distinct tradeoffs:

| Method | Strengths | Limitations | Rating |
|--------|-----------|------------|--------|
| **Vapi** | Fast, accurate, handles interruptions seamlessly | Minimal drawbacks | Strongly recommended |
| **Google** | Highly reliable, excellent accuracy | Slightly slower than Vapi | Recommended |
| **OpenAI** | Strong accuracy, adaptable phrasing | Higher expense | Good alternative |
| **Twilio** | Rapid beep detection | Susceptible to false alarms | Limited use cases |
| **Vapi Tool (beta)** | Maximum customization, cost-efficient | Demands quality prompting | Best for specialized needs |

## Core Configuration Parameters

**beepMaxAwaitSeconds** is the critical setting that determines when the bot begins its voicemail message. As the documentation warns: "Setting too low a value (under 15-20 seconds) may cut off your message." Most voicemail systems require 10-20 seconds before the beep.

Key parameters include:
- Detection delay onset (`startAtSeconds`)
- Polling interval (`frequencySeconds`, minimum 2.5 seconds)
- Maximum detection attempts (`maxRetries`)
- Maximum wait duration for beep detection (`beepMaxAwaitSeconds`, range 0-60 seconds)

## How Vapi's Engine Works

The detection mechanism leverages a hybrid approach combining Gemini-based pattern recognition, Twilio beep identification, real-time monitoring, and continuous polling during initial call stages.

## Implementation Examples

The documentation provides three complete configuration examples:

1. **Sales scenarios** - Fast detection (12 second beep wait)
2. **Support callbacks** - High accuracy via Google (20 second beep wait)
3. **Appointment reminders** - Balanced settings (15 second beep wait)

## Detection Types

Two detection methodologies exist:
- **Audio-based** (default, optimal for Google and Vapi)
- **Transcript-based** (recommended for OpenAI)

## Advanced Features

The system supports:
- Pre-recorded audio messages (MP3/WAV formats)
- Complete detection disabling via `"off"` setting
- Variable configurations per use case
- Interruption handling if humans answer mid-greeting

## Optimization Guidelines

**Cost reduction**: Lower retry counts, extend initial delay, use Vapi provider
**Accuracy improvement**: Choose Google, increase retry attempts, shorten initial delay

## Troubleshooting Framework

Common issues map to specific solutions:
- False positives require longer delays and higher frequency intervals
- Missed detections need shorter delays and more retries
- Slow detection benefits from Vapi selection and reduced initial delays

The documentation emphasizes that properly configured voicemail detection creates "faster, smarter, and more professional" call experiences while maintaining operational efficiency.
