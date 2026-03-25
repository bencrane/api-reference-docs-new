# Continuous Text Stream (Text-to-Speech WebSocket)
Source: https://developers.deepgram.com/reference/text-to-speech/speak-streaming

Convert text into natural-sounding speech using Deepgram's TTS WebSocket

## Handshake

**WSS** `wss://api.deepgram.com/v1/speak`

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
| encoding | enum | Optional | linear16 | Encoding allows you to specify the expected encoding of your audio output for streaming TTS. Only streaming-compatible encodings are supported. Allowed values: linear16, mulaw, alaw |
| mip_opt_out | any | Optional | | Opts out requests from the Deepgram Model Improvement Program. Refer to Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip |
| model | enum | Optional | aura-asteria-en | AI model used to process submitted text (63 enum values) |
| sample_rate | enum | Optional | 24000 | Sample Rate specifies the sample rate for the output audio. Based on encoding 8000 or 24000 are possible defaults. For some encodings sample rate is not configurable. Allowed values: 8000, 16000, 24000, 32000, 48000 |

## Send Messages

### SpeakV1Text
- **Type:** object
- **Required**
- Text to convert to audio

```json
{
  "type": "Speak",
  "text": "Hello, world!"
}
```

### SpeakV1Flush
- **Type:** object
- **Required**
- Flush the buffer and receive the final audio for text sent so far

```json
{
  "type": "Flush"
}
```

### SpeakV1Clear
- **Type:** object
- **Required**
- Clear the buffer and start a new audio generation. Potentially destructive operation for any text in the buffer

```json
{
  "type": "Clear"
}
```

### SpeakV1Close
- **Type:** object
- **Required**
- Flush the buffer and close the connection gracefully after all audio is generated

```json
{
  "type": "Close"
}
```

## Receive Messages

### SpeakV1Audio
- **Type:** string
- **Required**
- **Format:** binary
- Receive audio chunks as they are generated

### SpeakV1Metadata
- **Type:** object
- **Required**
- Receive metadata about the audio generation

```json
{
  "type": "Metadata",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "model_name": "aura-2-asteria-en",
  "model_version": "2024-01-18.29447",
  "model_uuid": "1842b5b2-ef26-4f13-bec5-48eaef70e9c0"
}
```

### SpeakV1Flushed
- **Type:** object
- **Required**
- Receive metadata about the audio generation

```json
{
  "type": "Flushed",
  "sequence_id": 0
}
```

### SpeakV1Cleared
- **Type:** object
- **Required**
- Receive metadata about the audio generation

```json
{
  "type": "Cleared",
  "sequence_id": 0
}
```

### SpeakV1Warning
- **Type:** object
- **Required**
- Receive a warning about the audio generation

```json
{
  "type": "Warning",
  "description": "Text input exceeds recommended length for optimal performance",
  "code": "TEXT_LENGTH_WARNING"
}
```
