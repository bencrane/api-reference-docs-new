# Update Agent Branch

## Endpoint Overview

The Update Agent Branch endpoint is a PATCH request to `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}` that allows modification of branch properties.

## Key Capabilities

This endpoint enables you to update agent branch properties such as archiving status and protection level.

## Request Parameters

**Path Parameters:**
- `agent_id` (required): The identifier returned upon agent creation
- `branch_id` (required): Unique identifier for the branch

**Header:**
- `xi-api-key` (optional): Authentication key

**Request Body:**
The endpoint accepts a JSON object with these optional properties:
- `name`: New branch name (must be unique within the agent)
- `is_archived`: Boolean for archiving the branch
- `protection_status`: Either "writer_perms_required" or "admin_perms_required"

## Response

A successful 200 response returns an `AgentBranchResponse` object containing:
- Branch metadata (id, name, agent_id, description)
- Timestamps (created_at, last_committed_at)
- Status information (is_archived, protection_status)
- Access control details
- Traffic distribution (current_live_percentage)
- Parent branch information
- Version history

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Support

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift implementations.
