# List Voices API Documentation

## Endpoint Overview

The **List Voices** endpoint retrieves all available voices for a user via a GET request to `https://api.elevenlabs.io/v1/voices`.

## Key Parameters

The API accepts two optional query parameters:

- **show_legacy** (boolean): When set to true, includes "legacy premade voices in responses"
- **xi-api-key** (header): API authentication key

## Response Structure

The successful 200 response returns a `GetVoicesResponse` object containing an array of voice objects. Each voice includes:

- Basic info: voice_id, name, description
- Audio sample data with processing details
- Category classification (generated, cloned, premade, professional, famous, high_quality)
- Fine-tuning state and verification status
- Voice settings (stability, similarity_boost, style, speed)
- Sharing information and community metrics
- Language verification data
- Safety control settings

## Error Handling

A 422 response indicates validation errors, returning an `HTTPValidationError` with detailed error messages about malformed requests.

## Available SDKs

The API supports implementations in TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with code examples provided for each language demonstrating basic usage with the `show_legacy` parameter.
