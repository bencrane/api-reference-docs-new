# Get Dubbing

**GET** https://api.elevenlabs.io/v1/dubbing/{dubbing_id}

This endpoint retrieves metadata about a dubbing project, including its current processing status.

## Overview

The API returns comprehensive information about a dubbing project, such as whether processing is still underway or complete.

## Request Details

**Path Parameter:**
- `dubbing_id` (required, string): The identifier for the dubbing project

**Header:**
- `xi-api-key` (optional, string): Authentication key

## Response Structure

A successful request (HTTP 200) returns a `DubbingMetadataResponse` object containing:

- `dubbing_id`: Project identifier
- `name`: Project name
- `status`: Current processing state
- `source_language`: ISO-639-1 code of the original media language (available after completion)
- `target_languages`: Array of ISO-639-1 codes for dubbed languages
- `editable`: Boolean indicating if the project is editable in Dubbing Studio
- `created_at`: Timestamp of project creation
- `media_metadata`: Object with content type and duration in seconds
- `error`: Error message (if processing failed)

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Code Examples

Implementation examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift across multiple SDK versions and native HTTP client approaches.
