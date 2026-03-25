# Introduction

The ElevenLabs API reference provides comprehensive guides, code examples, and endpoint documentation to help developers integrate text-to-speech capabilities.

## Installation

Developers can interact with the API via HTTP or WebSocket requests in any programming language, using official Python or Node.js libraries.

**Python installation:**
```bash
pip install elevenlabs
```

**Node.js installation:**
```bash
npm install @elevenlabs/elevenlabs-js
```

## Tracking Generation Costs

The API returns response headers containing generation metadata, including character cost information.

### Python Example

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your_api_key")

# Get raw response with headers
response = client.text_to_speech.with_raw_response.convert(
    text="Hello, world!",
    voice_id="voice_id"
)

# Access character cost from headers
char_cost = response.headers.get("x-character-count")
request_id = response.headers.get("request-id")
audio_data = response.data
```

### JavaScript Example

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const client = new ElevenLabsClient({ apiKey: 'your_api_key' });

// Get raw response with headers
const { data, rawResponse } = await client.textToSpeech
  .convert('voice_id', {
    text: 'Hello, world!',
    modelId: 'eleven_v3',
  })
  .withRawResponse();

// Access character cost from headers
const charCost = rawResponse.headers.get('x-character-count');
const requestId = rawResponse.headers.get('request-id');
const audioData = data;
```

## Response Contents

Raw responses provide access to response data (the actual API content) and HTTP headers (metadata including character costs and request identifiers).
