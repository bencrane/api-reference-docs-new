# Create Knowledge Base Document from File

## Endpoint Overview

This API endpoint allows you to upload a file to create a knowledge base document for conversational AI agents.

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/convai/knowledge-base/file`
**Content-Type:** multipart/form-data

## Request Parameters

The endpoint accepts the following form data fields:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| file | binary | Yes | "Documentation that the agent will have access to in order to interact with users" |
| name | string | No | A custom, human-readable identifier for the document |
| parent_folder_id | string | No | "If set, the created document or folder will be placed inside the given folder" |

## Response Schema

A successful request (HTTP 200) returns an object containing:

- **id** (string, required): The document's unique identifier
- **name** (string, required): The document's name
- **folder_path** (array, optional): Folder hierarchy segments from root to parent

## Error Handling

Validation errors (HTTP 422) return details about what went wrong with the request.

## SDK Examples

The documentation provides code samples for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift languages to implement this functionality across multiple development environments.
