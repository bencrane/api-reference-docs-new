# Create Workspace Webhook

**Endpoint:** `POST https://api.elevenlabs.io/v1/workspace/webhooks`

## Overview

This API endpoint allows you to "Create a new webhook for the workspace with the specified authentication type."

## Request Parameters

The request requires a JSON body with webhook settings:

- **auth_type**: Must be set to `"hmac"` (the only currently supported authentication method)
- **name**: Display name for the webhook
- **webhook_url**: HTTPS callback URL that receives webhook events

An optional header parameter is available:
- **xi-api-key**: API key for authentication (optional)

## Response

Successful requests return a 200 status with:
- **webhook_id**: Unique identifier for the created webhook
- **webhook_secret**: Secret key for HMAC authentication (required for validating webhook signatures)

Validation errors return a 422 status with detailed error information.

## SDK Examples

The documentation provides implementation examples in:
- **TypeScript/JavaScript** (ElevenLabs SDK)
- **Python** (ElevenLabs SDK)
- **Go** (HTTP standard library)
- **Ruby** (Net::HTTP)
- **Java** (Unirest)
- **PHP** (Guzzle)
- **C#** (RestSharp)
- **Swift** (Foundation URLSession)

All examples demonstrate posting to the endpoint with identical webhook settings: HMAC authentication type, a name, and a webhook URL.

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
