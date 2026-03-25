# Get Dubbing Resource

## Endpoint Overview

The GET endpoint retrieves dubbing resource data from a completed dubbing project. As documented, this API call requires "a dubbing ID generated from the '/v1/dubbing' endpoint with studio enabled."

## Request Details

**URL:** `GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}`

**Required Parameters:**
- `dubbing_id` (path): The identifier for the dubbing project

**Optional Parameters:**
- `xi-api-key` (header): API authentication key

## Response Structure

The endpoint returns a `DubbingResource` object containing:

- **Core metadata:** ID, version number, source language, and target languages
- **Media references:** Input file, background audio, and foreground audio
- **Speaker data:** Tracks and segments with associated voice assignments
- **Rendering outputs:** Available render formats (mp4, aac, mp3, wav, aaf, tracks_zip, clips_zip) with their processing status

The response includes detailed segment information with timing data, subtitles, and dubbed audio references for each speaker.

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The implementations consistently follow a straightforward pattern of instantiating the client and calling the resource getter with the dubbing ID parameter.
