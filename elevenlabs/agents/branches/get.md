# Get Agent Branch

**GET** `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}`

Retrieves detailed information about a specific agent branch.

## Parameters

| Parameter | Location | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| agent_id | path | string | Yes | The agent identifier returned upon creation |
| branch_id | path | string | Yes | Unique identifier for the branch |
| xi-api-key | header | string | No | API authentication key |

## Response

**Status 200 - Success**

Returns an `AgentBranchResponse` object containing:
- Branch metadata (id, name, agent_id, description)
- Timestamps (created_at, last_committed_at)
- Archival status
- Protection settings
- Access control information
- Live traffic percentage
- Parent branch details
- Recent version history

**Status 422 - Validation Error**

Returns validation error details when request parameters are invalid.

## Implementation Examples

**TypeScript:**
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.get(
        "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        "agtbranch_0901k4aafjxxfxt93gd841r7tv5t"
    );
}
main();
```

**Python:**
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.conversational_ai.agents.branches.get(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
)
```

Additional code examples available in Go, Ruby, Java, PHP, C#, and Swift formats as shown in the source documentation.
