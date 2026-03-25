# Share Workspace Resource

## Overview

The Share Workspace Resource endpoint allows you to "grant a role on a workspace resource to a user or a group" by making a POST request to `https://api.elevenlabs.io/v1/workspace/resources/{resource_id}/share`.

## Key Details

**Authentication Requirement:** You must have admin access to the resource to share it.

**Target Options:** You can share resources with:
- Individual users or service accounts (via email)
- Groups (via group ID)
- Workspace API keys (via API key ID)

**Role Override:** The operation will "override any existing role" the target principal has on that resource.

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resource_id` | string | Yes | The ID of the target resource |
| `role` | string | Yes | One of: admin, editor, commenter, viewer |
| `resource_type` | string | Yes | Type of resource being shared |
| `user_email` | string | No | Email of user or service account |
| `group_id` | string | No | Group ID (use 'default' for default permissions) |
| `workspace_api_key_id` | string | No | Workspace API key ID |

## Supported Resource Types

The endpoint supports 34+ resource types including: voice, voice_collection, pronunciation_dictionary, dubbing, project, convai_agents, dashboard, songs, and more.

## Response

A successful request returns HTTP 200 with the response body in JSON format. Validation errors return HTTP 422.
