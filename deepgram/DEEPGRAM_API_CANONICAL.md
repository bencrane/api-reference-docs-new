# Deepgram API — Canonical Reference

> **Purpose:** Definitive engineering reference for Deepgram integration in a real-time voice agent pipeline.
> **Critical path:** Twilio phone audio (8kHz mulaw) → Deepgram STT → text transcript → LLM.
> **Source:** Extracted from Deepgram developer docs (developers.deepgram.com), March 2026.

---

## Table of Contents

1. [Models Inventory](#1-models-inventory)
2. [Live Streaming STT — Complete Protocol](#2-live-streaming-stt--complete-protocol)
3. [Pre-recorded STT — REST API](#3-pre-recorded-stt--rest-api)
4. [Audio Format Deep Dive](#4-audio-format-deep-dive)
5. [Smart Features for Voice Agents](#5-smart-features-for-voice-agents)
6. [Text-to-Speech (TTS)](#6-text-to-speech-tts)
7. [Authentication](#7-authentication)
8. [Rate Limits + Concurrency](#8-rate-limits--concurrency)
9. [Pricing](#9-pricing)
10. [Python SDK](#10-python-sdk)
11. [Error Handling](#11-error-handling)
12. [Integration Architecture for Voice Agents](#12-integration-architecture-for-voice-agents)

---

## 1. Models Inventory

### Speech-to-Text Models

| Model | Identifier | Streaming | Batch | Best For | Languages |
|-------|-----------|-----------|-------|----------|-----------|
| **Nova-3** | `nova-3` | Yes | Yes | Highest accuracy, latest generation | `en`, `en-us`, and many more |
| **Flux** | `flux-general-en` | Yes (v2 only) | No | Turn-based conversational STT with contextual end-of-turn detection. Lowest latency for voice agents | `en` |
| **Nova-2** | `nova-2` | Yes | Yes | Production-grade real-time phone transcription. Best balance of accuracy + latency for streaming | 30+ languages |
| **Nova** | `nova` | Yes | Yes | Previous generation, still supported | Multiple |
| **Enhanced** | `enhanced` | Yes | Yes | Higher accuracy than Base, lower than Nova | Multiple |
| **Base** | `base` | Yes | Yes | Fastest, lowest cost, lower accuracy | Multiple |
| **Whisper Cloud** | `whisper` | No (batch only) | Yes | OpenAI Whisper hosted by Deepgram. High accuracy but high latency, not for real-time | Multiple |

**For real-time phone conversations: Use `nova-2` on the v1 streaming endpoint, or `flux-general-en` on the v2 streaming endpoint.**

Nova-2 is the proven choice for production Twilio pipelines — wide language support, low latency, high accuracy on phone audio. Flux is newer and purpose-built for turn-based voice agent conversations with contextual end-of-turn detection, but is English-only and uses the v2 WebSocket endpoint.

### Text-to-Speech Models

| Model Family | Example Identifier | Architecture |
|-------------|-------------------|-------------|
| **Aura-2** | `aura-2-asteria-en`, `aura-2-zeus-en`, `aura-2-luna-en`, `aura-2-thalia-en` | `aura-2` |
| **Aura** (v1) | `aura-asteria-en` | `aura` |

Default TTS model: `aura-asteria-en`

### Model Metadata API

```
GET https://api.deepgram.com/v1/models
GET https://api.deepgram.com/v1/models/:model_id
```

Response shape:
```json
{
  "stt": [
    {
      "name": "nova-3",
      "canonical_name": "nova-3",
      "architecture": "base",
      "languages": ["en", "en-us"],
      "version": "2021-11-10.1",
      "uuid": "6b28e919-8427-4f32-9847-492e2efd7daf",
      "batch": true,
      "streaming": true,
      "formatted_output": true
    }
  ],
  "tts": [
    {
      "name": "zeus",
      "canonical_name": "aura-2-zeus-en",
      "architecture": "aura-2",
      "languages": ["en", "en-US"],
      "version": "2025-04-07.0",
      "uuid": "2baf189d-91ac-481d-b6d1-750888667b31",
      "metadata": {
        "accent": "American",
        "age": "Adult",
        "tags": ["masculine", "deep", "trustworthy", "smooth"],
        "use_cases": ["IVR"]
      }
    }
  ]
}
```

Query param `include_outdated=true` returns non-latest model versions.

---

## 2. Live Streaming STT — Complete Protocol

This is the **critical integration** for the voice agent pipeline.

### 2.1 WebSocket Endpoint & Connection Setup

#### v1 Endpoint (Nova-2, Nova, Enhanced, Base)

```
wss://api.deepgram.com/v1/listen
```

Handshake: `GET` → `101 Switching Protocols`

#### v2 Endpoint (Flux)

```
wss://api.deepgram.com/v2/listen
```

Handshake: `GET` → `101 Switching Protocols`

### 2.2 Authentication

Two methods for WebSocket connections:

| Method | Header | Format |
|--------|--------|--------|
| API Key via header | `Authorization` | `Token YOUR_API_KEY` |
| Temporary JWT via header | `Authorization` | `Bearer YOUR_JWT_TOKEN` |
| Via WebSocket subprotocol | `Sec-WebSocket-Protocol` | For client-side environments where custom headers are not supported |

**For server-side integrations (our use case):** Use `Authorization: Token YOUR_API_KEY` header.

### 2.3 Connection Parameters (v1 — `/v1/listen`)

All passed as query parameters on the WebSocket URL.

| Parameter | Type | Default | Valid Values | Description |
|-----------|------|---------|-------------|-------------|
| `model` | enum | — | **Required.** `nova-2`, `nova-3`, `nova`, `enhanced`, `base` (30 enum values total, including language-specific variants) | AI model for transcription |
| `encoding` | enum | auto-detect | `linear16`, `mulaw`, `alaw`, `opus`, `flac`, `mp3`, `mp4`, `aac`, `amr-nb`, `amr-wb`, `g729` (11 values) | Audio encoding. **Required for raw/non-containerized audio** |
| `sample_rate` | integer | — | `8000`, `16000`, `22050`, `44100`, `48000`, etc. | Sample rate in Hz. **Required when encoding is specified** |
| `channels` | integer | 1 | Any positive integer | Number of audio channels |
| `language` | string | `en` | BCP-47 tag (e.g., `en`, `en-US`, `es`, `fr`) | Primary spoken language hint |
| `punctuate` | boolean | `false` | `true`, `false` | Add punctuation and capitalization |
| `diarize` | boolean | `false` | `true`, `false` | Speaker identification (each word gets speaker number starting at 0) |
| `smart_format` | boolean | `false` | `true`, `false` | Apply formatting (numbers, currency, dates) |
| `endpointing` | integer or boolean | — | Milliseconds (e.g., `300`) or `false` to disable | How long to wait before finalizing after speech pause. Controls `speech_final`. Lower = faster but may cut mid-sentence |
| `interim_results` | boolean | `false` | `true`, `false` | Send ongoing transcription updates as audio arrives. Essential for real-time UX |
| `utterance_end_ms` | integer | — | Milliseconds (e.g., `1000`) | How long after last word before sending `UtteranceEnd` event. Use with `interim_results` |
| `vad_events` | boolean | `false` | `true`, `false` | Enable `SpeechStarted` events |
| `multichannel` | boolean | `false` | `true`, `false` | Transcribe each channel independently |
| `numerals` | boolean | `false` | `true`, `false` | Convert written numbers to digits |
| `profanity_filter` | boolean | `false` | `true`, `false` | Replace profanity |
| `redact` | enum | `false` | `pci`, `numbers`, `ssn`, `true`, `false` (6 values) | Redact sensitive info |
| `replace` | string(s) | — | Term:replacement pairs | Find and replace in transcript |
| `search` | string(s) | — | Search terms | Search for terms in audio |
| `keywords` | string(s) | — | Terms with optional boost | Boost/suppress terminology |
| `keyterm` | string(s) | — | Terms | Key term prompting (Nova-3 only) |
| `detect_entities` | boolean | `false` | `true`, `false` | Extract entities. Enables punctuation automatically |
| `dictation` | boolean | `false` | `true`, `false` | Dictation mode |
| `version` | string | latest | Model version string | Specific model version |
| `tag` | string | — | Any string | Label for usage reporting |
| `extra` | string | — | Key-value pairs | Arbitrary metadata attached to response |
| `callback` | string | — | URL | Callback URL for results |
| `callback_method` | enum | `POST` | `POST`, `GET`, `PUT`, `DELETE` | Callback HTTP method |
| `mip_opt_out` | boolean | `false` | `true`, `false` | Opt out of Model Improvement Program (affects pricing) |

#### Twilio-Specific Connection URL

For Twilio media streams sending 8kHz mulaw mono audio:

```
wss://api.deepgram.com/v1/listen?model=nova-2&encoding=mulaw&sample_rate=8000&channels=1&punctuate=true&interim_results=true&endpointing=300&utterance_end_ms=1000&vad_events=true
```

**Key params for Twilio audio:**
- `encoding=mulaw` — Twilio sends mulaw-encoded audio
- `sample_rate=8000` — Twilio phone audio is 8kHz
- `channels=1` — Twilio media streams are mono

### 2.4 Connection Parameters (v2 — `/v2/listen` — Flux)

| Parameter | Type | Default | Valid Values | Description |
|-----------|------|---------|-------------|-------------|
| `model` | enum | — | **Required.** `flux-general-en` | Flux model |
| `encoding` | enum | auto-detect | 6 enum values | Audio encoding (required for raw audio) |
| `sample_rate` | integer | — | Hz value | Required for raw audio |
| `eager_eot_threshold` | float | — | `0.3` – `0.9` | End-of-turn confidence for eager (early) EOT events. Enables `EagerEndOfTurn` and `TurnResumed` events |
| `eot_threshold` | float | — | `0.5` – `0.9` | End-of-turn confidence to finish a turn |
| `eot_timeout_ms` | integer | — | Milliseconds | Force-finish turn after this silence duration regardless of EOT confidence |
| `keyterm` | string(s) | — | Terms | Boost specialized terminology |
| `tag` | string | — | Any string | Usage reporting label |
| `mip_opt_out` | boolean | — | `true`, `false` | Opt out of MIP |

### 2.5 Sending Audio Data

Audio is sent as **binary WebSocket frames**.

- Send raw audio bytes as binary messages
- **Chunk size recommendation:** Send audio as it arrives. For Twilio media streams, forward each media message's audio payload directly
- No special framing or headers needed — just raw audio bytes matching the declared encoding/sample_rate

### 2.6 Control Messages (Send)

#### v1 Messages

**KeepAlive** — Keep connection open during silence:
```json
{"type": "KeepAlive"}
```

**Finalize** — Flush buffered audio and get final transcript for current segment:
```json
{"type": "Finalize"}
```

**CloseStream** — Close connection gracefully (flushes remaining audio):
```json
{"type": "CloseStream"}
```

#### v2 Messages (Flux)

**CloseStream:**
```json
{"type": "CloseStream"}
```

**Configure** — Update thresholds and keyterms mid-stream:
```json
{
  "type": "Configure",
  "thresholds": {
    "eager_eot_threshold": 0.5,
    "eot_threshold": 0.5,
    "eot_timeout_ms": 1000
  },
  "keyterms": ["weather", "forecast"]
}
```

### 2.7 Response Message Types (v1 — Receive)

#### Results

The primary transcript message. Exact JSON shape:

```json
{
  "type": "Results",
  "channel_index": [0, 1],
  "duration": 3.5,
  "start": 0,
  "channel": {
    "alternatives": [
      {
        "transcript": "Hello, how are you doing today?",
        "confidence": 0.98,
        "words": [
          {
            "word": "hello",
            "start": 0,
            "end": 0.5,
            "confidence": 0.99,
            "language": "en-US",
            "punctuated_word": "Hello,",
            "speaker": 0
          },
          {
            "word": "how",
            "start": 0.6,
            "end": 0.8,
            "confidence": 0.98,
            "language": "en-US",
            "punctuated_word": "how",
            "speaker": 0
          }
        ],
        "languages": ["en-US"]
      }
    ]
  },
  "metadata": {
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "model_info": {
      "name": "nova-2",
      "version": "2024-01-18.29447",
      "arch": "nova-2"
    },
    "model_uuid": "1842b5b2-ef26-4f13-bec5-48eaef70e9c0"
  },
  "is_final": true,
  "speech_final": true,
  "from_finalize": false,
  "entities": [
    {
      "label": "ORIGIN",
      "value": "Iranian",
      "confidence": 1,
      "start_word": 5,
      "end_word": 6
    }
  ]
}
```

**Key fields in Results:**

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"Results"` |
| `channel_index` | array[int] | `[channel_number, total_channels]` |
| `duration` | float | Duration of audio segment in seconds |
| `start` | float | Start time of segment in seconds |
| `channel.alternatives` | array | Ranked transcript alternatives |
| `channel.alternatives[].transcript` | string | The transcript text |
| `channel.alternatives[].confidence` | float | 0–1 confidence score |
| `channel.alternatives[].words` | array | Word-level detail |
| `channel.alternatives[].words[].word` | string | Raw word |
| `channel.alternatives[].words[].start` | float | Word start time (seconds) |
| `channel.alternatives[].words[].end` | float | Word end time (seconds) |
| `channel.alternatives[].words[].confidence` | float | Word confidence (0–1) |
| `channel.alternatives[].words[].punctuated_word` | string | Word with punctuation/casing (if `punctuate=true`) |
| `channel.alternatives[].words[].speaker` | int | Speaker ID (if `diarize=true`) |
| `channel.alternatives[].words[].language` | string | Detected language |
| `is_final` | boolean | `true` = Deepgram will not revisit this audio segment. `false` = interim result that may change |
| `speech_final` | boolean | `true` = endpoint detected (speaker paused). Only present when `endpointing` is enabled |
| `from_finalize` | boolean | `true` = this result was triggered by a `Finalize` message |
| `metadata.request_id` | string | Unique request identifier |
| `entities` | array | Detected entities (if `detect_entities=true`) |

#### Metadata

Sent once at connection start:

```json
{
  "type": "Metadata",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "sha256": "a3c7d0f8e9b2d1a4c5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8",
  "created": "2025-10-02T14:30:00.000Z",
  "duration": 45.5,
  "channels": 2,
  "transaction_key": "deprecated"
}
```

#### SpeechStarted

Sent when VAD detects speech beginning (requires `vad_events=true`):

```json
{
  "type": "SpeechStarted",
  "channel": [0],
  "timestamp": 0.5
}
```

#### UtteranceEnd

Sent when silence exceeds `utterance_end_ms` after last transcribed word:

```json
{
  "type": "UtteranceEnd",
  "channel": [0],
  "last_word_end": 2.5
}
```

### 2.8 Response Message Types (v2 — Flux — Receive)

#### Connected

```json
{
  "type": "Connected",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "sequence_id": 0
}
```

#### TurnInfo

The primary transcript message for Flux. Contains contextual end-of-turn detection:

```json
{
  "type": "TurnInfo",
  "request_id": "ad12514a-0d38-4f7e-8fba-cce10d8f174c",
  "sequence_id": 11,
  "event": "EndOfTurn",
  "turn_index": 0,
  "audio_window_start": 0,
  "audio_window_end": 1.3,
  "transcript": "Hello, how are you?",
  "words": [
    {
      "word": "Hello,",
      "confidence": 0.96
    },
    {
      "word": "how",
      "confidence": 0.94
    },
    {
      "word": "are",
      "confidence": 0.97
    },
    {
      "word": "you?",
      "confidence": 0.92
    }
  ],
  "end_of_turn_confidence": 0.86
}
```

**`event` values:** `EndOfTurn`, `EagerEndOfTurn`, `TurnResumed`

#### ConfigureSuccess / ConfigureFailure

```json
{
  "type": "ConfigureSuccess",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "thresholds": {
    "eager_eot_threshold": 0.5,
    "eot_threshold": 0.5,
    "eot_timeout_ms": 1000
  },
  "keyterms": ["weather", "forecast"],
  "sequence_id": 0
}
```

#### Error (Fatal)

```json
{
  "type": "Error",
  "sequence_id": 5,
  "code": "INTERNAL_SERVER_ERROR",
  "description": "An internal server error occurred while processing the request"
}
```

### 2.9 Interim Results vs Final Results vs speech_final

| Signal | Meaning | When to Use |
|--------|---------|------------|
| `is_final: false` | **Interim result.** Deepgram's best guess so far — will be revised as more audio arrives. Transcript may change completely. | Display as "thinking" indicator. Show to user for real-time feel. **Never send to LLM.** |
| `is_final: true` | **Final result for this audio segment.** Deepgram will not revise this segment. The transcript is stable. | Accumulate these into the running transcript. |
| `speech_final: true` | **Endpoint detected.** The speaker has paused long enough for Deepgram to consider this a complete speech segment. Only fires when `endpointing` is configured. | **This is your trigger to send the accumulated transcript to the LLM.** Indicates the caller finished a thought. |
| `from_finalize: true` | Result was triggered by sending a `Finalize` message, not by natural speech pause. | Useful for forced flush scenarios. |

**Voice agent pattern:**
1. Enable `interim_results=true` — show partial text to indicate the system is listening
2. Enable `endpointing=300` (300ms) — balance between responsiveness and accuracy
3. Accumulate text from `is_final: true` results
4. When `speech_final: true` arrives → send accumulated text to LLM
5. Alternatively, listen for `UtteranceEnd` events as the trigger

### 2.10 Endpointing

Endpointing controls how long Deepgram waits after detecting a speech pause before finalizing the transcript.

- **Parameter:** `endpointing` (milliseconds or `false`)
- **Effect:** When the speaker pauses for longer than `endpointing` ms, Deepgram sends a result with `speech_final: true`
- **Lower value (e.g., 100–200ms):** Faster response, but may trigger mid-sentence on brief pauses
- **Higher value (e.g., 500–1000ms):** More accurate sentence boundaries, but added latency
- **`endpointing=false`:** Disables endpointing entirely. `speech_final` will never be `true`
- **Recommended for voice agents:** `300` ms — fast enough for conversational feel, tolerant of brief pauses

### 2.11 Utterance Detection

- **Parameter:** `utterance_end_ms` (milliseconds)
- **Requires:** `interim_results=true`
- When the last transcribed word was `utterance_end_ms` ago, Deepgram sends an `UtteranceEnd` event
- This groups speech into logical utterances
- **Use case:** Alternative or complement to `speech_final` for determining when the caller is done speaking
- **Recommended:** `1000` ms for phone conversations

### 2.12 VAD (Voice Activity Detection)

- **Parameter:** `vad_events=true`
- Enables `SpeechStarted` events when Deepgram detects the beginning of speech
- **Use case for voice agents:** Detect barge-in — if the caller starts speaking while the AI is outputting TTS audio, you can interrupt the TTS playback

### 2.13 Keep-Alive

During periods of silence (no audio being sent), send periodic KeepAlive messages to prevent the WebSocket from timing out:

```json
{"type": "KeepAlive"}
```

Send every ~10 seconds during silence periods.

### 2.14 Closing the Connection

1. **Graceful close:** Send `CloseStream` message — Deepgram flushes remaining audio and sends final results before closing
2. **Force flush without closing:** Send `Finalize` message — gets results for buffered audio, keeps connection open

```json
{"type": "CloseStream"}
```

### 2.15 Full Working Python Example — Streaming STT

```python
import asyncio
import json
import websockets

DEEPGRAM_API_KEY = "YOUR_API_KEY"

# Twilio 8kHz mulaw configuration
DEEPGRAM_URL = (
    "wss://api.deepgram.com/v1/listen"
    "?model=nova-2"
    "&encoding=mulaw"
    "&sample_rate=8000"
    "&channels=1"
    "&punctuate=true"
    "&interim_results=true"
    "&endpointing=300"
    "&utterance_end_ms=1000"
    "&vad_events=true"
    "&smart_format=true"
)

async def deepgram_streaming():
    extra_headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}"
    }

    async with websockets.connect(
        DEEPGRAM_URL,
        extra_headers=extra_headers
    ) as ws:
        print("Connected to Deepgram")

        # Track accumulated transcript
        transcript_parts = []

        async def receive_transcripts():
            async for message in ws:
                data = json.loads(message)
                msg_type = data.get("type")

                if msg_type == "Results":
                    transcript = data["channel"]["alternatives"][0]["transcript"]
                    is_final = data.get("is_final", False)
                    speech_final = data.get("speech_final", False)

                    if not transcript:
                        continue

                    if is_final:
                        transcript_parts.append(transcript)
                        print(f"[FINAL] {transcript}")

                        if speech_final:
                            full_utterance = " ".join(transcript_parts)
                            print(f">>> SEND TO LLM: {full_utterance}")
                            transcript_parts.clear()
                            # Here: send full_utterance to your LLM
                    else:
                        print(f"[INTERIM] {transcript}")

                elif msg_type == "SpeechStarted":
                    print("[VAD] Speech started — potential barge-in")
                    # Here: interrupt TTS playback if agent is speaking

                elif msg_type == "UtteranceEnd":
                    if transcript_parts:
                        full_utterance = " ".join(transcript_parts)
                        print(f">>> UTTERANCE END → LLM: {full_utterance}")
                        transcript_parts.clear()

                elif msg_type == "Metadata":
                    print(f"[META] Request ID: {data.get('request_id')}")

                elif msg_type == "Error":
                    print(f"[ERROR] {data}")

        async def send_audio():
            """
            Replace this with your actual audio source.
            For Twilio: forward the base64-decoded media payload.
            """
            # Example: read from a file in chunks
            chunk_size = 4096  # bytes
            with open("audio.raw", "rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    await ws.send(chunk)
                    await asyncio.sleep(0.1)  # simulate real-time

            # Close gracefully
            await ws.send(json.dumps({"type": "CloseStream"}))

        async def keep_alive():
            """Send keep-alive every 10 seconds."""
            while True:
                await asyncio.sleep(10)
                try:
                    await ws.send(json.dumps({"type": "KeepAlive"}))
                except websockets.exceptions.ConnectionClosed:
                    break

        await asyncio.gather(
            receive_transcripts(),
            send_audio(),
            keep_alive()
        )

if __name__ == "__main__":
    asyncio.run(deepgram_streaming())
```

---

## 3. Pre-recorded STT — REST API

### When to Use

- Post-call transcription
- Batch processing of recorded calls
- When latency is not a concern and you want maximum accuracy + full feature set

### Endpoint

```
POST https://api.deepgram.com/v1/listen
```

### Request Formats

**Option A — URL reference (JSON body):**

```bash
curl -X POST "https://api.deepgram.com/v1/listen?model=nova-2&punctuate=true&diarize=true&smart_format=true" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/audio.wav"}'
```

**Option B — Direct file upload (binary body):**

```bash
curl -X POST "https://api.deepgram.com/v1/listen?model=nova-2&punctuate=true" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

**Important:** When sending a JSON body with a URL, you **must** set `Content-Type: application/json`. Omitting this causes a `400 Bad Request`.

### All Query Parameters

Same as streaming v1 parameters (see Section 2.3), plus these pre-recorded-only options:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `utterances` | boolean | `false` | Segment speech into semantic units |
| `utt_split` | double | `0.8` | Seconds of pause to split utterances |
| `paragraphs` | boolean | `false` | Split into paragraphs |
| `summarize` | boolean/string | — | Summarize content |
| `topics` | boolean | `false` | Detect topics |
| `custom_topic` | string(s) | — | Up to 100 custom topics |
| `custom_topic_mode` | enum | `extended` | `extended` or `strict` |
| `intents` | boolean | `false` | Detect speaker intent |
| `custom_intent` | string(s) | — | Custom intents |
| `custom_intent_mode` | enum | `extended` | `extended` or `strict` |
| `detect_entities` | boolean | `false` | Extract entities |
| `sentiment` | boolean | `false` | Sentiment analysis |
| `detect_language` | boolean/list | — | Detect dominant language |
| `filler_words` | boolean | `false` | Transcribe "uh", "um" |
| `measurements` | boolean | `false` | Convert spoken measurements to abbreviations |

### Response Shape (200)

```json
{
  "metadata": {
    "request_id": "a847f427-4ad5-4d67-9b95-db801e58251c",
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33",
    "created": "2024-05-12T18:57:13.426Z",
    "duration": 25.933313,
    "channels": 1,
    "models": ["30089e05-99d1-4376-b32e-c263170674af"],
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "name": "2-general-nova",
        "version": "2024-01-09.29447",
        "arch": "nova-2"
      }
    }
  },
  "results": {
    "channels": [
      {
        "alternatives": [
          {
            "transcript": "This historic spacewalk marks a significant milestone.",
            "confidence": 0.95,
            "words": [
              {
                "word": "historic",
                "start": 0.5,
                "end": 1,
                "confidence": 0.96
              }
            ],
            "paragraphs": { "..." : "..." },
            "entities": [ { "label": "Event", "value": "spacewalk", "confidence": 0.98 } ],
            "summaries": [ { "summary": "...", "start_word": 0, "end_word": 12 } ],
            "topics": [ { "text": "...", "topics": ["Space Exploration"] } ]
          }
        ],
        "detected_language": "en"
      }
    ],
    "utterances": [
      {
        "start": 0,
        "end": 25.9,
        "confidence": 0.95,
        "channel": 1,
        "transcript": "...",
        "words": [ { "word": "...", "start": 0.5, "end": 1, "confidence": 0.96, "speaker": 1, "speaker_confidence": 0.99, "punctuated_word": "..." } ],
        "speaker": 1,
        "id": "utt-0001"
      }
    ],
    "summary": { "result": "success", "short": "..." },
    "topics": { "results": { "topics": { "segments": [...] } } },
    "intents": { "results": { "intents": { "segments": [...] } } },
    "sentiments": {
      "segments": [ { "text": "...", "sentiment": "positive", "sentiment_score": 0.58 } ],
      "average": { "sentiment": "positive", "sentiment_score": 0.58 }
    }
  }
}
```

### Python Example — Pre-recorded

```python
import requests

url = "https://api.deepgram.com/v1/listen"
params = {
    "model": "nova-2",
    "punctuate": "true",
    "diarize": "true",
    "smart_format": "true",
    "utterances": "true",
    "sentiment": "true",
}
headers = {
    "Authorization": "Token YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {"url": "https://example.com/call-recording.wav"}

response = requests.post(url, json=payload, headers=headers, params=params)
result = response.json()

for utterance in result["results"]["utterances"]:
    print(f"Speaker {utterance['speaker']}: {utterance['transcript']}")
```

---

## 4. Audio Format Deep Dive

### Supported Encodings

| Encoding | Streaming v1 | Streaming v2 (Flux) | Pre-recorded | Notes |
|----------|-------------|---------------------|-------------|-------|
| `linear16` | Yes | Yes | Yes | 16-bit PCM, little-endian. Most common raw format |
| `mulaw` | Yes | Yes | Yes | **Twilio default.** 8-bit µ-law companding |
| `alaw` | Yes | Yes | Yes | 8-bit A-law companding (European telephony) |
| `opus` | Yes | Yes | Yes | Compressed, low-latency |
| `flac` | Yes | Yes | Yes | Lossless compressed |
| `mp3` | Yes | — | Yes | Lossy compressed |
| `mp4` | Yes | — | Yes | Container format |
| `aac` | Yes | — | Yes | Advanced Audio Coding |
| `amr-nb` | Yes | — | Yes | Narrowband (8kHz) |
| `amr-wb` | Yes | — | Yes | Wideband (16kHz) |
| `g729` | Yes | — | Yes | Low-bitrate codec |

### Sample Rates

| Sample Rate | Typical Use |
|-------------|------------|
| **8000 Hz** | **Telephone/Twilio** — standard PSTN quality |
| 16000 Hz | VoIP, wideband telephony |
| 22050 Hz | Intermediate quality |
| 44100 Hz | CD quality |
| 48000 Hz | Professional audio |

### Twilio → Deepgram Audio Path

Twilio media streams send audio as:
- **Encoding:** mulaw (µ-law)
- **Sample rate:** 8000 Hz
- **Channels:** 1 (mono)
- **Format:** Base64-encoded chunks in JSON WebSocket messages

**No conversion needed.** Deepgram natively accepts mulaw at 8kHz. Just:
1. Extract the `media.payload` from Twilio's WebSocket message
2. Base64-decode it to raw bytes
3. Send the raw bytes directly to Deepgram's WebSocket

```python
import base64

# From Twilio WebSocket message:
twilio_message = json.loads(raw_message)
if twilio_message["event"] == "media":
    audio_bytes = base64.b64decode(twilio_message["media"]["payload"])
    await deepgram_ws.send(audio_bytes)
```

### Containerized vs Raw Audio

- **Containerized audio** (WAV, MP3, FLAC, OGG, etc.): Deepgram auto-detects encoding and sample rate from the container headers. **Do not** specify `encoding` or `sample_rate`.
- **Raw audio** (no container): You **must** specify `encoding` and `sample_rate` query params. Twilio sends raw mulaw, so these params are required.

---

## 5. Smart Features for Voice Agents

### Feature Matrix

| Feature | Parameter | Adds Latency? | Use in Real-time? | Use Post-call? |
|---------|-----------|--------------|-------------------|---------------|
| **Punctuation** | `punctuate=true` | Minimal | **Yes** — essential for LLM input | Yes |
| **Smart Formatting** | `smart_format=true` | Minimal | **Yes** — numbers, currency, dates formatted properly | Yes |
| **Numerals** | `numerals=true` | Minimal | Yes | Yes |
| **Diarization** | `diarize=true` | Moderate | Only if needed. Reduces concurrent stream limit to 50 | **Yes** — essential for multi-speaker recordings |
| **Profanity Filter** | `profanity_filter=true` | Minimal | Optional | Optional |
| **Redaction** | `redact=pci` / `redact=ssn` | Minimal | If handling sensitive data | If handling sensitive data |
| **Filler Words** | `filler_words=true` | Minimal | No (adds noise for LLM) | Yes (for analysis) |
| **Entity Detection** | `detect_entities=true` | Moderate | No — use post-call | **Yes** |
| **Sentiment Analysis** | `sentiment=true` | Moderate | No — not available streaming | **Yes** |
| **Topic Detection** | `topics=true` | Moderate | No — not available streaming | **Yes** |
| **Intent Recognition** | `intents=true` | Moderate | No — not available streaming | **Yes** |
| **Summarization** | `summarize=true` | High | No — not available streaming | **Yes** |
| **Utterance Segmentation** | `utterances=true` | None | N/A (pre-recorded only) | **Yes** |

### Recommended for Real-time Voice Agents

```
punctuate=true&smart_format=true&interim_results=true&endpointing=300&utterance_end_ms=1000&vad_events=true
```

Keep features minimal for streaming to minimize latency. Do post-call processing with the full feature set.

### Recommended for Post-call Processing

```
punctuate=true&smart_format=true&diarize=true&utterances=true&sentiment=true&topics=true&summarize=v2&detect_entities=true
```

---

## 6. Text-to-Speech (TTS)

### Models

| Model Family | Architecture | Voices Available |
|-------------|-------------|-----------------|
| **Aura-2** | `aura-2` | 63+ voices (e.g., `aura-2-asteria-en`, `aura-2-zeus-en`, `aura-2-luna-en`, `aura-2-thalia-en`) |
| **Aura** (v1) | `aura` | Same voice names without the "2" |

Default: `aura-asteria-en`

### REST TTS (Single Request)

```
POST https://api.deepgram.com/v1/speak
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | enum | `aura-asteria-en` | Voice model (63 options) |
| `encoding` | enum | — | Output encoding: `linear16`, `mulaw`, `alaw`, `opus`, `flac`, `mp3`, `aac` (7 variants) |
| `sample_rate` | enum | varies by encoding | Output sample rate (5 variants) |
| `container` | enum | — | File format wrapper (5 variants) |
| `bit_rate` | enum/double | — | Bitrate (3 variants) |
| `callback` | string | — | Callback URL |
| `callback_method` | enum | `POST` | `POST` or `PUT` |
| `tag` | string(s) | — | Usage label |
| `mip_opt_out` | boolean | `false` | Opt out of MIP |

**Request body:**
```json
{"text": "Hello, welcome to Deepgram!"}
```

**Max body size:** 2MB. **Max character limit:** Documented in error responses.

**Response:** Binary audio data with the specified encoding.

### Streaming TTS (WebSocket)

```
wss://api.deepgram.com/v1/speak
```

**For real-time voice agents, use WebSocket TTS for lowest latency.**

**Query Parameters:**

| Parameter | Type | Default | Valid Values |
|-----------|------|---------|-------------|
| `model` | enum | `aura-asteria-en` | 63 voice models |
| `encoding` | enum | `linear16` | `linear16`, `mulaw`, `alaw` (streaming only supports these 3) |
| `sample_rate` | enum | `24000` | `8000`, `16000`, `24000`, `32000`, `48000` |

**For Twilio output:** Use `encoding=mulaw&sample_rate=8000` to match Twilio's expected audio format.

**Send Messages:**

```json
{"type": "Speak", "text": "Hello, world!"}
```
```json
{"type": "Flush"}
```
(Flush buffer and receive final audio for text sent so far)

```json
{"type": "Clear"}
```
(Clear buffer — destructive, discards unprocessed text)

```json
{"type": "Close"}
```
(Flush buffer then close connection)

**Receive Messages:**

- **Binary frames** — raw audio chunks as they're generated
- **Metadata:**
  ```json
  {
    "type": "Metadata",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "model_name": "aura-2-asteria-en",
    "model_version": "2024-01-18.29447",
    "model_uuid": "1842b5b2-ef26-4f13-bec5-48eaef70e9c0"
  }
  ```
- **Flushed:** `{"type": "Flushed", "sequence_id": 0}`
- **Cleared:** `{"type": "Cleared", "sequence_id": 0}`
- **Warning:** `{"type": "Warning", "description": "...", "code": "TEXT_LENGTH_WARNING"}`

### Deepgram TTS vs ElevenLabs

| Aspect | Deepgram Aura-2 | ElevenLabs |
|--------|-----------------|-----------|
| Latency | Very low — purpose-built for real-time agents | Low, but slightly higher network overhead |
| Streaming | Native WebSocket support with `linear16`/`mulaw`/`alaw` output | WebSocket support |
| Voice quality | Natural, good for IVR/phone calls | Best-in-class naturalness |
| Voice cloning | Not available | Available |
| Pricing | Competitive per-character | Higher per-character |
| Twilio integration | Native mulaw 8kHz output — zero conversion needed | Requires format conversion |
| Voice count | 63+ voices | 100+ voices + custom |

**For our Twilio pipeline:** Deepgram Aura-2 has an edge because it outputs mulaw at 8kHz natively, eliminating audio format conversion latency.

---

## 7. Authentication

### API Key Authentication

All requests use the `Authorization` header:

```
Authorization: Token YOUR_DEEPGRAM_API_KEY
```

- Create keys in the Deepgram Console
- All requests must be over HTTPS
- Requests without authentication fail
- Requests over plain HTTP fail

### Temporary Tokens (JWT)

For client-side or short-lived access, generate a temporary JWT:

```
POST https://api.deepgram.com/v1/auth/grant
```

**Request body:**
```json
{"ttl_seconds": 30}
```

- `ttl_seconds`: 1–3600 seconds. Default: 30 seconds.
- Requires an API key with Member or higher authorization
- Generated tokens have `usage::write` permission for core voice APIs only
- **Tokens do NOT work with Manage APIs**

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 30
}
```

Use the token as:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### API Key Management

```
POST   https://api.deepgram.com/v1/projects/:project_id/keys     # Create key
GET    https://api.deepgram.com/v1/projects/:project_id/keys     # List keys
GET    https://api.deepgram.com/v1/projects/:project_id/keys/:key_id  # Get key
DELETE https://api.deepgram.com/v1/projects/:project_id/keys/:key_id  # Delete key
```

Key properties: `api_key_id`, `key`, `comment`, `scopes` (e.g., `["member"]`, `["admin"]`), `tags`, `expiration_date`.

Filter by status: `?status=active` or `?status=expired`

### WebSocket Authentication

For WebSocket connections (`/v1/listen`, `/v1/speak`):

| Method | How |
|--------|-----|
| **Header (preferred)** | `Authorization: Token YOUR_API_KEY` |
| **Header (JWT)** | `Authorization: Bearer YOUR_JWT` |
| **Subprotocol** | `Sec-WebSocket-Protocol: token, YOUR_API_KEY` — for environments that don't support custom headers |

---

## 8. Rate Limits + Concurrency

### Pay As You Go Plan

| Service | Limit |
|---------|-------|
| **STT Streaming (Nova-2, Nova-3, Nova, Enhanced, Base)** | **150 concurrent** |
| **STT Streaming (Flux)** | **150 concurrent** |
| STT Pre-recorded (Nova-2, Nova-3, etc.) | 50 concurrent |
| STT Pre-recorded (Whisper Cloud) | 3 concurrent |
| STT Streaming with Diarization | **50 concurrent** (reduced from 150) |
| TTS REST (Aura, Aura-2) | 15 concurrent |
| TTS Streaming (Aura, Aura-2) | 45 concurrent |
| Voice Agent | 45 concurrent connections |
| Sentiment Analysis | 10 concurrent |
| Entity Detection | 5 concurrent |
| Intent Recognition | 10 concurrent |
| Summarization | 10 concurrent |
| Topic Detection | 10 concurrent |

### Growth Plan

| Service | Limit |
|---------|-------|
| **STT Streaming** | **225 concurrent** |
| **STT Streaming (Flux)** | **225 concurrent** |
| STT Pre-recorded | 50 concurrent |
| TTS REST | 15 concurrent |
| TTS Streaming | 60 concurrent |
| Voice Agent | 60 concurrent connections |

### Enterprise Plan

| Service | Starting Limit |
|---------|---------------|
| **STT Streaming** | **300 concurrent** |
| **STT Streaming (Flux)** | **300 concurrent** |
| STT Pre-recorded | 200 concurrent |
| STT Pre-recorded (Whisper) | 15 concurrent |
| TTS REST | 25 concurrent |
| TTS Streaming | 100 concurrent |
| Voice Agent | 100 concurrent connections |
| STT with Diarization | 100 concurrent |

Enterprise customers can request limit increases.

### What Happens When You Hit Limits

HTTP `429 Too Many Requests`:

```json
{
  "err_code": "TOO_MANY_REQUESTS",
  "err_msg": "Too many requests. Please try again later",
  "request_id": "uuid"
}
```

**Strategy:** Exponential-backoff retry.

**Important:** If you combine multiple features in one API call (e.g., STT + Sentiment Analysis), **the lower rate limit applies**.

---

## 9. Pricing

Deepgram pricing is per-minute of audio processed. Exact rates depend on your plan and are available on the Deepgram pricing page and in your console.

**Key pricing factors:**
- Model tier (Nova-3 > Nova-2 > Nova > Enhanced > Base)
- Streaming vs pre-recorded
- Additional features (diarization, intelligence features)
- MIP opt-out (`mip_opt_out=true`) increases pricing — opting out of the Model Improvement Program costs more

**Billing APIs:**

```
GET https://api.deepgram.com/v1/projects/:project_id/balances          # Get balances
GET https://api.deepgram.com/v1/projects/:project_id/balances/:balance_id  # Get specific balance
GET https://api.deepgram.com/v1/projects/:project_id/billing            # Usage breakdown
GET https://api.deepgram.com/v1/projects/:project_id/purchases          # Purchase history
```

**Usage tracking:**

```
GET https://api.deepgram.com/v1/projects/:project_id/usage              # Usage summary
GET https://api.deepgram.com/v1/projects/:project_id/usage/breakdown    # Detailed breakdown
GET https://api.deepgram.com/v1/projects/:project_id/requests           # Request history
```

---

## 10. Python SDK

### Installation

```bash
pip install deepgram-sdk
```

### Client Initialization

```python
from deepgram import DeepgramClient

# Standard endpoint
client = DeepgramClient(api_key="YOUR_API_KEY")

# EU endpoint
import httpx
client = DeepgramClient(
    api_key="YOUR_API_KEY",
    httpx_client=httpx.Client(base_url="https://api.eu.deepgram.com")
)

# Custom/dedicated endpoint
client = DeepgramClient(
    api_key="YOUR_API_KEY",
    httpx_client=httpx.Client(base_url="https://YOUR_DEDICATED_ENDPOINT")
)
```

### Live Transcription Example

```python
import asyncio
from deepgram import DeepgramClient, LiveTranscriptionEvents, LiveOptions

async def main():
    client = DeepgramClient(api_key="YOUR_API_KEY")

    connection = client.listen.asynclive.v("1")

    async def on_message(self, result, **kwargs):
        transcript = result.channel.alternatives[0].transcript
        if transcript:
            is_final = result.is_final
            speech_final = result.speech_final
            print(f"[{'FINAL' if is_final else 'INTERIM'}] {transcript}")
            if speech_final:
                print(f">>> Speech final — send to LLM")

    async def on_metadata(self, metadata, **kwargs):
        print(f"[META] {metadata}")

    async def on_speech_started(self, speech_started, **kwargs):
        print("[VAD] Speech started")

    async def on_utterance_end(self, utterance_end, **kwargs):
        print("[UTTERANCE END]")

    async def on_error(self, error, **kwargs):
        print(f"[ERROR] {error}")

    connection.on(LiveTranscriptionEvents.Transcript, on_message)
    connection.on(LiveTranscriptionEvents.Metadata, on_metadata)
    connection.on(LiveTranscriptionEvents.SpeechStarted, on_speech_started)
    connection.on(LiveTranscriptionEvents.UtteranceEnd, on_utterance_end)
    connection.on(LiveTranscriptionEvents.Error, on_error)

    options = LiveOptions(
        model="nova-2",
        encoding="mulaw",
        sample_rate=8000,
        channels=1,
        punctuate=True,
        smart_format=True,
        interim_results=True,
        endpointing=300,
        utterance_end_ms=1000,
        vad_events=True,
    )

    await connection.start(options)

    # Send audio chunks
    # await connection.send(audio_bytes)

    # Keep alive during silence
    # await connection.keep_alive()

    # Close
    # await connection.finish()

asyncio.run(main())
```

### Pre-recorded Example

```python
from deepgram import DeepgramClient, PrerecordedOptions

client = DeepgramClient(api_key="YOUR_API_KEY")

options = PrerecordedOptions(
    model="nova-2",
    punctuate=True,
    diarize=True,
    smart_format=True,
    utterances=True,
    sentiment=True,
)

# From URL
source = {"url": "https://example.com/audio.wav"}
response = client.listen.rest.v("1").transcribe_url(source, options)

# From file
with open("audio.wav", "rb") as f:
    source = {"buffer": f.read(), "mimetype": "audio/wav"}
    response = client.listen.rest.v("1").transcribe_file(source, options)

print(response.results.channels[0].alternatives[0].transcript)
```

### Error Handling

```python
from deepgram import DeepgramError, DeepgramApiError

try:
    response = client.listen.rest.v("1").transcribe_url(source, options)
except DeepgramApiError as e:
    print(f"API Error: {e.status_code} - {e.message}")
except DeepgramError as e:
    print(f"SDK Error: {e}")
```

---

## 11. Error Handling

### REST API Error Responses

| Status | Code | Meaning |
|--------|------|---------|
| 400 | `INVALID_JSON` | Malformed JSON body |
| 400 | `Bad Request` | Corrupt audio or missing Content-Type |
| 401 | `INVALID_AUTH` | Invalid API key |
| 401 | `INSUFFICIENT_PERMISSIONS` | Key lacks required permissions |
| 402 | `ASR_PAYMENT_REQUIRED` | Insufficient credits |
| 403 | `INSUFFICIENT_PERMISSIONS` | No access to requested model |
| 404 | `PROJECT_NOT_FOUND` | Invalid project ID |
| 408 | — | Request timeout |
| 413 | `PAYLOAD_TOO_LARGE` | Body exceeds 2MB (TTS) |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | Wrong Content-Type |
| 422 | `ASR_UNPROCESSABLE_ENTITY` | Incomplete/interrupted audio upload |
| 429 | `TOO_MANY_REQUESTS` | Rate limit exceeded |
| 500 | — | Internal server error |
| 502 | — | Bad gateway |
| 503 | — | Service unavailable |
| 504 | — | Gateway timeout |

### Standard Error Shape

```json
{
  "err_code": "ERROR_CODE",
  "err_msg": "Human-readable description",
  "request_id": "uuid"
}
```

### WebSocket Error Handling

WebSocket connections can fail in several ways:

1. **Connection rejected** — Bad auth, invalid params. Check the HTTP response on handshake failure.
2. **Error message received** — Deepgram sends error JSON over the WebSocket:
   ```json
   {
     "type": "Error",
     "description": "Failed to connect to external API",
     "code": "EXTERNAL_API_ERROR"
   }
   ```
3. **Connection dropped** — Network issues, server errors, idle timeout.

### Common Failure Modes

| Problem | Cause | Fix |
|---------|-------|-----|
| Garbage transcript / silence | `encoding` or `sample_rate` doesn't match actual audio | For Twilio: ensure `encoding=mulaw&sample_rate=8000` |
| `400 corrupt or unsupported data` | Sending URL in body without `Content-Type: application/json` | Set the header |
| Connection drops after silence | No audio or KeepAlive sent | Send `{"type": "KeepAlive"}` every 10s |
| `429 Too Many Requests` | Concurrent stream limit exceeded | Implement exponential backoff. Check your plan limits |
| `402 Payment Required` | Out of credits | Add funds in Console |
| Empty transcript | Audio too quiet, wrong format, or corrupted | Validate audio with ffprobe/Audacity |

### Reconnection Strategy for Long-running Streams

```python
import asyncio
import websockets

MAX_RETRIES = 5
BASE_DELAY = 1  # seconds

async def connect_with_retry():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            async with websockets.connect(DEEPGRAM_URL, extra_headers=headers) as ws:
                retries = 0  # Reset on successful connection
                await handle_stream(ws)
        except websockets.exceptions.ConnectionClosed as e:
            retries += 1
            delay = BASE_DELAY * (2 ** retries)
            print(f"Connection closed ({e.code}). Retry {retries}/{MAX_RETRIES} in {delay}s")
            await asyncio.sleep(delay)
        except Exception as e:
            retries += 1
            delay = BASE_DELAY * (2 ** retries)
            print(f"Error: {e}. Retry {retries}/{MAX_RETRIES} in {delay}s")
            await asyncio.sleep(delay)

    print("Max retries exceeded. Giving up.")
```

---

## 12. Integration Architecture for Voice Agents

### Pipeline Overview

```
Phone Call
    ↓
Twilio (receives PSTN audio)
    ↓
Twilio Media Stream (WebSocket)
  → 8kHz mulaw audio, base64-encoded chunks
    ↓
Your Server
  → base64-decode audio
  → Forward raw bytes to Deepgram
    ↓
Deepgram STT (WebSocket: /v1/listen)
  → encoding=mulaw, sample_rate=8000
  → Returns transcript with is_final, speech_final
    ↓
Your Server (transcript accumulation logic)
  → On speech_final or UtteranceEnd → send to LLM
    ↓
LLM (generates response text)
    ↓
Deepgram TTS (WebSocket: /v1/speak)
  → encoding=mulaw, sample_rate=8000
  → Returns audio chunks
    ↓
Your Server
  → base64-encode audio
  → Send via Twilio Media Stream
    ↓
Twilio → Phone
```

### Latency Budget

| Stage | Expected Latency |
|-------|-----------------|
| Twilio audio → your server | ~50–100ms (network) |
| Audio → Deepgram WebSocket | ~50ms (network) |
| Deepgram STT processing | ~200–500ms (depends on endpointing setting + model) |
| Transcript → LLM | ~50ms (network) |
| LLM generation | ~500–2000ms (depends on model/provider) |
| LLM text → Deepgram TTS | ~50ms (network) |
| Deepgram TTS generation | ~200–400ms (first byte) |
| TTS audio → Twilio → phone | ~100–200ms (network) |
| **Total end-to-end** | **~1.2–3.3 seconds** |

The biggest levers for latency reduction:
1. **Endpointing value** — Lower = faster trigger but riskier mid-sentence cuts
2. **LLM choice** — Fastest possible model for the task
3. **Streaming TTS** — Start sending audio to Twilio as LLM tokens arrive (don't wait for full response)
4. **Interim results** — Show "thinking" state immediately

### Using Interim Results for "Thinking" Indicators

```python
# When interim_results=true, you get rapid partial transcripts
# Use these to show the user the system is listening

if msg_type == "Results":
    transcript = data["channel"]["alternatives"][0]["transcript"]
    is_final = data.get("is_final", False)

    if not is_final and transcript:
        # Show typing indicator or partial text to indicate system is active
        show_thinking_indicator()

    if is_final:
        accumulated.append(transcript)

        if data.get("speech_final"):
            # NOW send to LLM
            full_text = " ".join(accumulated)
            send_to_llm(full_text)
            accumulated.clear()
```

### Barge-in Handling

Barge-in = the caller starts speaking while the AI agent is still talking (playing TTS audio).

**Detection:** Enable `vad_events=true`. When you receive a `SpeechStarted` event while TTS is playing:

```python
is_agent_speaking = False

async def on_speech_started():
    if is_agent_speaking:
        # BARGE-IN detected!
        # 1. Stop TTS playback
        await tts_ws.send(json.dumps({"type": "Clear"}))
        # 2. Stop sending TTS audio to Twilio
        stop_twilio_audio()
        # 3. Clear Twilio's audio buffer
        send_twilio_clear_message()
        is_agent_speaking = False

async def on_agent_started_speaking():
    is_agent_speaking = True

async def on_agent_audio_done():
    is_agent_speaking = False
```

### Custom Endpoints

| Environment | WebSocket URL |
|-------------|--------------|
| Standard | `wss://api.deepgram.com/v1/listen` |
| EU | `wss://api.eu.deepgram.com/v1/listen` |
| Dedicated | `wss://{SHORT_UID}.{REGION}.api.deepgram.com/v1/listen` |
| Self-hosted (HTTPS) | `wss://your-instance.com/v1/listen` |
| Self-hosted (HTTP) | `ws://your-instance.com:8080/v1/listen` |

**EU limitation:** Flux is not currently available in the EU region.

---

## Appendix A: Text Intelligence API

For analyzing text content (not audio):

```
POST https://api.deepgram.com/v1/read
```

Accepts `{"url": "..."}` or `{"text": "..."}`. Supports: sentiment, topics, intents, summarization with custom topics/intents.

## Appendix B: Voice Agent API

Deepgram offers a full voice agent WebSocket API that combines STT + LLM + TTS in a single connection:

```
wss://agent.deepgram.com/v1/agent/converse
```

This is an alternative to building the pipeline yourself. It handles STT → LLM → TTS internally. Key features:
- Configure STT (listen), LLM (think), and TTS (speak) providers in a single Settings message
- Supports function calling (server-side and client-side)
- Built-in barge-in handling
- Conversation context management
- Latency metrics in `AgentStartedSpeaking` events (`total_latency`, `tts_latency`, `ttt_latency`)

See the voice agent source docs for full message protocol.

## Appendix C: Manage API Endpoints

```
# Projects
GET    /v1/projects
GET    /v1/projects/:project_id
PATCH  /v1/projects/:project_id
DELETE /v1/projects/:project_id
DELETE /v1/projects/:project_id/leave

# Keys
POST   /v1/projects/:project_id/keys
GET    /v1/projects/:project_id/keys
GET    /v1/projects/:project_id/keys/:key_id
DELETE /v1/projects/:project_id/keys/:key_id

# Members
GET    /v1/projects/:project_id/members
DELETE /v1/projects/:project_id/members/:member_id
GET    /v1/projects/:project_id/members/:member_id/scopes
PUT    /v1/projects/:project_id/members/:member_id/scopes

# Invites
POST   /v1/projects/:project_id/invites
GET    /v1/projects/:project_id/invites
DELETE /v1/projects/:project_id/invites/:email

# Models
GET    /v1/models
GET    /v1/models/:model_id
GET    /v1/projects/:project_id/models
GET    /v1/projects/:project_id/models/:model_id

# Usage & Billing
GET    /v1/projects/:project_id/usage
GET    /v1/projects/:project_id/usage/breakdown
GET    /v1/projects/:project_id/usage/fields
GET    /v1/projects/:project_id/requests
GET    /v1/projects/:project_id/requests/:request_id
GET    /v1/projects/:project_id/balances
GET    /v1/projects/:project_id/balances/:balance_id
GET    /v1/projects/:project_id/billing
GET    /v1/projects/:project_id/purchases

# Self-hosted Distribution Credentials
POST   /v1/projects/:project_id/self-hosted/distribution/credentials
GET    /v1/projects/:project_id/self-hosted/distribution/credentials
GET    /v1/projects/:project_id/self-hosted/distribution/credentials/:credential_id
DELETE /v1/projects/:project_id/self-hosted/distribution/credentials/:credential_id

# Auth
POST   /v1/auth/grant
```
