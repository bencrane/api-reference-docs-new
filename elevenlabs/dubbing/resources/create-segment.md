# Create Segment API Documentation

## Overview
This API endpoint enables creation of new segments within a dubbing resource, establishing time boundaries for speakers across all available languages. The operation does not automatically generate transcripts, translations, or audio files.

## Endpoint Details

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/segment`
**Content-Type:** application/json

## Request Parameters

### Path Parameters
- **dubbing_id** (required): Identifier for the dubbing project
- **speaker_id** (required): Identifier for the speaker

### Headers
- **xi-api-key** (optional): Authentication key

### Request Body
```json
{
  "start_time": number,      // Required: decimal format
  "end_time": number,        // Required: decimal format
  "text": string,            // Optional: segment text
  "translations": {          // Optional: language-keyed translations
    "language_code": "string"
  }
}
```

## Response

**Success (201):** Returns segment creation confirmation
```json
{
  "version": integer,
  "new_segment": string
}
```

**Validation Error (422):** Returns validation details with error information

## Available Servers
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples
Code samples provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift demonstrating how to call this endpoint with minimal required parameters (start_time and end_time).
