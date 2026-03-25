# Merge Agent Branch API Documentation

## Endpoint Overview

The merge agent branch endpoint allows you to consolidate changes from a source branch into a target branch within the ElevenLabs Conversational AI platform.

**HTTP Method:** POST
**URL:** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge`

## Parameters

**Path Parameters:**
- `agent_id` (required): The unique identifier returned upon agent creation
- `source_branch_id` (required): Identifier for the branch being merged from

**Query Parameters:**
- `target_branch_id` (required): The destination branch ID (must be the main branch)

**Headers:**
- `xi-api-key` (optional): Authentication key

## Request Body

The request accepts a JSON object with one optional property:

- `archive_source_branch` (boolean, default: true): Determines whether the source branch should be archived following the merge operation

## Response Codes

- **200:** Successful merge operation
- **422:** Validation error in request parameters

## Code Examples

The documentation provides implementation examples in multiple programming languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call the endpoint with appropriate parameters.

All examples show merging a source branch into a target branch, with the option to archive the source branch automatically.
