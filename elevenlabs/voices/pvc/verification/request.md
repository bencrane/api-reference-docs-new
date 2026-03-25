# Request PVC Manual Verification

## Endpoint Overview

The API enables developers to submit verification documents for PVC (Professional Voice Clone) voices through a POST request to `https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/verification`.

## Key Parameters

**Path Parameter:**
- `voice_id` (required): The voice identifier, obtainable via the voices listing endpoint

**Request Body:**
- `files` (required array): Verification documents in binary format
- `extra_text` (optional string): Supplementary information for the verification workflow

**Authentication:**
- `xi-api-key` header (optional)

## Response Structure

A successful request returns a JSON object containing a `status` field. If the request was successful, the status will be "ok" or an error response with status 500.

## Available Server Regions

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

The documentation provides implementation samples across multiple languages (TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift), demonstrating multipart form-data submission with voice identifiers and file attachments.
