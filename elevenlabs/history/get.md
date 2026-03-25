# Get History Item

## Overview

This endpoint retrieves a specific history item from the ElevenLabs API using its unique identifier.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/history/{history_item_id}`

## Parameters

### Path Parameter
- **history_item_id** (required, string): The unique identifier for the history item you wish to retrieve

### Header Parameter
- **xi-api-key** (optional, string): API authentication key

## Response

A successful request returns HTTP 200 with a `SpeechHistoryItemResponse` object containing:

- **history_item_id**: Unique identifier for the history item
- **voice_id**: ID of the voice used
- **voice_name**: Name of the voice
- **voice_category**: Type of voice (premade, cloned, generated, or professional)
- **text**: The original text input
- **date_unix**: Creation timestamp
- **model_id**: ID of the model used
- **character_count_change_from/to**: Character count metrics
- **content_type**: Format of the generated content
- **feedback**: User feedback (if provided)
- **source**: Origin of the item (TTS, STS, Projects, Dubbing, etc.)
- **alignments**: Text-to-speech alignment data
- **dialogue**: Array of voice and text pairs
- **output_format**: Audio format specification

## SDK Examples

Multiple language implementations are available including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
