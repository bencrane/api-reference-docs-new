# Recording Consent Plan Documentation

## Overview

The recording consent plan feature is an enterprise-only capability that automatically creates a consent assistant to request call recording permission before transferring to your main assistant. This ensures compliance with privacy regulations like GDPR and CCPA.

Key capabilities include:
- Automatic consent requests prior to each call
- Two interaction patterns for different use cases
- Regulatory compliance support
- Audit trail maintenance

## Two Consent Types

**Stay-on-Line Consent**: Assumes agreement if the caller remains connected after hearing the disclosure. As the documentation states, users should "clearly state that staying on the line implies consent" and provide "clear instructions to hang up if they don't consent."

**Verbal Consent**: Requires explicit spoken confirmation. The system repeatedly requests clear yes/no responses until the user provides explicit agreement or refuses.

## Configuration Requirements

The consent plan integrates into the assistant's `compliancePlan` object. A stay-on-line setup requires specifying the message, voice parameters, and wait duration. A verbal consent configuration includes the message, voice settings, and a decline tool ID for handling refusals.

## Webhook Data Structure

When calls complete, the end-of-call-report webhook includes a `compliance` section. The `recordingConsent` field shows the consent type used. A `grantedAt` timestamp appears only when users explicitly grant permission; its absence indicates decline or disconnection before approval.

## Implementation Steps

Configuration occurs through the Vapi dashboard (Assistants > Compliance > Recording Consent Plan) or via the TypeScript SDK. Testing verifies both consent and decline flows function correctly. Call logs subsequently reveal whether consent was obtained.

## Best Practices

- Maintain concise, professional messaging
- Select voices that distinguish consent exchanges
- Choose appropriate decline actions (call termination or transfer)
- Thoroughly test all scenarios before deployment
