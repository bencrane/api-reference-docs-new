# Voice Design API Documentation

## Endpoint Overview

The Voice Design API enables creation of voice previews from text descriptions using ElevenLabs' text-to-voice technology.

**Endpoint:** `POST https://api.elevenlabs.io/v1/text-to-voice/create-previews`

## Request Parameters

### Required Fields
- **voice_description** (string): Description defining the voice characteristics to generate

### Optional Fields
- **text** (string): Text for preview generation (100-1000 characters)
- **auto_generate_text** (boolean): Automatically create suitable preview text
- **loudness** (number): Volume control from -1 (quietest) to 1 (loudest)
- **quality** (number): Output fidelity setting (default 0.9)
- **seed** (integer): Controls voice generation reproducibility
- **guidance_scale** (number): Prompt adherence strength (default 5)
- **should_enhance** (boolean): AI-powered prompt expansion
- **output_format** (query): Audio format selection

## Audio Format Options

Supported formats include MP3 variants (22050-44100 Hz), PCM formats (8000-48000 Hz), ULAW/ALAW, and Opus codec options.

## Response Structure

Success responses (HTTP 200) contain:
- **previews** array with generated voice samples
- **audio_base_64**: Encoded audio data
- **generated_voice_id**: Reference identifier for voice creation
- **duration_secs**: Preview length
- **text**: Actual text used for preview generation

## SDK Implementation

The API supports integration across TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift with language-specific client libraries available.
