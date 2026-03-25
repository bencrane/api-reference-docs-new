# Create Knowledge Base Document from Text

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/knowledge-base/text` that enables users to "Create a knowledge base document containing the provided text."

## Request Parameters

The endpoint accepts a JSON request body with the following fields:

- **text** (required, string): The actual content to be added to the knowledge base
- **name** (optional, string): A descriptive label for the document
- **parent_folder_id** (optional, string): Designates which folder should contain the new document

An optional `xi-api-key` header parameter can be included for authentication.

## Response Schema

A successful request returns HTTP 200 with an object containing:
- **id**: Unique identifier for the created document
- **name**: The document's name
- **folder_path**: Array of folder segments showing the document's location hierarchy

Validation errors return HTTP 422 with detailed error information.

## Server Locations

The API is accessible across multiple regional endpoints, including US, EU residency, and India residency variants.

## Implementation Examples

The documentation provides code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the basic pattern of posting text content to create a knowledge base entry.
