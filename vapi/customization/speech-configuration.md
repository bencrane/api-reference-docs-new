# Speech Configuration

## Overview

Speech configuration enables precise control over when an assistant begins and stops speaking during conversations. According to the documentation, "Speech configuration lets you control exactly when your assistant starts and stops speaking during a conversation."

The system includes two primary mechanisms:

1. **Speaking Plan** — determines when the assistant initiates speech after customer pauses
2. **Stop Speaking Plan** — governs when the assistant ceases speaking if the customer interjects

**Note:** These configurations are currently API-only and PlayHT is the sole provider supporting adjustable speech speed.

## Start Speaking Plan

This component manages assistant speech initiation parameters:

**Wait Time Before Speaking**
The default 0.4-second delay can be modified. Technical support scenarios may benefit from longer waits (1+ seconds) to allow customers to complete thoughts despite mid-sentence pausing.

**Smart Endpointing Plan**
Advanced processing detects genuine completion of customer statements. The documentation notes that turn-taking involves "End-of-turn prediction" and "Backchannel prediction" for acknowledging listener cues like "yeah" or "uh-huh."

Available providers include:

- **Krisp** (audio-based): Analyzes prosodic features with configurable thresholds (0-1 range)
- **Deepgram Flux** (audio-text): Combines transcription with native turn detection
- **Assembly** (audio-text): Reports end-of-turn flags during transcription
- **LiveKit** (text-based): Recommended for English conversations; uses customizable `waitFunction` parameters
- **Vapi** (text-based): Suitable for non-English interactions

**Transcription-Based Detection**
Customizes completion detection based on spoken content, utilizing `WaitSeconds`, `onPunctuationSeconds`, and `onNoPunctuationSeconds` parameters.

## Stop Speaking Plan

This plan determines assistant interruption handling:

- **Words to Stop Speaking**: Set minimum word count (0 for immediate response; 2-3 words recommended for appointment scheduling)
- **Voice Activity Detection**: Default 0.2 seconds; higher values reduce false positives from background noise
- **Pause Before Resuming**: Default 1 second; adjustable based on desired response speed

Example configuration:
```json
"stopSpeakingPlan": {
  "numWords": 0,
  "voiceSeconds": 0.2,
  "backoffSeconds": 1
}
```

## Configuration Best Practices

Consider customer communication patterns, environmental noise levels, and desired responsiveness. Background sound settings default to 'office' for phone calls and 'off' for web interactions. Testing various parameters ensures optimal conversation flow balancing responsiveness with natural interaction patterns.
