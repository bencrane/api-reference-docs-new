# List Dubs API Documentation

## Endpoint Overview
The ElevenLabs "List Dubs" endpoint enables retrieval of dubbing projects accessible to the authenticated user via a GET request to `https://api.elevenlabs.io/v1/dubbing`.

## Key Parameters
The API accepts several optional query parameters:

- **cursor**: Enables pagination by retrieving subsequent pages
- **page_size**: Controls result count (maximum 200, defaults to 100)
- **dubbing_status**: Filters by project state — "dubbing," "dubbed," or "failed"
- **filter_by_creator**: Narrows results to "personal," "others," or "all" (defaults to "all")
- **order_by**: Currently supports "created_at" for sorting
- **order_direction**: Specifies "ASCENDING" or "DESCENDING" ordering (defaults to descending)
- **xi-api-key**: Optional header for API authentication

## Response Structure
Successful requests return a paginated response containing:

- **dubs array**: Collection of dubbing project objects
- **next_cursor**: Token for fetching additional pages
- **has_more**: Boolean indicating whether more results exist

## Dubbing Project Metadata
Each dub object includes properties such as dubbing ID, project name, current status, source language (ISO-639-1 code), target languages, editability status, creation timestamp, media metadata (duration and content type), and error messages for failed projects.

## Available SDK Implementations
Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for developers preferring language-specific integration approaches.
