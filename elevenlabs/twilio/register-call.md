# Register Call API Documentation

## Endpoint Overview

The Register Call endpoint is a POST request to `https://api.elevenlabs.io/v1/convai/twilio/register-call` that enables Twilio call registration and TwiML response generation.

## Key Parameters

**Required Fields:**
- `agent_id` (string): Identifier for the conversational agent
- `from_number` (string): Originating phone number
- `to_number` (string): Destination phone number

**Optional Fields:**
- `direction`: Call direction (inbound/outbound, defaults to inbound)
- `conversation_initiation_client_data`: Advanced configuration including:
  - Conversation config overrides
  - Agent configuration customization
  - Dynamic variables
  - User identification
  - Source information

## Authentication

An optional `xi-api-key` header can be provided for API authentication.

## Response

The endpoint returns a 200 status on success with TwiML to connect the call. Validation errors return a 422 status with error details.

## Available Implementations

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating consistent implementation patterns across platforms.

## Regional Endpoints

Four server URLs are available for different geographic regions, including standard, US, EU residency, and India residency options.
