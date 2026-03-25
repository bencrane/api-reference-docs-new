# Delete Workspace Webhook

## API Endpoint

`DELETE https://api.elevenlabs.io/v1/workspace/webhooks/{webhook_id}`

This endpoint removes a specified workspace webhook from your account.

## Parameters

The request requires:
- **webhook_id** (path parameter): A unique identifier for the webhook to be deleted
- **xi-api-key** (header, optional): Authentication credential

## Response

A successful deletion returns HTTP 200 with a response object containing a `status` field. Per the documentation, "If the request was successful, the status will be 'ok'."

## Implementation Examples

The page provides code samples across multiple languages:

- **TypeScript/JavaScript**: Uses the ElevenLabsClient with `client.webhooks.delete()`
- **Python**: Calls `client.webhooks.delete()` with the webhook_id parameter
- **Go, Ruby, Java, PHP, C#, Swift**: Direct HTTP DELETE requests to the API endpoint

All examples demonstrate deleting the same sample webhook ID: `G007vmtq9uWYl7SUW9zGS8GZZa1K`

## API Servers

The service is available across multiple regional endpoints in the US, EU, and India.
