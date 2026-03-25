# Live Call Control

Vapi provides two primary capabilities for managing active calls:

1. **Call Control**: Inject conversation elements dynamically during ongoing calls
2. **Call Listen**: Stream real-time audio data via WebSocket connections

## Obtaining URLs for Call Control and Listen

To retrieve the `listenUrl` and `controlUrl`, send a POST request to the `/call` endpoint.

### Sample Request

```bash
curl 'https://api.vapi.ai/call' \
  -H 'authorization: Bearer YOUR_API_KEY' \
  -H 'content-type: application/json' \
  --data-raw '{
    "assistantId": "5b0a4a08-133c-4146-9315-0984f8c6be80",
    "customer": {
      "number": "+12345678913"
    },
    "phoneNumberId": "42b4b25d-031e-4786-857f-63b346c9580f"
  }'
```

### Sample Response

```json
{
  "id": "7420f27a-30fd-4f49-a995-5549ae7cc00d",
  "assistantId": "5b0a4a08-133c-4146-9315-0984f8c6be80",
  "phoneNumberId": "42b4b25d-031e-4786-857f-63b346c9580f",
  "type": "outboundPhoneCall",
  "createdAt": "2024-09-10T11:14:12.339Z",
  "updatedAt": "2024-09-10T11:14:12.339Z",
  "orgId": "eb166faa-7145-46ef-8044-589b47ae3b56",
  "cost": 0,
  "customer": {
    "number": "+12345678913"
  },
  "status": "queued",
  "phoneCallProvider": "twilio",
  "phoneCallProviderId": "CA4c6793d069ef42f4ccad69a0957451ec",
  "phoneCallTransport": "pstn",
  "monitor": {
    "listenUrl": "wss://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/transport",
    "controlUrl": "https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control"
  }
}
```

## Call Control Features

### 1. Say Message

Direct the assistant to speak a specific message during the call.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "say",
    "content": "Welcome to Vapi, this message was injected during the call.",
    "endCallAfterSpoken": false
  }'
```

### 2. Add Message to Conversation

Insert a message into conversation history with optional response triggering.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "add-message",
    "message": {
      "role": "system",
      "content": "New message added to conversation"
    },
    "triggerResponseEnabled": true
  }'
```

### 3. Assistant Control

Manage assistant behavior during the call.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "control",
    "control": "mute-assistant"
  }'
```

Options: `mute-assistant`, `unmute-assistant`, `say-first-message`

### 4. End Call

Terminate the active call programmatically.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "end-call"
  }'
```

### 5. Transfer Call

Route the call to a different destination by phone number or SIP URI.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "transfer",
    "destination": {
      "type": "number",
      "number": "+1234567890"
    },
    "content": "Transferring your call now"
  }'
```

SIP URI transfer:

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "transfer",
    "destination": {
      "type": "sip",
      "sipUri": "sip:+transferPhoneNumber@sip.telnyx.com"
    },
    "content": "Testing transfer call."
  }'
```

### 6. Handoff Call

Transfer the call to a different assistant.

```bash
curl -X POST 'https://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/control' \
  -H 'content-type: application/json' \
  --data-raw '{
    "type": "handoff",
    "destination": {
      "type": "assistant",
      "contextEngineeringPlan": "none",
      "assistant": {
          "name": "new_assistant",
          "voice": {
              "provider": "vapi",
              "voiceId": "Neha"
          }
      }
    },
    "content": "Handing off your call now"
  }'
```

## Call Listen Feature

The `listenUrl` establishes a WebSocket connection for streaming audio in real-time. Process audio directly or store binary data for later analysis.

### Example: Saving Audio Data from a Live Call

Node.js implementation for capturing and storing audio buffer:

```jsx
const WebSocket = require('ws');
const fs = require('fs');

let pcmBuffer = Buffer.alloc(0);

const ws = new WebSocket("wss://aws-us-west-2-production1-phone-call-websocket.vapi.ai/7420f27a-30fd-4f49-a995-5549ae7cc00d/transport");

ws.on('open', () => console.log('WebSocket connection established'));

ws.on('message', (data, isBinary) => {
  if (isBinary) {
    pcmBuffer = Buffer.concat([pcmBuffer, data]);
    console.log(`Received PCM data, buffer size: ${pcmBuffer.length}`);
  } else {
    console.log('Received message:', JSON.parse(data.toString()));
  }
});

ws.on('close', () => {
  if (pcmBuffer.length > 0) {
    fs.writeFileSync('audio.pcm', pcmBuffer);
    console.log('Audio data saved to audio.pcm');
  }
});

ws.on('error', (error) => console.error('WebSocket error:', error));
```
