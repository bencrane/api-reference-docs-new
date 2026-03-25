# WebSocket Transport Documentation

## Overview

Vapi's WebSocket transport enables real-time, bidirectional audio communication between applications and AI assistants. This approach streams raw audio with minimal latency, distinguishing it from traditional phone or web calls.

## Key Benefits

The documentation highlights several advantages:

- **Low Latency**: Direct streaming minimizes delays
- **Bidirectional Streaming**: Real-time audio flows both ways
- **Easy Integration**: Works with WebSocket-compatible environments
- **Flexible Audio Formats**: Customizable audio parameters including sample rate
- **Automatic Sample Rate Conversion**: Handles various audio rates seamlessly

## Creating a WebSocket Call

### PCM Format (Default)

The default configuration uses 16-bit PCM audio:

```bash
curl 'https://api.vapi.ai/call' \
  -H 'authorization: Bearer YOUR_API_KEY' \
  -H 'content-type: application/json' \
  --data-raw '{
    "assistantId": "YOUR_ASSISTANT_ID",
    "transport": {
      "provider": "vapi.websocket",
      "audioFormat": {
        "format": "pcm_s16le",
        "container": "raw",
        "sampleRate": 16000
      }
    }
  }'
```

### Mu-Law Format

An alternative for bandwidth-constrained scenarios:

```bash
curl 'https://api.vapi.ai/call' \
  -H 'authorization: Bearer YOUR_API_KEY' \
  -H 'content-type: application/json' \
  --data-raw '{
    "assistantId": "YOUR_ASSISTANT_ID",
    "transport": {
      "provider": "vapi.websocket",
      "audioFormat": {
        "format": "mulaw",
        "container": "raw",
        "sampleRate": 8000
      }
    }
  }'
```

### Sample API Response

```json
{
  "id": "7420f27a-30fd-4f49-a995-5549ae7cc00d",
  "assistantId": "5b0a4a08-133c-4146-9315-0984f8c6be80",
  "type": "vapi.websocketCall",
  "createdAt": "2024-09-10T11:14:12.339Z",
  "updatedAt": "2024-09-10T11:14:12.339Z",
  "orgId": "eb166faa-7145-46ef-8044-589b47ae3b56",
  "cost": 0,
  "status": "queued",
  "transport": {
    "provider": "vapi.websocket",
    "websocketCallUrl": "wss://api.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/transport"
  }
}
```

## Audio Format Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `format` | Audio encoding format | `pcm_s16le` (16-bit PCM) |
| `container` | Audio container format | `raw` (Raw audio) |
| `sampleRate` | Sample rate in Hz | 16000 for PCM, 8000 for Mu-Law |

### Supported Formats

- **`pcm_s16le`**: 16-bit PCM, signed little-endian
- **`mulaw`**: Mu-Law encoded audio (ITU-T G.711 standard)

### Selection Guidelines

- **PCM**: Higher quality, increased bandwidth usage—optimal for quality-focused applications
- **Mu-Law**: Lower bandwidth, telephony-standard encoding—suitable for bandwidth constraints

## Connecting to the WebSocket

```javascript
const socket = new WebSocket("wss://api.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/transport");

socket.onopen = () => console.log("WebSocket connection opened.");
socket.onclose = () => console.log("WebSocket connection closed.");
socket.onerror = (error) => console.error("WebSocket error:", error);
```

## Sending and Receiving Data

The WebSocket handles two message types: binary audio data and text-based JSON control messages.

### Sending Audio Data

```javascript
function sendAudioChunk(audioBuffer) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(audioBuffer);
  }
}

navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
  const audioContext = new AudioContext();
  const source = audioContext.createMediaStreamSource(stream);
  const processor = audioContext.createScriptProcessor(1024, 1, 1);

  processor.onaudioprocess = (event) => {
    const pcmData = event.inputBuffer.getChannelData(0);
    const int16Data = new Int16Array(pcmData.length);

    for (let i = 0; i < pcmData.length; i++) {
      int16Data[i] = Math.max(-32768, Math.min(32767, pcmData[i] * 32768));
    }

    sendAudioChunk(int16Data.buffer);
  };

  source.connect(processor);
  processor.connect(audioContext.destination);
});
```

### Receiving Data

```javascript
socket.onmessage = (event) => {
  if (event.data instanceof Blob) {
    event.data.arrayBuffer().then(buffer => {
      const audioData = new Int16Array(buffer);
      playAudio(audioData);
    });
  } else {
    try {
      const message = JSON.parse(event.data);
      handleControlMessage(message);
    } catch (error) {
      console.error("Failed to parse message:", error);
    }
  }
};
```

### Sending Control Messages

```javascript
function sendControlMessage(messageObj) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(messageObj));
  }
}

// Example: hangup call
function hangupCall() {
  sendControlMessage({ type: "hangup" });
}
```

## Ending the Call

Use Live Call Control for better management, or end directly:

```javascript
sendControlMessage({ type: "end-call" });
socket.close();
```

## WebSocket Transport vs. Call Listen Feature

| WebSocket Transport | Call Listen Feature |
|-------------------|-------------------|
| Primary communication method | Secondary, monitoring-only channel |
| Bidirectional audio streaming | Unidirectional (listen-only) |
| Replaces phone/web as transport | Supplements existing calls |
| Uses `provider: "vapi.websocket"` | Accessed via `monitor.listenUrl` |

## Important Constraint

When using WebSocket transport, phone-based parameters (`phoneNumber` or `phoneNumberId`) cannot be used—these approaches are mutually exclusive.
