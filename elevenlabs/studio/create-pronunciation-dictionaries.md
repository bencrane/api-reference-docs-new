# Create Pronunciation Dictionaries

## Endpoint Overview

The API enables creation of pronunciation dictionaries for a studio project via POST request to `https://api.elevenlabs.io/v1/studio/projects/{project_id}/pronunciation-dictionaries`.

## Key Functionality

According to the documentation, this endpoint will "automatically mark text within this project as requiring reconverting where the new dictionary would apply or the old one no longer does."

## Request Parameters

**Path Parameter:**
- `project_id` (required): Project identifier, obtainable from the List projects endpoint

**Header:**
- `xi-api-key` (optional): Authentication key

**Request Body:**
- `pronunciation_dictionary_locators` (required): Array of dictionary locators containing:
  - `pronunciation_dictionary_id` (required): Dictionary identifier
  - `version_id` (optional): Specific version; defaults to latest if omitted
- `invalidate_affected_text` (optional, default: true): Triggers automatic text reconversion when dictionaries are applied or removed

## Response

Success returns HTTP 200 with response model containing:
- `status`: String indicating "ok" for successful requests; error messages with status 500 indicate failures

## Error Handling

HTTP 422 returns validation errors with detailed error information including location, message, and error type.

## Available Server Endpoints

- Standard: `https://api.elevenlabs.io`
- US Residency: `https://api.us.elevenlabs.io`
- EU Residency: `https://api.eu.residency.elevenlabs.io`
- India Residency: `https://api.in.residency.elevenlabs.io`

## SDK Examples

Code implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call the endpoint with the required parameters.
