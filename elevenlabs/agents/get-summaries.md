# Get Agent Summaries

**Endpoint:** GET https://api.elevenlabs.io/v1/convai/agents/summaries

This API retrieves summaries for specified conversational AI agents.

## Parameters

- **agent_ids** (query, optional): A string containing a list of agent IDs to fetch summaries for
- **xi-api-key** (header, optional): API authentication key

## Response

A successful 200 response returns an object with agent IDs as keys and summary objects as values. Each summary contains:

- `agent_id`: The agent's unique identifier
- `name`: Agent display name
- `tags`: Array of categorization tags
- `created_at_unix_secs`: Creation timestamp
- `access_info`: Permission details including creator status, name, email, and user role
- `last_call_time_unix_secs`: Most recent call timestamp (null if no calls made)
- `archived`: Boolean indicating archive status

## Error Handling

A 422 response indicates validation errors in the request parameters.

The response uses a discriminator pattern with either success or failure status, where failures include `error_code`, `error_status`, and `error_message` fields.

## Code Examples

Available implementations are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. All examples demonstrate passing agent IDs as parameters to retrieve their summaries.
