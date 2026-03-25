# List Similar Voices API Documentation

## Endpoint Overview

The "List similar voices" endpoint is a POST request to `https://api.elevenlabs.io/v1/similar-voices` that accepts multipart form data.

## Purpose

Returns a list of shared voices similar to the provided audio sample. If neither similarity_threshold nor top_k is provided, default values will be applied.

## Request Parameters

The endpoint accepts three form data fields:

1. **audio_file** (binary, required) - The audio sample to analyze
2. **similarity_threshold** (number, optional) - Ranges from 0 to 2; lower values return more similar voices
3. **top_k** (integer, optional) - Number of results to return (1-100); may return fewer if similarity_threshold is set

## Authentication

An optional `xi-api-key` header parameter can be provided in the request.

## Response

The endpoint returns a `GetLibraryVoicesResponse` object containing:
- An array of `LibraryVoiceResponse` objects with detailed voice metadata
- A boolean `has_more` flag indicating pagination availability
- An optional `last_sort_id` field for pagination

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Code Examples

Official SDKs are available for TypeScript, Python, and Go, with additional examples in Ruby, Java, PHP, C#, and Swift.
