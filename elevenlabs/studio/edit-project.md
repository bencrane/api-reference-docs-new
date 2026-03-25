# Update Studio Project

**Endpoint:** `POST https://api.elevenlabs.io/v1/studio/projects/{project_id}`

## Overview

This API endpoint allows you to modify an existing Studio project by updating specific parameters. The request requires authentication via API key and expects a JSON payload with the project configuration changes.

## Required Parameters

The request body must include:
- **name** (string): The project identifier name
- **default_title_voice_id** (string): Voice ID for new title audio
- **default_paragraph_voice_id** (string): Voice ID for new paragraph audio

## Optional Parameters

- **title** (string): Author name added as MP3 metadata
- **author** (string): Author attribution for metadata
- **isbn_number** (string): ISBN for audiobook metadata
- **volume_normalization** (boolean): Enable audiobook volume compliance processing

## Response

A successful request returns a 200 status with an `EditProjectResponseModel` containing the complete updated `ProjectResponse` object, including all project properties like state, access level, creation metadata, and caption styling configuration.

## Error Handling

The API returns validation errors (422 status) with detailed error information if required fields are missing or invalid parameters are provided.

## SDK Support

Official client libraries are available for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrated in the documentation with working code examples.
