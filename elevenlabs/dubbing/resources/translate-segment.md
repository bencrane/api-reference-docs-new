# Translate Segment API Documentation

## Endpoint Overview

The Translate Segment endpoint allows you to regenerate translations for dubbing projects. According to the documentation, it will "automatically transcribe missing transcriptions" but "Will not automatically regenerate the dubs."

**Request Method:** POST
**URL:** `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/translate`

## Required Parameters

- **dubbing_id** (path parameter): The identifier for your dubbing project
- **segments** (body parameter): An array of segment identifiers to translate

## Optional Parameters

- **languages** (body parameter): Specify particular target languages for translation
- **xi-api-key** (header): API authentication key

## Response

Successful requests return a `SegmentTranslationResponse` object containing a `version` integer field.

## Available Implementation Examples

The documentation provides code examples in eight programming languages:

- TypeScript (using ElevenLabsClient SDK)
- Python (using ElevenLabs SDK)
- Go (raw HTTP request)
- Ruby (Net::HTTP)
- Java (Unirest)
- PHP (Guzzle)
- C# (RestSharp)
- Swift (URLSession)

Each example demonstrates how to construct the POST request with the required segments parameter in the JSON body.
