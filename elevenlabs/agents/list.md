# List Agents

GET https://api.elevenlabs.io/v1/convai/agents

This endpoint retrieves a list of your agents and their metadata.

## Key Parameters

The API accepts several query parameters for filtering and pagination:

- **page_size**: Maximum number of agents to return (default: 30, max: 100)
- **search**: Filter agents by name
- **archived**: Filter by archived status (boolean)
- **created_by_user_id**: Filter agents by creator; use '@me' for the authenticated user
- **sort_by**: Sort by "name" or "created_at"
- **sort_direction**: Choose "asc" or "desc"
- **cursor**: For pagination through results

## Response Structure

The successful 200 response returns an object containing:

- **agents**: An array of agent summaries with agent_id, name, tags, creation timestamp, access information, and last call time
- **has_more**: Boolean indicating if additional results exist
- **next_cursor**: Token for retrieving the next page of results

Each agent summary includes access details showing creator information and the user's role (admin, editor, commenter, or viewer).

## Implementation Examples

The page provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift for making requests to this endpoint.
