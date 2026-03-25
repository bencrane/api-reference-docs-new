# Delete API Key Documentation

## Endpoint Overview

The ElevenLabs API provides a DELETE endpoint for removing API keys from service accounts:

**DELETE** `https://api.elevenlabs.io/v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}`

This operation allows developers to "Delete an existing API key for a service account."

## Required Parameters

- **service_account_user_id** (path): The identifier for the service account
- **api_key_id** (path): The identifier for the API key to remove
- **xi-api-key** (header): Optional authentication header

## Response

A successful request returns HTTP 200 with the response body in JSON format. Validation errors return HTTP 422 with detailed error information including location, message, and error type.

## Implementation Examples

The documentation provides code samples across multiple languages:

- **TypeScript/JavaScript**: Uses the ElevenLabsClient SDK with `serviceAccounts.apiKeys.delete()`
- **Python**: Employs the ElevenLabs client library with similar method chaining
- **Go, Ruby, Java, PHP, C#, Swift**: Native HTTP library implementations using DELETE requests

All examples demonstrate calling the endpoint with placeholder values for the service account and API key identifiers.

## Regional Endpoints

The service supports multiple regional servers including US, EU, and India residency endpoints.
