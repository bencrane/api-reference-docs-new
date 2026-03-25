# Pronunciation Dictionaries Documentation

## Overview
This documentation explains how to customize AI assistant pronunciation for specific words, names, and technical terms using ElevenLabs voices through Vapi's platform.

## Key Features

**Core Capability**: The feature allows you to "customize how your AI assistant pronounces specific words, names, acronyms, or technical terms."

**Two Rule Types**:
1. **Phoneme Rules** - Use IPA or CMU Arpabet notation for precise control (compatible with `eleven_turbo_v2` and `eleven_flash_v2` models)
2. **Alias Rules** - Replace words with alternative spellings or phrases (work with all ElevenLabs models)

## Implementation Steps

The process involves four stages: creating pronunciation rules, uploading to Vapi via API, configuring your assistant's voice settings, and automatic application during conversations.

**API Endpoint Example**:
```
POST https://api.vapi.ai/provider/11labs/pronunciation-dictionary
```

You provide a JSON payload with rules specifying the text to replace and pronunciation format (phoneme with alphabet choice, or alias).

## Important Requirements

- Exclusive to ElevenLabs voices
- Specific model compatibility for phoneme rules
- Case-sensitive matching for replacements
- Rules applied in order (first match wins)
- SSML parsing automatically enabled when dictionaries are added

## Best Practices

Key recommendations include testing pronunciation changes with your specific voice/model combination, ensuring accurate stress marking for multi-syllable words, and verifying exact case matching between your rules and assistant content.

The documentation also covers managing dictionaries through API endpoints, supporting BYOK (Bring Your Own Key) ElevenLabs accounts, and troubleshooting common issues like incompatible models or SSML conflicts.
