# Build a Voice Agent
Source: https://developers.deepgram.com/reference/voice-agent/voice-agent

Build a conversational voice agent using Deepgram's Voice Agent WebSocket

## Handshake

**WSS** `wss://agent.deepgram.com/v1/agent/converse`

- **Method:** GET
- **Status:** 101 Switching Protocols

## Headers

### Authorization
- **Type:** string
- **Required**
- Use your API key or a temporary token for authentication via the `Authorization` header. In client-side environments where custom headers are not supported, use the `Sec-WebSocket-Protocol` header instead.
- Example: `Authorization: Token %DEEPGRAM_API_KEY%` or `Authorization: Bearer %DEEPGRAM_TOKEN%`

## Messages

### Send

#### AgentV1Settings (object, Required)
Send settings configuration to Deepgram's Voice Agent API

Example:
```json
{
  "type": "Settings",
  "audio": {
    "input": {
      "encoding": "linear16",
      "sample_rate": 24000
    },
    "output": {
      "encoding": "linear16",
      "sample_rate": 24000,
      "bitrate": 384000,
      "container": "none"
    }
  },
  "agent": {
    "context": {
      "messages": [
        {
          "type": "History",
          "role": "user",
          "content": "What's the weather like?"
        },
        {
          "type": "History",
          "role": "assistant",
          "content": "I can help you check the weather. Where are you located?"
        }
      ]
    },
    "listen": {
      "provider": {
        "type": "deepgram",
        "model": "flux-general-en",
        "version": "v2",
        "keyterms": [
          "weather",
          "forecast"
        ],
        "eot_threshold": 0.8,
        "eager_eot_threshold": 0.5
      }
    },
    "think": {
      "provider": {
        "type": "open_ai",
        "model": "gpt-4o",
        "temperature": 0.7
      },
      "functions": [
        {
          "name": "get_weather",
          "description": "Get current weather for a location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "City name"
              }
            }
          },
          "endpoint": {
            "url": "https://api.example.com/weather",
            "method": "GET",
            "headers": {
              "Authorization": "Bearer token123"
            }
          }
        }
      ],
      "prompt": "You are a helpful weather assistant.",
      "context_length": 4000
    },
    "speak": {
      "provider": {
        "type": "deepgram",
        "model": "aura-2-asteria-en"
      }
    },
    "greeting": "Hello! How can I help you today?",
    "language": "en"
  },
  "tags": [
    "customer-support",
    "production"
  ],
  "experimental": false,
  "flags": {
    "history": true
  },
  "mip_opt_out": false
}
```

Properties: 7

---

#### AgentV1Media (string, Required)
- **Format:** binary
- Send raw binary audio data to Deepgram's Voice Agent API for processing

---

#### AgentV1UpdateSpeak (object, Required)
Send update speak to Deepgram's Voice Agent API

Example:
```json
{
  "type": "UpdateSpeak",
  "speak": {
    "provider": {
      "type": "deepgram",
      "model": "aura-2-luna-en"
    }
  }
}
```

Properties: 2

---

#### AgentV1UpdateThink (object, Required)
Send update think to Deepgram's Voice Agent API

Example:
```json
{
  "type": "UpdateThink",
  "think": {
    "provider": {
      "type": "open_ai",
      "model": "gpt-4o-mini"
    }
  }
}
```

---

#### AgentV1InjectUserMessage (object, Required)
Send inject user message to Deepgram's Voice Agent API

Example:
```json
{
  "type": "InjectUserMessage",
  "content": "What's the capital of France?"
}
```

Properties: 2

---

#### AgentV1InjectAgentMessage (object, Required)
Send inject agent message to Deepgram's Voice Agent API

Example:
```json
{
  "type": "InjectAgentMessage",
  "message": "I'm here to help you with any questions you might have."
}
```

Properties: 2

---

#### AgentV1SendFunctionCallResponse (object, Required)
Send a function call response from the client to the server after executing a client-side function call. This is used when the server requests execution of a function marked with `client_side: true`.

Example:
```json
{
  "type": "FunctionCallResponse",
  "name": "get_weather",
  "content": "{\"temperature\": 72, \"condition\": \"sunny\", \"humidity\": 65}",
  "id": "func_12345"
}
```

