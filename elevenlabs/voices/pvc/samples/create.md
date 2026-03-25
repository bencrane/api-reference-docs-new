# Add samples to PVC voice

**Endpoint:** `POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples`

**Content-Type:** `multipart/form-data`

## Overview

This API endpoint enables users to add audio samples to a PVC voice for voice creation and customization purposes.

## Request Parameters

**Path Parameter:**
- `voice_id` (required, string): The voice identifier that can be obtained from the voices list endpoint

**Header Parameter:**
- `xi-api-key` (optional, string): API authentication key

**Request Body:**
The endpoint accepts multipart form data with:
- `files` (required, array): Audio files for voice creation
- `remove_background_noise` (optional, boolean, default: false): Applies noise removal via audio isolation model, though this may reduce quality if samples lack background noise

## Response

**Success (200):**
Returns an array of `VoiceSample` objects containing:
- `sample_id`, `file_name`, `mime_type`, `size_bytes`, `hash`
- `duration_secs`, `remove_background_noise`, `has_isolated_audio`
- `speaker_separation` data with status and speaker details
- `trim_start`, `trim_end` values

**Validation Error (422):**
Returns HTTP validation error details

## SDK Examples

Implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift languages, demonstrating multipart file upload patterns specific to each platform.
