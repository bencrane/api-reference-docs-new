# Call Recording, Logging and Transcribing

## Overview

Vapi's artifact plan system enables comprehensive call management through recording, logging, and transcription. The system allows capture and storage of voice conversations for "quality assurance, training, and compliance purposes."

Key capabilities include:
- Audio conversation recording for quality monitoring
- Detailed call logs for debugging and analysis
- Conversation transcripts with speaker identification
- Flexible storage options (Vapi cloud or custom storage)
- Conversation quality and assistant performance monitoring
- Regulatory compliance support

## Primary Use Cases

### Payment Processing Flows

The documentation provides a squad-based architecture example where a middle assistant handles sensitive payment information without artifact generation, while service and confirmation assistants maintain full recording capabilities. This protects "credit card numbers, CVV codes" from being captured.

### Consent Gathering

Enterprise customers access built-in recording consent plans that automatically request permission before transferring to main assistants. The system supports both verbal consent (requiring explicit "yes" confirmation) and implicit consent (assuming agreement if callers remain on the line).

## Configuration Options

### Basic Artifact Plan Setup

Enable artifacts using these properties:
- `recordingEnabled` - Call recording control (default: true)
- `recordingFormat` - Audio format specification (e.g., "wav;l16")
- `loggingEnabled` - Detailed logging activation (default: true)
- `pcapEnabled` - SIP packet capture for phone calls (default: true)
- `transcriptPlan` - Transcript generation with speaker naming

### Storage Configuration

**Default Storage**: Vapi provides encrypted cloud storage with automatic cleanup based on retention policies.

**Custom Storage Options**:
- AWS S3 with path configuration and credentials
- Google Cloud Storage with service account authentication
- Individual control flags for recordings, logs, and PCAP files

## Transcript Features

The transcript system generates "real-time transcription" with speaker identification, timestamp inclusion, and OpenAI formatting compatibility. Speaker names are customizable through `assistantName` and `userName` properties.

Transcripts provide:
- Conversation flow analysis capability
- Response quality evaluation data
- Customer satisfaction metrics
- Assistant performance tracking
- Workflow optimization information

## Squad Transfer Behavior

In multi-assistant squads, recording and logging pause when disabled assistants are active and resume when enabled assistants take over. This supports "privacy-conscious flows" including payment processing and consent collection.

## Privacy and Compliance

The documentation emphasizes that "call recording laws vary by jurisdiction" and requires compliance with:
- Participant notification and consent requirements
- GDPR, CCPA, and similar data protection regulations
- PCI DSS and HIPAA industry standards

Enterprise customers access automated consent management that maintains "audit trails of consent decisions."

## Artifact Access

Artifacts are retrievable through:
- **Dashboard**: Vapi call details interface
- **API**: Programmatic access via call object properties (`recording`, `transcript`, `logUrl`, `pcapUrl`)
- **Custom storage**: Direct access to configured S3/GCP buckets

## FAQ Highlights

Retention periods vary by plan: Pay-as-you-go offers "up to 30 days for chats and 14 days for calls," while Enterprise provides configurable retention policies. Per-call configuration enables granular artifact control for individual conversations.
