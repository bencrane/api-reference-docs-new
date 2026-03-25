# Search User Group

The ElevenLabs API provides a GET endpoint at `https://api.elevenlabs.io/v1/workspace/groups/search` that allows developers to "Searches for user groups in the workspace. Multiple or no groups may be returned."

## Required Parameters

The endpoint requires one query parameter:
- **name** (string): "Name of the target group."

An optional header parameter `xi-api-key` can be included for authentication.

## Response Format

A successful 200 response returns an array of group objects, each containing:
- **name**: The group's name
- **id**: The group's unique identifier
- **members_emails**: An array of member email addresses

## Available Implementations

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Here's a representative example in Python:

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.workspace.groups.search(name="name")
```

## Error Handling

A 422 response indicates a validation error with details about what failed in the request parameters.

The endpoint supports multiple regional servers across different geographic locations for API requests.
