# Bulk Move Documents

## Endpoint Overview

The ElevenLabs API provides a bulk move endpoint at `POST https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move` that facilitates "Moves multiple entities from one folder to another."

## Request Structure

The endpoint accepts a JSON payload with two properties:

- **document_ids** (required): An array of strings representing "The ids of documents or folders from the knowledge base."
- **move_to** (optional): A string parameter where "If not set, the entities will be moved to the root folder."

## Response Handling

The API returns a 200 status code for successful operations. Validation errors produce a 422 response containing details about what failed.

## Available Servers

The endpoint is accessible across multiple regional servers:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Implementation Examples

Code samples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates moving two sample document IDs to illustrate the required request format.

## Authentication

An optional `xi-api-key` header parameter can be included for authentication purposes.
