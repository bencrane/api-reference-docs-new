# Get Studio Project API Documentation

## Overview

The Get Studio Project endpoint retrieves detailed information about a specific ElevenLabs Studio project. This endpoint provides more comprehensive data than the general studio list endpoint.

## Endpoint Details

**URL:** `GET https://api.elevenlabs.io/v1/studio/projects/{project_id}`

**Purpose:** "Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`."

## Request Parameters

### Path Parameters
- **project_id** (required): The identifier for the project you want to retrieve. You can discover available projects using the List projects endpoint.

### Query Parameters
- **share_id** (optional): The share identifier of the project

### Headers
- **xi-api-key** (optional): Your API authentication key

## Response

A successful request returns HTTP 200 with a `ProjectExtendedResponse` object containing comprehensive project metadata including:

- Project identifiers and timestamps
- Voice configurations (default title and paragraph voices)
- Chapter information with conversion statistics
- Asset details (videos, audio, images)
- Caption styling preferences
- Quality settings and conversion state
- Publishing data if applicable
- Pronunciation dictionary associations

## Error Handling

The endpoint returns HTTP 422 for validation errors with detailed error information.

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift to facilitate integration across various platforms.
