# Create Environment Variable

**Endpoint:** POST https://api.elevenlabs.io/v1/convai/environment-variables

This API enables workspace administrators to establish new environment variables for configuration management within the ElevenLabs platform.

## Request Structure

The endpoint accepts a JSON payload with three supported variable types:

**String Type:** Stores simple text values across different environments, requiring a "production" key within the values object.

**Secret Type:** References encrypted secrets by their secret_id, ideal for sensitive credentials that shouldn't be stored as plain text.

**Auth Connection Type:** Links to authentication connection resources via auth_connection_id for managing API integrations.

All requests require a unique "label" identifier and an environment-specific values mapping.

## Response Format

Upon successful creation, the API returns a comprehensive EnvironmentVariableResponse containing:
- Unique variable identifier
- Workspace association
- Creation and modification timestamps
- User attribution
- Complete values mapping across all configured environments

## Status Codes

- **200:** Variable successfully created
- **400:** Invalid request parameters provided
- **409:** "Environment variable with this label already exists" -- duplicate label detected
- **422:** Request validation failed

## Available Implementations

SDK support includes TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Additionally, raw HTTP requests can be constructed using standard REST conventions with appropriate JSON serialization.
