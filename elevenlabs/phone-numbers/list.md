# List Phone Numbers

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/phone-numbers`

This API retrieves all phone numbers associated with your ElevenLabs account.

## Key Features

The response returns an array of phone number objects that support two provider types:

1. **Twilio Provider** - Includes basic phone number details with optional agent assignment
2. **SIP Trunk Provider** - Includes advanced SIP configuration for inbound/outbound trunks and LiveKit stack type

## Response Structure

Each phone number object contains:
- `phone_number`: The actual phone number string
- `label`: A descriptive label for the phone number
- `phone_number_id`: Unique identifier for the phone number
- `assigned_agent`: Optional agent information (agent_id and agent_name)
- Provider-specific configuration details

SIP Trunk responses additionally include:
- Outbound trunk configuration (address, transport protocol, media encryption, authentication status)
- Inbound trunk configuration (allowed addresses/numbers, media encryption, authentication)
- LiveKit stack type (standard or static)

## Authentication

The endpoint accepts an optional `xi-api-key` header for authentication.

## SDK Support

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift.

## Error Handling

A 422 response indicates validation errors with detailed error information returned in the response body.
