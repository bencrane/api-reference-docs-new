# Server Message Webhook API Reference

## Endpoint

**POST** `https://{yourserver}.com/server`

**Content-Type:** `application/json`

## Overview

The Server Message webhook allows your backend to receive and respond to various events from Vapi during call handling. Most messages are informational, but three types require responses: `assistant-request`, `tool-calls`, and `transfer-destination-request`.

## Request Schema

### ServerMessage

The incoming webhook payload uses the `ServerMessage` schema, which can be one of several message types:

- **assistant-request**: Sent to fetch assistant configuration for incoming calls
- **tool-calls**: Triggered when the assistant needs to execute tool functions
- **transfer-destination-request**: Used to determine transfer destinations
- **custom-message**: User-defined message types
- Call status updates and other event notifications

### ServerMessageAssistantRequest

For incoming calls without a pre-assigned assistant, a request is sent with:

```json
{
  "type": "assistant-request",
  "phoneNumber": {
    "provider": "twilio|vapi|vonage|telnyx|byo-phone-number",
    "number": "+14155551234",
    "assistantId": "optional-id",
    "squadId": "optional-id",
    "workflowId": "optional-id"
  }
}
```

## Response Schema

### ServerMessageResponse

The expected response depends on the message type:

**For assistant-request:**
```json
{
  "assistant": {
    "id": "assistant-id",
    "name": "Assistant Name",
    "model": {
      "provider": "openai",
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        }
      ]
    }
  }
}
```

**For tool-calls:**

Provide the result of the tool execution:
```json
{
  "toolCallResults": [
    {
      "toolCallId": "call-id",
      "result": "Tool execution result"
    }
  ]
}
```

## Configuration

### Server Settings

Configure where webhooks are sent:

```yaml
server:
  url: "https://yourserver.com/webhooks"
  timeoutSeconds: 20
  headers:
    Authorization: "Bearer your-token"
  credentialId: "credential-id"
  backoffPlan:
    type: "exponential"
    maxRetries: 3
    baseDelaySeconds: 1
```

### Key Properties

- **timeoutSeconds**: Request timeout (default: 20 seconds)
- **credentialId**: Authentication credential ID
- **staticIpAddressesEnabled**: Use static IP addresses for requests
- **encryptedPaths**: Specify request body paths to encrypt
- **backoffPlan**: Configure retry behavior for failed requests

## Message Types

### Phone Number Hooks

Configure behavior for specific call events:

**call.ringing**: Triggered when call arrives
**call.ending**: Triggered when call disconnects

### Hook Actions

- **transfer**: Direct call to a destination
- **say**: Play a message to caller

### Transfer Configuration

```yaml
transfer:
  mode: "blind-transfer|warm-transfer-say-message"
  message: "Transferring now"
  destination:
    type: "number"
    number: "+1234567890"
```

## Error Handling

Failed requests follow the configured `backoffPlan`:

- **type**: "fixed" or "exponential"
- **maxRetries**: Maximum retry attempts (default: 0)
- **baseDelaySeconds**: Base delay between retries
- **excludedStatusCodes**: Status codes to not retry

## Authentication

Configure authentication via:

1. `credentialId` - Referenced credential from dashboard
2. Custom `headers` - Override with custom Authorization header
3. SIP Authentication - For SIP-based phone numbers with `username` and `password`

## Important Notes

- Responses expected only for: `assistant-request`, `tool-calls`, `transfer-destination-request`
- Webhook precedence: `assistant.server` > `phoneNumber.server` > `org.server`
- Include the X-Transfer-Summary SIP header with `blind-transfer-add-summary-to-sip-header` mode
- Maximum TwiML length: 4096 characters for warm transfers
