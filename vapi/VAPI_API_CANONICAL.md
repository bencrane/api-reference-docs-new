# Vapi API Canonical Reference

> **Purpose**: The definitive Vapi API reference for the OEX engineering team. Covers every endpoint, webhook, configuration option, and integration pattern needed to build the complete voice integration in our multi-tenant outbound orchestration engine.
>
> **Last updated**: 2026-03-25
>
> **Base URL**: `https://api.vapi.ai`
> **Authentication**: `Authorization: <API Key>` header on all REST calls

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Authentication & Account Setup](#2-authentication--account-setup)
3. [Assistants — Complete Configuration](#3-assistants--complete-configuration)
4. [Outbound Calls — Complete API](#4-outbound-calls--complete-api)
5. [Inbound Calls — Complete Setup](#5-inbound-calls--complete-setup)
6. [Phone Number Management](#6-phone-number-management)
7. [Tool Use / Function Calling — Deep Dive](#7-tool-use--function-calling--deep-dive)
8. [Call Transfer — Deep Dive](#8-call-transfer--deep-dive)
9. [Webhooks / Server Events — Complete Specification](#9-webhooks--server-events--complete-specification)
10. [Call Recording & Transcription](#10-call-recording--transcription)
11. [Conversation Design for Voice](#11-conversation-design-for-voice)
12. [Provider Configuration — Our Stack](#12-provider-configuration--our-stack)
13. [Pricing — Itemized Cost Breakdown](#13-pricing--itemized-cost-breakdown)
14. [Rate Limits & Concurrency](#14-rate-limits--concurrency)
15. [Error Handling & Edge Cases](#15-error-handling--edge-cases)
16. [Voicemail Detection & Handling](#16-voicemail-detection--handling)
17. [Multi-Tenant Considerations](#17-multi-tenant-considerations)
18. [Squads — Multi-Assistant Architecture](#18-squads--multi-assistant-architecture)
19. [Outbound Campaigns](#19-outbound-campaigns)
20. [Structured Outputs & Call Analysis](#20-structured-outputs--call-analysis)
21. [Observability & Testing](#21-observability--testing)
22. [Security & Compliance](#22-security--compliance)
23. [Complete API Reference — All Endpoints](#23-complete-api-reference--all-endpoints)
24. [Python/REST Code Examples Collection](#24-pythonrest-code-examples-collection)

---

## 1. Architecture Overview

### How Vapi Works Under the Hood

Vapi is a **voice AI orchestration layer** that sits between telephony, speech-to-text (STT), large language models (LLMs), and text-to-speech (TTS) providers. It manages the entire real-time conversation pipeline.

#### What Vapi Manages
- **Call state**: Lifecycle from initiation through active conversation to termination
- **Turn-taking**: Proprietary models determine when each party should speak
- **Audio routing**: Bidirectional audio between all pipeline components
- **Provider coordination**: Manages connections to STT, LLM, TTS simultaneously
- **Barge-in detection**: Differentiates genuine interruptions from backchanneling ("yeah", "uh-huh")
- **Endpointing**: Custom fusion audio-text model (NOT simple silence detection) determines when a speaker has finished
- **Background noise filtering**: Real-time removal of ambient noise
- **Background voice filtering**: Proprietary model isolates primary speaker, blocks TV/echoes/other voices
- **Backchanneling**: Proprietary model selects timing/content of affirmations
- **Emotion detection**: Real-time audio analysis conveyed to LLM
- **Filler injection**: Adds "um", "like" to streaming output without added latency

#### What Vapi Does NOT Manage (What We Handle)
- Business logic (lead selection, qualification criteria, CRM updates)
- Campaign orchestration (which leads to call, when, in what order)
- Answering machine detection at the Twilio layer (optional — Vapi also has built-in AMD)
- Post-call workflows (follow-up emails, status updates, agency notifications)
- Multi-tenant routing logic (which brand/number/assistant for which campaign)

#### Audio Flow Diagram

```
┌─────────────┐     ┌──────────────────────────────────────────────────┐     ┌──────────────┐
│   Twilio     │     │                    Vapi                          │     │   Providers   │
│  (Telephony) │     │                                                  │     │               │
│              │◄───►│  ┌──────────┐   ┌──────────┐   ┌──────────┐    │     │  Deepgram     │
│  PSTN/SIP    │     │  │ Audio    │──►│ STT      │──►│ LLM      │    │◄───►│  (STT)        │
│  Call Leg    │     │  │ Router   │   │ Adapter  │   │ Adapter  │    │     │               │
│              │     │  │          │◄──│          │◄──│          │    │     │  Anthropic    │
│              │     │  │          │   │          │   │          │    │     │  (LLM)        │
│              │     │  │          │   └──────────┘   └──────────┘    │     │               │
│              │     │  │          │                                    │     │  ElevenLabs   │
│              │     │  │          │◄──────────────────┐               │     │  (TTS)        │
│              │     │  └──────────┘   ┌──────────┐   │               │     │               │
│              │     │                 │ TTS      │───┘               │     └──────────────┘
│              │     │                 │ Adapter  │                    │
│              │     │                 └──────────┘                    │
│              │     │                                                  │
│              │     │  ┌──────────────────────────────────────────┐   │
│              │     │  │ Orchestration Layer (proprietary)         │   │
│              │     │  │ • Endpointing  • Interruption handling   │   │
│              │     │  │ • Backchanneling • Emotion detection     │   │
│              │     │  │ • Filler injection • Noise filtering     │   │
│              │     │  └──────────────────────────────────────────┘   │
└─────────────┘     └──────────────────────────────────────────────────┘
```

#### Latency Budget Per Hop

| Hop | Typical Latency | Notes |
|-----|----------------|-------|
| Twilio → Vapi | ~50ms | Network transport |
| Vapi STT (Deepgram) | ~100-300ms | Streaming; partial results in ~100ms |
| Vapi Endpointing | ~50-200ms | Proprietary model; configurable via `startSpeakingPlan` |
| LLM Inference (Claude) | ~200-800ms | Streaming; first token ~200ms |
| TTS (ElevenLabs) | ~100-300ms | Streaming; first chunk ~100ms |
| Vapi → Twilio | ~50ms | Network transport |
| **Total voice-to-voice** | **~500-1700ms** | Target: under 700ms; typical ~800ms |

**Performance target**: Complete voice-to-voice cycle under 500-700ms. The system streams between each layer to minimize perceived latency.

---

## 2. Authentication & Account Setup

### API Key Types

| Key Type | Scope | Use Case |
|----------|-------|----------|
| **Private API Key** | Full access to all endpoints | Server-side operations (call initiation, assistant CRUD, webhooks) |
| **Public API Key** | Limited to web call creation (`/call/web`) | Client-side SDK initialization |

**Get your keys**: Dashboard → Organization Settings → API Keys

### REST API Authentication

All API calls require the private key in the `Authorization` header:

```bash
curl -X GET https://api.vapi.ai/assistant \
  -H "Authorization: Bearer <YOUR_PRIVATE_API_KEY>"
```

### JWT Authentication (Advanced)

For secure client-side operations without exposing the private key:

```python
import jwt
import os
from datetime import datetime, timedelta

token = jwt.encode(
    {
        "orgId": os.environ["VAPI_ORG_ID"],
        "exp": datetime.utcnow() + timedelta(hours=1),
        "scope": "public",  # or "private"
        # Optional restrictions for public scope:
        "allowedOrigins": ["https://yourdomain.com"],
        "allowedAssistantIds": ["asst_abc123"],
    },
    os.environ["VAPI_PRIVATE_KEY"],
    algorithm="HS256"
)
```

**Token scopes**:
- `private`: Access to all endpoints
- `public`: Only web call creation; can restrict by `allowedOrigins`, `allowedAssistantIds`, `allowTransientAssistant`

### Webhook Authentication

Three methods to authenticate webhook callbacks from Vapi to your server:

| Method | How It Works |
|--------|-------------|
| **Bearer Token** | Vapi sends token in `Authorization` header (or legacy `X-Vapi-Secret`) |
| **OAuth 2.0** | Client credentials flow with automatic token refresh |
| **HMAC** | Signature-based request integrity verification |

Configure via Dashboard → Custom Credentials, then reference `credentialId` in your server config.

### Organization Structure

- **Organization**: Top-level entity; contains all assistants, phone numbers, calls
- **API Keys**: Scoped to the organization
- **No sub-account concept**: Multi-tenancy is handled via separate assistants/phone numbers per brand (see [Section 17](#17-multi-tenant-considerations))

---

## 3. Assistants — Complete Configuration

The assistant is the **agent definition** — it encapsulates the AI's personality, voice, tools, and behavior.

### Creating an Assistant

```
POST /assistant
```

### Complete Assistant Configuration Object

```json
{
  "name": "OEX Insurance Qualifier",

  "firstMessage": "Hi, this is Sarah from LicensedToHaul. Am I speaking with {{customerName}}?",
  "firstMessageMode": "assistant-speaks-first",

  "model": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-20250514",
    "temperature": 0.7,
    "maxTokens": 300,
    "messages": [
      {
        "role": "system",
        "content": "You are Sarah, an insurance specialist at LicensedToHaul..."
      }
    ],
    "tools": [],
    "toolIds": ["tool_abc123"],
    "emotionRecognitionEnabled": true
  },

  "voice": {
    "provider": "11labs",
    "voiceId": "21m00Tcm4TlvDq8ikWAM",
    "model": "eleven_turbo_v2",
    "speed": 1.0,
    "stability": 0.5,
    "similarityBoost": 0.75,
    "style": 0.0,
    "useSpeakerBoost": false,
    "chunkPlan": {
      "enabled": true,
      "minCharacters": 30,
      "formatPlan": {
        "enabled": true,
        "numberToDigitsCutoff": 2025,
        "replacements": []
      }
    },
    "fallbackPlan": {
      "voices": [
        {
          "provider": "openai",
          "voiceId": "alloy"
        }
      ]
    }
  },

  "transcriber": {
    "provider": "deepgram",
    "model": "nova-2",
    "language": "en",
    "confidenceThreshold": 0.4,
    "endpointing": 255,
    "keywords": ["DOT:5", "FMCSA:5", "LicensedToHaul:3"],
    "smartFormat": true,
    "fallbackPlan": {
      "transcribers": [
        {
          "provider": "deepgram",
          "model": "nova-3"
        }
      ]
    }
  },

  "silenceTimeoutSeconds": 30,
  "maxDurationSeconds": 600,
  "backgroundSound": "office",
  "backchannelingEnabled": true,
  "hipaaEnabled": false,

  "startSpeakingPlan": {
    "waitSeconds": 0.4,
    "smartEndpointingEnabled": true,
    "smartEndpointingPlan": {
      "provider": "livekit",
      "waitFunction": "(20 + 500 * sqrt(x) + 2500 * x^3 + 700 + 4000 * max(0, x-0.5)) / 2"
    },
    "transcriptionEndpointingPlan": {
      "onPunctuationSeconds": 0.1,
      "onNoPunctuationSeconds": 1.5,
      "onNumberSeconds": 0.5
    }
  },

  "stopSpeakingPlan": {
    "numWords": 2,
    "voiceSeconds": 0.2,
    "backoffSeconds": 1.0
  },

  "serverUrl": "https://oex-api.yourdomain.com/vapi/webhook",
  "serverUrlSecret": "your_webhook_secret_here",

  "analysisPlan": {
    "summaryPrompt": "Summarize this insurance qualification call in 2-3 sentences.",
    "structuredDataPrompt": "Extract the following from the call.",
    "structuredDataSchema": {
      "type": "object",
      "properties": {
        "dotNumber": { "type": "string" },
        "truckCount": { "type": "number" },
        "qualified": { "type": "boolean" },
        "interestLevel": { "type": "string", "enum": ["high", "medium", "low", "none"] }
      }
    },
    "successEvaluationPrompt": "Did the assistant successfully qualify the lead and either schedule a transfer or get permission to call back?",
    "successEvaluationRubric": "PassFail"
  },

  "artifactPlan": {
    "recordingEnabled": true,
    "recordingFormat": "wav;l16",
    "loggingEnabled": true,
    "transcriptPlan": {
      "assistantName": "Sarah",
      "userName": "Prospect"
    }
  },

  "backgroundSpeechDenoisingPlan": {
    "enabled": true
  },

  "hooks": [
    {
      "on": "customer.speech.timeout",
      "do": [{ "type": "say", "exact": "Are you still there?" }],
      "options": { "timeoutSeconds": 10, "maxCount": 3 }
    }
  ],

  "compliancePlan": {},
  "clientMessages": ["transcript", "tool-calls"],
  "serverMessages": ["end-of-call-report", "status-update", "tool-calls", "transfer-destination-request"]
}
```

### Field-by-Field Reference

#### Top-Level Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | — | Display name for the assistant |
| `firstMessage` | string | — | Opening message spoken by the assistant. Supports `{{variables}}` |
| `firstMessageMode` | enum | `"assistant-speaks-first"` | Options: `assistant-speaks-first`, `assistant-speaks-first-with-model-generated-message`, `assistant-waits-for-user` |
| `silenceTimeoutSeconds` | number | 30 | Seconds of silence before the call ends |
| `maxDurationSeconds` | number | 600 | Maximum call duration in seconds |
| `backgroundSound` | enum | `"office"` (phone), `"off"` (web) | Options: `office`, `off` |
| `backchannelingEnabled` | bool | false | Enable "yeah", "uh-huh" during user speech |
| `hipaaEnabled` | bool | false | Disable storage of call logs/recordings/transcriptions |
| `serverUrl` | string | — | URL where Vapi sends webhook events |
| `serverUrlSecret` | string | — | Secret for webhook signature verification (legacy; prefer credential-based auth) |

#### Model Configuration

| Field | Type | Description |
|-------|------|-------------|
| `provider` | enum | `anthropic`, `openai`, `google`, `groq`, `custom-llm`, `openrouter`, `perplexity`, `togetherai`, `deepinfra`, `azure-openai`, `anthropic-bedrock` |
| `model` | string | Model identifier (e.g., `claude-sonnet-4-20250514`, `gpt-4o`) |
| `temperature` | number | 0-2. Recommended 0.5-0.7 for voice |
| `maxTokens` | number | Max tokens per response. Recommended 200-300 for voice |
| `messages` | array | Conversation history injection. `[{role: "system", content: "..."}]` |
| `tools` | array | Inline tool definitions |
| `toolIds` | array | References to saved tool IDs |
| `emotionRecognitionEnabled` | bool | Enable real-time emotion detection conveyed to LLM |
| `metadataSendMode` | string | Controls metadata sent to custom LLMs |

#### Voice Configuration

| Field | Type | Description |
|-------|------|-------------|
| `provider` | enum | `11labs`, `playht`, `deepgram`, `openai`, `azure`, `cartesia`, `lmnt`, `rime-ai`, `vapi` |
| `voiceId` | string | Provider-specific voice identifier |
| `model` | string | Voice model (e.g., `eleven_turbo_v2`, `eleven_flash_v2`) |
| `speed` | number | Speech rate (PlayHT only currently supports adjustable speed) |
| `stability` | number | 0-1. Lower = more expressive, higher = more consistent (ElevenLabs) |
| `similarityBoost` | number | 0-1. How closely to match the original voice (ElevenLabs) |
| `style` | number | 0-1. Style exaggeration (ElevenLabs) |
| `chunkPlan` | object | Controls text chunking and formatting before TTS |
| `fallbackPlan` | object | Sequential fallback voices if primary fails |

#### Transcriber Configuration

| Field | Type | Description |
|-------|------|-------------|
| `provider` | enum | `deepgram`, `assembly-ai`, `azure`, `gladia`, `google`, `speechmatics`, `openai`, `cartesia`, `talkscriber`, `custom` |
| `model` | string | Provider model (e.g., `nova-2`, `nova-3`, `flux-general-en`) |
| `language` | string | Language code (e.g., `en`, `es`, `multi` for auto-detect) |
| `confidenceThreshold` | number | Default 0.4. Minimum confidence for accepted transcriptions |
| `endpointing` | number | Milliseconds for silence-based endpointing |
| `keywords` | array | Deepgram keyword boosting (e.g., `["DOT:5"]`) — single words only, Nova-2/Nova-1/Enhanced/Base |
| `keyterm` | array | Deepgram keyterm prompting — multi-word phrases, Nova-3 only |
| `smartFormat` | bool | Enable smart formatting |
| `fallbackPlan` | object | Sequential fallback transcribers |

#### Start Speaking Plan (Endpointing)

Controls when the assistant begins speaking after the customer pauses:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `waitSeconds` | number | 0.4 | Base wait time after speech ends (0-5s) |
| `smartEndpointingEnabled` | bool | false | Enable AI-driven endpointing |
| `smartEndpointingPlan.provider` | enum | — | `livekit` (English only), `vapi` (non-English), `krisp` (audio-based), `deepgram-flux`, `assembly` |
| `transcriptionEndpointingPlan.onPunctuationSeconds` | number | 0.1 | Wait after punctuation detected |
| `transcriptionEndpointingPlan.onNoPunctuationSeconds` | number | 1.5 | Wait when no punctuation |
| `transcriptionEndpointingPlan.onNumberSeconds` | number | 0.5 | Wait after number detected |

#### Stop Speaking Plan (Interruption Handling)

Controls when the assistant stops talking if the customer interjects:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `numWords` | number | 0 | Minimum word count to trigger stop. 0 = VAD-based (50-100ms). 2-3 recommended for appointment scheduling |
| `voiceSeconds` | number | 0.2 | VAD duration threshold when `numWords=0` |
| `backoffSeconds` | number | 1.0 | Blocks all audio after interruption. Sequential with `waitSeconds` |

#### Dynamic Variables

Use `{{variable_name}}` syntax in `firstMessage` and system prompts. Set via `assistantOverrides.variableValues`:

**Auto-populated variables**:
- Time: `{{now}}`, `{{date}}`, `{{time}}`, `{{month}}`, `{{day}}`, `{{year}}`
- Customer: `{{customer.number}}`, `{{customer.name}}`
- Transport: `{{transport.conversationType}}`

**Custom variables**: Any key in `variableValues` is available as `{{key}}`

**LiquidJS date formatting**: `{{"now" | date: "%A, %B %d, %Y, %I:%M %p", "America/Los_Angeles"}}`

---

## 4. Outbound Calls — Complete API

### Initiate an Outbound Call

```
POST /call
```

#### Request Body

```json
{
  "assistantId": "asst_abc123",

  "phoneNumberId": "pn_xyz789",

  "customer": {
    "number": "+15551234567",
    "name": "John Smith",
    "extension": "123"
  },

  "assistantOverrides": {
    "variableValues": {
      "customerName": "John Smith",
      "dotNumber": "12345",
      "truckCount": "3",
      "carrierName": "Smith Trucking LLC"
    },
    "model": {
      "messages": [
        {
          "role": "system",
          "content": "You are calling John Smith, DOT# 12345, a carrier with 3 trucks based in Dallas, TX. They are a potential customer for commercial auto insurance."
        }
      ]
    }
  },

  "schedulePlan": {
    "earliestAt": "2026-03-26T14:00:00Z",
    "latestAt": "2026-03-26T15:00:00Z"
  }
}
```

#### Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `assistantId` | string | Yes* | Reference to a saved assistant |
| `assistant` | object | Yes* | Inline (transient) assistant definition. *One of `assistantId` or `assistant` required |
| `phoneNumberId` | string | Yes | Vapi-managed phone number ID |
| `customer.number` | string | Yes | E.164 format destination number |
| `customer.name` | string | No | Prospect name |
| `customer.extension` | string | No | Extension to dial after connection |
| `assistantOverrides` | object | No | Override any assistant field for this call |
| `assistantOverrides.variableValues` | object | No | Dynamic variables for `{{variable}}` substitution |
| `schedulePlan.earliestAt` | string | No | ISO 8601 datetime for scheduled calls |
| `schedulePlan.latestAt` | string | No | Latest time to attempt the call |
| `customers` | array | No | **Batch calling**: array of customer objects for multiple simultaneous calls |

#### How to Pass Custom Context into the Call

Three approaches (can combine):

1. **Dynamic variables** (`assistantOverrides.variableValues`): Best for simple key-value data referenced in `firstMessage` and prompts via `{{variable}}`

2. **System prompt override** (`assistantOverrides.model.messages`): Best for rich context. The system prompt is where you inject "You are calling John Smith, DOT# 12345..."

3. **Both together**: Use variables for the greeting, system prompt override for detailed context

```python
# Recommended approach for OEX:
call_payload = {
    "assistantId": QUALIFIER_ASSISTANT_ID,
    "phoneNumberId": PHONE_NUMBER_ID,
    "customer": {"number": lead.phone},
    "assistantOverrides": {
        "variableValues": {
            "customerName": lead.name,
            "dotNumber": lead.dot_number,
        },
        "model": {
            "messages": [{
                "role": "system",
                "content": f"""You are Sarah from LicensedToHaul calling {lead.name}.

Context about this carrier:
- DOT Number: {lead.dot_number}
- Company: {lead.company_name}
- Truck Count: {lead.truck_count}
- Location: {lead.city}, {lead.state}
- Current insurance status: {lead.insurance_status}

Your goal: Qualify this carrier for commercial auto insurance and transfer to an agency if qualified."""
            }]
        }
    }
}
```

#### Answering Machine Detection (AMD)

Vapi has **built-in AMD**. Configure in the assistant or call:

```json
{
  "voicemailDetection": {
    "provider": "vapi",
    "voicemailDetectionTypes": ["audio"],
    "startAtSeconds": 0,
    "frequencySeconds": 2.5,
    "maxRetries": 3,
    "beepMaxAwaitSeconds": 15,
    "enabled": true
  }
}
```

**Provider options**: `vapi` (strongly recommended — hybrid Gemini + Twilio beep detection), `google` (highly reliable, slightly slower), `openai` (strong accuracy, higher cost), `twilio` (fast but prone to false alarms)

**What happens when AMD detects a machine**: Vapi can play a pre-recorded audio message (MP3/WAV) or have the AI leave a voicemail, then end the call.

**Alternative pattern (Twilio-layer AMD)**: Twilio AMD → if human → forward to Vapi; if machine → Twilio plays pre-recorded ElevenLabs audio (bypasses Vapi entirely). This is cheaper but requires separate Twilio configuration.

#### Call Scheduling

Yes — use `schedulePlan`:
```json
{
  "schedulePlan": {
    "earliestAt": "2026-03-26T14:00:00Z",
    "latestAt": "2026-03-26T15:00:00Z"
  }
}
```

Resources are re-fetched at execution time. **Warning**: If using `assistantId` and the assistant is deleted before the scheduled time, the call fails. Use transient (inline) assistant definitions for static scheduled configs.

#### Batch Calling

Yes — use the `customers` array to initiate multiple calls in one API request:

```json
{
  "assistantId": "asst_abc123",
  "phoneNumberId": "pn_xyz789",
  "customers": [
    { "number": "+15551111111", "name": "John Smith" },
    { "number": "+15552222222", "name": "Jane Doe" },
    { "number": "+15553333333", "name": "Bob Wilson" }
  ]
}
```

Combinable with `schedulePlan`. **Limitation**: Per-customer `assistantOverrides` require separate API calls per lead.

**OEX approach**: For personalized outbound (which we need), call the API per lead to inject custom context.

#### Response Format

```json
{
  "id": "call_abc123",
  "orgId": "org_xyz",
  "type": "outboundPhoneCall",
  "status": "queued",
  "phoneNumberId": "pn_xyz789",
  "assistantId": "asst_abc123",
  "customer": {
    "number": "+15551234567",
    "name": "John Smith"
  },
  "monitor": {
    "listenUrl": "wss://api.vapi.ai/call_abc123/listen",
    "controlUrl": "https://api.vapi.ai/call_abc123/control"
  },
  "createdAt": "2026-03-25T10:30:00Z",
  "updatedAt": "2026-03-25T10:30:00Z",
  "costBreakdown": {
    "transport": 0,
    "stt": 0,
    "llm": 0,
    "tts": 0,
    "vapi": 0,
    "total": 0
  }
}
```

**Status values**: `scheduled`, `queued`, `ringing`, `in-progress`, `forwarding`, `ended`

#### Full Working Code Example (Python httpx)

```python
import httpx
import os

VAPI_API_KEY = os.environ["VAPI_API_KEY"]
ASSISTANT_ID = os.environ["VAPI_QUALIFIER_ASSISTANT_ID"]
PHONE_NUMBER_ID = os.environ["VAPI_PHONE_NUMBER_ID"]

async def initiate_outbound_call(lead: dict) -> dict:
    """Initiate an outbound qualification call to a trucking lead."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.vapi.ai/call",
            headers={
                "Authorization": f"Bearer {VAPI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "assistantId": ASSISTANT_ID,
                "phoneNumberId": PHONE_NUMBER_ID,
                "customer": {
                    "number": lead["phone"],  # E.164 format
                    "name": lead["name"],
                },
                "assistantOverrides": {
                    "variableValues": {
                        "customerName": lead["name"],
                        "dotNumber": lead["dot_number"],
                        "truckCount": str(lead["truck_count"]),
                    },
                    "model": {
                        "messages": [
                            {
                                "role": "system",
                                "content": f"""You are Sarah from LicensedToHaul.

You are calling {lead['name']} at {lead['company_name']}.
DOT Number: {lead['dot_number']}
Trucks: {lead['truck_count']}
Location: {lead['city']}, {lead['state']}

GOAL: Qualify for commercial auto insurance. Ask about:
1. Current insurance provider and renewal date
2. Fleet size and vehicle types
3. Safety record and claims history
4. Decision-making authority

If qualified (has trucks, needs insurance, is decision maker), transfer to agency.
If not qualified, thank them and end the call politely."""
                            }
                        ]
                    },
                },
            },
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()

# Usage:
# result = await initiate_outbound_call({
#     "phone": "+15551234567",
#     "name": "John Smith",
#     "company_name": "Smith Trucking LLC",
#     "dot_number": "12345",
#     "truck_count": 3,
#     "city": "Dallas",
#     "state": "TX"
# })
# print(f"Call ID: {result['id']}, Status: {result['status']}")
```

---

## 5. Inbound Calls — Complete Setup

### How Inbound Works

1. Prospect calls a phone number
2. If the phone number has an `assistantId` → Vapi uses that assistant
3. If the phone number has no `assistantId` but has a `serverUrl` → Vapi sends `assistant-request` webhook to dynamically select the assistant
4. The assistant handles the conversation

### Option 1: Static Assistant Assignment

Assign an assistant to a phone number:

```bash
curl -X PATCH https://api.vapi.ai/phone-number/pn_xyz789 \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"assistantId": "asst_abc123"}'
```

### Option 2: Dynamic Assistant Selection (IVR-Style Routing)

Leave `assistantId` null and configure a `serverUrl`:

```bash
curl -X PATCH https://api.vapi.ai/phone-number/pn_xyz789 \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistantId": null,
    "server": {
      "url": "https://oex-api.yourdomain.com/vapi/assistant-request"
    }
  }'
```

When a call comes in, Vapi sends an `assistant-request` webhook:

```json
{
  "type": "assistant-request",
  "phoneNumber": {
    "provider": "twilio",
    "number": "+14155551234"
  },
  "call": {
    "customer": {
      "number": "+15559876543"
    }
  }
}
```

Your server responds with the assistant to use:

```json
{
  "assistantId": "asst_inbound_qualifier"
}
```

Or with a full inline assistant:

```json
{
  "assistant": {
    "name": "LicensedToHaul Inbound",
    "firstMessage": "Thank you for calling LicensedToHaul! How can I help you today?",
    "firstMessageMode": "assistant-speaks-first",
    "model": {
      "provider": "anthropic",
      "model": "claude-sonnet-4-20250514",
      "messages": [{ "role": "system", "content": "You are a helpful insurance specialist..." }]
    },
    "voice": { "provider": "11labs", "voiceId": "21m00Tcm4TlvDq8ikWAM" },
    "transcriber": { "provider": "deepgram", "model": "nova-2", "language": "en" }
  }
}
```

**Critical**: Your server must respond within **7.5 seconds** or the call fails.

### Using Twilio Numbers for Inbound

If using your own Twilio number (not imported to Vapi):

1. Import the Twilio number to Vapi (see [Section 6](#6-phone-number-management))
2. Vapi automatically configures Twilio's webhook to route calls to Vapi
3. Assign an assistant to the number

**No manual TwiML or webhook URL configuration needed** — importing handles it.

### Routing Different Callers to Different Assistants

Use the `assistant-request` webhook pattern. Your server looks up the caller's number and returns the appropriate assistant:

```python
@app.post("/vapi/assistant-request")
async def handle_assistant_request(request: Request):
    data = await request.json()
    caller_number = data["call"]["customer"]["number"]

    # Look up caller in your database
    customer = await db.get_customer_by_phone(caller_number)

    if customer and customer.brand == "LicensedToHaul":
        return {"assistantId": LICENSED_TO_HAUL_ASSISTANT_ID}
    elif customer and customer.brand == "BuildersUSA":
        return {"assistantId": BUILDERS_USA_ASSISTANT_ID}
    else:
        return {"assistantId": DEFAULT_INBOUND_ASSISTANT_ID}
```

---

## 6. Phone Number Management

### Creating / Importing Phone Numbers

#### Free Vapi Number (US Only)

```
POST /phone-number
```

```json
{
  "provider": "vapi",
  "numberDesiredAreaCode": "415"
}
```

- US only, max 10 per account
- Cannot make international calls
- Not compatible with outbound campaigns (use Twilio 10DLC)

#### Import Twilio Number

```
POST /phone-number
```

```json
{
  "provider": "twilio",
  "number": "+14155551234",
  "twilioAccountSid": "AC...",
  "twilioAuthToken": "auth_token_here"
}
```

#### Import Telnyx Number

```json
{
  "provider": "telnyx",
  "number": "+14155551234",
  "credentialId": "cred_telnyx_abc"
}
```

#### BYO SIP Trunk Number

```json
{
  "provider": "byo-phone-number",
  "number": "+14155551234",
  "credentialId": "cred_sip_abc",
  "numberE164CheckEnabled": true
}
```

### Phone Number Configuration

| Field | Type | Description |
|-------|------|-------------|
| `assistantId` | string | Static assistant for this number |
| `squadId` | string | Squad for multi-assistant routing |
| `workflowId` | string | Workflow for complex routing (deprecated — use squads) |
| `server.url` | string | Webhook URL for dynamic assistant selection |
| `fallbackDestination` | object | Number to forward to if Vapi is unavailable |
| `hooks` | array | Automated actions on call events (e.g., `call.ringing`) |
| `smsEnabled` | bool | Enable inbound SMS (Twilio US numbers only) |
| `name` | string | Display name |

### Number-to-Assistant Mapping (Multi-Tenant)

Each phone number can be assigned a different assistant:

```python
# LicensedToHaul number → insurance qualifier assistant
await patch_phone_number("pn_lth_001", {"assistantId": "asst_lth_qualifier"})

# BuildersUSA number → builders insurance assistant
await patch_phone_number("pn_busa_001", {"assistantId": "asst_busa_qualifier"})
```

### List Phone Numbers

```
GET /phone-number?limit=100
```

### Get / Update / Delete

```
GET /phone-number/{id}
PATCH /phone-number/{id}
DELETE /phone-number/{id}
```

---

## 7. Tool Use / Function Calling — Deep Dive

### Overview

Tools let the AI call functions mid-conversation — look up a DOT number, check carrier status, log outcomes, trigger transfers. This is the backbone of our qualification flow.

### Tool Types

| Type | Description | When to Use |
|------|-------------|-------------|
| **Custom Tool** (Function) | Vapi calls YOUR server when AI invokes the tool | Database lookups, CRM updates, any backend logic |
| **API Request Tool** | Vapi makes HTTP requests directly | Simple REST API calls without custom logic |
| **Code Tool** | TypeScript executed on Vapi infrastructure | Data transformation, calculations, simple API calls |
| **Default Tools** | Built-in: `transferCall`, `endCall`, `sms`, `dtmf`, `apiRequest` | Call routing, ending calls, IVR navigation |

### Defining Tools in the Assistant Config

Tools can be defined inline in the assistant's `model.tools` array or referenced by ID via `model.toolIds`:

```json
{
  "model": {
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "lookup_carrier",
          "description": "Look up a motor carrier's information by DOT number in our database. Call this when the prospect mentions their DOT number or company name.",
          "parameters": {
            "type": "object",
            "properties": {
              "dot_number": {
                "type": "string",
                "description": "The carrier's USDOT number"
              }
            },
            "required": ["dot_number"]
          }
        },
        "server": {
          "url": "https://oex-api.yourdomain.com/vapi/tools/lookup-carrier",
          "timeoutSeconds": 20,
          "headers": {
            "Authorization": "Bearer {{env.OEX_API_KEY}}"
          }
        },
        "messages": [
          {
            "type": "request-start",
            "content": "Let me look that up for you real quick."
          },
          {
            "type": "request-complete",
            "content": "Got it. I found your carrier information."
          },
          {
            "type": "request-failed",
            "content": "I'm having trouble looking that up. Can you repeat the DOT number?"
          },
          {
            "type": "request-response-delayed",
            "content": "Still looking... one moment.",
            "timingMilliseconds": 3000
          }
        ]
      }
    ]
  }
}
```

### Tool Definition Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | enum | Yes | `function`, `apiRequest`, `code`, `transferCall`, `endCall`, `dtmf`, `handoff` |
| `function.name` | string | Yes | a-z/A-Z/0-9/underscore/dash, max 64 chars |
| `function.description` | string | Yes | When the AI should call this tool |
| `function.parameters` | object | Yes | JSON Schema for tool input |
| `function.parameters.properties` | object | Yes | Parameter definitions |
| `function.parameters.required` | array | Yes | Required parameter names |
| `strict` | bool | No | Enable strict schema validation |
| `server.url` | string | Yes* | Your endpoint URL (*not needed for client-side or code tools) |
| `server.method` | enum | No | `POST` (default), `GET`, `PUT`, `PATCH`, `DELETE` |
| `server.headers` | object | No | Custom headers |
| `server.timeoutSeconds` | number | No | Default 20 |
| `server.backoffPlan` | object | No | Retry config: `{type: "fixed"|"exponential", maxRetries, baseDelaySeconds}` |
| `messages` | array | No | Status messages during tool execution |
| `async` | bool | No | If true, tool resolves immediately (for long-running operations) |

### Server-Side Tool Request Format

When the AI invokes a tool, Vapi POSTs to your server URL:

```json
{
  "message": {
    "type": "tool-calls",
    "toolCalls": [
      {
        "id": "call_VaJOd8ZeZgWCEHDYomyCPfwN",
        "type": "function",
        "function": {
          "name": "lookup_carrier",
          "arguments": "{\"dot_number\": \"12345\"}"
        }
      }
    ],
    "toolCallList": [
      {
        "id": "call_VaJOd8ZeZgWCEHDYomyCPfwN",
        "function": {
          "name": "lookup_carrier",
          "arguments": { "dot_number": "12345" }
        }
      }
    ],
    "call": {
      "id": "call_abc123",
      "assistantId": "asst_abc123",
      "customer": { "number": "+15551234567" }
    }
  }
}
```

### Server-Side Tool Response Format

**CRITICAL RULES**:
- Always return HTTP 200, even for errors
- No line breaks (`\n`) in result strings
- `toolCallId` must exactly match the request's ID
- Both `result` and `error` must be strings, never objects

```json
{
  "results": [
    {
      "toolCallId": "call_VaJOd8ZeZgWCEHDYomyCPfwN",
      "result": "Found carrier: Smith Trucking LLC, DOT# 12345, 3 power units, Active status, Insurance: Expired 2026-01-15, Location: Dallas TX"
    }
  ]
}
```

For errors:
```json
{
  "results": [
    {
      "toolCallId": "call_VaJOd8ZeZgWCEHDYomyCPfwN",
      "error": "Carrier not found in our database. DOT number may be invalid."
    }
  ]
}
```

### How Tool Results Get Injected Back

The tool result is injected into the conversation as a `tool` message. The AI sees the result and responds naturally. For example, after receiving the carrier lookup result, the AI might say:

> "Great, I found your information. You're with Smith Trucking, 3 trucks in Dallas. It looks like your insurance expired back in January — that's actually why I'm calling. We work with agencies that specialize in commercial auto coverage for fleets your size..."

### Async Tools

For long-running operations, set `async: true`. The AI says the "request-start" message and continues the conversation. When your server finishes, it can inject the result via the call's `controlUrl`:

```bash
POST {controlUrl}
{
  "type": "add-message",
  "message": {
    "role": "tool",
    "content": "CRM has been updated with the call outcome.",
    "toolCallId": "call_xyz"
  }
}
```

### Multiple Tools in One Conversation

Yes — the AI can call tool A, get the result, then call tool B. For example:

1. AI calls `lookup_carrier` → gets carrier info
2. AI asks qualification questions
3. AI calls `score_lead` → gets qualification score
4. If qualified, AI calls `transferCall` → transfers to agency

### Error Handling

When your tool server returns an error (in the `error` field), the AI sees it and responds contextually — typically asking the user to repeat information or apologizing for the issue.

### Full Working Example: lookup_carrier Tool

**Assistant config** (the tool definition):

```json
{
  "type": "function",
  "function": {
    "name": "lookup_carrier",
    "description": "Look up a motor carrier by DOT number. Returns carrier name, truck count, insurance status, and location.",
    "parameters": {
      "type": "object",
      "properties": {
        "dot_number": {
          "type": "string",
          "description": "The carrier's USDOT number"
        }
      },
      "required": ["dot_number"]
    }
  },
  "server": {
    "url": "https://oex-api.yourdomain.com/vapi/tools/lookup-carrier",
    "timeoutSeconds": 10
  },
  "messages": [
    { "type": "request-start", "content": "Let me pull up your carrier information." },
    { "type": "request-complete", "content": "Found it." },
    { "type": "request-failed", "content": "I'm having trouble looking that up right now." },
    { "type": "request-response-delayed", "content": "Still searching, one moment.", "timingMilliseconds": 3000 }
  ]
}
```

**Server endpoint** (FastAPI):

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/vapi/tools/lookup-carrier")
async def lookup_carrier(request: Request):
    data = await request.json()
    tool_call = data["message"]["toolCallList"][0]
    args = tool_call["function"]["arguments"]
    dot_number = args["dot_number"]

    # Query data-engine-x API
    carrier = await data_engine_client.get_carrier(dot_number)

    if carrier:
        result = (
            f"Carrier: {carrier['name']}, "
            f"DOT# {carrier['dot_number']}, "
            f"Power Units: {carrier['power_units']}, "
            f"Status: {carrier['status']}, "
            f"Insurance Expiry: {carrier['insurance_expiry']}, "
            f"Location: {carrier['city']}, {carrier['state']}"
        )
    else:
        result = f"No carrier found with DOT number {dot_number}."

    return {
        "results": [
            {
                "toolCallId": tool_call["id"],
                "result": result,
            }
        ]
    }
```

### Tool Rejection Plan

Prevents tool execution based on conversation state:

```json
{
  "rejectionPlan": {
    "conditions": [
      {
        "type": "regex",
        "regex": "\\b(cancel|stop|nevermind)\\b",
        "target": { "role": "user", "position": -1 }
      }
    ]
  }
}
```

### Static Variables and Aliases (Tool Chaining)

**Static variables**: Key-value pairs merged into tool requests after LLM args (invisible to LLM):

```json
{
  "server": { "url": "..." },
  "parameters": {
    "api_key": "secret_123",
    "customer_phone": "{{ customer.number }}"
  }
}
```

**Variable extraction** (from tool responses for chaining):

```json
{
  "variableExtractionPlan": {
    "aliases": [
      { "name": "carrier_id", "template": "{{ $.data.id }}" },
      { "name": "carrier_status", "template": "{{ $.data.status }}" }
    ]
  }
}
```

Extracted variables persist for the entire call and are globally accessible.

---

## 8. Call Transfer — Deep Dive

### Transfer Mechanism

Call transfer is implemented as a **tool the AI calls** — specifically the `transferCall` tool type. When the AI determines a transfer is needed (based on its system prompt), it invokes the transfer tool.

### Transfer Modes

#### Blind Transfer (Default)

Direct transfer without context to the receiving party:

```json
{
  "type": "transferCall",
  "destinations": [
    {
      "type": "number",
      "number": "+15559876543",
      "message": "I'm going to connect you with one of our insurance specialists now."
    }
  ]
}
```

#### Warm Transfer

The AI provides context to the receiving agent before connecting the caller. **Requires Twilio-based telephony.**

| Mode | Behavior |
|------|----------|
| `warm-transfer-with-summary` | Provides AI-generated summary from `{{transcript}}` to recipient |
| `warm-transfer-with-message` | Delivers a custom static message to recipient |
| `warm-transfer-wait-for-operator-to-speak-first-and-then-say-message` | Waits for recipient to speak, then delivers message |
| `warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary` | Waits for recipient to speak, then delivers summary |
| `warm-transfer-with-twiml` | Executes TwiML on destination leg (max 4096 chars) |
| `warm-transfer-experimental` | Dials destination, places caller on hold; merges if answered; plays fallback if voicemail |

**Warm transfer with summary example**:

```json
{
  "type": "transferCall",
  "destinations": [
    {
      "type": "number",
      "number": "+15559876543",
      "message": "Transferring you now to a specialist who can help with your coverage.",
      "transferMode": "warm-transfer-with-summary",
      "summaryPlan": {
        "messages": [
          {
            "role": "system",
            "content": "Summarize this call for the insurance agent. Include: caller name, DOT number, truck count, qualification status, and any specific coverage needs mentioned."
          }
        ]
      }
    }
  ]
}
```

**Can the AI say something to the agent before connecting the caller?**

Yes — this is exactly what warm transfer does. In `warm-transfer-with-summary` mode, the AI generates a summary like: *"I have John Smith on the line, DOT# 12345. He runs Smith Trucking with 3 trucks in Dallas. His insurance expired in January and he's looking for commercial auto coverage. He confirmed he's the decision maker."*

#### Assistant-Based Warm Transfer (Experimental)

A separate AI assistant manages the handoff with the operator:

```json
{
  "type": "transferCall",
  "destinations": [
    {
      "type": "number",
      "number": "+15559876543",
      "transferMode": "warm-transfer-experimental",
      "assistant": {
        "firstMessage": "Hi, this is Sarah's AI assistant from LicensedToHaul. I have a qualified lead on the line — John Smith, DOT 12345, 3 trucks in Dallas, needs commercial auto coverage. Are you available to take the call?",
        "model": {
          "provider": "openai",
          "model": "gpt-4o"
        }
      }
    }
  ]
}
```

The transfer assistant calls `transferSuccessful` to merge calls or `transferCancel` to return the customer.

### Dynamic Transfer Destinations

For transfers where the destination depends on conversation context:

**Option 1**: Empty `destinations` + `transfer-destination-request` webhook:

```json
{
  "type": "transferCall",
  "destinations": []
}
```

When the AI invokes this tool, Vapi sends a `transfer-destination-request` to your server:

```json
{
  "type": "transfer-destination-request",
  "call": { "id": "call_abc123" },
  "assistant": { "id": "asst_abc123" }
}
```

Your server responds with the destination:

```json
{
  "destination": {
    "type": "number",
    "number": "+15559876543",
    "message": "Connecting you now."
  }
}
```

**Option 2**: Server-controlled via `controlUrl`:

Your custom tool receives the `controlUrl` in the request payload, then POSTs the transfer command directly:

```bash
POST {controlUrl}
{
  "type": "transfer",
  "destination": {
    "type": "number",
    "number": "+15559876543"
  }
}
```

### What Happens After Transfer

- **Blind transfer**: Vapi session ends. The call continues between caller and destination.
- **Warm transfer**: Vapi session ends after the merge. The call recording continues if the destination's system records.
- The `endedReason` will be `"assistant-forwarded-call"`.
- The `end-of-call-report` webhook fires with the full transcript up to the transfer point.

### Transfer to Specific Phone Number (Agency)

```json
{
  "type": "transferCall",
  "destinations": [
    {
      "type": "number",
      "number": "+15559876543",
      "callerId": "+14155551234",
      "message": "Great news — I'm connecting you with a licensed insurance agent right now who can get you covered today.",
      "transferMode": "warm-transfer-with-summary"
    }
  ]
}
```

### Full Working Example: Qualification → Transfer Flow

```json
{
  "name": "OEX Insurance Qualifier",
  "firstMessage": "Hi {{customerName}}, this is Sarah from LicensedToHaul. I'm calling because we help trucking companies like yours find the best rates on commercial auto insurance. Do you have a quick moment?",
  "model": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-20250514",
    "messages": [
      {
        "role": "system",
        "content": "You are Sarah, an insurance qualification specialist at LicensedToHaul.\n\nContext: {{customerName}}, DOT# {{dotNumber}}, {{truckCount}} trucks.\n\nGOALS:\n1. Get permission to continue the call\n2. Verify their fleet details (truck count, types)\n3. Ask about current insurance (provider, renewal date, satisfaction)\n4. Confirm they are the decision maker\n5. If qualified: use the transfer_to_agency tool to connect them with a licensed agent\n6. If not qualified: thank them, offer to call back later\n\nQUALIFICATION CRITERIA:\n- Has at least 1 commercial vehicle\n- Insurance is expiring within 90 days OR they're shopping\n- They are the decision maker (or can connect you)\n\nSTYLE: Friendly, professional, concise. Keep responses under 30 words. Never mention you're an AI."
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "lookup_carrier",
          "description": "Look up carrier info by DOT number",
          "parameters": {
            "type": "object",
            "properties": {
              "dot_number": { "type": "string" }
            },
            "required": ["dot_number"]
          }
        },
        "server": { "url": "https://oex-api.yourdomain.com/vapi/tools/lookup-carrier" }
      },
      {
        "type": "transferCall",
        "destinations": [
          {
            "type": "number",
            "number": "+15559876543",
            "message": "Wonderful! I'm connecting you with a licensed agent right now who can review your options. One moment.",
            "transferMode": "warm-transfer-with-summary",
            "summaryPlan": {
              "messages": [
                {
                  "role": "system",
                  "content": "Summarize for the insurance agent: caller name, DOT#, truck count, current insurance status, any specific needs, and qualification assessment."
                }
              ]
            }
          }
        ]
      }
    ]
  }
}
```

---

## 9. Webhooks / Server Events — Complete Specification

### Overview

Vapi sends events to your `serverUrl` during and after calls. Some events require a response; others are informational.

### Server URL Priority

| Priority | Level | Where to Configure |
|----------|-------|--------------------|
| 1 (highest) | Tool/Function-level | Tool `server.url` |
| 2 | Assistant-level | Assistant `serverUrl` |
| 3 | Phone number-level | Phone number `server.url` |
| 4 (lowest) | Account-wide | Organization settings |

### Events Requiring Responses

#### `assistant-request`

Fires when an inbound call arrives on a number without a static assistant assignment.

**Timeout**: 7.5 seconds (hard limit from telephony providers)

**Request payload**:
```json
{
  "type": "assistant-request",
  "phoneNumber": {
    "provider": "twilio",
    "number": "+14155551234",
    "assistantId": null,
    "squadId": null
  },
  "call": {
    "customer": {
      "number": "+15559876543"
    }
  }
}
```

**Response options**:
```json
// Option 1: Reference a saved assistant
{ "assistantId": "asst_abc123" }

// Option 2: Inline assistant
{ "assistant": { "name": "...", "model": {...}, "voice": {...} } }

// Option 3: Reject the call
{ "error": "This number is not authorized. Goodbye." }
```

#### `tool-calls` (Function Call)

Fires when the AI invokes a server-side tool.

**Request payload**:
```json
{
  "type": "tool-calls",
  "toolCallList": [
    {
      "id": "call_abc123",
      "function": {
        "name": "lookup_carrier",
        "arguments": { "dot_number": "12345" }
      }
    }
  ],
  "call": {
    "id": "call_xyz",
    "customer": { "number": "+15551234567" }
  }
}
```

**Required response**:
```json
{
  "results": [
    {
      "toolCallId": "call_abc123",
      "result": "Carrier found: Smith Trucking LLC, 3 trucks, Active status"
    }
  ]
}
```

#### `transfer-destination-request`

Fires when a transfer tool has empty destinations and needs dynamic routing.

**Request**: Call context + conversation history
**Response**: `{ "destination": { "type": "number", "number": "+1555..." } }`

#### `knowledge-base-request`

Fires for custom knowledge base queries.

### Informational Events (No Response Required)

#### `status-update`

Fires on call status transitions.

```json
{
  "type": "status-update",
  "status": "in-progress",
  "call": {
    "id": "call_abc123",
    "type": "outboundPhoneCall",
    "status": "in-progress"
  }
}
```

**Status values**: `scheduled`, `queued`, `ringing`, `in-progress`, `forwarding`, `ended`

#### `end-of-call-report`

Fires after a call ends. Contains everything about the call.

```json
{
  "type": "end-of-call-report",
  "call": {
    "id": "call_abc123",
    "type": "outboundPhoneCall",
    "status": "ended",
    "endedReason": "assistant-forwarded-call",
    "startedAt": "2026-03-25T10:30:00Z",
    "endedAt": "2026-03-25T10:35:00Z",
    "duration": 300,
    "costBreakdown": {
      "transport": 0.05,
      "stt": 0.15,
      "llm": 0.20,
      "tts": 0.10,
      "vapi": 0.50,
      "total": 1.00
    }
  },
  "artifact": {
    "transcript": "AI: Hi John, this is Sarah from LicensedToHaul...\nUser: Yeah, hi...",
    "recording": "https://storage.vapi.ai/recordings/call_abc123.wav",
    "recordingUrl": "https://storage.vapi.ai/recordings/call_abc123.wav",
    "messages": [
      { "role": "assistant", "content": "Hi John...", "secondsFromStart": 0.5 },
      { "role": "user", "content": "Yeah, hi...", "secondsFromStart": 3.2 }
    ],
    "structuredData": {
      "dotNumber": "12345",
      "truckCount": 3,
      "qualified": true,
      "interestLevel": "high"
    }
  },
  "analysis": {
    "summary": "Outbound call to John Smith (DOT# 12345). Successfully qualified — 3 trucks, insurance expired, decision maker. Transferred to agency.",
    "successEvaluation": "pass",
    "structuredData": { "dotNumber": "12345", "qualified": true }
  }
}
```

#### `transcript`

Real-time transcript updates during the call.

```json
{
  "type": "transcript",
  "role": "user",
  "transcript": "Yeah I have three trucks, two box trucks and a flatbed.",
  "transcriptType": "final"
}
```

`transcriptType`: `"partial"` (streaming) or `"final"` (confirmed)

#### `speech-update`

Voice activity indicators.

```json
{
  "type": "speech-update",
  "role": "assistant",
  "status": "started"
}
```

#### `hang`

Fires when the assistant fails to respond (silence/error).

### Webhook Signature Verification

**Legacy method** (inline secret):
```json
{ "serverUrlSecret": "your_secret" }
```
Vapi sends this in the `X-Vapi-Secret` header. Verify:
```python
if request.headers.get("X-Vapi-Secret") != EXPECTED_SECRET:
    return Response(status_code=401)
```

**Recommended method** (credential-based HMAC):
Configure via Dashboard → Custom Credentials with HMAC type.

### OEX Webhook Consumption Patterns

| Event | OEX Action |
|-------|------------|
| `status-update` (ringing) | Update campaign status: "calling" |
| `status-update` (in-progress) | Update campaign status: "connected" |
| `end-of-call-report` | Log outcome, update lead status, trigger follow-up |
| `tool-calls` (lookup_carrier) | Query data-engine-x, return carrier info |
| `transfer-destination-request` | Look up assigned agency, return transfer number |
| `transcript` | Real-time monitoring dashboard |

### Full Working Python Webhook Handler (FastAPI)

```python
from fastapi import FastAPI, Request, Response
import json
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

WEBHOOK_SECRET = "your_vapi_webhook_secret"

@app.post("/vapi/webhook")
async def vapi_webhook(request: Request):
    # Verify webhook signature
    secret = request.headers.get("X-Vapi-Secret")
    if secret != WEBHOOK_SECRET:
        return Response(status_code=401)

    data = await request.json()
    event_type = data.get("type") or data.get("message", {}).get("type")

    # ── Events requiring responses ──

    if event_type == "assistant-request":
        caller = data.get("call", {}).get("customer", {}).get("number")
        assistant_id = await select_assistant_for_caller(caller)
        return {"assistantId": assistant_id}

    if event_type == "tool-calls":
        tool_calls = data.get("message", {}).get("toolCallList", [])
        results = []
        for tc in tool_calls:
            fn_name = tc["function"]["name"]
            args = tc["function"]["arguments"]

            if fn_name == "lookup_carrier":
                carrier = await lookup_carrier_in_dex(args["dot_number"])
                results.append({
                    "toolCallId": tc["id"],
                    "result": format_carrier_result(carrier)
                })
            elif fn_name == "score_lead":
                score = await score_lead(args)
                results.append({
                    "toolCallId": tc["id"],
                    "result": json.dumps(score)
                })
            elif fn_name == "update_crm":
                await update_lead_in_crm(args)
                results.append({
                    "toolCallId": tc["id"],
                    "result": "CRM updated successfully"
                })
            else:
                results.append({
                    "toolCallId": tc["id"],
                    "error": f"Unknown tool: {fn_name}"
                })

        return {"results": results}

    if event_type == "transfer-destination-request":
        call_id = data.get("call", {}).get("id")
        agency = await get_assigned_agency(call_id)
        return {
            "destination": {
                "type": "number",
                "number": agency["phone"],
                "message": f"Connecting you with {agency['name']} now."
            }
        }

    # ── Informational events ──

    if event_type == "status-update":
        status = data.get("status")
        call_id = data.get("call", {}).get("id")
        await update_campaign_call_status(call_id, status)
        return {"ok": True}

    if event_type == "end-of-call-report":
        call = data.get("call", {})
        analysis = data.get("analysis", {})
        artifact = data.get("artifact", {})

        await log_call_outcome(
            call_id=call["id"],
            duration=call.get("duration"),
            ended_reason=call.get("endedReason"),
            cost=call.get("costBreakdown", {}).get("total"),
            summary=analysis.get("summary"),
            success=analysis.get("successEvaluation"),
            structured_data=analysis.get("structuredData"),
            transcript=artifact.get("transcript"),
            recording_url=artifact.get("recordingUrl"),
        )
        return {"ok": True}

    if event_type == "transcript":
        # Real-time transcript for monitoring
        logger.info(f"[{data.get('role')}]: {data.get('transcript')}")
        return {"ok": True}

    return {"ok": True}
```

---

## 10. Call Recording & Transcription

### Recording Configuration

Controlled via the `artifactPlan` in the assistant:

```json
{
  "artifactPlan": {
    "recordingEnabled": true,
    "recordingFormat": "wav;l16",
    "loggingEnabled": true,
    "pcapEnabled": true,
    "transcriptPlan": {
      "assistantName": "Sarah",
      "userName": "Prospect"
    }
  }
}
```

| Field | Default | Description |
|-------|---------|-------------|
| `recordingEnabled` | true | Enable call recording |
| `recordingFormat` | — | Audio format (e.g., `"wav;l16"`) |
| `loggingEnabled` | true | Detailed logging |
| `pcapEnabled` | true | SIP packet capture for phone calls |
| `transcriptPlan.assistantName` | "AI" | Name label for assistant in transcript |
| `transcriptPlan.userName` | "User" | Name label for caller in transcript |

### Are Calls Recorded Automatically?

Yes — recording is enabled by default. Set `recordingEnabled: false` to disable.

### Storage

**Default**: Vapi encrypted cloud. Retention: 14 days (calls), 30 days (chat) on pay-as-you-go; configurable on Enterprise.

**Custom storage**: AWS S3, GCP, Cloudflare R2, Supabase. Configure in Dashboard → Provider Credentials → Cloud Providers.

```json
{
  "artifactPlan": {
    "recordingPath": "s3://your-bucket/recordings/",
    "recordingCredentialId": "cred_s3_abc"
  }
}
```

### Recording Format

Stereo WAV by default. Channel 0 = caller, Channel 1 = AI assistant.

### Real-Time Transcription

Delivered via the `transcript` webhook event during the call:

```json
{
  "type": "transcript",
  "role": "user",
  "transcript": "I have three trucks.",
  "transcriptType": "final"
}
```

`transcriptType`: `"partial"` (streaming, may change) or `"final"` (confirmed)

### Post-Call Transcription

Full transcript available in the `end-of-call-report` webhook and via API:

```
GET /call/{id}
```

Response includes:
- `artifact.transcript` — full text transcript
- `artifact.messages` — array of timestamped messages with roles
- `artifact.recordingUrl` — URL to download the recording

### Retrieval Options

1. **Webhook** (`end-of-call-report`): Automatic delivery after call ends
2. **API poll**: `GET /call/{id}` — includes `artifact.transcript`, `artifact.recordingUrl`, `artifact.messages`
3. **Custom storage**: Recordings auto-uploaded to your S3/GCP/R2 bucket

---

## 11. Conversation Design for Voice

### System Prompt Structure for Voice Agents

Voice prompts differ from chat — shorter sentences, more direct:

```
You are Sarah, an insurance specialist at LicensedToHaul.

STYLE:
- Keep responses under 30 words
- Use short, direct sentences
- Never use bullet points or numbered lists (the caller can't see them)
- Spell out numbers: say "three trucks" not "3 trucks"
- Never mention you're an AI

GOALS:
1. Get permission to continue the call
2. Verify fleet details
3. Ask about current insurance
4. Qualify the lead
5. Transfer to agency if qualified

QUALIFICATION CRITERIA:
- Has commercial vehicles
- Insurance expiring within 90 days or actively shopping
- Is the decision maker

<wait for user response>

If the caller says they're busy, offer to call back at a specific time.
If the caller is hostile, apologize for bothering them and end the call politely.
```

### First Message Handling

| Scenario | firstMessageMode | firstMessage |
|----------|-----------------|-------------|
| **Outbound** (AI speaks first) | `assistant-speaks-first` | "Hi {{customerName}}, this is Sarah from LicensedToHaul..." |
| **Inbound** (caller speaks first) | `assistant-waits-for-user` | — (no firstMessage needed) |
| **Inbound with greeting** | `assistant-speaks-first` | "Thanks for calling LicensedToHaul! How can I help?" |

### Interruption Handling

Configure via `stopSpeakingPlan`:
- `numWords: 0` — VAD-based, most sensitive (50-100ms detection)
- `numWords: 2-3` — Requires 2-3 words before stopping, fewer false positives
- `voiceSeconds: 0.2` — Default VAD threshold
- `backoffSeconds: 1.0` — Pause after interruption before resuming

### Silence Handling

- `silenceTimeoutSeconds`: Ends call after X seconds of silence (default: 30)
- **Idle messages** via hooks: Prompt the caller after periods of silence

```json
{
  "hooks": [
    {
      "on": "customer.speech.timeout",
      "do": [{ "type": "say", "exact": "Are you still there?" }],
      "options": { "timeoutSeconds": 10, "maxCount": 3 }
    }
  ]
}
```

### Guardrails

In the system prompt:
```
NEVER discuss:
- Competitor pricing
- Legal advice
- Specific policy terms (you're not a licensed agent)
- Anything outside of insurance qualification

If asked about these topics, say: "That's a great question for the licensed agent I can connect you with."
```

### Call Ending

```
ENDING THE CALL:
- If qualified and transferred: "Great talking with you, John. The agent will take great care of you."
- If not qualified: "Thanks for your time, John. We'll keep you in mind if your situation changes."
- If hostile: "I apologize for the interruption. Have a great day."
```

The AI can also use the built-in `endCall` tool to terminate programmatically.

### Turn-Taking

Vapi manages turn-taking via its proprietary endpointing model. Key configs:
- `startSpeakingPlan.waitSeconds`: How long to wait after user stops before AI speaks
- `stopSpeakingPlan.numWords`: How many words trigger an interruption
- `backchannelingEnabled`: Allow "yeah", "uh-huh" without triggering a full response

### Example System Prompt: Insurance Qualification Call to a Trucker

```
You are Sarah, a friendly insurance specialist at LicensedToHaul.

CONTEXT:
You are calling {{customerName}} at {{companyName}}.
DOT Number: {{dotNumber}}
Fleet Size: {{truckCount}} trucks
Location: {{city}}, {{state}}

PERSONALITY:
- Warm but professional
- Knowledgeable about trucking insurance
- Empathetic to the challenges of running a trucking business
- Never pushy — you're there to help, not hard-sell

OPENING:
After the greeting, briefly explain why you're calling: "We specialize in helping trucking companies find competitive rates on commercial auto insurance."

QUALIFICATION FLOW:
1. Ask if they have a moment to chat
2. Verify their fleet details: "I show you have about {{truckCount}} trucks — is that still accurate?"
3. Ask about current coverage: "Who handles your insurance currently?"
4. Ask about renewal: "When does your current policy renew?"
5. Ask about satisfaction: "How have your rates been trending?"
6. Gauge decision authority: "Are you the one who handles insurance decisions?"

TRANSFER CRITERIA:
Transfer to agency if ALL are true:
- Has at least 1 commercial vehicle
- Open to discussing coverage options
- Insurance renewing within 90 days OR actively shopping
- Is decision maker or can conference them in

Before transferring, say: "I'd love to connect you with one of our licensed agents who can pull actual quotes for you. It'll just take a couple minutes. Sound good?"

OBJECTION HANDLING:
- "I'm busy": "Totally understand. When would be a better time to chat? I can have someone call you back."
- "Not interested": "No problem at all. Just so you know, we typically save carriers 15-20% on their premiums. If that ever becomes relevant, we're here."
- "Already have good insurance": "That's great to hear. Mind if I ask who you're with? Sometimes we can still find savings."
- "How did you get my number?": "Your information is part of the public FMCSA database that all carriers are listed in."
```

---

## 12. Provider Configuration — Our Stack

### Deepgram as STT (Transcriber)

```json
{
  "transcriber": {
    "provider": "deepgram",
    "model": "nova-2",
    "language": "en",
    "smartFormat": true,
    "keywords": ["DOT:5", "FMCSA:5", "LicensedToHaul:3", "trucking:2"],
    "confidenceThreshold": 0.4,
    "endpointing": 255
  }
}
```

**Credential config**: Add Deepgram API key in Dashboard → Integrations → Transcription Providers. Once added, charges go directly to your Deepgram account (bypass Vapi billing).

**Model options**: `nova-2` (recommended), `nova-3` (newer, supports `keyterm`), `enhanced`, `base`, `whisper`

**For multilingual**: Set `language: "multi"` for auto-detection (Nova-2/Nova-3).

### Anthropic/Claude as LLM

```json
{
  "model": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-20250514",
    "temperature": 0.7,
    "maxTokens": 300,
    "messages": [
      {
        "role": "system",
        "content": "Your system prompt here..."
      }
    ],
    "emotionRecognitionEnabled": true
  }
}
```

**Credential config**: Add Anthropic API key in Dashboard → Integrations → Model Providers.

**Model options**: `claude-sonnet-4-20250514`, `claude-3-5-sonnet-20241022`, `claude-3-opus-20240229`, `claude-3-5-haiku-20241022`

**For Bedrock**: Use `provider: "anthropic-bedrock"` with AWS IAM role (Vapi AWS account ID to trust: `533267069243`).

### ElevenLabs as TTS (Voice)

```json
{
  "voice": {
    "provider": "11labs",
    "voiceId": "21m00Tcm4TlvDq8ikWAM",
    "model": "eleven_turbo_v2",
    "stability": 0.5,
    "similarityBoost": 0.75,
    "style": 0.0,
    "useSpeakerBoost": false,
    "chunkPlan": {
      "enabled": true,
      "minCharacters": 30,
      "formatPlan": {
        "enabled": true,
        "numberToDigitsCutoff": 2025
      }
    },
    "fallbackPlan": {
      "voices": [
        { "provider": "openai", "voiceId": "alloy" }
      ]
    }
  }
}
```

**Credential config**: Add ElevenLabs API key in Dashboard → Integrations. Voice library auto-syncs.

**Model options**: `eleven_turbo_v2` (recommended — low latency), `eleven_flash_v2`, `eleven_multilingual_v2`

**Voice settings**:
- `stability` (0-1): Lower = more expressive, higher = more consistent
- `similarityBoost` (0-1): How closely to match the original voice
- `style` (0-1): Style exaggeration

**Pronunciation dictionaries**: ElevenLabs-exclusive feature. Upload via `POST /provider/11labs/pronunciation-dictionary`.

### Twilio as Telephony

Twilio is configured when you import a phone number:

```json
{
  "provider": "twilio",
  "number": "+14155551234",
  "twilioAccountSid": "AC...",
  "twilioAuthToken": "..."
}
```

**How Vapi connects to Twilio**: When you import a Twilio number, Vapi automatically configures Twilio's webhook to route calls to Vapi. No manual TwiML setup needed.

**For SIP trunking**: Create credentials via `POST /credential` with `provider: "byo-sip-trunk"`. Whitelist Vapi SIP IPs: `44.229.228.186/32` and `44.238.177.138/32`.

---

## 13. Pricing — Itemized Cost Breakdown

### Per-Minute Costs (Our Stack)

| Component | Provider | Cost | Notes |
|-----------|----------|------|-------|
| **Vapi orchestration** | Vapi | ~$0.05/min | Orchestration layer fee |
| **STT** | Deepgram Nova-2 | ~$0.0043/min | $0.0043/min streaming |
| **LLM** | Claude Sonnet | ~$0.02-0.05/min | Varies by tokens/min; estimated 500-1000 tokens/min of conversation |
| **TTS** | ElevenLabs Turbo v2 | ~$0.04/min | Depends on plan tier |
| **Telephony** | Twilio | ~$0.014/min | Outbound US calls |
| **Total estimated** | — | **~$0.13-0.16/min** | Per call |

**Note**: With BYOK (bring your own keys), provider charges go directly to each provider at your negotiated rates. Vapi charges only the orchestration fee.

### Competitor Comparison

| Platform | Per-Minute Cost | Notes |
|----------|----------------|-------|
| **Bland.ai** | $0.09/min | All-inclusive |
| **Retell.ai** | $0.07/min | All-inclusive |
| **Vapi (our stack)** | ~$0.13-0.16/min | Itemized; more control over providers |

Vapi is more expensive per-minute but offers full provider flexibility, custom model selection, and no vendor lock-in.

### Cost Breakdown in Call Response

Every call response includes a `costBreakdown` object:

```json
{
  "costBreakdown": {
    "transport": 0.014,
    "stt": 0.0043,
    "llm": 0.035,
    "tts": 0.04,
    "vapi": 0.05,
    "total": 0.1433
  }
}
```

---

## 14. Rate Limits & Concurrency

### Concurrent Call Limits

| Plan | Default Concurrent Calls |
|------|-------------------------|
| Free/Starter | 10 |
| Growth | Configurable |
| Enterprise | Unlimited (reserved capacity) |

- Each active call occupies one slot
- Incoming calls **queue** when capacity is exhausted
- Upgrade: Dashboard → Settings → Billing → Reserved Concurrency (takes effect immediately)

### API Rate Limits

Standard REST API rate limiting applies. Enterprise plans get higher limits.

### What Happens When You Exceed

- **Concurrent calls**: Additional calls queue; `subscriptionLimits` in the API response shows remaining slots
- **API rate limit**: HTTP 429 response

### Monitoring

```
POST /analytics
```

```json
{
  "queries": [{
    "table": "call",
    "name": "concurrent_calls",
    "operations": [{ "operation": "max", "column": "concurrency" }],
    "timeRange": { "start": "2026-03-24T00:00:00Z", "end": "2026-03-25T23:59:59Z" }
  }]
}
```

### Scaling Strategy for OEX

- Batch contact lists into groups of 50-100
- Execute groups sequentially
- Monitor `subscriptionLimits` in API responses
- For 50,000+ monthly minutes: explore custom enterprise plans

---

## 15. Error Handling & Edge Cases

### Call Failure Categories

#### Phone Never Rang

| endedReason | Cause |
|-------------|-------|
| `call.start.error-*` | Configuration errors |
| `subscription-frozen` | Account suspended |
| `insufficient-credits` | No balance |
| `assistant-not-found` | Invalid assistant ID |
| `phone-number-not-found` | Invalid phone number ID |
| `international-call-restriction` | Free number can't call internationally |

#### Phone Rang, No Answer

| endedReason | Cause |
|-------------|-------|
| `customer-did-not-answer` | Rang out |
| `customer-busy` | Line busy |

#### Mid-Call Drop

| endedReason | Cause |
|-------------|-------|
| `call.in-progress.error-vapifault-*` | Vapi platform failure (typically no charge) |
| `call.in-progress.error-providerfault-*` | Third-party provider failure |
| `pipeline-error-*` | Credential or quota issue with custom provider keys |
| `*-worker-died` | Infrastructure error |

#### Provider Failures

- **LLM**: Validation errors, authorization failures, quota exceeded, server errors
- **TTS**: Voice not found, quota exceeded, credential problems
- **STT**: Bad requests, invalid credentials, provider outages
- **Twilio**: Connection failures, invalid numbers

### Failover Strategy

1. **Transcriber fallback**: Configure `fallbackPlan` with alternate STT providers
2. **Voice fallback**: Configure `fallbackPlan` with alternate TTS providers
3. **LLM**: No automatic failover — monitor provider status pages
4. **Telephony**: SIP trunking failover via multiple gateway IPs

### Recommended Error Handling for OEX

```python
async def handle_end_of_call(report):
    ended_reason = report["call"]["endedReason"]

    if ended_reason == "customer-did-not-answer":
        await schedule_retry(report["call"]["id"], delay_hours=2)
    elif ended_reason == "customer-busy":
        await schedule_retry(report["call"]["id"], delay_hours=1)
    elif "vapifault" in ended_reason:
        # Vapi issue — retry immediately
        await schedule_retry(report["call"]["id"], delay_minutes=5)
    elif "providerfault" in ended_reason:
        # Provider issue — retry with delay
        await schedule_retry(report["call"]["id"], delay_minutes=15)
    elif ended_reason == "assistant-forwarded-call":
        await mark_lead_transferred(report)
    elif ended_reason in ("assistant-ended-call", "customer-ended-call"):
        await process_call_outcome(report)
```

---

## 16. Voicemail Detection & Handling

### Does Vapi Have Built-In AMD?

**Yes.** Vapi has built-in answering machine detection.

### Provider Comparison

| Provider | Speed | Accuracy | Cost | Recommendation |
|----------|-------|----------|------|----------------|
| `vapi` | Fast | High | Included | **Strongly recommended** — hybrid Gemini + Twilio beep detection |
| `google` | Moderate | Very high | Moderate | Highly reliable alternative |
| `openai` | Moderate | High | Higher | Transcript-based detection |
| `twilio` | Very fast | Moderate | Low | Fast beep detection, prone to false alarms |

### Configuration

```json
{
  "voicemailDetection": {
    "provider": "vapi",
    "enabled": true,
    "voicemailDetectionTypes": ["audio"],
    "startAtSeconds": 0,
    "frequencySeconds": 2.5,
    "maxRetries": 3,
    "beepMaxAwaitSeconds": 15
  }
}
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `provider` | — | `vapi`, `google`, `openai`, `twilio` |
| `voicemailDetectionTypes` | `["audio"]` | `audio` (optimal for vapi/google) or `transcript` (recommended for openai) |
| `startAtSeconds` | 0 | Delay before detection begins |
| `frequencySeconds` | 2.5 | Polling interval (minimum 2.5s) |
| `maxRetries` | 3 | Max detection attempts |
| `beepMaxAwaitSeconds` | 15 | Max wait for voicemail beep (0-60s). Below 15-20s risks cutting off the greeting |

### What Happens When Voicemail Is Detected

Vapi can:
1. Play a **pre-recorded audio message** (MP3/WAV URL)
2. Have the **AI leave a voicemail** using the voicemail tool
3. **End the call** immediately

### Recommended Pattern for OEX

**Option A — Vapi AMD (simpler)**:
```json
{
  "voicemailDetection": {
    "provider": "vapi",
    "enabled": true,
    "beepMaxAwaitSeconds": 15
  }
}
```
When voicemail detected, the voicemail tool plays a pre-recorded ElevenLabs message.

**Option B — Twilio AMD before Vapi (cheaper)**:
1. Twilio receives the call
2. Twilio AMD runs (~3-5 seconds)
3. If **human** → forward to Vapi for AI conversation
4. If **machine** → Twilio plays pre-recorded audio directly (no Vapi charge)

This approach avoids Vapi charges on voicemails entirely. Requires Twilio Studio or TwiML configuration.

### Voicemail Tool (AI-Driven)

For AI-generated voicemails:

```json
{
  "type": "function",
  "function": {
    "name": "leave_voicemail",
    "description": "Leave a voicemail when the system detects voicemail"
  },
  "messages": [
    {
      "type": "request-complete",
      "content": "Hi {{customerName}}, this is Sarah from LicensedToHaul. I'm calling about commercial auto insurance for your fleet. We often save carriers 15-20% on premiums. Please call us back at 1-800-555-0199. Thanks!"
    }
  ]
}
```

**Warning**: Do not combine the voicemail tool with automatic detection simultaneously.

---

## 17. Multi-Tenant Considerations

### Architecture for Multiple Brands

Vapi doesn't have a built-in multi-tenant account structure. Multi-tenancy is achieved by:

1. **Separate assistants per brand**: Each brand (LicensedToHaul, BuildersUSA) gets its own assistant with brand-specific prompts, voice, and tools

2. **Separate phone numbers per brand**: Each brand gets dedicated phone numbers

3. **Dynamic assistant selection**: Use the `assistant-request` webhook to route based on:
   - Inbound: Which number was called → which brand → which assistant
   - Outbound: Campaign specifies which assistant and number to use

### Number-to-Brand Mapping

```python
BRAND_CONFIG = {
    "licensed_to_haul": {
        "assistant_id": "asst_lth_001",
        "phone_number_id": "pn_lth_001",
        "transfer_number": "+15559876543",
    },
    "builders_usa": {
        "assistant_id": "asst_busa_001",
        "phone_number_id": "pn_busa_001",
        "transfer_number": "+15559876544",
    },
}
```

### Dynamic Assistant Per Campaign

For outbound, each call specifies its own assistant config:

```python
async def make_campaign_call(lead, campaign):
    brand = BRAND_CONFIG[campaign.brand]
    await httpx.post("https://api.vapi.ai/call", json={
        "assistantId": brand["assistant_id"],
        "phoneNumberId": brand["phone_number_id"],
        "customer": {"number": lead.phone},
        "assistantOverrides": {
            "variableValues": {
                "customerName": lead.name,
                "brandName": campaign.brand_display_name,
            }
        }
    })
```

### Per-Number Assistant Assignment (Inbound)

```python
@app.post("/vapi/assistant-request")
async def route_inbound(request: Request):
    data = await request.json()
    called_number = data["phoneNumber"]["number"]

    # Map the called number to a brand/assistant
    for brand, config in BRAND_CONFIG.items():
        if config["phone_number"] == called_number:
            return {"assistantId": config["assistant_id"]}

    return {"assistantId": DEFAULT_ASSISTANT_ID}
```

---

## 18. Squads — Multi-Assistant Architecture

Squads enable **multiple specialized assistants** that hand off to each other within a single call. Useful for complex flows where different AI "personas" handle different parts of the conversation.

### When to Use Squads vs Single Assistant

| Use Case | Approach |
|----------|----------|
| Simple qualification + transfer | Single assistant |
| Complex multi-step qualification with different personas | Squad |
| IVR-style routing (language selection, department) | Squad |
| Payment collection requiring PCI compliance | Squad (disable recording during payment assistant) |

### Squad Configuration

```json
{
  "squad": {
    "members": [
      {
        "assistantId": "asst_greeter",
        "assistantOverrides": {},
        "assistantDestinations": [
          { "type": "assistant", "assistantName": "Qualifier" }
        ]
      },
      {
        "assistant": {
          "name": "Qualifier",
          "model": { "provider": "anthropic", "model": "claude-sonnet-4-20250514" },
          "tools": [{ "type": "transferCall", "destinations": [...] }]
        },
        "assistantDestinations": [
          { "type": "assistant", "assistantName": "Greeter" }
        ]
      }
    ],
    "memberOverrides": {}
  }
}
```

### Handoff Tools

```json
{
  "type": "handoff",
  "destinations": [
    {
      "type": "assistant",
      "assistantName": "Payment Specialist",
      "contextEngineeringPlan": {
        "type": "all"
      }
    }
  ]
}
```

**Context transfer types**: `all`, `last-n-messages`, `user-and-assistant-messages-only`, `none`

### Silent Handoffs (Invisible Transfers)

Set destination assistant's `firstMessage` to empty string and `firstMessageMode` to `assistant-speaks-first-with-model-generated-message`. Clear all tool messages. Result: caller perceives one unified interaction.

---

## 19. Outbound Campaigns

Vapi has a built-in campaigns feature via Dashboard:

```
POST /campaign
```

### Campaign Workflow

1. Configure campaign name and phone number
2. Upload recipient CSV (required column: `phone` in E.164 format)
3. Assign assistant (with dynamic variables from CSV columns)
4. Review and execute
5. Monitor via dashboard analytics

### Important Limitations

- Vapi's free numbers are NOT compatible with outbound campaigns
- Requires 10DLC-registered Twilio numbers for compliance
- Concurrency limited by org account limits
- Per-customer assistant overrides require separate API calls

### For OEX

We'll likely manage campaigns at the OEX level (not Vapi campaigns) because we need per-lead customization and our own scheduling logic. Use the `/call` API endpoint directly per lead.

---

## 20. Structured Outputs & Call Analysis

### Structured Outputs

AI-powered data extraction from call transcripts, processed after calls end.

```
POST /structured-output
```

```json
{
  "name": "Insurance Qualification Data",
  "schema": {
    "type": "object",
    "properties": {
      "customerName": { "type": "string" },
      "dotNumber": { "type": "string" },
      "truckCount": { "type": "number" },
      "currentInsurer": { "type": "string" },
      "renewalDate": { "type": "string" },
      "qualified": { "type": "boolean" },
      "qualificationReason": { "type": "string" }
    },
    "required": ["qualified"]
  },
  "type": "ai",
  "model": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-20250514"
  },
  "assistantIds": ["asst_lth_qualifier"]
}
```

### Call Analysis Plan

Built into the assistant's `analysisPlan`:

```json
{
  "analysisPlan": {
    "summaryPrompt": "Summarize this insurance qualification call.",
    "structuredDataPrompt": "Extract qualification data per the JSON Schema.",
    "structuredDataSchema": {
      "type": "object",
      "properties": {
        "dotNumber": { "type": "string" },
        "truckCount": { "type": "number" },
        "qualified": { "type": "boolean" }
      }
    },
    "successEvaluationPrompt": "Did the assistant qualify the lead?",
    "successEvaluationRubric": "PassFail"
  }
}
```

**Rubric options**: `NumericScale` (1-10), `DescriptiveScale`, `Checklist`, `Matrix`, `PercentageScale`, `LikertScale`, `AutomaticRubric`, `PassFail`

**Results available at**:
- `call.analysis.summary`
- `call.analysis.structuredData`
- `call.analysis.successEvaluation`

---

## 21. Observability & Testing

### Analytics API

```
POST /analytics
```

```json
{
  "queries": [{
    "table": "call",
    "name": "daily_call_volume",
    "operations": [{ "operation": "count", "column": "id" }],
    "groupBy": "type",
    "timeRange": {
      "start": "2026-03-18T00:00:00Z",
      "end": "2026-03-25T23:59:59Z",
      "step": "day"
    }
  }]
}
```

### Eval System (Automated Testing)

Create mock conversations to test assistant behavior:

```
POST /eval
```

```json
{
  "type": "chat.mockConversation",
  "name": "Qualification Flow Test",
  "messages": [
    { "role": "user", "content": "Yeah I have 5 trucks" },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "ai",
        "model": { "provider": "openai", "model": "gpt-4o" }
      }
    }
  ]
}
```

### Langfuse Integration

Native observability integration:

```json
{
  "observabilityPlan": {
    "metadata": { "campaign_id": "camp_123", "brand": "LicensedToHaul" },
    "tags": ["outbound", "insurance", "qualification"]
  }
}
```

---

## 22. Security & Compliance

### HIPAA

- Enable: `hipaaEnabled: true` in assistant config
- Effect: No call logs, recordings, or transcriptions stored
- Approved LLM providers: OpenAI, Azure OpenAI, Anthropic, Google, Together AI
- Approved TTS: Vapi, ElevenLabs, Cartesia, Rime AI, Deepgram, Azure
- Approved STT: Azure, Deepgram only

### GDPR

- Personal data processed: emails, names, phone numbers, usage stats
- User rights: access, correction, deletion, restriction, portability
- International transfers via standard contractual clauses
- Details: `security.vapi.ai`

### PCI

- Squad-based architecture for payment collection: disable recording during payment assistant
- Combined HIPAA + PCI: most restrictive rules apply

### TCPA (Outbound Calls)

- Marketing calls require Prior Express Written Consent (PEWC)
- Non-marketing calls require Prior Express Consent (PEC)
- Affirmative opt-in mandatory; pre-checked boxes insufficient

### Static IP Addresses

Webhook requests from Vapi originate from CIDR block: **`167.150.224.0/23`**

SIP signaling IPs: **`44.229.228.186/32`** and **`44.238.177.138/32`**

Enable: `"staticIpAddressesEnabled": true` in server config.

### Data Flow

- **Orchestration layer** (endpointing, interruption, backchanneling): Runs on Vapi infrastructure, NOT customizable, processes audio in real-time without persistence
- **Custom storage**: AWS S3, GCP, Cloudflare R2, Supabase for call artifacts
- **HIPAA mode without custom storage**: Vapi will NOT store recordings or transcripts

---

## 23. Complete API Reference — All Endpoints

### Core Resources

| Method | Endpoint | Description |
|--------|----------|-------------|
| **Assistants** | | |
| POST | `/assistant` | Create assistant |
| GET | `/assistant` | List assistants |
| GET | `/assistant/{id}` | Get assistant |
| PATCH | `/assistant/{id}` | Update assistant |
| DELETE | `/assistant/{id}` | Delete assistant |
| **Calls** | | |
| POST | `/call` | Create call (outbound, web, or WebSocket) |
| GET | `/call` | List calls |
| GET | `/call/{id}` | Get call (includes transcript, recording URL, cost) |
| PATCH | `/call/{id}` | Update call (name only) |
| DELETE | `/call/{id}` | Delete call (supports bulk via `ids[]` body) |
| **Phone Numbers** | | |
| POST | `/phone-number` | Create/import phone number |
| GET | `/phone-number` | List phone numbers |
| GET | `/phone-number/{id}` | Get phone number |
| PATCH | `/phone-number/{id}` | Update phone number |
| DELETE | `/phone-number/{id}` | Delete phone number |
| **Tools** | | |
| POST | `/tool` | Create tool |
| GET | `/tool` | List tools |
| GET | `/tool/{id}` | Get tool |
| PATCH | `/tool/{id}` | Update tool |
| DELETE | `/tool/{id}` | Delete tool |
| POST | `/tool/{id}/mcp-children` | Discover MCP child tools |
| POST | `/tool/code/test` | Test code execution |
| **Files** | | |
| POST | `/file` | Upload file (multipart/form-data) |
| GET | `/file` | List files |
| GET | `/file/{id}` | Get file |
| PATCH | `/file/{id}` | Update file |
| DELETE | `/file/{id}` | Delete file |
| **Squads** | | |
| POST | `/squad` | Create squad |
| GET | `/squad` | List squads |
| GET | `/squad/{id}` | Get squad |
| PATCH | `/squad/{id}` | Update squad |
| DELETE | `/squad/{id}` | Delete squad |
| **Analytics** | | |
| POST | `/analytics` | Query analytics |

### Campaign Resources

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/campaign` | Create campaign |
| GET | `/campaign` | List campaigns (paginated) |
| GET | `/campaign/{id}` | Get campaign |
| PATCH | `/campaign/{id}` | Update campaign |
| DELETE | `/campaign/{id}` | Delete campaign |

### Observability Resources

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/structured-output` | Create structured output |
| GET | `/structured-output` | List structured outputs |
| GET | `/structured-output/{id}` | Get structured output |
| PATCH | `/structured-output/{id}` | Update structured output |
| DELETE | `/structured-output/{id}` | Delete structured output |
| POST | `/structured-output/run` | Run structured output on calls |
| POST | `/eval` | Create eval |
| GET | `/eval` | List evals |
| GET | `/eval/{id}` | Get eval |
| PATCH | `/eval/{id}` | Update eval |
| DELETE | `/eval/{id}` | Delete eval |
| POST | `/eval/run` | Create eval run |
| GET | `/eval/run` | List eval runs |
| GET | `/eval/run/{id}` | Get eval run |
| DELETE | `/eval/run/{id}` | Delete eval run |
| POST | `/observability/scorecard` | Create scorecard |
| GET | `/observability/scorecard` | List scorecards |
| GET | `/observability/scorecard/{id}` | Get scorecard |
| PATCH | `/observability/scorecard/{id}` | Update scorecard |
| DELETE | `/observability/scorecard/{id}` | Delete scorecard |

### Insight / Reporting Resources

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/reporting/insight` | Create insight |
| GET | `/reporting/insight` | List insights |
| GET | `/reporting/insight/{id}` | Get insight |
| PATCH | `/reporting/insight/{id}` | Update insight |
| DELETE | `/reporting/insight/{id}` | Delete insight |
| POST | `/reporting/insight/preview` | Preview insight |
| POST | `/reporting/insight/{id}/run` | Run insight |

### Session Resources (Chat)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/session` | Create session |
| GET | `/session` | List sessions |
| GET | `/session/{id}` | Get session |
| PATCH | `/session/{id}` | Update session |
| DELETE | `/session/{id}` | Delete session |
| POST | `/chat` | Create chat |
| GET | `/chat` | List chats |
| GET | `/chat/{id}` | Get chat |
| DELETE | `/chat/{id}` | Delete chat |
| POST | `/chat/responses` | Create chat (OpenAI compatible) |

### Provider Resources

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/provider/{provider}/{resourceName}` | Create provider resource |
| GET | `/provider/{provider}/{resourceName}` | List provider resources |
| GET | `/provider/{provider}/{resourceName}/{id}` | Get provider resource |
| PATCH | `/provider/{provider}/{resourceName}/{id}` | Update provider resource |
| DELETE | `/provider/{provider}/{resourceName}/{id}` | Delete provider resource |

### Common Query Parameters (List Endpoints)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | number | 100 | Results per page |
| `page` | number | 1 | Page number (paginated endpoints) |
| `sortOrder` | enum | DESC | `ASC` or `DESC` |
| `createdAtGt` | string | — | Filter: created after (ISO 8601) |
| `createdAtLt` | string | — | Filter: created before |
| `createdAtGe` | string | — | Filter: created at or after |
| `createdAtLe` | string | — | Filter: created at or before |
| `updatedAtGt/Lt/Ge/Le` | string | — | Same filters for update time |

### Webhook Events Reference

| Event | Direction | Response Required | Description |
|-------|-----------|-------------------|-------------|
| `assistant-request` | Vapi → Server | Yes (7.5s timeout) | Dynamic assistant selection for inbound |
| `tool-calls` | Vapi → Server | Yes | Tool/function invocation |
| `transfer-destination-request` | Vapi → Server | Yes | Dynamic transfer routing |
| `knowledge-base-request` | Vapi → Server | Yes | Custom KB queries |
| `status-update` | Vapi → Server | No | Call lifecycle changes |
| `end-of-call-report` | Vapi → Server | No | Post-call summary with full data |
| `transcript` | Vapi → Server | No | Real-time transcript |
| `speech-update` | Vapi → Server | No | Voice activity indicators |
| `hang` | Vapi → Server | No | Assistant failed to respond |

---

## 24. Python/REST Code Examples Collection

### 1. Create an Assistant with Our Full Stack Config

```python
import httpx, os

VAPI_API_KEY = os.environ["VAPI_API_KEY"]

async def create_qualifier_assistant():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.vapi.ai/assistant",
            headers={"Authorization": f"Bearer {VAPI_API_KEY}", "Content-Type": "application/json"},
            json={
                "name": "OEX Insurance Qualifier",
                "firstMessage": "Hi {{customerName}}, this is Sarah from LicensedToHaul. I'm calling about commercial auto insurance for your fleet. Do you have a quick moment?",
                "firstMessageMode": "assistant-speaks-first",
                "model": {
                    "provider": "anthropic",
                    "model": "claude-sonnet-4-20250514",
                    "temperature": 0.7,
                    "maxTokens": 300,
                    "messages": [{"role": "system", "content": "You are Sarah, an insurance qualification specialist..."}],
                    "toolIds": []
                },
                "voice": {
                    "provider": "11labs",
                    "voiceId": "21m00Tcm4TlvDq8ikWAM",
                    "model": "eleven_turbo_v2",
                    "stability": 0.5,
                    "similarityBoost": 0.75
                },
                "transcriber": {
                    "provider": "deepgram",
                    "model": "nova-2",
                    "language": "en",
                    "keywords": ["DOT:5", "FMCSA:5"]
                },
                "silenceTimeoutSeconds": 30,
                "maxDurationSeconds": 600,
                "backgroundSound": "office",
                "backchannelingEnabled": true,
                "serverUrl": "https://oex-api.yourdomain.com/vapi/webhook",
                "artifactPlan": {
                    "recordingEnabled": true,
                    "transcriptPlan": {"assistantName": "Sarah", "userName": "Prospect"}
                }
            }
        )
        resp.raise_for_status()
        return resp.json()
```

### 2. Initiate an Outbound Call

```python
async def initiate_call(lead: dict) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.vapi.ai/call",
            headers={"Authorization": f"Bearer {VAPI_API_KEY}", "Content-Type": "application/json"},
            json={
                "assistantId": "asst_abc123",
                "phoneNumberId": "pn_xyz789",
                "customer": {"number": lead["phone"], "name": lead["name"]},
                "assistantOverrides": {
                    "variableValues": {
                        "customerName": lead["name"],
                        "dotNumber": lead["dot_number"],
                        "truckCount": str(lead["truck_count"]),
                    },
                    "model": {
                        "messages": [{"role": "system", "content": f"Context: Calling {lead['name']}, DOT# {lead['dot_number']}, {lead['truck_count']} trucks."}]
                    }
                }
            },
            timeout=30.0,
        )
        resp.raise_for_status()
        return resp.json()
```

### 3. Handle a Webhook (FastAPI)

```python
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/vapi/webhook")
async def vapi_webhook(request: Request):
    if request.headers.get("X-Vapi-Secret") != os.environ["VAPI_WEBHOOK_SECRET"]:
        return Response(status_code=401)

    data = await request.json()
    event_type = data.get("type") or data.get("message", {}).get("type")

    if event_type == "assistant-request":
        return {"assistantId": "asst_abc123"}

    if event_type == "tool-calls":
        results = []
        for tc in data["message"]["toolCallList"]:
            if tc["function"]["name"] == "lookup_carrier":
                carrier = await lookup_carrier(tc["function"]["arguments"]["dot_number"])
                results.append({"toolCallId": tc["id"], "result": format_carrier(carrier)})
        return {"results": results}

    if event_type == "end-of-call-report":
        await process_call_report(data)

    return {"ok": True}
```

### 4. Define and Handle a Server-Side Tool

**Tool definition** (in assistant config):
```json
{
  "type": "function",
  "function": {
    "name": "lookup_carrier",
    "description": "Look up carrier by DOT number",
    "parameters": {
      "type": "object",
      "properties": { "dot_number": { "type": "string" } },
      "required": ["dot_number"]
    }
  },
  "server": { "url": "https://oex-api.yourdomain.com/vapi/tools/lookup-carrier" },
  "messages": [
    { "type": "request-start", "content": "Let me look that up." },
    { "type": "request-failed", "content": "I couldn't find that. Can you repeat the DOT number?" }
  ]
}
```

**Server handler**:
```python
@app.post("/vapi/tools/lookup-carrier")
async def tool_lookup_carrier(request: Request):
    data = await request.json()
    tc = data["message"]["toolCallList"][0]
    dot = tc["function"]["arguments"]["dot_number"]
    carrier = await data_engine_x.get_carrier(dot)
    return {"results": [{"toolCallId": tc["id"], "result": f"Carrier: {carrier['name']}, {carrier['power_units']} trucks, Status: {carrier['status']}"}]}
```

### 5. Trigger a Call Transfer

Transfer is a tool the AI invokes. Define in the assistant:

```json
{
  "type": "transferCall",
  "destinations": [{
    "type": "number",
    "number": "+15559876543",
    "message": "Connecting you with an agent now.",
    "transferMode": "warm-transfer-with-summary"
  }]
}
```

The AI decides when to transfer based on the system prompt instructions.

### 6. Retrieve Call Recording and Transcript

```python
async def get_call_details(call_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"https://api.vapi.ai/call/{call_id}",
            headers={"Authorization": f"Bearer {VAPI_API_KEY}"},
        )
        resp.raise_for_status()
        call = resp.json()
        return {
            "transcript": call.get("artifact", {}).get("transcript"),
            "recording_url": call.get("artifact", {}).get("recordingUrl"),
            "messages": call.get("artifact", {}).get("messages", []),
            "summary": call.get("analysis", {}).get("summary"),
            "structured_data": call.get("analysis", {}).get("structuredData"),
            "success": call.get("analysis", {}).get("successEvaluation"),
            "cost": call.get("costBreakdown", {}).get("total"),
            "duration": call.get("duration"),
            "ended_reason": call.get("endedReason"),
        }
```

### 7. List Recent Calls with Outcomes

```python
async def list_recent_calls(assistant_id: str, limit: int = 50) -> list:
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.vapi.ai/call",
            headers={"Authorization": f"Bearer {VAPI_API_KEY}"},
            params={
                "assistantId": assistant_id,
                "limit": limit,
                "createdAtGt": "2026-03-24T00:00:00Z",
            },
        )
        resp.raise_for_status()
        calls = resp.json()
        return [
            {
                "id": c["id"],
                "status": c["status"],
                "type": c["type"],
                "duration": c.get("duration"),
                "ended_reason": c.get("endedReason"),
                "cost": c.get("costBreakdown", {}).get("total"),
                "customer": c.get("customer", {}).get("number"),
            }
            for c in calls
        ]
```

---

## Appendix: Key Reference Data

### Vapi SIP Static IPs
- **Signaling**: `44.229.228.186/32`, `44.238.177.138/32`
- **Signaling ports**: 5060 (UDP), 5061 (TLS)
- **RTP media**: Dynamic IPs, ports 40000-60000 (UDP)

### Vapi Webhook Static IP CIDR
- `167.150.224.0/23`

### Server Response Deadlines
- `assistant-request`: 7.5 seconds
- `tool-calls`: 20 seconds (configurable via `server.timeoutSeconds`)

### Compliance Certifications
- SOC 2 Type II
- HIPAA (with BAA)
- GDPR
- PCI DSS (via squad architecture)

### Enterprise Features
- Unlimited concurrency
- Reserved capacity on weekly deployment clusters
- Dedicated support + shared Slack channel
- SSO (Okta, Azure AD, SAML, OIDC)
- RBAC
- SLA commitments
- Configurable data retention
