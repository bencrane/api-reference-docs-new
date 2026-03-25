# Update Member API Documentation

## Endpoint Overview

The Update Member endpoint modifies workspace member attributes via a POST request to `https://api.elevenlabs.io/v1/workspace/members`. This operation requires administrator privileges.

## Key Details

**Required Parameter:**
- `email` (string): Identifies the target user account

**Optional Parameters:**
- `is_locked` (boolean): Controls account lock status
- `workspace_seat_type` (enum): Assigns role level -- options include "workspace_admin," "workspace_member," or "workspace_lite_member"
- `workspace_role` (deprecated): Replaced by workspace_seat_type

## Response Format

A successful request returns HTTP 200 with a status field confirming "ok" completion. Validation errors trigger a 422 response with detailed error information.

## Available Implementations

Code examples are provided across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates the basic request structure with minimal required parameters.

## Important Notes

- Only workspace administrators can execute this operation
- Unmodified parameters retain their existing values
- The endpoint supports optional API key authentication via header
