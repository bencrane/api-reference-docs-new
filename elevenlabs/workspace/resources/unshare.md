# Unshare Workspace Resource

## Overview
The Unshare Workspace Resource endpoint removes access permissions from users, service accounts, groups, or workspace API keys for a specified workspace resource.

## Endpoint Details
- **Method:** POST
- **URL:** `https://api.elevenlabs.io/v1/workspace/resources/{resource_id}/unshare`
- **Content-Type:** application/json

## Key Constraints
According to the documentation, you must have administrative access to the resource to unshare it, and "You cannot remove permissions from the user who created the resource."

## Required Parameters
- **resource_type** (required): The type of resource being unshared (e.g., voice, project, dubbing, etc.)

## Optional Parameters
Choose one of the following to specify the target:
- **user_email:** Email address of the user or service account
- **group_id:** ID of the target group
- **workspace_api_key_id:** ID of the workspace API key

## Supported Resource Types
The API supports 33+ resource types including: voice, voice_collection, pronunciation_dictionary, dubbing, project, convai_agents, convai_knowledge_base_documents, and many others.

## Response
A successful request returns a 200 status code. Validation errors return a 422 status with detailed error information.

## SDK Examples
Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift formats.
