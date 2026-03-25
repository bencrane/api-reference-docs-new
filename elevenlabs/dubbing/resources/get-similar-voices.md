# Get Similar Voices

## Overview

This endpoint retrieves the top 10 voices from the ElevenLabs library that match characteristics of a specified speaker in a dubbing project.

**Endpoint:** `GET https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices`

## Purpose

The API call "Fetch the top 10 similar voices to a speaker, including the voice IDs, names, descriptions, and, where possible, a sample audio recording."

## Required Parameters

- **dubbing_id** (path): The identifier for the dubbing project
- **speaker_id** (path): The identifier for the speaker whose similar voices you want to find

## Optional Parameters

- **xi-api-key** (header): API authentication key

## Response Schema

The successful response returns a `SimilarVoicesForSpeakerResponse` object containing:

- **voices**: Array of similar voice objects with:
  - voice_id (string)
  - name (string)
  - category (enum: premade, cloned, generated, professional, famous)
  - description (string, optional)
  - preview_url (string, optional)

## Implementation Examples

Code samples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift across multiple HTTP client libraries.
