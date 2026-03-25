# Delete Dubbing

## API Endpoint

The DELETE endpoint located at `https://api.elevenlabs.io/v1/dubbing/{dubbing_id}` allows developers to remove a dubbing project.

## Request Parameters

The endpoint requires a `dubbing_id` path parameter identifying which project to remove. An optional `xi-api-key` header can be included for authentication.

## Response

A successful deletion returns a response object with a status field. According to the specification, "The status of the dubbing project. If the request was successful, the status will be 'ok'."

## Server Endpoints

The API is accessible through multiple regional servers:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

Code examples are provided for multiple programming languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates the basic syntax for invoking the delete operation with the appropriate client library or HTTP request method.

The page documentation includes complete OpenAPI specifications defining the schema for successful responses and validation error handling.
