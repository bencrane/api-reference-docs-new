# Add Member to User Group

## Overview

This endpoint enables workspace administrators to add members to user groups via the ElevenLabs API.

**Endpoint:** `POST https://api.elevenlabs.io/v1/workspace/groups/{group_id}/members`

**Required Permission:** `group_members_manage`

## Request Details

### Path Parameter
- **group_id** (required): The identifier for the target group

### Request Body
The request requires JSON with:
- **email** (required, string): The email address of the workspace member to add

### Authentication
Optional header parameter `xi-api-key` for API authentication

## Response Format

**Success (200):**
Returns an object with a status field. Successful requests receive "ok" as the status value.

**Validation Error (422):**
Returns validation error details with location, message, and error type information.

## Implementation Examples

The API documentation provides code samples across multiple languages:
- TypeScript/JavaScript
- Python
- Go
- Ruby
- Java
- PHP
- C#
- Swift

All examples demonstrate adding a member by email to a specified group using the respective language's HTTP client or SDK.

## Available API Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
