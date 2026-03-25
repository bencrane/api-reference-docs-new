# Turn-based Audio (Flux) - Speech-to-Text WebSocket
Source: https://developers.deepgram.com/reference/speech-to-text/listen-flux

Real-time conversational speech recognition with contextual turn detection for natural voice conversations

## Handshake

**WSS** `wss://api.deepgram.com/v2/listen`

- **Method:** GET
- **Status:** 101 Switching Protocols

## Headers

### Authorization
- **Type:** string
- **Required**
- Use your API key or a temporary token for authentication via the Authorization header. In client-side environments where custom headers are not supported, use the Sec-WebSocket-Protocol header instead.
- Example: `Authorization: Token %DEEPGRAM_API_KEY%` or `Authorization: Bearer %DEEPGRAM_TOKEN%`

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| model | enum | Required | | Defines the AI model used to process submitted audio. Allowed values: flux-general-en |
| encoding | enum | Optional | | Encoding of the audio stream. Required if sending non-containerized/raw audio. If sending containerized audio, this parameter should be omitted. (6 enum values) |
| sample_rate | any | Optional | | Sample rate of the audio stream in Hz. Required if sending non-containerized/raw audio. If sending containerized audio, this parameter should be omitted. |
| eager_eot_threshold | any | Optional | | End-of-turn confidence required to fire an eager end-of-turn event. When set, enables EagerEndOfTurn and TurnResumed events. Valid Values 0.3 - 0.9. |
| eot_threshold | any | Optional | | End-of-turn confidence required to finish a turn. Valid Values 0.5 - 0.9. |
| eot_timeout_ms | any | Optional | | A turn will be finished when this much time has passed after speech, regardless of EOT confidence. |
| keyterm | string or list of strings | Optional | | Keyterm prompting can improve recognition of specialized terminology. Pass multiple keyterm query parameters to boost multiple keyterms. |
| mip_opt_out | any | Optional | | Opts out requests from the Deepgram Model Improvement Program. Refer to Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip |
| tag | any | Optional | | Label your requests for the purpose of identification during usage reporting |

## Send Messages

### ListenV2Media
- **Type:** string
- **Required**
- **Format:** binary
- Send audio or video data to be transcribed

### ListenV2CloseStream
- **Type:** object
- **Required**
- Send a CloseStream message to close the WebSocket stream

```json
{
  "type": "CloseStream"
}
```

### ListenV2Configure
- **Type:** object
- Send a Configure message to update thresholds and keyterms

```json
{
  "type": "Configure",
  "thresholds": {
    "eager_eot_threshold": 0.5,
    "eot_threshold": 0.5,
    "eot_timeout_ms": 1000
  },
  "keyterms": [
    "weather",
    "forecast"
  ]
}
```

## Receive Messages

### ListenV2Connected
- **Type:** object
- Receive a connected message

```json
{
  "type": "Connected",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "sequence_id": 0
}
```

### ListenV2TurnInfo
- **Type:** object
- Receive a turn info message

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

### ListenV2FatalError
- **Type:** object
- Receive a fatal error message

```json
{
  "type": "Error",
  "sequence_id": 5,
  "code": "INTERNAL_SERVER_ERROR",
  "description": "An internal server error occurred while processing the request"
}
```

### ListenV2ConfigureSuccess
- **Type:** object
- Receive a configure success message

```json
{
  "type": "ConfigureSuccess",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "thresholds": {
    "eager_eot_threshold": 0.5,
    "eot_threshold": 0.5,
    "eot_timeout_ms": 1000
  },
  "keyterms": [
    "weather",
    "forecast"
  ],
  "sequence_id": 0
}
```

### ListenV2ConfigureFailure
- **Type:** object
- Receive a configure failure message

```json
{
  "type": "ConfigureFailure",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "sequence_id": 0
}
```
