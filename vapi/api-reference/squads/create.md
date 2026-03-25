# Create Squad API Reference

## Endpoint

**POST** `https://api.vapi.ai/squad`

Creates a new squad configuration for managing multiple AI assistants.

## Authentication

Required header:
- **Authorization**: API Key (retrieve from [Dashboard](dashboard.vapi.ai))

## Request Body

The request accepts a `CreateSquadDTO` schema containing squad configuration details.

## Response

**Status Code**: 201 Created

Returns a `Squad` object with the created squad configuration.

## Key Schema Components

### Squad Configuration

Squads support complex assistant management including:

- **Transfer Destinations**: Route calls between assistants with customizable messaging and transfer modes
  - `rolling-history`: Maintains full conversation history
  - `swap-system-message-in-history`: Replaces system message on transfer
  - `delete-history`: Clears conversation history
  - `swap-system-message-in-history-and-remove-transfer-tool-messages`: Hybrid approach

- **Handoff Planning**: Manage conversation context when transitioning between assistants using context engineering plans (all messages, last N messages, user/assistant messages only, or none)

- **Transcriber Configuration**: Support for multiple transcription providers including Assembly AI, Azure, Deepgram, ElevenLabs, Gladia, Google, OpenAI, Cartesia, Soniox, and custom implementations

- **Fallback Mechanisms**: Define backup transcribers if primary provider fails

- **Custom Vocabulary**: Enhance recognition accuracy for domain-specific terminology across providers

### Transfer Modes

The API supports four transfer mode strategies for managing conversation context during assistant handoffs, each with distinct implications for history preservation and system message handling.

---

*For complete schema definitions and additional configuration options, refer to the OpenAPI specification documentation.*
