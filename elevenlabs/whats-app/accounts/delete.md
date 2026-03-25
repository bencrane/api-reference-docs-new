# Delete WhatsApp Account

## Overview
This endpoint allows you to remove a WhatsApp account from the ElevenLabs conversational AI system using a DELETE request to `https://api.elevenlabs.io/v1/convai/whatsapp-accounts/{phone_number_id}`.

## API Details

**Required Parameter:**
- `phone_number_id` (path): The identifier for the WhatsApp account to delete

**Optional Parameter:**
- `xi-api-key` (header): Authentication key for the request

**Response Codes:**
- 200: Successful deletion
- 422: Validation error in request parameters

## Implementation Examples

The documentation provides code samples across multiple languages:

- **TypeScript/JavaScript**: Uses the ElevenLabsClient SDK with the syntax `client.conversationalAi.whatsappAccounts.delete()`
- **Python**: Employs the ElevenLabs client library calling `client.conversational_ai.whatsapp_accounts.delete()`
- **Go, Ruby, Java, PHP, C#, and Swift**: Raw HTTP implementations using respective language libraries

Each example demonstrates sending a DELETE request to the endpoint with the phone number ID parameter substituted in the URL path.

## Available Servers
The API is accessible across multiple regional endpoints including US, EU, and Indian residency options.
