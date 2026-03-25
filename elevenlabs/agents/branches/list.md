# List Agent Branches

## Overview

The endpoint `GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches` retrieves a list of branches an agent has.

## Key Parameters

- **agent_id** (required, path): The unique identifier returned upon agent creation
- **include_archived** (optional, query): Boolean to include archived branches; defaults to false
- **limit** (optional, query): Maximum results to return; defaults to 100
- **xi-api-key** (optional, header): Authentication header

## Response Structure

The successful 200 response returns a `ListResponseAgentBranchSummary` object containing:

- **meta**: Pagination information (total, page, page_size)
- **results**: Array of `AgentBranchSummary` objects

Each branch summary includes:
- Basic info: id, name, agent_id, description
- Timestamps: created_at, last_committed_at
- Status fields: is_archived, protection_status
- Access info: creator details and user role (admin, editor, commenter, viewer)
- Traffic metrics: current_live_percentage (defaults to 0)
- Draft status: whether a draft exists

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same query with `include_archived=true` and `limit=1` parameters.

## Error Handling

A 422 response indicates validation errors with detailed error information including location, message, and error type.
