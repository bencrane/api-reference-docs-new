# List WhatsApp Accounts

This endpoint retrieves all WhatsApp accounts configured in your ElevenLabs workspace.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/convai/whatsapp-accounts`

## Purpose

The endpoint enables you to "List all WhatsApp accounts" associated with your account, providing comprehensive information about each configured WhatsApp integration.

## Response Structure

The API returns a `ListWhatsAppAccountsResponse` containing an array of account objects. Each account includes:

- `business_account_id` (string, required)
- `phone_number_id` (string, required)
- `business_account_name` (string, required)
- `phone_number_name` (string, required)
- `phone_number` (string, required)
- `assigned_agent_id` (string, optional)
- `assigned_agent_name` (string, optional)
- `enable_messaging` (boolean, defaults to true)
- `enable_audio_message_response` (boolean, defaults to true)

## Authentication

The endpoint accepts an optional `xi-api-key` header parameter for authentication.

## Implementation Examples

Code examples are provided across multiple languages including TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The simplest approach uses the official SDK:

**Python:** `client.conversational_ai.whatsapp_accounts.list()`

**TypeScript:** `client.conversationalAi.whatsappAccounts.list()`
