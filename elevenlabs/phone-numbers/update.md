# Update Phone Number

## Overview
This endpoint allows you to modify the assigned agent and configuration settings for an existing phone number in the ElevenLabs Conversational AI system.

## Endpoint Details
- **Method:** PATCH
- **URL:** `https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}`
- **Content-Type:** application/json

## Parameters

### Path Parameter
- **phone_number_id** (required, string): The identifier of the phone number to update

### Header Parameter
- **xi-api-key** (optional, string): Authentication key for API access

## Request Body

The request accepts a JSON object with these optional fields:

- **agent_id** (string): ID of the agent to assign to this phone number
- **label** (string): A descriptive label for the phone number
- **inbound_trunk_config** (object): Configuration for incoming SIP trunk connections
- **outbound_trunk_config** (object): Configuration for outgoing SIP trunk connections
- **livekit_stack** (string): Type of LiveKit stack ("standard" or "static")

## Response

### Success (200 OK)
Returns a `PhoneNumbersUpdateResponse` object containing:
- Phone number details
- Assigned agent information
- Provider type (Twilio or SIP trunk)
- SIP trunk configurations (if applicable)
- LiveKit stack type

### Error (422)
Returns validation errors for malformed requests

## Code Examples

The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to make PATCH requests with minimal or custom payload configurations.
