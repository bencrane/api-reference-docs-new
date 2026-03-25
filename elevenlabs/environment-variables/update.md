# Update Environment Variable

**Endpoint:** PATCH https://api.elevenlabs.io/v1/convai/environment-variables/{env_var_id}

## Purpose

This API endpoint allows you to modify an environment variable's values. You can "Replace an environment variable's values. Use null to remove an environment (except production)."

## Key Parameters

- **env_var_id** (required, path): The identifier for the environment variable
- **xi-api-key** (optional, header): API authentication key
- **values** (required, body): An object containing the replacement values

## Value Types Supported

The values object accepts three types:
1. **String**: Direct text values
2. **Secret reference**: Object with `secret_id` property
3. **Auth connection reference**: Object with `auth_connection_id` property

## Response Details

A successful (200) response returns an `EnvironmentVariableResponse` containing:
- `label`: Variable name
- `id`: Variable identifier
- `type`: One of string, secret, or auth_connection
- `values`: The updated values object
- `workspace_id`: Associated workspace
- `created_at_unix_secs` and `updated_at_unix_secs`: Timestamps

## Error Responses

- **400**: Invalid parameters or type mismatch
- **404**: Environment variable not found
- **422**: Validation error

## Available SDK Implementations

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to invoke this endpoint across multiple platforms.
