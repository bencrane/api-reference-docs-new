# Voice Pipeline Configuration

## Overview

VAPI's voice pipeline allows developers to configure conversation timing and interruption handling for natural interaction flow. The system manages how voice data progresses through processing stages including detection, transcription, decision-making, and synthesis.

**Key capabilities include:**

- Fine-tune conversation timing for specific use cases
- Control assistant response initiation
- Configure interruption detection and recovery behavior
- Optimize response timing for different languages and contexts

## Quick Start Options

### English Conversations

For English, the recommended setup uses smart endpointing with LiveKit:

```json
{
  "startSpeakingPlan": {
    "smartEndpointingPlan": {
      "provider": "livekit",
      "waitFunction": "2000 / (1 + exp(-10 * (x - 0.5)))"
    },
    "waitSeconds": 0.4
  },
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0
  }
}
```

This provides intelligent detection of user speech completion, rapid interruption response (50-100ms), and natural conversation pacing.

### Non-English Languages

Text-based endpointing works across all languages:

```json
{
  "startSpeakingPlan": {
    "transcriptionEndpointingPlan": {
      "onPunctuationSeconds": 0.1,
      "onNoPunctuationSeconds": 1.5,
      "onNumberSeconds": 0.5
    },
    "waitSeconds": 0.4
  },
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0
  }
}
```

## Voice Pipeline Flow

**Processing sequence:**
```
User Audio → VAD → Transcription → Start Speaking Decision → LLM → TTS → waitSeconds → Assistant Audio
```

### Start Speaking Process

1. **User stops speaking**: Voice Activity Detection identifies utterance end
2. **Endpointing decision**: System evaluates completion using:
   - Transcriber EOT detection (if available and no smart endpointing configured)
   - Custom rules (highest priority when set)
   - Smart Endpointing Plan
3. **Response generation**: LLM processes immediately, TTS generates audio, then `waitSeconds` delay applies before assistant speaks

### Stop Speaking Process

1. **User starts speaking**: VAD detects utterance start during assistant output
2. **Interruption evaluation**: System checks for:
   - `interruptionPhrases` (instant pipeline clear)
   - `acknowledgementPhrases` (ignore interruption)
   - Threshold evaluation based on `numWords` setting
3. **Pipeline management**: If threshold met, clear pipeline, apply `backoffSeconds`, prepare for next input

## Start Speaking Plan

Determines when the assistant begins responding after user stops speaking.

### Transcription Endpointing

Analyzes transcription patterns to determine user completion:

- **onPunctuationSeconds** (Default: 0.1): Wait after punctuation detection
- **onNoPunctuationSeconds** (Default: 1.5): Wait when no punctuation detected
- **onNumberSeconds** (Default: 0.5): Wait after numbers detected

**Best for:** Non-English languages, rule-based predictability, fallback scenarios

### Smart Endpointing

AI-driven models analyze speech patterns and context. English-only capability.

**Available providers:**
- **livekit**: Advanced text-based model (English only)
- **vapi**: VAPI-trained model (non-English or alternative to LiveKit)
- **krisp**: Audio-based model analyzing prosodic features
- **deepgram-flux**: Built-in conversational speech recognition (English only)
- **assembly**: Neural network-based turn detection (English only)

### Deepgram Flux Configuration

Configure end-of-turn detection at the transcriber level:

```json
{
  "transcriber": {
    "provider": "deepgram",
    "model": "flux-general-en",
    "language": "en",
    "eotThreshold": 0.7,
    "eotTimeoutMs": 5000
  }
}
```

**eotThreshold** ranges:
- 0.5-0.6: Aggressive (quick but may interrupt mid-sentence)
- 0.6-0.8: Balanced (default: 0.7)
- 0.9-1.0: Conservative (waits longer)

**eotTimeoutMs** ranges:
- 2000-3000: Fast interactions
- 4000-6000: Standard natural flow (default: 5000)
- 7000-10000: Extended for complex responses

### LiveKit Wait Function

Mathematical expressions determine wait time based on speech completion probability (0-1 confidence):

**Aggressive (Fast):**
```
"waitFunction": "2000 / (1 + exp(-10 * (x - 0.5)))"
```
~200ms at 50% confidence, ~50ms at 90% confidence

