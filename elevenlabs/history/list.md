# Get Generated Items

The ElevenLabs API provides a GET endpoint at `https://api.elevenlabs.io/v1/history` that "Returns a list of your generated audio."

## Key Parameters

The endpoint accepts optional query parameters for filtering and pagination:

- **page_size**: Maximum items to return (up to 1,000; defaults to 100)
- **start_after_history_item_id**: Cursor for pagination through large collections
- **voice_id**: Filter results by specific voice
- **model_id**: Filter by model identifier
- **date_before_unix** / **date_after_unix**: Unix timestamp-based date filtering
- **sort_direction**: Order results as ascending or descending
- **search**: Text-based filtering capability
- **source**: Filter by generation source (TTS, STS, Projects, Dubbing, etc.)

## Response Structure

The successful 200 response returns a `GetSpeechHistoryResponse` object containing:

- **history**: Array of `SpeechHistoryItemResponse` objects with details like history_item_id, voice information, text content, timestamps, and feedback
- **last_history_item_id**: Identifier for pagination reference
- **has_more**: Boolean indicating additional results exist
- **scanned_until**: Timestamp of the last item scanned

Each history item includes metadata such as character counts, voice category (premade, cloned, generated, professional), content type, and associated feedback when available.

## SDK Support

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for implementing this endpoint across different platforms.
