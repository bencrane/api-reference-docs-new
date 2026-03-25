# Transcriber Fallback Configuration

## Overview

The documentation explains how to set up backup speech-to-text providers that automatically activate if your primary transcriber fails. As stated, "Your assistant will sequentially fallback to the transcribers you configure, in the exact order you specify."

Key advantages include maintaining call continuity during outages, automatic failover without user action, and protection through provider diversity.

## How Failover Works

When a transcription provider encounters issues, the system detects the failure, switches to the first configured backup, and continues down the list as needed. Calls only terminate if all transcribers in your plan fail.

## Configuration Methods

**Dashboard Setup:** Navigate to your assistant's Transcriber tab, locate the Fallback Transcribers section, and add backups by selecting a provider, model, and language. Additional provider-specific settings are available through an expandable configuration menu.

**API Configuration:** Use the `fallbackPlan` property within your transcriber configuration to specify an array of fallback transcribers with their respective settings.

## Provider-Specific Options

The documentation provides detailed configuration parameters for nine transcriber providers:

- Deepgram (models, keywords, smart formatting, timing thresholds)
- AssemblyAI (speech models, custom vocabulary, confidence settings)
- Azure (language codes, silence timeouts, segmentation strategy)
- Gladia (models, confidence thresholds, prosody detection)
- Speechmatics (operating points, diarization, regional processing)
- Google, OpenAI, ElevenLabs, and Cartesia (with varying model and language options)

## Best Practices & Compliance

Use different providers to guard against widespread outages, ensure language compatibility across all fallbacks, and test transitions thoroughly. For HIPAA or PCI compliance, only Deepgram and Azure are available options.

## Key Takeaways

Failover occurs within milliseconds, involves no additional charges, and supports all major transcription providers without pricing implications.
