# Create Agent - ElevenLabs API Documentation

## Endpoint Overview

**POST** `https://api.elevenlabs.io/v1/convai/agents/create`

This endpoint allows you to create a conversational AI agent from a configuration object.

## Parameters

### Query Parameters
- **enable_versioning** (boolean, optional): Enable versioning for the agent. Default: `false`

### Header Parameters
- **xi-api-key** (string, optional): API authentication key

## Request Body

The request requires a JSON object with the following structure:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `conversation_config` | ConversationalConfig | Yes | Conversation configuration for an agent |
| `platform_settings` | AgentPlatformSettingsRequestModel | No | Settings not related to conversation orchestration |
| `workflow` | AgentWorkflowRequestModel | No | Flow definition for agent interactions with tools |
| `name` | string | No | Name to identify the agent |
| `tags` | array of strings | No | Tags for classification and filtering |

## Key Configuration Sections

### Conversation Config
Includes ASR (speech recognition), turn detection, TTS (text-to-speech), and conversation event settings.

### Agent Config
- First message content
- Language selection
- Hinglish mode support
- Dynamic variables
- Prompt and LLM configuration

### Prompt Agent Model
- LLM selection (supports GPT, Claude, Gemini, and custom models)
- System prompt definition
- Tool integration
- Knowledge base configuration
- RAG (Retrieval-Augmented Generation) settings

## Response

**Status 200**: Returns a `CreateAgentResponseModel` containing the created agent configuration.

**Status 422**: Returns validation errors for malformed requests.

## Available LLM Models

The system supports numerous language models including:
- GPT family (4, 4o, 4-turbo, 5 variants)
- Claude family (3-series through latest versions)
- Gemini family (1.5 through 3-series)
- Custom LLM integrations
- Open-source alternatives

## Additional Features

- **Tool Support**: API integrations, webhooks, client tools, system tools (end call, transfers, voicemail detection)
- **Audio Configuration**: Multiple input/output formats (PCM 8000-48000, ulaw)
- **Dynamic Variables**: Placeholder system for runtime value injection
- **Language Presets**: Multi-language support with customizable overrides
- **Widget Configuration**: Browser embedding options with extensive customization