Properties: 4

---

#### AgentV1KeepAlive (object, Required)
Send keep alive to Deepgram's Voice Agent API

Example:
```json
{
  "type": "KeepAlive"
}
```

Properties: 1

---

#### AgentV1UpdatePrompt (object, Required)
Send a prompt update to Deepgram's Voice Agent API

Example:
```json
{
  "type": "UpdatePrompt",
  "prompt": "You are now a helpful travel assistant. Help users plan their trips and provide destination information."
}
```

Properties: 2

---

### Receive

#### AgentV1ReceiveFunctionCallResponse (object, Required)
Receive a function call response from the server after the server has executed a server-side function call internally. This occurs when functions are marked with `client_side: false`.

Example:
```json
{
  "type": "FunctionCallResponse",
  "name": "get_weather",
  "content": "{\"temperature\": 72, \"condition\": \"sunny\", \"humidity\": 65}",
  "id": "func_12345",
  "client_side": false
}
```

Properties: 4

---

#### AgentV1PromptUpdated (object, Required)
Receive prompt update from Deepgram's Voice Agent API

Example:
```json
{
  "type": "PromptUpdated"
}
```

Properties: 1

---

#### AgentV1SpeakUpdated (object, Required)
Receive speak update from Deepgram's Voice Agent API

Example:
```json
{
  "type": "SpeakUpdated"
}
```

Properties: 1

---

#### AgentV1InjectionRefused (object, Required)
Receive injection refused message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "InjectionRefused",
  "message": "Cannot inject message while agent is currently speaking"
}
```

Properties: 2

---

#### AgentV1ThinkUpdated (object, Required)
Receive think updated message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "ThinkUpdated"
}
```

---

#### AgentV1Welcome (object, Required)
Receive welcome message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "Welcome",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

Properties: 2

---

#### AgentV1SettingsApplied (object, Required)
Receive settings applied message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "SettingsApplied"
}
```

Properties: 1

---

#### AgentV1ConversationText (object, Required)
Receive conversation text from Deepgram's Voice Agent API

Example:
```json
{
  "type": "ConversationText",
  "role": "user",
  "content": "What's the weather like today?"
}
```

Properties: 3

---

#### AgentV1UserStartedSpeaking (object, Required)
Receive user started speaking message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "UserStartedSpeaking"
}
```

Properties: 1

---

#### AgentV1AgentThinking (object, Required)
Receive agent thinking message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "AgentThinking",
  "content": "Let me check the weather information for your location."
}
```

Properties: 2

---

#### AgentV1FunctionCallRequest (object, Required)
Receive function call request from Deepgram's Voice Agent API

Example:
```json
{
  "type": "FunctionCallRequest",
  "functions": [
    {
      "id": "func_12345",
      "name": "get_weather",
      "arguments": "{\"location\": \"San Francisco\"}",
      "client_side": true
    }
  ]
}
```

Properties: 2

---

#### AgentV1AgentStartedSpeaking (object, Required)
Receive agent started speaking message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "AgentStartedSpeaking",
  "total_latency": 0.85,
  "tts_latency": 0.35,
  "ttt_latency": 0.5
}
```

Properties: 4

---

#### AgentV1AgentAudioDone (object, Required)
Receive agent audio done message from Deepgram's Voice Agent API

Example:
```json
{
  "type": "AgentAudioDone"
}
```

Properties: 1

---

#### AgentV1Error (object, Required)
Receive error response from Deepgram's Voice Agent API

Example:
```json
{
  "type": "Error",
  "description": "Failed to connect to external API",
  "code": "EXTERNAL_API_ERROR"
}
```

Properties: 3

---

#### AgentV1Warning (object, Required)
Receive warning messages from Deepgram's Voice Agent API

Example:
```json
{
  "type": "Warning",
  "description": "Audio quality is degraded due to network conditions",
  "code": "POOR_AUDIO_QUALITY"
}
```

Properties: 3

---

#### AgentV1Audio (string, Required)
- **Format:** binary
- Receive raw binary audio data generated by Deepgram's Voice Agent API
