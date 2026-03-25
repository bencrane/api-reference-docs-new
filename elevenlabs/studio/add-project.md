# Create Studio Project API Documentation Summary

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/studio/projects` that "Creates a new Studio project, it can be either initialized as blank, from a document or from a URL."

## Key Request Parameters

**Required:**
- `name` (string): Project identification name

**Content Initialization Options** (mutually exclusive):
- `from_url`: Extract content from a URL
- `from_document`: Upload a file (.epub, .pdf, .txt, etc.)
- `from_content_json`: Provide structured content as JSON
- If none provided, project initializes as blank

**Audio & Voice Configuration:**
- `default_title_voice_id`: Voice for new titles
- `default_paragraph_voice_id`: Voice for new paragraphs
- `default_model_id`: Model selection via GET /v1/models
- `quality_preset`: standard, high, ultra, or ultra_lossless

**Metadata Fields:**
- `title`, `author`, `description`
- `genres` (array), `language` (ISO 639-1 code)
- `isbn_number`, `content_type`
- `target_audience`: children, young adult, adult, or all ages
- `original_publication_date` (YYYY-MM-DD or YYYY format)
- `mature_content` (boolean)
- `fiction`: fiction or non-fiction

**Processing Options:**
- `volume_normalization`: Apply audiobook compliance postprocessing
- `apply_text_normalization`: auto, on, off, or apply_english
- `auto_convert`: Enable automatic audio conversion
- `auto_assign_voices`: Alpha feature for voice assignment
- `pronunciation_dictionary_locators`: JSON-encoded dictionary settings

**Advanced Settings:**
- `callback_url`: Webhook for conversion status updates
- `source_type`: blank, book, article, genfm, video, or screenplay
- `voice_settings`: Override stability, similarity, style parameters
- `create_publishing_read`: Creates draft publishing read

## Response

Returns an `AddProjectResponseModel` containing a `ProjectResponse` object with project_id and configuration details.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
