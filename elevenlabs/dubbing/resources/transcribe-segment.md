# Transcribe Segment API Documentation

## Endpoint Overview

The ElevenLabs Transcribe Segment API allows you to "regenerate the transcriptions for the specified segments" without automatically updating translations or dubs.

**Endpoint:** `POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/transcribe`

## Request Parameters

The API accepts the following in the request path and body:

- **dubbing_id** (path parameter): The identifier for the dubbing project
- **xi-api-key** (header, optional): Authentication key
- **segments** (body, required): An array of segment identifiers to transcribe

## Response

A successful request returns HTTP 200 with a `SegmentTranscriptionResponse` object containing a version number.

## Error Handling

Validation errors return HTTP 422 with detailed error information about malformed requests.

## Available Implementation Examples

The documentation provides code samples for multiple programming languages:

- TypeScript (using ElevenLabs SDK)
- Python (using ElevenLabs client)
- Go (using net/http)
- Ruby (using Net::HTTP)
- Java (using Unirest)
- PHP (using Guzzle)
- C# (using RestSharp)
- Swift (using Foundation URLSession)

## Server Endpoints

Four regional API servers are available:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
