# Get Default Voice Settings

The ElevenLabs API provides an endpoint to retrieve default voice configuration parameters.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/voices/settings/default`

**Purpose:** This endpoint retrieves the baseline settings applied to voice synthesis, where "similarity_boost" maps to the "Clarity + Similarity Enhancement" feature and "stability" corresponds to the "Stability" slider found in the web interface.

## Response Schema

The API returns a VoiceSettings object containing:

- **stability** (number): Controls voice consistency and emotional variation. Lower values produce broader emotional range; higher values create more monotonous output.
- **similarity_boost** (number): Regulates how closely the AI replicates the original voice characteristics.
- **use_speaker_boost** (boolean): Enhances speaker similarity but increases computational requirements and latency.
- **style** (number): Amplifies stylistic elements of the original speaker; increases latency when non-zero.
- **speed** (number): Adjusts playback speed where 1.0 is standard, values below 1.0 slow speech, and values above 1.0 accelerate it.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Implementation Examples

SDKs are available for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with each providing straightforward methods to retrieve these default settings without requiring authentication parameters for basic access.
