# Live Audio (Streaming Speech-to-Text)
Source: https://developers.deepgram.com/reference/speech-to-text/listen-streaming

Transcribe audio and video using Deepgram's speech-to-text WebSocket

## Handshake

**WSS** `wss://api.deepgram.com/v1/listen`

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
| callback | any | Optional | | URL to which we'll make the callback request |
| callback_method | enum | Optional | POST | HTTP method by which the callback request will be made. Allowed values: POST, GET, PUT, DELETE |
| channels | any | Optional | | The number of channels in the submitted audio |
| detect_entities | enum | Optional | false | Identifies and extracts key entities from content in submitted audio. Entities appear in final results. When enabled, Punctuation will also be enabled by default. Allowed values: true, false |
| diarize | enum | Optional | false | Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0. Allowed values: true, false |
| dictation | enum | Optional | false | Identify and extract key entities from content in submitted audio. Allowed values: true, false |
| encoding | enum | Optional | | Specify the expected encoding of your submitted audio (11 enum values) |
| endpointing | any | Optional | | Indicates how long Deepgram will wait to detect whether a speaker has finished speaking or pauses for a significant period of time. When set to a value, the streaming endpoint immediately finalizes the transcription for the processed time range and returns the transcript with a speech_final parameter set to true. Can also be set to false to disable endpointing |
| extra | any | Optional | | Arbitrary key-value pairs that are attached to the API response for usage in downstream processing |
| interim_results | enum | Optional | false | Specifies whether the streaming endpoint should provide ongoing transcription updates as more audio is received. When set to true, the endpoint sends continuous updates, meaning transcription results may evolve over time. Allowed values: true, false |
| keyterm | any | Optional | | Key term prompting can boost specialized terminology and brands. Only compatible with Nova-3 |
| keywords | any | Optional | | Keywords can boost or suppress specialized terminology and brands |
| language | any | Optional | | The BCP-47 language tag that hints at the primary spoken language. Depending on the Model you choose only certain languages are available |
| mip_opt_out | any | Optional | | Opts out requests from the Deepgram Model Improvement Program. Refer to Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip |
| model | enum | Required | | AI model to use for the transcription (30 enum values) |
| multichannel | enum | Optional | false | Transcribe each audio channel independently. Allowed values: true, false |
| numerals | enum | Optional | false | Convert numbers from written format to numerical format. Allowed values: true, false |
| profanity_filter | enum | Optional | false | Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely. Allowed values: true, false |
| punctuate | enum | Optional | false | Add punctuation and capitalization to the transcript. Allowed values: true, false |
| redact | enum | Optional | false | Redaction removes sensitive information from your transcripts (6 enum values) |
| replace | any | Optional | | Search for terms or phrases in submitted audio and replaces them |
| sample_rate | any | Optional | | Sample rate of submitted audio. Required (and only read) when a value is provided for encoding |
| search | any | Optional | | Search for terms or phrases in submitted audio |
| smart_format | enum | Optional | false | Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability. Allowed values: true, false |
| tag | any | Optional | | Label your requests for the purpose of identification during usage reporting |
| utterance_end_ms | any | Optional | | Indicates how long Deepgram will wait to send an UtteranceEnd message after a word has been transcribed. Use with interim_results |
| vad_events | enum | Optional | false | Indicates that speech has started. You'll begin receiving Speech Started messages upon speech starting. Allowed values: true, false |
| version | any | Optional | | Version of an AI model to use |

## Send Messages

### ListenV1Media
- **Type:** string
- **Required**
- **Format:** binary
- Send audio or video data to be transcribed

### ListenV1Finalize
- **Type:** object
- **Required**
- Send a Finalize message to flush the WebSocket stream

```json
{
  "type": "Finalize"
}
```

### ListenV1CloseStream
- **Type:** object
- **Required**
- Send a CloseStream message to close the WebSocket stream

```json
{
  "type": "CloseStream"
}
```

### ListenV1KeepAlive
- **Type:** object
- **Required**
- Send a KeepAlive message to keep the WebSocket stream alive

```json
{
  "type": "KeepAlive"
}
```

## Receive Messages

### ListenV1Results
- **Type:** object
- Receive transcription results

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
          },
          {
            "word": "are",
            "start": 0.9,
            "end": 1.1,
            "confidence": 0.97,
            "language": "en-US",
            "punctuated_word": "are",
            "speaker": 0
          },
          {
            "word": "you",
            "start": 1.2,
            "end": 1.4,
            "confidence": 0.99,
            "language": "en-US",
            "punctuated_word": "you",
            "speaker": 0
          },
          {
            "word": "doing",
            "start": 1.5,
            "end": 1.9,
            "confidence": 0.98,
            "language": "en-US",
            "punctuated_word": "doing",
            "speaker": 0
          },
          {
            "word": "today",
            "start": 2,
            "end": 2.5,
            "confidence": 0.99,
            "language": "en-US",
            "punctuated_word": "today?",
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

### ListenV1Metadata
- **Type:** object
- Receive metadata about the transcription

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

### ListenV1UtteranceEnd
- **Type:** object
- Receive an utterance end event

```json
{
  "type": "UtteranceEnd",
  "channel": [0],
  "last_word_end": 2.5
}
```

### ListenV1SpeechStarted
- **Type:** object
- Receive a speech started event

```json
{
  "type": "SpeechStarted",
  "channel": [0],
  "timestamp": 0.5
}
```
