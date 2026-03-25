# Download History Items

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/history/download` that enables downloading audio files from your speech synthesis history.

## Core Functionality

The endpoint accepts one or more history item IDs and returns audio files. When a single ID is provided, you receive an individual audio file. When multiple IDs are submitted, the response consists of "a .zip file containing multiple audio files when multiple history items are requested."

## Request Parameters

**Required:**
- `history_item_ids` (array of strings): A collection of history item identifiers. You can retrieve these IDs and metadata through the GET `https://api.elevenlabs.io/v1/history` endpoint.

**Optional:**
- `output_format` (string): Specifies the audio format, accepting either "wav" or "default"
- `xi-api-key` (header): API authentication key

## Response Formats

**Success (200):** Returns binary audio data as `application/octet-stream`

**Errors:**
- 400: Invalid request with error details
- 422: Validation error with field-specific issues

## Available SDKs

Code examples are provided for:
- TypeScript/JavaScript
- Python
- Go
- Ruby
- Java
- PHP
- C#
- Swift

Each demonstrates passing history item IDs to the download function using the respective language's HTTP client libraries.
