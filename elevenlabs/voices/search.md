# List Voices API Endpoint

## Overview

The ElevenLabs "List voices" endpoint (`GET /v2/voices`) retrieves all available voices for a user with search, filtering and pagination.

## Key Parameters

The endpoint accepts multiple query parameters for filtering and organizing results:

- **Pagination**: `next_page_token` and `page_size` (maximum 100, defaults to 10)
- **Search & Sort**: `search` term, `sort` field (`created_at_unix` or `name`), and `sort_direction`
- **Filtering Options**:
  - `voice_type`: personal, community, default, workspace, non-default, or saved
  - `category`: premade, cloned, generated, or professional
  - `fine_tuning_state`: draft, not_verified, not_started, queued, fine_tuning, fine_tuned, failed, delayed
  - `collection_id`: filter by specific collection

- **Additional Options**: `include_total_count` (boolean), `voice_ids` (up to 100 IDs)

## Response Structure

The successful response returns a `GetVoicesV2Response` object containing:

- **voices**: array of Voice objects with comprehensive metadata
- **has_more**: boolean indicating additional pages exist
- **total_count**: live snapshot of matching voices
- **next_page_token**: token for retrieving subsequent results

## Available Servers

The API is accessible via multiple regional endpoints:
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Support

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
