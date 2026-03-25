# Remove Member from User Group

## Endpoint Overview

The Remove member from user group endpoint allows you to delete a member from a specified group via a POST request to `https://api.elevenlabs.io/v1/workspace/groups/{group_id}/members/remove`. This operation requires the `group_members_manage` permission.

## Request Details

**Method:** POST
**Content-Type:** application/json

### Path Parameters
- `group_id` (required, string): The identifier for the target group

### Headers
- `xi-api-key` (optional, string): API authentication key

### Request Body
The endpoint accepts a JSON object with the following property:
- `email` (required, string): The email address of the workspace member to be removed

## Response Format

**Success Response (HTTP 200):**
The response includes a status field indicating the result. A successful deletion returns `"status": "ok"`.

**Error Response (HTTP 422):**
Validation errors return detailed error information including location, message, and error type.

## Available Implementations

Code examples are provided for multiple programming languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates the proper syntax for calling the removal function with the required group ID and email parameters.
