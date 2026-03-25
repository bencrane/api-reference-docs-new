# Get WhatsApp Account

## Endpoint Overview

This API endpoint retrieves information about a WhatsApp business account using the phone number ID as an identifier.

**Request Method:** GET
**URL:** `https://api.elevenlabs.io/v1/convai/whatsapp-accounts/{phone_number_id}`

## Parameters

The endpoint requires one path parameter:
- **phone_number_id** (string, required): Identifies the specific WhatsApp phone number account

An optional header parameter is available:
- **xi-api-key** (string, optional): API authentication key

## Response Schema

A successful request returns a 200 status with account details including:
- business_account_id
- phone_number_id
- business_account_name
- phone_number_name
- phone_number
- assigned_agent_id (optional)
- enable_messaging (boolean, defaults to true)
- enable_audio_message_response (boolean, defaults to true)
- assigned_agent_name (optional)

Required fields are the account ID, phone number ID, business name, phone number name, and actual phone number.

## Error Handling

The endpoint returns a 422 status for validation errors with details about what failed in the request.

## Implementation Examples

Code samples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift to demonstrate how to call this endpoint across different programming languages and frameworks.
