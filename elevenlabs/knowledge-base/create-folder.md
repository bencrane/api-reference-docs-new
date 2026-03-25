# Create Folder API Documentation

## Overview

The Create Folder endpoint allows developers to establish organizational structures within the ElevenLabs knowledge base system. This POST operation enables grouping of documents through folder hierarchies.

## Endpoint Details

**URL:** `https://api.elevenlabs.io/v1/convai/knowledge-base/folder`

**Method:** POST

**Content-Type:** application/json

## Request Parameters

The request body accepts the following properties:

- **name** (required, string): "A custom, human-readable name for the document."
- **parent_folder_id** (optional, string): Designates the parent container for placement
- **enable_auto_sync** (optional, boolean): Defaults to false; activates synchronization for URL documents
- **auto_remove** (optional, boolean): Defaults to false; removes documents when URLs become inaccessible (requires auto-sync enabled)

## Response Schema

Success responses (HTTP 200) return an object containing:
- **id** (string): Unique identifier for the created folder
- **name** (string): The folder's designated name
- **folder_path** (array): Hierarchical path segments from root to parent

## Error Handling

Validation errors (HTTP 422) return detailed error information including location, message, and error type.

## Available Server Endpoints

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Support

The documentation provides implementation examples across TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift programming languages.
