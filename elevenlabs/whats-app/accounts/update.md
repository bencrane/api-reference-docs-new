# Update WhatsApp Account

## Endpoint Overview

The API provides a PATCH endpoint to modify WhatsApp account settings:

**PATCH** `https://api.elevenlabs.io/v1/convai/whatsapp-accounts/{phone_number_id}`

## Request Parameters

The endpoint accepts a `phone_number_id` path parameter and supports these optional request body fields:

- `assigned_agent_id` (string): Agent identifier for the account
- `enable_messaging` (boolean): Toggle messaging functionality
- `enable_audio_message_response` (boolean): Toggle audio message responses

An optional `xi-api-key` header can be included for authentication.

## Response

A successful request returns a 200 status code with the updated account details in JSON format. Validation errors return a 422 status.

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Examples

The documentation provides implementation examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call the update method with the phone number ID and request body parameters.
