# Deepgram Keywords and Keyterm Prompting

## Overview

Vapi enables transcription accuracy improvements by leveraging Deepgram's keyword boosting capabilities, particularly beneficial for specialized terminology and uncommon proper nouns.

## Key Benefits

According to the documentation, keyword boosting helps with:

- Recognizing specialized terms and proper nouns more effectively
- Improving transcription quality without custom model training
- Rapidly updating vocabulary with new or uncommon words

## Important Distinctions

The guide emphasizes: "Use single words for `keywords` (no spaces or punctuation). For multi-word phrases, use `keyterm` instead."

Single-word keywords accept optional intensifiers (e.g., `apple:3`), while keyterms are plain strings without intensifiers.

## Model Compatibility

- **Keywords supported:** Deepgram Nova-2, Nova-1, Enhanced, and Base models
- **Nova-3 models:** Use Keyterm Prompting instead

## Implementation Example

To add keyword boosting to an assistant, include the `keywords` and `keyterm` arrays in the transcriber configuration:

```json
"transcriber": {
  "provider": "deepgram",
  "model": "nova-2",
  "keywords": ["snuffleupagus:5", "systrom"],
  "keyterm": ["order number", "PCI compliance"]
}
```

## Best Practices

The documentation recommends: starting small, focusing on uncommon terms, avoiding duplicates, using moderate intensifiers, and considering custom models for extensive vocabularies.
