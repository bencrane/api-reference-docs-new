# Delete Invite API Documentation

## Overview

The Delete Invite endpoint allows workspace members with appropriate permissions to invalidate existing email invitations. Once deleted, invitations cannot be activated to join the workspace.

## Endpoint Details

**Method:** DELETE
**URL:** `https://api.elevenlabs.io/v1/workspace/invites`
**Content-Type:** application/json

## Key Information

According to the documentation, this operation "Invalidates an existing email invitation. The invitation will still show up in the inbox it has been delivered to, but activating it to join the workspace won't work."

**Permission Required:** Only workspace members with the `WORKSPACE_MEMBERS_INVITE` permission may call this endpoint.

## Request Parameters

The request body requires a single parameter:

| Parameter | Type | Description |
|-----------|------|-------------|
| email | string | The email address of the customer whose invitation should be deleted |

## Response

**Success (200):** Returns a JSON object with a `status` field. On successful deletion, the status will be 'ok'.

**Validation Error (422):** Returns validation error details.

## Available Server URLs

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for implementing this endpoint across multiple platforms.
