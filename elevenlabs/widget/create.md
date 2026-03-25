# Create Widget Avatar

**POST** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/avatar`
**Content-Type:** `multipart/form-data`

## Purpose

This endpoint "Sets the avatar for an agent displayed in the widget" according to the API documentation.

## Key Parameters

- **agent_id** (path, required): The agent identifier returned upon creation
- **avatar_file** (form-data, required): A binary image file for the agent's avatar
- **xi-api-key** (header, optional): API authentication key

## Response

Success (HTTP 200) returns an object containing:
- `agent_id`: The agent's identifier
- `avatar_url`: The URL of the uploaded avatar (optional field)

Validation errors (HTTP 422) return detailed error information about request issues.

## Implementation Examples

The documentation provides code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The Python example shows the most straightforward usage:

```python
client.conversational_ai.agents.widget.avatar.create(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    avatar_file="example_avatar_file",
)
```

Lower-level implementations handle multipart form-data encoding manually with appropriate boundary markers and content-type headers.
