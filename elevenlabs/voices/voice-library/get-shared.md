# List Shared Voices - ElevenLabs API Documentation

## Overview
The ElevenLabs API provides a GET endpoint at `https://api.elevenlabs.io/v1/shared-voices` that "Retrieves a list of shared voices."

## Key Parameters

The endpoint accepts numerous optional query parameters for filtering and pagination:

- **page_size**: Maximum voices to return (default: 30, max: 100)
- **category**: Filter by voice category (professional, famous, high_quality)
- **Demographic filters**: gender, age, accent
- **Localization**: language, locale
- **Search**: search term or descriptives
- **use_cases**: Filter by use case
- **featured**: Boolean to filter featured voices only
- **Moderation & Rates**: min_notice_period_days, include_custom_rates, include_live_moderated
- **Accessibility**: reader_app_enabled
- **Ownership**: owner_id (filter by public owner)
- **Pagination**: page (default: 0), sort criteria

## Response Structure

The successful 200 response returns a `GetLibraryVoicesResponse` object containing:
- **voices**: Array of LibraryVoiceResponse objects with detailed voice metadata
- **has_more**: Boolean indicating additional pages available
- **last_sort_id**: For pagination tracking

Each voice includes properties like voice_id, name, category, usage statistics, pricing, social media handles, and moderation status.

## SDK Support

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
