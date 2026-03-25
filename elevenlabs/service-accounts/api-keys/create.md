# Create API Key - ElevenLabs Service Accounts

## Endpoint Overview

The API enables creation of new authentication credentials for service accounts via a POST request to `https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys`.

## Request Parameters

**Path Parameter:**
- `service_account_user_id` (required, string): The identifier for the target service account

**Header:**
- `xi-api-key` (optional, string): Authentication token

**Request Body:**
The payload requires two mandatory fields:
- `name` (string): Identifier for the API key
- `permissions` (string or array): Either "all" or an array of specific permission types

Optional field:
- `character_limit` (integer): "The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month"

## Available Permissions

The system supports granular access control including: text_to_speech, speech_to_speech, speech_to_text, models operations, voices operations, speech_history operations, sound_generation, voice_generation, dubbing operations, pronunciation_dictionaries operations, user operations, projects operations, workspace operations, and several specialized features like convai, music_generation, and webhooks_write.

## Response Format

A successful 200 response returns:
```json
{
  "xi-api-key": "string",
  "key_id": "string"
}
```

## Code Examples

SDKs are available for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with consistent method signatures across languages.
