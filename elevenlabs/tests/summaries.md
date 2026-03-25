# Get Test Summaries

## Overview

The endpoint `POST https://api.elevenlabs.io/v1/convai/agent-testing/summaries` allows you to retrieve multiple agent response test summaries by their IDs. The API "returns a dictionary mapping test IDs to test summaries."

## Request Details

**Content-Type:** application/json

**Required Parameter:**
- `test_ids` (array of strings): List of test identifiers to fetch. No duplicates are permitted.

**Optional Header:**
- `xi-api-key`: API authentication key

## Response Structure

A successful response (HTTP 200) returns a dictionary with a `tests` property containing test summaries mapped by their IDs.

Each test summary includes:
- `id`: Test identifier
- `name`: Test name
- `created_at_unix_secs`: Creation timestamp
- `last_updated_at_unix_secs`: Last modification timestamp
- `type`: Test category (llm, tool, simulation, or folder)
- `entity_type`: Either "test" or "folder"
- `access_info`: Creator details and user role
- `folder_path`: Hierarchical path information
- `children_count`: Number of direct children (for folders)

## Error Handling

A 422 response indicates validation errors in your request payload.

## Available SDK Examples

Code implementations are provided for: TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates passing test identifiers and making the POST request with appropriate headers.
