# Create Deployment

## Endpoint
POST https://api.elevenlabs.io/v1/convai/agents/{agent_id}/deployments

## Purpose
This endpoint enables users to create a new deployment for an agent by specifying which branches should receive traffic and their respective percentages.

## Key Parameters

**Path Parameter:**
- `agent_id` (required): The identifier returned when an agent is created

**Request Body:**
The deployment request requires a `requests` array containing deployment items, each with:
- `branch_id`: The branch identifier to deploy
- `deployment_strategy`: Contains `traffic_percentage` (0-1 range) and `type: "percentage"`

## Response
The API returns an `AgentDeploymentResponse` containing a `traffic_percentage_branch_id_map` that shows the distribution of traffic across deployed branches.

## Code Examples
The documentation provides implementations in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. A representative example shows deploying a single branch with 50% traffic allocation to an agent.

## Server Locations
The API is available across multiple regional endpoints including US, EU, and India residency options.
