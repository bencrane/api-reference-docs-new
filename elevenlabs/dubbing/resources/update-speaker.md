# Update Speaker - ElevenLabs Dubbing API

## Endpoint Overview

The Update Speaker endpoint allows modification of speaker metadata in dubbing projects through a PATCH request to `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}`.

## Core Functionality

According to the documentation, this operation can "amend the metadata associated with a speaker, such as their voice," supporting both voice cloning and library voices.

## Request Parameters

**Path Parameters:**
- `dubbing_id` (required): The dubbing project identifier
- `speaker_id` (required): The speaker identifier

**Header:**
- `xi-api-key` (optional): Authentication key

**Request Body Properties:**
- `speaker_name` (string): Name attribution for the speaker
- `voice_id` (string): Either a voice library identifier or `['track-clone', 'clip-clone']`
- `voice_stability` (number): Range [0.0, 1.0], defaults to 0.65
- `voice_similarity` (number): Range [0.0, 1.0], defaults to 1.0
- `voice_style` (number): Range [0.0, 1.0], defaults to 1.0
- `languages` (array): Target languages; empty array applies changes globally

## Response

**Success (200):** Returns `SpeakerUpdatedResponse` containing a `version` integer property

**Validation Error (422):** Returns `HTTPValidationError` with detailed error information

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the basic update pattern with minimal or empty request bodies.
