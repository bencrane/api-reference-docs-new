# Streaming

## Overview

The ElevenLabs API enables real-time audio streaming for select endpoints using chunked transfer encoding. The service returns raw audio bytes (e.g., MP3 data) directly over HTTP, allowing incremental processing.

## Supported Endpoints

Streaming functionality is available for three APIs:
- Text to Speech API
- Voice Changer API
- Audio Isolation API

## Available Libraries

ElevenLabs provides official SDKs in Node.js and Python that include utilities to simplify handling this continuous audio stream.

## Python Implementation

```python
from elevenlabs import stream
from elevenlabs.client import ElevenLabs

elevenlabs = ElevenLabs()

audio_stream = elevenlabs.text_to_speech.stream(
    text="This is a test",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2"
)

# option 1: play the streamed audio locally
stream(audio_stream)

# option 2: process the audio bytes manually
for chunk in audio_stream:
    if isinstance(chunk, bytes):
        print(chunk)
```

## Node.js / TypeScript Implementation

```javascript
import { ElevenLabsClient, stream } from '@elevenlabs/elevenlabs-js';
import { Readable } from 'stream';

const elevenlabs = new ElevenLabsClient();

async function main() {
  const audioStream = await elevenlabs.textToSpeech.stream('JBFqnCBsd6RMkjVDRZzb', {
    text: 'This is a test',
    modelId: 'eleven_v3',
  });

  // option 1: play the streamed audio locally
  await stream(Readable.from(audioStream));

  // option 2: process the audio manually
  for await (const chunk of audioStream) {
    console.log(chunk);
  }
}

main();
```

Both implementations offer two usage patterns: direct playback or manual chunk processing.
