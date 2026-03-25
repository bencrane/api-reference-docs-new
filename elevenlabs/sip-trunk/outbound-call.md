# Outbound Call via SIP Trunk

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/sip-trunk/outbound-call` for initiating outbound calls through SIP trunk infrastructure.

## Required Parameters

The API requires three mandatory fields:

- **agent_id**: Identifies the conversational agent handling the call
- **agent_phone_number_id**: Specifies which phone number the agent uses
- **to_number**: The recipient's phone number for the outbound call

## Optional Configuration

Calls can be enhanced with optional parameters:

- **conversation_initiation_client_data**: Allows dynamic variables, user identification, and conversation configuration overrides
- **telephony_call_config**: Controls ringing timeout (defaults to 60 seconds)

## Response Structure

A successful response returns a JSON object containing:

- `success`: Boolean indicating call initiation status
- `message`: Descriptive response text
- `conversation_id`: Unique identifier for the conversation
- `sip_call_id`: SIP protocol-specific call identifier

## Available Servers

The API operates across four regional endpoints:
- Standard US: `https://api.elevenlabs.io`
- US residency: `https://api.us.elevenlabs.io`
- EU residency: `https://api.eu.residency.elevenlabs.io`
- India residency: `https://api.in.residency.elevenlabs.io`

## SDK Support

Implementation examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
