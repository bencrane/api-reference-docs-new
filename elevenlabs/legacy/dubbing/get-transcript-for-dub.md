# Get Dubbed Transcript

## Endpoint Overview

The ElevenLabs API provides a GET endpoint at `https://api.elevenlabs.io/v1/dubbing/{dubbing_id}/transcript/{language_code}` that "Returns transcript for the dub as an SRT or WEBVTT file."

## Required Parameters

- **dubbing_id** (path): ID of the dubbing project
- **language_code** (path): ISO-693 language code for the transcript, or 'source' for original media

## Optional Parameters

- **format_type** (query): Specifies output format—srt, webvtt, or json. The "json format is not yet supported for Dubbing Studio." Defaults to srt.
- **xi-api-key** (header): API authentication key

## Response Formats

The endpoint returns transcripts in multiple formats:

- **SRT/WEBVTT**: Subtitle format with timing information
- **JSON**: Structured format containing utterances with word-level and character-level timing data

## JSON Response Structure

When using JSON format, responses include:
- Language identifier
- Array of utterances containing speaker ID, text, timing (start_s/end_s)
- Word-level data with type classification
- Character-level granularity for precise timing

## HTTP Status Codes

- **200**: Successful retrieval
- **403**: Authentication required; anonymous users cannot access
- **404**: Dubbing or transcript not found
- **422**: Validation error in request parameters
- **425**: Dubbing project not yet ready for transcript retrieval

## SDK Examples

The documentation provides implementation examples across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating basic usage patterns with standard parameters.