**Normal (Balanced):**
```
"waitFunction": "(20 + 500 * sqrt(x) + 2500 * x^3 + 700 + 4000 * max(0, x-0.5)) / 2"
```
~800ms at 50% confidence, ~300ms at 90% confidence

**Conservative (Careful):**
```
"waitFunction": "700 + 4000 * max(0, x-0.5)"
```
~2700ms at 50% confidence, ~700ms at 90% confidence

### Vapi Heuristic Endpointing

Text-based heuristic rules applied in priority order:

1. **Number detection**: Latest message ends with number → `onNumberSeconds` (0.5s default)
2. **Punctuation detection**: Message contains punctuation → `onPunctuationSeconds` (0.1s default)
3. **No punctuation fallback**: No punctuation found → `onNoPunctuationSeconds` (1.5s default)
4. **Default**: No rules match → immediate response (0ms)

### Krisp Threshold Configuration

Audio-based probability model (0-1 scale, where 1 = user stopped):

- 0.0-0.3: Very aggressive (risk of noise false positives)
- 0.4-0.6: Balanced (default: 0.5)
- 0.7-1.0: Conservative (reduces false alarms)

**Important:** Configure `acknowledgementPhrases` and `numWords` in stop speaking plan for proper backchanneling.

### Assembly Turn Detection

Neural network-based model understanding speech meaning and flow.

**Aggressive (Fast):**
```json
{
  "endOfTurnConfidenceThreshold": 0.4,
  "minEndOfTurnSilenceWhenConfident": 160,
  "maxTurnSilence": 400
}
```

**Balanced (Natural):**
```json
{
  "endOfTurnConfidenceThreshold": 0.4,
  "minEndOfTurnSilenceWhenConfident": 400,
  "maxTurnSilence": 1280
}
```

**Conservative (Patient):**
```json
{
  "endOfTurnConfidenceThreshold": 0.7,
  "minEndOfTurnSilenceWhenConfident": 800,
  "maxTurnSilence": 3600
}
```

### Wait Seconds

Final audio delay applied before assistant speaks.

**Range:** 0-5 seconds (Default: 0.4)

- 0.0-0.2: Gaming, real-time
- 0.3-0.5: Standard conversations
- 0.6-0.8: Healthcare, formal settings

### Pipeline Timeline

**Complete processing example:**
```
0.0s: User stops speaking
0.1s: Smart endpointing evaluation begins
0.6s: Smart endpointing triggers
0.6s: LLM request sent
1.4s: LLM response (0.8s processing)
1.9s: TTS audio generated (0.5s)
1.9s: waitSeconds (0.4s) starts
2.3s: Assistant begins speaking
```

**Total Response Time: 2.3 seconds**

Key insights: Aggressive functions reduce endpointing to ~0.2s; conservative functions extend to ~2.7s. Total response ranges from 1.9s (aggressive) to 4.7s (conservative).

### Custom Endpointing Rules

Highest priority rules overriding all other endpointing decisions:

```json
{
  "customEndpointingRules": [
    {
      "type": "assistant",
      "regex": "(phone|email|address)",
      "timeoutSeconds": 3.0
    },
    {
      "type": "user",
      "regex": "\\d{3}-\\d{3}-\\d{4}",
      "timeoutSeconds": 2.0
    }
  ]
}
```

**Use cases:** Data collection, spelling sequences, complex responses requiring extra processing time

## Stop Speaking Plan

Controls interruption detection and handling when users speak during assistant output.

### Number of Words

**VAD-based (numWords = 0):**
```json
{
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.2
  }
}
```
Uses Voice Activity Detection for faster interruption (50-100ms), language-independent, but more sensitive to background noise.

**Transcription-based (numWords > 0):**
```json
{
  "stopSpeakingPlan": {
    "numWords": 2
  }
}
```
Waits for specified word count before triggering, more accurate but slower response (200-500ms).

**Range:** 0-10 words (Default: 0)

### Voice Seconds

VAD duration threshold when `numWords = 0`. Determines voice activity duration before interruption triggering.

**Range:** 0-0.5 seconds (Default: 0.2)

- 0.1: Very sensitive (background noise risk)
- 0.2: Balanced (recommended)
- 0.4: Conservative (fewer false positives)

**Relationship with numWords=0:**
```
User Starts Speaking → VAD Detects Voice → Duration Continuous for voiceSeconds → Interrupt Assistant
```

Faster than transcription (50-100ms vs 200-500ms) and language-independent.

