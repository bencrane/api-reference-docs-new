# Dub a Video or Audio File

## Overview

The ElevenLabs dubbing API enables conversion of audio or video content into different languages through a POST request to `https://api.elevenlabs.io/v1/dubbing`.

## Key Parameters

**Required:**
- `target_lang` - Target language (ISO 639-1 or ISO 639-3 code)

**File Input Options:**
- `file` - Audio/video file for dubbing
- `source_url` - Alternative URL-based source
- `csv_file` - Transcription/translation metadata (manual mode)

**Audio Processing:**
- `source_lang` - Defaults to "auto" detection
- `num_speakers` - Set to 0 for automatic detection
- `drop_background_audio` - Remove background tracks for speeches
- `use_profanity_filter` - Censor profanities (beta feature)

**Output Options:**
- `target_accent` - Apply specific accent preference (experimental)
- `highest_resolution` - Enable maximum output quality
- `watermark` - Add watermark to video
- `dubbing_studio` - Prepare for studio editing

**Advanced Settings:**
- `mode` - "automatic" (default) or "manual"
- `disable_voice_cloning` - Use Voice Library instead
- `csv_fps` - Frame rate for CSV parsing

## Response

Returns a JSON object containing:
- `dubbing_id` - Project identifier
- `expected_duration_sec` - Estimated processing time

## SDK Support

Code examples provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
