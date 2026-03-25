# Outbound Call via Twilio API Documentation

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/twilio/outbound-call` for initiating outbound calls through Twilio integration.

## Required Parameters

The API requires three mandatory fields in the request body:

- **agent_id**: Identifier for the conversational agent
- **agent_phone_number_id**: ID of the phone number from which the call originates
- **to_number**: The recipient's phone number

## Optional Parameters

Additional configuration options include:

- **conversation_initiation_client_data**: Client data for conversation setup, supporting dynamic variables, user identification, and custom LLM configurations
- **call_recording_enabled**: Boolean flag to enable Twilio call recording
- **telephony_call_config**: Configuration for call behavior, including ringing timeout (default: 60 seconds)

## Authentication

The endpoint accepts an optional `xi-api-key` header for authentication purposes.

## Response Structure

A successful response (HTTP 200) returns a JSON object containing:

- **success**: Boolean indicating call initiation success
- **message**: Descriptive response text
- **conversation_id**: Unique identifier for the conversation
- **callSid**: Twilio call session identifier

## SDK Support

The API is accessible through multiple SDK implementations including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with code examples provided for each language.
