# Provider Keys

**Subtitle:** Bring your own API keys to Vapi.

## Overview

Users can integrate their own API keys with Vapi for custom models, voices, or enterprise accounts with special pricing. Keys are added through the Dashboard's **Integrations** tab. Once validated, charges bypass Vapi and go directly to the provider.

## Transcription Providers

Deepgram is the supported transcription option. Custom models can be configured by specifying the model ID in the `transcriber.model` parameter when creating an Assistant.

## Model Providers

"We are currently have support for any OpenAI-compatible endpoint" including OpenRouter, AnyScale, Together AI, and self-hosted servers. The `provider` and `model` parameters are specified in the Assistant creation process. Additional guidance is available in the Custom LLMs documentation section.

## Voice Providers

All voice providers are supported. After validating API credentials in the Dashboard, any provider voice ID can be used in the `voice.voiceId` field of the Assistant configuration.

## Cloud Providers

Conversation recordings default to Cloudflare R2 storage. Users can configure their own buckets on AWS S3, GCP, or Cloudflare R2. Detailed setup instructions are provided for each cloud platform option.
