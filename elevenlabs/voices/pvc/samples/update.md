# Update PVC Voice Sample

## Endpoint

POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples/{sample_id}

This endpoint enables modifications to PVC voice samples, including noise reduction, speaker selection, trim adjustments, and file renaming.

## Request Parameters

**Path Parameters:**
- `voice_id` (string, required): The voice identifier; available voices can be retrieved via the voices list endpoint
- `sample_id` (string, required): The sample identifier

**Header:**
- `xi-api-key` (optional): API authentication key

**Request Body (JSON):**
- `remove_background_noise` (boolean, default: false): Applies audio isolation to reduce background noise, though this may degrade quality if minimal noise is present
- `selected_speaker_ids` (array of strings): Speaker identifiers for PVC training; the latest request overrides previous selections
- `trim_start_time` (integer): Audio start point in milliseconds for training
- `trim_end_time` (integer): Audio end point in milliseconds for training
- `file_name` (string): The audio filename for training purposes

## Response

**Success (200):**
Returns `AddVoiceResponseModel` containing the `voice_id` as a string.

**Validation Error (422):**
Returns `HTTPValidationError` with detailed error information.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples

Code implementations are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift languages, demonstrating POST requests with empty or configured request bodies to the specified endpoint.
