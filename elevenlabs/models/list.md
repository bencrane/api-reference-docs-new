# List Models API Documentation

## Overview
The ElevenLabs "List models" endpoint is a GET request to `https://api.elevenlabs.io/v1/models` that retrieves "a list of available models."

## Request Details
- **Method:** GET
- **Endpoint:** `/v1/models`
- **Optional Header:** `xi-api-key` (string)

## Response Structure
The API returns a 200 status with an array of Model objects. Each model contains:

- `model_id` (string, required): Unique identifier
- `name` (string): Model name
- `can_be_finetuned` (boolean): Fine-tuning capability
- `can_do_text_to_speech` (boolean): TTS support
- `can_do_voice_conversion` (boolean): Voice conversion capability
- `can_use_style` (boolean): Style parameter support
- `can_use_speaker_boost` (boolean): Speaker boost support
- `serves_pro_voices` (boolean): Pro voice availability
- `token_cost_factor` (number): Cost multiplier
- `description` (string): Model description
- `requires_alpha_access` (boolean): Alpha access requirement
- `max_characters_request_free_user` (integer): Free tier character limit
- `max_characters_request_subscribed_user` (integer): Paid tier character limit
- `maximum_text_length_per_request` (integer): Max text length
- `languages` (array): Supported languages with IDs and names
- `model_rates` (object): Character cost multiplier
- `concurrency_group` (string): Concurrency classification

## Error Response
A 422 status returns validation errors with location, message, and error type details.

## Implementation Examples
The documentation provides code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for implementing this API call.
