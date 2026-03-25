# Create Podcast API Documentation

## Endpoint Overview

The Create Podcast endpoint allows developers to generate podcast projects through the ElevenLabs API. According to the documentation, this feature will "auto-convert a podcast project" with current cost coverage for LLM processing, though audio generation remains chargeable.

## Required Parameters

Three parameters are mandatory for podcast creation:

1. **model_id** - Specifies the AI model (query `GET /v1/models` for available options)
2. **mode** - Defines podcast type as either "conversation" (two voices) or "bulletin" (single voice)
3. **source** - Content input via text, URL, or array of sources

## Mode Configuration

**Conversation mode** requires:
- `host_voice_id` - The host's voice identifier
- `guest_voice_id` - The guest's voice identifier

**Bulletin mode** requires:
- `host_voice_id` - The narrator's voice identifier

## Optional Parameters

- **quality_preset** - Output formats ranging from "standard" (128kbps) to "ultra_lossless" (705.6kbps)
- **duration_scale** - Options: "short" (<3 min), "default" (3-7 min), "long" (>7 min)
- **language** - ISO 639-1 two-letter code
- **intro/outro** - Text automatically added to podcast boundaries
- **instructions_prompt** - Style and tone adjustments
- **callback_url** - Webhook for conversion status updates
- **apply_text_normalization** - Text processing with "auto," "on," "off," or "apply_english" modes

## Response Format

Successful requests return a `PodcastProjectResponseModel` containing project metadata including ID, creation date, state, and access level information.
