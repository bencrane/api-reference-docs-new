# ElevenLabs API — Canonical Engineering Reference

> **Purpose:** Definitive engineering reference for all ElevenLabs TTS integration. Covers two critical use cases: (1) real-time streaming TTS in a live voice agent pipeline where an LLM generates text and ElevenLabs converts it to speech streamed back to a phone caller with minimal latency, and (2) offline high-quality audio generation for pre-recorded voicemail drops played via Twilio. This document is the single source of truth for every integration decision, parameter choice, and latency optimization.

---

## Table of Contents

1. [Models Inventory](#1-models-inventory)
2. [REST TTS API — Complete Specification](#2-rest-tts-api--complete-specification)
3. [Streaming TTS via WebSocket — Complete Protocol](#3-streaming-tts-via-websocket--complete-protocol)
4. [REST Streaming TTS](#4-rest-streaming-tts)
5. [Voices — Complete Management](#5-voices--complete-management)
6. [Voice Cloning — Complete Guide](#6-voice-cloning--complete-guide)
7. [Voice Design / Voice Generation](#7-voice-design--voice-generation)
8. [Pronunciation Control](#8-pronunciation-control)
9. [Audio Output Formats — Deep Dive](#9-audio-output-formats--deep-dive)
10. [Authentication](#10-authentication)
11. [Rate Limits + Concurrency](#11-rate-limits--concurrency)
12. [Pricing](#12-pricing)
13. [Python SDK](#13-python-sdk)
14. [Error Handling](#14-error-handling)
15. [Pre-generating Audio for Voicemail Drops](#15-pre-generating-audio-for-voicemail-drops)
16. [Real-time Voice Agent Integration Architecture](#16-real-time-voice-agent-integration-architecture)

---

## 1. Models Inventory

### TTS Models

| Model ID | Quality | Latency | Streaming | Best For |
|----------|---------|---------|-----------|----------|
| `eleven_multilingual_v2` | Highest quality, most natural | Higher latency | Yes | Voicemail drops, offline generation, quality-critical audio |
| `eleven_v3` | High quality | Moderate | Yes | General purpose, good balance |
| `eleven_flash_v2_5` | Good quality | Lowest latency | Yes | Real-time voice agents, latency-critical applications |

### Speech-to-Speech Models

| Model ID | Description |
|----------|-------------|
| `eleven_english_sts_v2` | Default STS model, English |
| `eleven_multilingual_sts_v2` | Multilingual STS |

### Other Models

| Model ID | Use Case |
|----------|----------|
| `eleven_text_to_sound_v2` | Sound effects generation |
| `music_v1` | Music generation |

### Model Response Object Properties

| Property | Type | Description |
|----------|------|-------------|
| `model_id` | string (required) | Unique identifier |
| `name` | string | Display name |
| `can_be_finetuned` | boolean | Fine-tuning support |
| `can_do_text_to_speech` | boolean | TTS capability |
| `can_do_voice_conversion` | boolean | Voice conversion capability |
| `can_use_style` | boolean | Style parameter support |
| `can_use_speaker_boost` | boolean | Speaker boost support |
| `serves_pro_voices` | boolean | Pro voice availability |
| `token_cost_factor` | number | Cost multiplier |
| `max_characters_request_free_user` | integer | Free tier char limit per request |
| `max_characters_request_subscribed_user` | integer | Paid tier char limit per request |
| `maximum_text_length_per_request` | integer | Absolute max text length |
| `languages` | array | Supported languages (`{id, name}`) |
| `model_rates` | object | `character_cost_multiplier` |
| `concurrency_group` | string | Concurrency classification |

### Recommendation

- **Real-time voice agents (latency-critical):** Use `eleven_flash_v2_5`. Lowest time-to-first-byte. Text normalization on this model requires Enterprise plan.
- **Voicemail drops (quality-critical, latency irrelevant):** Use `eleven_multilingual_v2`. Highest quality and naturalness. Best for pre-recorded content where generation time doesn't matter.
- **General purpose:** Use `eleven_v3` for a balance of quality and speed.

### List Models Endpoint

```
GET https://api.elevenlabs.io/v1/models
```

Auth: Optional `xi-api-key` header. Returns array of model objects.

---

## 2. REST TTS API — Complete Specification

### Endpoint

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
```

- **Content-Type:** `application/json`
- **Response:** `application/octet-stream` (binary audio data)

### Authentication

Header: `xi-api-key: YOUR_API_KEY`

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `voice_id` | string | Yes | Voice identifier. Example: `JBFqnCBsd6RMkjVDRZzb` |

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enable_logging` | boolean | `true` | When `false`, zero retention mode (Enterprise only). History and stitching unavailable. |
| `optimize_streaming_latency` | integer | None | `0`=default, `1`=normal (~50% latency reduction), `2`=strong (~75%), `3`=max, `4`=max + no text normalizer |
| `output_format` | string | `mp3_44100_128` | Audio output format. See [Audio Output Formats](#9-audio-output-formats--deep-dive). |

### Request Body

| Property | Type | Default | Required | Description |
|----------|------|---------|----------|-------------|
| `text` | string | — | **Yes** | Text to convert to speech |
| `model_id` | string | `eleven_multilingual_v2` | No | Model identifier string |
| `language_code` | string | — | No | ISO 639-1 language code (for multilingual models) |
| `voice_settings` | object | — | No | Override stored voice settings (see below) |
| `pronunciation_dictionary_locators` | array | — | No | Up to 3 pronunciation dictionaries (`{pronunciation_dictionary_id, version_id}`) |
| `seed` | integer | — | No | 0–4294967295. Deterministic sampling (not guaranteed identical across versions) |
| `previous_text` | string | — | No | Text before current segment for continuity |
| `next_text` | string | — | No | Text after current segment for continuity |
| `previous_request_ids` | array[string] | — | No | Max 3 request IDs for audio stitching (overrides `previous_text`) |
| `next_request_ids` | array[string] | — | No | Max 3 request IDs for audio stitching (overrides `next_text`) |
| `use_pvc_as_ivc` | boolean | `false` | No | Use IVC version of PVC voice (latency workaround) |
| `apply_text_normalization` | string | `auto` | No | `auto`, `on`, or `off` |
| `apply_language_text_normalization` | boolean | `false` | No | Language-specific normalization (currently Japanese only; increases latency) |

### VoiceSettings Object

| Property | Type | Range | Description |
|----------|------|-------|-------------|
| `stability` | number | 0.0–1.0 | Lower = broader emotional range, more expressive. Higher = more consistent, monotonous. **Recommended for phone: 0.5** |
| `similarity_boost` | number | 0.0–1.0 | How closely AI adheres to original voice. Higher = more faithful. **Recommended: 0.75** |
| `style` | number | 0.0–1.0 | Style exaggeration. Non-zero adds latency. Not available on all models (check `can_use_style`). **For real-time: 0** |
| `use_speaker_boost` | boolean | — | Enhances speaker similarity. Adds latency. **For real-time: false** |
| `speed` | number | — | 1.0 = default. <1.0 = slower, >1.0 = faster |

### Response Headers

| Header | Description |
|--------|-------------|
| `x-character-count` | Character cost of this generation |
| `request-id` | Unique request identifier (use for stitching via `previous_request_ids`) |

### With Timestamps Variant

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps
```

Returns JSON instead of binary:

```json
{
  "audio_base64": "base64-encoded-audio",
  "alignment": {
    "characters": ["H", "e", "l", "l", "o"],
    "character_start_times_seconds": [0.0, 0.05, 0.1, 0.15, 0.2],
    "character_end_times_seconds": [0.05, 0.1, 0.15, 0.2, 0.3]
  },
  "normalized_alignment": {
    "characters": ["H", "e", "l", "l", "o"],
    "character_start_times_seconds": [0.0, 0.05, 0.1, 0.15, 0.2],
    "character_end_times_seconds": [0.05, 0.1, 0.15, 0.2, 0.3]
  }
}
```

### Python Code Example — Generate Voicemail Drop

```python
import requests

XI_API_KEY = "your_api_key"
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
    headers={
        "xi-api-key": XI_API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "text": "Hi, this is a message from our team. We wanted to reach out regarding your recent inquiry. Please call us back at your earliest convenience.",
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8,
            "style": 0.2,
            "use_speaker_boost": True
        }
    },
    params={
        "output_format": "mp3_44100_128"  # Twilio <Play> compatible
    }
)

with open("voicemail_drop.mp3", "wb") as f:
    f.write(response.content)
```

### Python Code Example — Streaming Response

```python
import requests

response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream",
    headers={"xi-api-key": XI_API_KEY, "Content-Type": "application/json"},
    json={"text": "Hello world", "model_id": "eleven_flash_v2_5"},
    params={"output_format": "ulaw_8000"},
    stream=True
)

for chunk in response.iter_content(chunk_size=4096):
    if chunk:
        process_audio_chunk(chunk)
```

---

## 3. Streaming TTS via WebSocket — Complete Protocol

This is the lowest-latency path for real-time voice agents. The LLM generates text token-by-token, tokens are streamed to ElevenLabs, and audio comes back in real-time.

### Connection URL

```
wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input
```

### Regional Endpoints

| Region | WebSocket URL |
|--------|---------------|
| Default | `wss://api.elevenlabs.io/` |
| US | `wss://api.us.elevenlabs.io/` |
| EU Residency | `wss://api.eu.residency.elevenlabs.io/` |
| India Residency | `wss://api.in.residency.elevenlabs.io/` |

### Authentication Methods (choose one)

1. `xi-api-key` header on WebSocket connection
2. `authorization` query parameter (bearer token)
3. `single_use_token` query parameter
4. `xi-api-key` field in first WebSocket message
5. `authorization` field in first WebSocket message

### Query Parameters (on connection URL)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model_id` | string | — | Model identifier (e.g., `eleven_flash_v2_5`) |
| `language_code` | string | — | ISO 639-1 language code |
| `enable_logging` | boolean | `true` | Zero retention when `false` (Enterprise) |
| `enable_ssml_parsing` | boolean | `false` | Enable SSML tag parsing |
| `output_format` | string | — | See WebSocket-specific formats below |
| `inactivity_timeout` | integer | `20` | Seconds before timeout on inactivity |
| `sync_alignment` | boolean | `false` | Synchronous alignment data |
| `auto_mode` | boolean | `false` | Auto mode |
| `apply_text_normalization` | string | `auto` | `auto`, `on`, `off` |
| `seed` | integer | — | Deterministic sampling |
| `optimize_streaming_latency` | integer | — | 0–4 (same as REST) |

### WebSocket-Specific Output Formats

```
mp3_22050_32, mp3_44100_32, mp3_44100_64, mp3_44100_96,
mp3_44100_128, mp3_44100_192, pcm_8000, pcm_16000, pcm_22050,
pcm_24000, pcm_44100, ulaw_8000, alaw_8000, opus_48000_32,
opus_48000_64, opus_48000_96, opus_48000_128, opus_48000_192
```

**For Twilio media streams:** Use `ulaw_8000` — this is native Twilio format, no conversion needed.

### Client → Server Messages

#### 1. InitializeConnection (first message)

```json
{
  "text": " ",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0,
    "use_speaker_boost": false,
    "speed": 1.0
  },
  "generation_config": {
    "chunk_length_schedule": [120, 160, 250, 290]
  },
  "pronunciation_dictionary_locators": [
    {"pronunciation_dictionary_id": "...", "version_id": "..."}
  ],
  "xi-api-key": "your_api_key",
  "authorization": "Bearer your_token"
}
```

**Critical details:**
- `text` **must** be `" "` (single space) in the first message
- `xi-api-key` and `authorization` are only valid in the first message
- `pronunciation_dictionary_locators` can only be set in the first message
- `chunk_length_schedule` controls audio chunk sizes. Default: `[120, 160, 250, 290]`. Each value range: 50–500. Lower values = smaller chunks = lower latency but more overhead.

#### 2. SendText (subsequent messages)

```json
{
  "text": "Hello world ",
  "try_trigger_generation": false,
  "flush": false
}
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `text` | string | — | Text chunk. Should end with a single space. |
| `try_trigger_generation` | boolean | `false` | Attempt immediate audio generation if buffer meets minimum threshold. Set `true` for lower latency at cost of slightly less natural prosody. |
| `flush` | boolean | `false` | Force generation of all remaining buffered text. Use when done sending text but keeping connection open for next utterance. |

**Chunking strategy for voice agents:**
- Send text after each complete sentence or natural phrase boundary
- Setting `try_trigger_generation: true` on each chunk reduces latency
- Use `flush: true` after the final chunk of an utterance to force remaining audio out
- Text should end with a space for proper word boundary detection

#### 3. CloseConnection (final message)

```json
{
  "text": ""
}
```

Empty string signals end of input and closes the stream.

### Server → Client Messages

#### AudioOutput

```json
{
  "audio": "base64-encoded-audio-chunk",
  "normalizedAlignment": {
    "charStartTimesMs": [0, 3, 7, 12],
    "charDurationsMs": [3, 4, 5, 6],
    "chars": ["H", "e", "l", "l"]
  },
  "alignment": {
    "charStartTimesMs": [0, 3, 7, 12],
    "charDurationsMs": [3, 4, 5, 6],
    "chars": ["H", "e", "l", "l"]
  }
}
```

- `audio`: Base64-encoded audio chunk in the format specified by `output_format`
- `alignment` / `normalizedAlignment`: Character-level timing data (only when `sync_alignment: true`)

#### FinalOutput

```json
{
  "isFinal": true
}
```

Received after the last audio chunk. The stream is complete.

### Multi-Stream Input WebSocket

```
wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/multi-stream-input
```

For managing multiple concurrent streams over a single WebSocket connection.

### Full Working Python Code Example — Real-time WebSocket TTS

```python
import asyncio
import websockets
import json
import base64

XI_API_KEY = "your_api_key"
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

async def text_to_speech_stream(text_chunks):
    """Stream text to ElevenLabs and receive audio in real-time."""
    uri = (
        f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input"
        f"?model_id=eleven_flash_v2_5"
        f"&output_format=ulaw_8000"
        f"&optimize_streaming_latency=3"
    )

    async with websockets.connect(uri) as ws:
        # 1. Initialize connection
        init_msg = {
            "text": " ",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0,
                "use_speaker_boost": False
            },
            "generation_config": {
                "chunk_length_schedule": [120, 160, 250, 290]
            },
            "xi-api-key": XI_API_KEY
        }
        await ws.send(json.dumps(init_msg))

        # 2. Start receive task
        async def receive_audio():
            audio_chunks = []
            async for message in ws:
                data = json.loads(message)
                if data.get("audio"):
                    audio_bytes = base64.b64decode(data["audio"])
                    audio_chunks.append(audio_bytes)
                    # In a voice agent, send audio_bytes to Twilio here
                if data.get("isFinal"):
                    break
            return audio_chunks

        receive_task = asyncio.create_task(receive_audio())

        # 3. Send text chunks (simulating LLM token stream)
        for i, chunk in enumerate(text_chunks):
            is_last = (i == len(text_chunks) - 1)
            msg = {
                "text": chunk + " ",
                "try_trigger_generation": True,
                "flush": is_last
            }
            await ws.send(json.dumps(msg))

        # 4. Close the stream
        await ws.send(json.dumps({"text": ""}))

        # 5. Wait for all audio
        audio_chunks = await receive_task
        return b"".join(audio_chunks)

# Usage
text_chunks = [
    "Hello,",
    "thank you for calling.",
    "How can I help you today?"
]
audio = asyncio.run(text_to_speech_stream(text_chunks))
```

---

## 4. REST Streaming TTS

### Endpoint

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream
```

- **Content-Type:** `application/json`
- **Response:** `application/octet-stream` (chunked transfer encoding)

### How It Differs from WebSocket Streaming

| Aspect | REST Streaming | WebSocket Streaming |
|--------|---------------|-------------------|
| Protocol | HTTP chunked transfer | WebSocket frames |
| Text input | Single complete text | Token-by-token streaming |
| Latency | Higher (full text must be sent first) | Lower (text streams in, audio streams out) |
| Best for | Pre-known text, simpler integration | LLM token streaming, lowest latency |
| Connection overhead | New HTTP connection per request | Persistent connection |

**Use REST streaming** when you have the complete text upfront and want simpler code.
**Use WebSocket streaming** when the LLM is generating text token-by-token.

### Parameters

Same as the non-streaming REST TTS endpoint (Section 2). All parameters apply.

### Stream With Timestamps

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream/with-timestamps
```

### Python SDK Example

```python
from elevenlabs import stream
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your_api_key")
audio_stream = client.text_to_speech.stream(
    text="This is a streaming test",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_flash_v2_5"
)

# Play directly
stream(audio_stream)

# Or process chunks
for chunk in audio_stream:
    if isinstance(chunk, bytes):
        process_audio(chunk)
```

---

## 5. Voices — Complete Management

### List All Voices (v2)

```
GET https://api.elevenlabs.io/v2/voices
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page_size` | integer | 10 | Max 100 |
| `next_page_token` | string | — | Pagination token |
| `search` | string | — | Search term |
| `sort` | string | — | `created_at_unix` or `name` |
| `sort_direction` | string | — | Sort direction |
| `voice_type` | string | — | `personal`, `community`, `default`, `workspace`, `non-default`, `saved` |
| `category` | string | — | `premade`, `cloned`, `generated`, `professional` |
| `fine_tuning_state` | string | — | `draft`, `not_verified`, `not_started`, `queued`, `fine_tuning`, `fine_tuned`, `failed`, `delayed` |
| `collection_id` | string | — | Filter by collection |
| `include_total_count` | boolean | — | Include total in response |
| `voice_ids` | array | — | Up to 100 specific IDs |

**Response:**

```json
{
  "voices": [Voice],
  "has_more": true,
  "total_count": 150,
  "next_page_token": "..."
}
```

### Voice Object Structure

```json
{
  "voice_id": "JBFqnCBsd6RMkjVDRZzb",
  "name": "George",
  "category": "premade",
  "description": "Warm, friendly male voice",
  "labels": {"accent": "american", "gender": "male", "age": "middle_aged"},
  "preview_url": "https://...",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0,
    "use_speaker_boost": true,
    "speed": 1.0
  },
  "fine_tuning": { "state": "fine_tuned" },
  "sharing": { "status": "enabled" }
}
```

### Get Specific Voice

```
GET https://api.elevenlabs.io/v1/voices/{voice_id}
```

### Get Voice Settings

```
GET https://api.elevenlabs.io/v1/voices/{voice_id}/settings
```

### Get Default Voice Settings

```
GET https://api.elevenlabs.io/v1/voices/settings/default
```

### Edit Voice Settings

```
POST https://api.elevenlabs.io/v1/voices/{voice_id}/settings/edit
```

Body: VoiceSettings object.

### Edit Voice

```
POST https://api.elevenlabs.io/v1/voices/{voice_id}/edit
Content-Type: multipart/form-data
```

- `name` (string, required)
- `files` (array[binary], optional)
- `remove_background_noise` (boolean, default false)
- `description`, `labels` (optional)

### Delete Voice

```
DELETE https://api.elevenlabs.io/v1/voices/{voice_id}
```

### Voice Library (Shared Voices)

```
GET https://api.elevenlabs.io/v1/shared-voices
```

Query: `page_size` (default 30, max 100), `category` (professional/famous/high_quality), `gender`, `age`, `accent`, `language`, `locale`, `search`, `use_cases`, `featured`, `owner_id`, `page` (default 0).

### Add Shared Voice to Account

```
POST https://api.elevenlabs.io/v1/voices/add/{public_user_id}/{voice_id}
```

Body: `{ "new_name": "My Voice Name", "bookmarked": true }`

### Find Similar Voices

```
POST https://api.elevenlabs.io/v1/similar-voices
Content-Type: multipart/form-data
```

- `audio_file` (binary, required)
- `similarity_threshold` (number, 0–2, lower = more similar)
- `top_k` (integer, 1–100)

### Voice Settings Deep Dive

**For phone conversations (natural, warm, professional):**
- `stability`: 0.5–0.6 (some variation for naturalness, not too wild)
- `similarity_boost`: 0.75–0.85 (faithful to voice character)
- `style`: 0 (zero for real-time to avoid latency hit)
- `use_speaker_boost`: false (for real-time), true (for voicemail drops)
- `speed`: 1.0 (natural pace)

**For energetic/salesperson persona:**
- `stability`: 0.3–0.4 (more expressive range)
- `similarity_boost`: 0.7
- `style`: 0.3 (offline only — adds latency)
- `speed`: 1.1

**For calm, authoritative tone:**
- `stability`: 0.7–0.8
- `similarity_boost`: 0.8
- `style`: 0
- `speed`: 0.95

---

## 6. Voice Cloning — Complete Guide

### Instant Voice Cloning (IVC)

```
POST https://api.elevenlabs.io/v1/voices/add
Content-Type: multipart/form-data
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Display name for the voice |
| `files` | array[binary] | Yes | Audio recordings for cloning |
| `remove_background_noise` | boolean | No (default false) | Apply audio isolation preprocessing |
| `description` | string | No | Voice description |
| `labels` | object/string | No | Metadata: language, accent, gender, age |

**Response:**

```json
{
  "voice_id": "new_voice_id_string",
  "requires_verification": false
}
```

**Audio Sample Requirements:**
- Multiple samples recommended for better quality
- Clean audio with minimal background noise
- Consistent recording conditions across samples
- Single speaker per sample set

### Professional Voice Cloning (PVC)

Higher quality than IVC. Requires more audio, has a training step.

**Step 1 — Create PVC Voice (metadata):**

```
POST https://api.elevenlabs.io/v1/voices/pvc
```

Body: `{ "name": "Brand Voice", "language": "en", "description": "...", "labels": {} }`
Response: `{ "voice_id": "..." }`

**Step 2 — Add Samples:**

```
POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples
Content-Type: multipart/form-data
```

- `files` (array, required)
- `remove_background_noise` (boolean, default false)

**Step 3 — (Optional) Speaker Separation:**

```
POST /v1/voices/pvc/{voice_id}/samples/{sample_id}/separate-speakers
GET  /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers  # status: not_started, pending, completed, failed
GET  /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio
```

**Step 4 — Train:**

```
POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/train
```

Body: `{ "model_id": "eleven_multilingual_v2" }`

**PVC Verification (consent):**

```
GET  /v1/voices/pvc/{voice_id}/captcha           # Get captcha text
POST /v1/voices/pvc/{voice_id}/captcha           # Submit recording (multipart)
POST /v1/voices/pvc/{voice_id}/verification      # Manual verification (multipart files)
```

### Delete Voice

```
DELETE https://api.elevenlabs.io/v1/voices/{voice_id}
```

### Full Working Code — Clone and Use Voice

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your_api_key")

# Clone a voice from audio samples
with open("sample1.mp3", "rb") as f1, open("sample2.mp3", "rb") as f2:
    voice = client.voices.add(
        name="Brand Voice",
        files=[f1, f2],
        remove_background_noise=True,
        description="Professional warm male voice for outbound calls"
    )

# Use the cloned voice
audio = client.text_to_speech.convert(
    voice_id=voice.voice_id,
    text="Hello, this is a test of the cloned voice.",
    model_id="eleven_multilingual_v2"
)

with open("cloned_output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)
```

---

## 7. Voice Design / Voice Generation

Create voices from text descriptions — no audio samples needed.

### Design Voice Preview

```
POST https://api.elevenlabs.io/v1/text-to-voice/design
```

### Remix Existing Voice

```
POST https://api.elevenlabs.io/v1/text-to-voice/{voice_id}/remix
```

### Stream Voice Design

```
POST https://api.elevenlabs.io/v1/text-to-voice/stream
```

### Create Voice from Preview

```
POST https://api.elevenlabs.io/v1/text-to-voice
```

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `voice_name` | string | Yes | Name for the created voice |
| `voice_description` | string | Yes | Description |
| `generated_voice_id` | string | Yes | From `/design` or `/remix` preview |
| `labels` | object | No | Metadata key-value pairs |
| `played_not_selected_voice_ids` | array[string] | No | For RLHF feedback |

Response: Full Voice object with `voice_id`.

---

## 8. Pronunciation Control

### SSML Support

Enable via `enable_ssml_parsing: true` query parameter on WebSocket connections.

**Note:** SSML parsing is available on WebSocket TTS, not on REST TTS endpoints.

### Pronunciation Dictionaries

#### Create from File (PLS Lexicon)

```
POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file
Content-Type: multipart/form-data
```

- `name` (string, required)
- `file` (binary, `.pls` lexicon file)
- `description` (string, optional)
- `workspace_access` (enum: `admin`, `editor`, `commenter`, `viewer`)

#### Create from Rules

```
POST https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-rules
```

```json
{
  "rules": [
    {
      "type": "alias",
      "string_to_replace": "FMCSA",
      "alias": "F-M-C-S-A",
      "case_sensitive": true,
      "word_boundaries": true
    },
    {
      "type": "phoneme",
      "string_to_replace": "DOT",
      "phoneme": "diːoʊtiː",
      "alphabet": "ipa",
      "case_sensitive": true,
      "word_boundaries": true
    }
  ],
  "name": "Trucking Industry Terms"
}
```

**Rule Types:**

| Type | Fields | Description |
|------|--------|-------------|
| `alias` | `string_to_replace`, `alias`, `case_sensitive` (default true), `word_boundaries` (default true) | Replace text with phonetic alias |
| `phoneme` | `string_to_replace`, `phoneme`, `alphabet` (e.g., `"ipa"`), `case_sensitive`, `word_boundaries` | Specify exact phonetic pronunciation |

**Response:**

```json
{
  "id": "dict_id",
  "name": "Trucking Industry Terms",
  "created_by": "user_id",
  "creation_time_unix": 1700000000,
  "version_id": "version_id",
  "version_rules_num": 2,
  "description": "...",
  "permission_on_resource": "admin"
}
```

#### Other Dictionary Endpoints

```
GET  /v1/pronunciation-dictionaries/{id}                    # Get dictionary
GET  /v1/pronunciation-dictionaries/{id}/{version}/download  # Download PLS file
GET  /v1/pronunciation-dictionaries                          # List all
POST /v1/pronunciation-dictionaries/{id}/rules               # Add/remove rules
```

#### Using Dictionaries in TTS Requests

Pass in `pronunciation_dictionary_locators` (up to 3):

```json
{
  "pronunciation_dictionary_locators": [
    {
      "pronunciation_dictionary_id": "dict_id",
      "version_id": "version_id"
    }
  ]
}
```

### Text Normalization

| Parameter | Values | Description |
|-----------|--------|-------------|
| `apply_text_normalization` | `auto` (default), `on`, `off` | General text normalization (numbers, dates, currency) |
| `apply_language_text_normalization` | `true`, `false` (default) | Language-specific normalization. Currently Japanese only. Adds latency. |

**Note:** For `eleven_flash_v2_5`, text normalization requires Enterprise plan.

---

## 9. Audio Output Formats — Deep Dive

### All Supported Format Strings

#### REST TTS (including with-timestamps)

| Format String | Codec | Sample Rate | Bitrate/Depth | Notes |
|---------------|-------|-------------|---------------|-------|
| `mp3_22050_32` | MP3 | 22.05 kHz | 32 kbps | Smallest MP3 |
| `mp3_24000_48` | MP3 | 24 kHz | 48 kbps | |
| `mp3_44100_32` | MP3 | 44.1 kHz | 32 kbps | |
| `mp3_44100_64` | MP3 | 44.1 kHz | 64 kbps | |
| `mp3_44100_96` | MP3 | 44.1 kHz | 96 kbps | |
| `mp3_44100_128` | MP3 | 44.1 kHz | 128 kbps | **DEFAULT** |
| `mp3_44100_192` | MP3 | 44.1 kHz | 192 kbps | Creator+ tier |
| `pcm_8000` | PCM | 8 kHz | 16-bit | |
| `pcm_16000` | PCM | 16 kHz | 16-bit | |
| `pcm_22050` | PCM | 22.05 kHz | 16-bit | |
| `pcm_24000` | PCM | 24 kHz | 16-bit | |
| `pcm_32000` | PCM | 32 kHz | 16-bit | |
| `pcm_44100` | PCM | 44.1 kHz | 16-bit | Pro+ tier |
| `pcm_48000` | PCM | 48 kHz | 16-bit | |
| `ulaw_8000` | μ-law | 8 kHz | 8-bit | **Twilio media streams** |
| `alaw_8000` | A-law | 8 kHz | 8-bit | |
| `wav_8000` | WAV | 8 kHz | 16-bit | REST only |
| `wav_16000` | WAV | 16 kHz | 16-bit | REST only |
| `wav_22050` | WAV | 22.05 kHz | 16-bit | REST only |
| `wav_24000` | WAV | 24 kHz | 16-bit | REST only |
| `wav_32000` | WAV | 32 kHz | 16-bit | REST only |
| `wav_44100` | WAV | 44.1 kHz | 16-bit | REST only, Pro+ |
| `wav_48000` | WAV | 48 kHz | 16-bit | REST only |
| `opus_48000_32` | Opus | 48 kHz | 32 kbps | |
| `opus_48000_64` | Opus | 48 kHz | 64 kbps | |
| `opus_48000_96` | Opus | 48 kHz | 96 kbps | |
| `opus_48000_128` | Opus | 48 kHz | 128 kbps | |
| `opus_48000_192` | Opus | 48 kHz | 192 kbps | |

#### WebSocket TTS (no WAV formats)

All formats above **except** WAV formats. WebSocket does not support WAV output.

### Twilio Compatibility

| Twilio Use Case | Recommended Format | Notes |
|-----------------|-------------------|-------|
| `<Play>` TwiML verb | `mp3_44100_128` | Twilio supports MP3 and WAV playback |
| `<Play>` TwiML verb (alt) | `wav_8000` or `wav_16000` | WAV also works, larger files |
| Media Streams (real-time) | `ulaw_8000` | **Native Twilio media stream format.** No conversion needed. |

**Yes, ElevenLabs can output `ulaw_8000` directly.** The exact format string is `ulaw_8000`. This is the ideal format for Twilio media streams — zero transcoding overhead.

### Tier Restrictions

| Format | Minimum Tier |
|--------|-------------|
| `mp3_44100_192` | Creator |
| `pcm_44100` | Pro |
| `wav_44100` | Pro |

---

## 10. Authentication

### REST API Authentication

**Header:** `xi-api-key: YOUR_API_KEY`

```python
headers = {"xi-api-key": "your_api_key"}
```

### WebSocket Authentication (5 methods)

1. **Header:** `xi-api-key` header on WebSocket handshake
2. **Query parameter:** `?authorization=Bearer+YOUR_TOKEN`
3. **Query parameter:** `?single_use_token=TOKEN`
4. **First message field:** `"xi-api-key": "your_api_key"` in init JSON
5. **First message field:** `"authorization": "Bearer your_token"` in init JSON

### Single-Use Tokens (for client-side apps)

```
POST https://api.elevenlabs.io/v1/single-use-token/{token_type}
```

Token types: `realtime_scribe`, `tts_websocket`

Response: `{ "token": "..." }` — expires after 15 minutes, consumed on first use.

**Use case:** Generate server-side, pass to browser client for WebSocket connection. Never expose API key in client-side code.

### API Key Features

- Scope restrictions (limit to specific endpoints)
- Credit quotas per key
- Multiple keys per account
- Service accounts for programmatic access

### SDK Initialization

```python
from elevenlabs.client import ElevenLabs
client = ElevenLabs(api_key="your_api_key")
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
const client = new ElevenLabsClient({ apiKey: 'your_api_key' });
```

---

## 11. Rate Limits + Concurrency

### Concurrency

- Models have a `concurrency_group` property that determines concurrency limits
- Concurrent connections are limited per subscription tier
- Each simultaneous voice agent call requires its own connection

### Usage Monitoring

```
GET https://api.elevenlabs.io/v1/usage/character-stats
```

Available metrics: `credits`, `tts_characters`, `minutes_used`, `request_count`, `ttfb_avg`, `ttfb_p95`, `fiat_units_spent`, `concurrency`, `concurrency_average`

Breakdown by: `voice`, `voice_multiplier`, `user`, `groups`, `api_keys`, `all_api_keys`, `product_type`, `model`, `resource`, `request_queue`, `region`, `subresource_id`, `reporting_workspace_id`, `has_api_key`, `request_source`

Aggregation periods: `hour`, `day`, `week`, `month`, `cumulative`

### Character Limits

- Per-request limits vary by model and tier (see `max_characters_request_free_user` and `max_characters_request_subscribed_user` on model objects)
- Monthly character quotas per subscription plan

---

## 12. Pricing

### Character-Based Billing

- Billing is per-character, not per-minute or per-request
- Model-specific cost multipliers via `token_cost_factor` and `model_rates.character_cost_multiplier`

### Subscription Info

```
GET https://api.elevenlabs.io/v1/user/subscription
```

Response includes:

| Field | Description |
|-------|-------------|
| `tier` | Current plan tier |
| `status` | `trialing`, `active`, `incomplete`, `past_due`, `free`, `free_disabled` |
| `billing_period` | `monthly_period`, `3_month_period`, `6_month_period`, `annual_period` |
| `character_count` | Characters used this period |
| `character_limit` | Characters allowed this period |
| `character_refresh_period` | When quota resets |
| `currency` | `usd`, `eur`, `inr` |
| `voice_slots_used` / `voice_limit` | Voice storage limits |
| `professional_voice_slots_used` | PVC slots used |
| `can_extend_character_limit` | Overage available |
| `can_use_instant_voice_cloning` | IVC enabled |
| `can_use_professional_voice_cloning` | PVC enabled |
| `next_invoice` | Next billing info |

### Cost Estimate — 2-Minute Phone Conversation

- Average speaking rate: ~150 words/minute
- 2 minutes = ~300 words ≈ ~1,500 characters (including spaces)
- AI speaks roughly half the conversation ≈ ~750 characters of TTS
- With model cost multiplier applied, check `token_cost_factor` for your model
- `eleven_flash_v2_5` may have a lower cost multiplier than `eleven_multilingual_v2`

---

## 13. Python SDK

### Installation

```bash
pip install elevenlabs
```

### Client Initialization

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your_api_key")
```

### Text-to-Speech (Non-Streaming)

```python
audio = client.text_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    text="Hello world",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128"
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)
```

### Text-to-Speech (Streaming)

```python
from elevenlabs import stream

audio_stream = client.text_to_speech.stream(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    text="Hello world",
    model_id="eleven_flash_v2_5"
)

# Play audio directly
stream(audio_stream)

# Or process chunks
for chunk in audio_stream:
    if isinstance(chunk, bytes):
        process(chunk)
```

### Text-to-Speech With Timestamps

```python
result = client.text_to_speech.convert_with_timestamps(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    text="Hello world",
    model_id="eleven_multilingual_v2"
)
# result.audio_base64, result.alignment
```

### Raw Response (Access Headers)

```python
response = client.text_to_speech.with_raw_response.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    text="Hello world"
)
char_cost = response.headers.get("x-character-count")
audio_data = response.data
```

### List Voices

```python
voices = client.voices.list()
for voice in voices.voices:
    print(f"{voice.voice_id}: {voice.name} ({voice.category})")
```

### Get Voice Details

```python
voice = client.voices.get(voice_id="JBFqnCBsd6RMkjVDRZzb")
```

### Voice Settings

```python
# Get settings
settings = client.voices.settings.get(voice_id="JBFqnCBsd6RMkjVDRZzb")

# Update settings
client.voices.settings.update(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    stability=0.5,
    similarity_boost=0.75
)
```

### Clone a Voice

```python
voice = client.voices.add(
    name="My Voice",
    files=[open("sample.mp3", "rb")],
    remove_background_noise=True
)
print(voice.voice_id)
```

### Delete a Voice

```python
client.voices.delete(voice_id="voice_id_to_delete")
```

### Pronunciation Dictionaries

```python
# Create from rules
dictionary = client.pronunciation_dictionaries.create_from_rules(
    rules=[
        {"type": "alias", "string_to_replace": "FMCSA", "alias": "F-M-C-S-A"}
    ],
    name="Industry Terms"
)

# Create from file
dictionary = client.pronunciation_dictionaries.create_from_file(
    file=open("lexicon.pls", "rb"),
    name="My Lexicon"
)
```

### Speech-to-Speech

```python
audio = client.speech_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    audio=open("input.mp3", "rb"),
    output_format="mp3_44100_128"
)
```

### Audio Isolation

```python
audio = client.audio_isolation.convert(audio=open("noisy.mp3", "rb"))
# Streaming variant
audio_stream = client.audio_isolation.stream(audio=open("noisy.mp3", "rb"))
```

### Sound Effects

```python
audio = client.text_to_sound_effects.convert(text="thunder rolling in the distance")
```

### Speech-to-Text

```python
result = client.speech_to_text.convert(
    file=open("recording.mp3", "rb"),
    model_id="scribe_v1"
)
```

### Models

```python
models = client.models.list()
for model in models:
    print(f"{model.model_id}: {model.name}")
```

### User & Subscription

```python
user = client.user.get()
subscription = client.user.subscription.get()
print(f"Characters used: {subscription.character_count}/{subscription.character_limit}")
```

### History

```python
history = client.history.list()
item = client.history.get(history_item_id="item_id")
```

### Conversational AI Agents

```python
# Create agent
agent = client.conversational_ai.agents.create(name="My Agent", ...)

# List agents
agents = client.conversational_ai.agents.list()

# Get agent
agent = client.conversational_ai.agents.get(agent_id="agent_id")
```

---

## 14. Error Handling

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 422 | Validation Error |
| 401 | Authentication failure (invalid API key) |
| 429 | Rate limit / quota exceeded |
| 500 | Server error |

### Validation Error Response (422)

```json
{
  "detail": [
    {
      "loc": ["body", "text"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Common Errors and Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid `voice_id` | Voice doesn't exist or not accessible | Verify voice ID via `GET /v1/voices` |
| Text too long | Exceeds model's `maximum_text_length_per_request` | Split text into smaller chunks |
| Rate limit exceeded | Too many concurrent requests | Implement exponential backoff |
| Invalid output format | Format string not supported | Use exact format strings from Section 9 |
| Authentication failure | Invalid or missing API key | Check `xi-api-key` header |
| Quota exceeded | Monthly character limit reached | Upgrade plan or wait for reset |
| Model not available | Model ID doesn't exist | Check `GET /v1/models` |

### WebSocket Error Handling

- Connection drops: Implement reconnection with exponential backoff
- Inactivity timeout: Connection closes after `inactivity_timeout` seconds (default 20). Send keep-alive text or adjust timeout.
- Invalid first message: Connection closes immediately if init message is malformed

### Zero Retention Mode

- Set `enable_logging=false` on requests
- History features become unavailable
- Audio stitching (`previous_request_ids`) not available
- Enterprise customers only

---

## 15. Pre-generating Audio for Voicemail Drops

### Complete Guide

#### Step 1 — Choose Model and Settings

- **Model:** `eleven_multilingual_v2` (highest quality, latency irrelevant for offline)
- **Voice settings for voicemail:**
  - `stability`: 0.6 (clear and consistent but not robotic)
  - `similarity_boost`: 0.8 (faithful to voice character)
  - `style`: 0.15–0.25 (slight expressiveness, acceptable since offline)
  - `use_speaker_boost`: true (enhanced clarity)
  - `speed`: 0.95 (slightly slower for voicemail clarity)

#### Step 2 — Choose Output Format

- **For Twilio `<Play>` verb:** `mp3_44100_128` (good quality, reasonable size)
- **Alternative:** `wav_16000` (larger file, lossless)

#### Step 3 — Generate Audio

```python
import requests

XI_API_KEY = "your_api_key"
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

scripts = {
    "trucking_intro": "Hi, this is Sarah from LicensedToHaul. I'm reaching out because we help owner-operators like you find the best freight loads in your area. I'd love to chat about how we can help grow your business. Give me a call back when you get a chance.",
    "follow_up": "Hey, it's Sarah again from LicensedToHaul. Just wanted to follow up on my earlier message. We've got some great loads available in your region right now. Call me back at your convenience.",
    "compliance_reminder": "Hi, this is a courtesy call from LicensedToHaul regarding your upcoming DOT compliance deadline. Please give us a call back so we can make sure everything is in order."
}

for name, text in scripts.items():
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        headers={
            "xi-api-key": XI_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.6,
                "similarity_boost": 0.8,
                "style": 0.2,
                "use_speaker_boost": True,
                "speed": 0.95
            }
        },
        params={"output_format": "mp3_44100_128"}
    )

    filename = f"voicemail_{name}.mp3"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Generated {filename} ({len(response.content)} bytes)")
```

#### Step 4 — Store and Serve

Upload generated files to accessible storage (S3, Supabase Storage, etc.) with a public URL.

#### Step 5 — Twilio Playback

```xml
<Response>
  <Play>https://your-storage.com/voicemail_trucking_intro.mp3</Play>
</Response>
```

#### Audio Stitching for Multi-Part Messages

Use `previous_request_ids` and `next_request_ids` to generate seamless multi-segment audio:

```python
# Generate part 1
r1 = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
    headers={"xi-api-key": XI_API_KEY, "Content-Type": "application/json"},
    json={
        "text": "First part of the message.",
        "model_id": "eleven_multilingual_v2",
        "next_text": "Second part continues here."
    },
    params={"output_format": "mp3_44100_128"}
)
request_id_1 = r1.headers.get("request-id")

# Generate part 2 with stitching
r2 = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
    headers={"xi-api-key": XI_API_KEY, "Content-Type": "application/json"},
    json={
        "text": "Second part continues here.",
        "model_id": "eleven_multilingual_v2",
        "previous_request_ids": [request_id_1]
    },
    params={"output_format": "mp3_44100_128"}
)
```

---

## 16. Real-time Voice Agent Integration Architecture

### The Pipeline

```
LLM generates text tokens
    → Tokens accumulated into phrases/sentences
    → Text sent to ElevenLabs WebSocket
    → Audio chunks received (base64 ulaw_8000)
    → Audio decoded and sent to Twilio media stream
    → Caller hears speech
```

### Latency Analysis

| Stage | Expected Latency |
|-------|-----------------|
| LLM first token | 200–500ms (model dependent) |
| LLM token accumulation | 50–200ms (depends on chunking strategy) |
| ElevenLabs text → first audio byte | 100–300ms (`eleven_flash_v2_5` with `optimize_streaming_latency=3`) |
| Audio transmission to Twilio | ~20ms |
| **Total: caller finishes → hears response** | **~400–1000ms** |

### Recommended Configuration for Real-time Voice Agents

```python
# WebSocket connection parameters
ws_url = (
    f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input"
    f"?model_id=eleven_flash_v2_5"
    f"&output_format=ulaw_8000"
    f"&optimize_streaming_latency=3"
)

# Init message
init = {
    "text": " ",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0,               # Zero for minimum latency
        "use_speaker_boost": False, # Off for minimum latency
        "speed": 1.0
    },
    "generation_config": {
        "chunk_length_schedule": [120, 160, 250, 290]
    },
    "xi-api-key": XI_API_KEY
}
```

### Chunking Strategy

| Strategy | Latency | Prosody Quality | When to Use |
|----------|---------|-----------------|-------------|
| Send every token | Lowest | Worst (choppy) | Not recommended |
| Send after each sentence | Higher | Best | When latency budget allows |
| Send after each phrase/clause | Medium | Good | **Recommended for voice agents** |
| Send after N characters (~50–80) | Medium | Good | Simple to implement |

**Recommended approach:** Accumulate LLM tokens until you hit a natural phrase boundary (comma, period, semicolon, newline) or ~80 characters, whichever comes first. Send with `try_trigger_generation: true`. After the final chunk, send with `flush: true`.

### Handling Interruptions (Barge-in)

When the caller starts speaking while ElevenLabs is still generating:

1. Deepgram `SpeechStarted` event fires → caller is speaking
2. Stop sending text to ElevenLabs immediately
3. Send `flush: true` to clear the buffer, then close with `{"text": ""}`
4. Stop sending ElevenLabs audio to Twilio
5. Open a new ElevenLabs WebSocket for the next response

### Buffer Management

- Don't buffer too much audio before starting playback — start sending to Twilio as soon as the first audio chunk arrives
- Each audio chunk from ElevenLabs is already a playable unit
- For Twilio media streams, audio is sent as base64 μ-law in JSON messages — each ElevenLabs chunk maps to one or more Twilio media messages

### Concurrent Connections

- Each active phone call needs its own ElevenLabs WebSocket connection
- Monitor concurrent connections against your tier's limit via `concurrency` metric
- Implement connection pooling if handling many simultaneous calls
- Consider regional endpoints for lower latency (`api.us.elevenlabs.io` for US-based callers)

### Complete Async Voice Agent Integration Example

```python
import asyncio
import websockets
import json
import base64

XI_API_KEY = "your_api_key"
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

class ElevenLabsTTSStream:
    """Manages a single ElevenLabs WebSocket TTS stream for a voice agent call."""

    def __init__(self, on_audio_chunk):
        self.on_audio_chunk = on_audio_chunk  # callback: (bytes) -> None
        self.ws = None
        self._receive_task = None

    async def connect(self):
        uri = (
            f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input"
            f"?model_id=eleven_flash_v2_5"
            f"&output_format=ulaw_8000"
            f"&optimize_streaming_latency=3"
        )
        self.ws = await websockets.connect(uri)

        # Send init message
        await self.ws.send(json.dumps({
            "text": " ",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0,
                "use_speaker_boost": False
            },
            "generation_config": {
                "chunk_length_schedule": [120, 160, 250, 290]
            },
            "xi-api-key": XI_API_KEY
        }))

        # Start receiving audio
        self._receive_task = asyncio.create_task(self._receive_loop())

    async def _receive_loop(self):
        try:
            async for message in self.ws:
                data = json.loads(message)
                if data.get("audio"):
                    audio_bytes = base64.b64decode(data["audio"])
                    await self.on_audio_chunk(audio_bytes)
                if data.get("isFinal"):
                    break
        except websockets.exceptions.ConnectionClosed:
            pass

    async def send_text(self, text, flush=False):
        """Send a text chunk to ElevenLabs."""
        if self.ws:
            await self.ws.send(json.dumps({
                "text": text + " ",
                "try_trigger_generation": True,
                "flush": flush
            }))

    async def close(self):
        """Close the stream gracefully."""
        if self.ws:
            await self.ws.send(json.dumps({"text": ""}))
            if self._receive_task:
                await self._receive_task
            await self.ws.close()

    async def interrupt(self):
        """Handle barge-in — stop generation immediately."""
        if self.ws:
            await self.ws.send(json.dumps({
                "text": " ",
                "flush": True
            }))
            await self.ws.send(json.dumps({"text": ""}))
            if self._receive_task:
                self._receive_task.cancel()
            await self.ws.close()


# Usage in a voice agent pipeline:
async def handle_llm_response(llm_token_stream, send_audio_to_twilio):
    tts = ElevenLabsTTSStream(on_audio_chunk=send_audio_to_twilio)
    await tts.connect()

    buffer = ""
    async for token in llm_token_stream:
        buffer += token
        # Send at phrase boundaries
        if any(buffer.endswith(p) for p in [".", ",", "!", "?", ";", ":"]):
            await tts.send_text(buffer)
            buffer = ""

    # Flush remaining text
    if buffer:
        await tts.send_text(buffer, flush=True)

    await tts.close()
```

---

## API Server Endpoints

| Region | REST API | WebSocket |
|--------|----------|-----------|
| Default | `https://api.elevenlabs.io` | `wss://api.elevenlabs.io` |
| US | `https://api.us.elevenlabs.io` | `wss://api.us.elevenlabs.io` |
| EU Residency | `https://api.eu.residency.elevenlabs.io` | `wss://api.eu.residency.elevenlabs.io` |
| India Residency | `https://api.in.residency.elevenlabs.io` | `wss://api.in.residency.elevenlabs.io` |

---

## Appendix: Conversational AI Platform

ElevenLabs also offers a full Conversational AI platform for building voice agents natively on their infrastructure. Key endpoints:

### Agents

| Operation | Endpoint |
|-----------|----------|
| Create | `POST /v1/convai/agents/create` |
| Get | `GET /v1/convai/agents/{agent_id}` |
| Update | `PATCH /v1/convai/agents/{agent_id}` |
| Delete | `DELETE /v1/convai/agents/{agent_id}` |
| List | `GET /v1/convai/agents` |
| Duplicate | `POST /v1/convai/agents/{agent_id}/duplicate` |

### Conversations

| Operation | Endpoint |
|-----------|----------|
| Create | `POST /v1/convai/conversations` |
| List | `GET /v1/convai/conversations` |
| Get | `GET /v1/convai/conversations/{conversation_id}` |
| Delete | `DELETE /v1/convai/conversations/{conversation_id}` |
| Get Audio | `GET /v1/convai/conversations/{conversation_id}/audio` |

### Phone Integration

| Operation | Endpoint |
|-----------|----------|
| Import Number | `POST /v1/convai/phone-numbers` (Twilio SID/token or SIP trunk) |
| List Numbers | `GET /v1/convai/phone-numbers` |
| Batch Calling | `POST /v1/convai/batch-calling` |

### Knowledge Base

Full CRUD at `/v1/convai/knowledge-base/*` — create from file, text, or URL. RAG index management included.

---

## Appendix: Other APIs

### Audio Isolation

```
POST /v1/audio-isolation          # Returns binary audio
POST /v1/audio-isolation/stream   # Returns streamed binary audio
```

### Speech-to-Text

```
POST /v1/speech-to-text           # File up to 3GB
GET  /v1/speech-to-text/{id}      # Get transcript
```

### Text-to-Dialogue (Multi-Speaker)

```
POST /v1/text-to-dialogue         # Up to 10 unique voices
POST /v1/text-to-dialogue/stream
```

### Sound Effects

```
POST /v1/sound-generation         # text, duration_seconds (0.5-30), prompt_influence (0-1)
```

### Music Generation

```
POST /v1/music/stream             # prompt or composition_plan, music_length_ms (3000-600000)
POST /v1/music/plan               # Free composition planning
POST /v1/music/stem-separation    # two_stems_v1 or six_stems_v1
```

### Dubbing

```
POST   /v1/dubbing                          # Create dub job
GET    /v1/dubbing/{id}                     # Status
GET    /v1/dubbing/{id}/audio/{lang_code}   # Get dubbed audio
GET    /v1/dubbing/{id}/transcript/{lang}   # Get transcript
DELETE /v1/dubbing/{id}                     # Delete
```

### Forced Alignment

```
POST /v1/forced-alignment    # multipart: file (max 1GB) + text → character-level timing
```