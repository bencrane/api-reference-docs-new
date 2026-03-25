# Delete Conversation

## API Endpoint

The page documents a DELETE endpoint for removing conversations from the ElevenLabs Conversational AI service:

**DELETE** `https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}`

## Purpose

This endpoint enables users to "Delete a particular conversation" by specifying the conversation ID in the URL path.

## Required Parameters

- **conversation_id** (path parameter): A string identifying the specific conversation to remove
- **xi-api-key** (header): An optional API authentication key

## Response Information

The API returns a 200 status code for successful deletions with a JSON response body. Validation errors produce a 422 response containing details about what failed.

## Available Server Endpoints

The service operates across multiple regional endpoints:
- Standard US: `https://api.elevenlabs.io`
- US residency: `https://api.us.elevenlabs.io`
- EU residency: `https://api.eu.residency.elevenlabs.io`
- India residency: `https://api.in.residency.elevenlabs.io`

## SDK Support

Code examples demonstrate implementation across multiple programming languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with consistent syntax patterns adapted to each language's conventions.
