# Invite User API Documentation

## Endpoint Overview

The "Invite user" endpoint allows workspace members with appropriate permissions to send email invitations to join their workspace.

**Endpoint:** `POST https://api.elevenlabs.io/v1/workspace/invites/add`

## Key Functionality

The API sends an invitation email to a specified address. New recipients are prompted to create an account if needed, while existing users are added directly to the workspace using available subscription seats.

## Required Parameters

- **email** (string, required): The recipient's email address

## Optional Parameters

- **seat_type**: Determines user access level with three options: workspace_admin, workspace_member, or workspace_lite_member
- **workspace_permission**: Deprecated parameter; use seat_type instead
- **group_ids** (array): Assigns user to specific workspace groups

## Authorization

The `xi-api-key` header is optional for authentication purposes.

## Response Format

Successful requests return a status field indicating completion with value 'ok'. Validation errors produce 422 responses with detailed error information.

## Error Conditions

The endpoint returns a 400 error if the recipient already belongs to the workspace. Only workspace members with the WORKSPACE_MEMBERS_INVITE permission can execute this endpoint.

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift implementations.