### Backoff Seconds

Blocks all assistant audio output following user interruption, creating a recovery period.

**Range:** 0-10 seconds (Default: 1.0)

- 0.5: Quick recovery for fast-paced interactions
- 1.0: Natural pause for most conversations
- 2.0: Deliberate pause for formal settings

**Interruption timeline example:**
```
0.0s: Assistant speaking: "I can help you book..."
1.2s: User interrupts: "Actually, wait"
1.2s: backoffSeconds (1.0s) starts → All audio blocked
2.2s: backoffSeconds completes
2.5s: User says: "What about tomorrow?"
3.0s: Endpointing triggers
3.8s: TTS completes → waitSeconds (0.4s)
4.2s: Assistant responds: "For tomorrow..."
```

**Total Recovery: 3.2 seconds**

**Important:** `backoffSeconds` blocks output during interruption; `waitSeconds` delays normal responses. They're sequential, not cumulative.

## Configuration Examples

### E-commerce Customer Support

```json
{
  "startSpeakingPlan": {
    "waitSeconds": 0.4,
    "smartEndpointingPlan": {
      "provider": "livekit",
      "waitFunction": "2000 / (1 + exp(-10 * (x - 0.5)))"
    }
  },
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.15,
    "backoffSeconds": 0.8
  }
}
```

Optimized for rapid responses to customer queries about orders and products.

### Non-English (Spanish Example)

```json
{
  "transcriber": { "language": "es" },
  "startSpeakingPlan": {
    "waitSeconds": 0.4,
    "transcriptionEndpointingPlan": {
      "onPunctuationSeconds": 0.1,
      "onNoPunctuationSeconds": 2.0
    }
  },
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.3,
    "backoffSeconds": 1.2
  }
}
```

Uses text-based endpointing with longer timeouts for different speech patterns and international support.

### Krisp Audio-Based Endpointing

```json
{
  "startSpeakingPlan": {
    "waitSeconds": 0.4,
    "smartEndpointingPlan": {
      "provider": "krisp",
      "threshold": 0.5
    }
  },
  "stopSpeakingPlan": {
    "numWords": 2,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0,
    "acknowledgementPhrases": [
      "okay",
      "right",
      "uh-huh",
      "yeah",
      "mm-hmm",
      "got it"
    ]
  }
}
```

Configured for non-English conversations with robust backchanneling.

### Assembly Audio-Text Endpointing

```json
{
  "transcriber": {
    "provider": "assembly",
    "endOfTurnConfidenceThreshold": 0.4,
    "minEndOfTurnSilenceWhenConfident": 400,
    "maxTurnSilence": 1280
  },
  "startSpeakingPlan": {
    "waitSeconds": 0.4
  },
  "stopSpeakingPlan": {
    "numWords": 0,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0
  }
}
```

For English conversations with integrated transcriber and sophisticated turn detection.

### Deepgram Flux Audio-Text Endpointing

```json
{
  "transcriber": {
    "provider": "deepgram",
    "model": "flux-general-en",
    "language": "en",
    "eotThreshold": 0.7,
    "eotTimeoutMs": 5000
  },
  "stopSpeakingPlan": {
    "numWords": 2,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0,
    "acknowledgementPhrases": [
      "okay",
      "right",
      "uh-huh",
      "yeah",
      "mm-hmm",
      "got it"
    ]
  }
}
```

For English conversations using Deepgram as transcriber.

### Education and Training

```json
{
  "startSpeakingPlan": {
    "waitSeconds": 0.7,
    "smartEndpointingPlan": {
      "provider": "livekit",
      "waitFunction": "(20 + 500 * sqrt(x) + 2500 * x^3 + 700 + 4000 * max(0, x-0.5)) / 2"
    },
    "customEndpointingRules": [
      {
        "type": "assistant",
        "regex": "(spell|define|explain|example)",
        "timeoutSeconds": 4.0
      }
    ]
  },
  "stopSpeakingPlan": {
    "numWords": 1,
    "backoffSeconds": 1.5
  }
}
```

Accommodates learning pace with extended time for complex questions and explanations.

## Next Steps

- **Speech configuration:** Provider-specific voice settings
- **Custom transcriber:** Configure transcription providers by language
- **Voice fallback plan:** Set up backup voice options
- **Debugging voice agents:** Troubleshoot voice pipeline issues
