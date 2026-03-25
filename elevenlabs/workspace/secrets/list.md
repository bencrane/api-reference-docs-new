# Get Secrets

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/secrets`

**Purpose:** Retrieve all workspace secrets available to the authenticated user.

## Key Parameters

The API accepts two optional query parameters:

- **page_size** (integer): Controls pagination, with a maximum of 100 results. If omitted, the endpoint returns all secrets.
- **cursor** (string): Enables pagination by fetching subsequent pages using the cursor value provided in previous responses.

An optional `xi-api-key` header can authenticate the request.

## Response Structure

Successful responses return a JSON object containing:
- **secrets**: An array of secret configurations, each with type, secret ID, name, and dependency information
- **next_cursor**: A pagination token for retrieving additional results
- **has_more**: A boolean indicating whether more secrets remain

Each secret object details which tools, agents, phone numbers, and webhooks depend on it.

## SDK Examples

The documentation provides implementation examples across TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript example demonstrates calling `client.conversationalAi.secrets.list()` with pagination parameters, while the Python equivalent uses `client.conversational_ai.secrets.list()`.

HTTP clients can construct requests directly to the endpoint with query parameters, as shown in the Go and cURL implementations provided.
