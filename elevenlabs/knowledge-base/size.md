# Get Knowledge Base Size

This ElevenLabs API endpoint retrieves the number of pages stored in an agent's knowledge base.

## Endpoint Details

**Method:** GET
**URL:** `https://api.elevenlabs.io/v1/convai/agent/{agent_id}/knowledge-base/size`

## Parameters

- **agent_id** (path, required): The unique identifier for the agent
- **xi-api-key** (header, optional): API authentication key

## Response

The endpoint returns a JSON object containing:
- **number_of_pages** (number): The count of pages in the knowledge base

## Status Codes

- **200**: Successful request, returns page count
- **422**: Validation error in request parameters

## Code Examples

The documentation provides implementation samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. For instance, the TypeScript SDK usage is: `client.conversationalAi.agents.knowledgeBase.size("agent_id")`, while Python uses: `client.conversational_ai.agents.knowledge_base.size(agent_id="agent_id")`.

The raw HTTP examples demonstrate straightforward GET requests without request bodies, with responses containing the JSON schema defining the knowledge base size structure.
