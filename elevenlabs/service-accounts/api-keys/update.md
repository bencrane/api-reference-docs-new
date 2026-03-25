# Update API Key - ElevenLabs API Documentation

## Endpoint Overview

The Update API Key endpoint modifies an existing API key associated with a service account using a PATCH request to `https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}`.

## Required Parameters

The endpoint requires two path parameters:
- **service_account_user_id**: The identifier for the service account
- **api_key_id**: The identifier for the specific API key being modified

## Request Body

The PATCH request accepts a JSON body with the following fields:

- **is_enabled** (boolean, required): Controls whether the API key is active
- **name** (string, required): A label for identification purposes only
- **permissions** (required): Either an array of specific permission strings or "all" for complete access
- **character_limit** (integer, optional): Enforces a monthly character usage quota; requests fail after exceeding this limit

## Available Permissions

The API supports granular permissions including: "text_to_speech", "speech_to_speech", "speech_to_text", "models_read", "models_write", "voices_read", "voices_write", "speech_history_read", "speech_history_write", "sound_generation", "audio_isolation", "voice_generation", "dubbing_read", "dubbing_write", and many others.

## Response Details

A successful request returns HTTP 200 with response content. Validation errors return HTTP 422 with detailed error information.

## SDK Implementation Examples

Multiple language implementations are provided (TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift) demonstrating how to construct and execute the PATCH request with proper authentication headers and formatted JSON payloads.
