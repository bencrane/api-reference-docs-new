# Troubleshoot Call Errors

## Overview

This guide helps diagnose failed calls by matching caller-reported symptoms to specific error codes. It organizes issues into categories like "Phone never rang," "Call dropped mid-conversation," and "Assistant went silent" to enable quick troubleshooting.

## Key Symptom Categories

The documentation identifies six main failure patterns:

1. **Phone never rang** — Call failed immediately with zero or near-zero duration
2. **Phone rang, no answer** — Line rang but wasn't picked up or was busy
3. **Call dropped mid-conversation** — Connection was lost during active conversation
4. **Assistant went silent** — Connected but assistant stopped responding
5. **Transfer failed** — Transfer attempt didn't complete successfully
6. **Call ended normally** — Expected termination, not an error

## Common Error Classifications

The guide uses two fault types:
- **vapifault** — Issues on Vapi's infrastructure (typically no charge)
- **providerfault** — Issues from telephony providers like Twilio or Vonage

## Notable Error Categories

**Account/Billing issues** include frozen subscriptions, insufficient credits, and concurrency limits.

**Configuration errors** involve missing assistant IDs, invalid phone numbers, or improperly set server URLs.

**Provider errors** cover telephony disconnects, SIP authentication failures, and service unavailability.

**AI/Voice errors** include LLM API key failures, TTS quota exhaustion, and transcriber authentication problems.

## Recommended Actions

The guide emphasizes configuring fallback providers to prevent outages from terminating calls and checking provider status pages during infrastructure issues. It references related resources like voicemail detection settings and SIP trunk troubleshooting guides.
