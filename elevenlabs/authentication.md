# API Authentication

The ElevenLabs API employs API key-based authentication to secure all requests. Each API key must be included in the `xi-api-key` HTTP header for every API call.

## Key Features

API keys can be configured with two types of restrictions:

1. **Scope restriction** - Limit which endpoints the key can access
2. **Credit quota** - Set custom usage limits

## Security Considerations

The documentation emphasizes that "your API key is a secret" and should never be shared or embedded in client-side code.

## Implementation Methods

**cURL request example:**
```bash
curl 'https://api.elevenlabs.io/v1/models' \
  -H 'Content-Type: application/json' \
  -H 'xi-api-key: $ELEVENLABS_API_KEY'
```

**Python implementation** uses the ElevenLabs client library with the API key passed during initialization.

**JavaScript/Node.js implementation** similarly passes the API key when creating a new ElevenLabsClient instance.

## Alternative Authentication

For specific use cases (particularly client-side applications), the API supports single-use tokens as an alternative to API keys, allowing developers to authenticate without exposing their primary credentials.
