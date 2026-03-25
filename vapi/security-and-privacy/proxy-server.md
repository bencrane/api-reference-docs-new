# Proxy Server Guide

## Overview

The proxy server pattern keeps assistant configurations and API keys secure on your backend while your frontend sends only non-sensitive custom data. As the guide explains, "Proxy server keeps assistant configs and API keys on your backend. Frontend sends custom data, backend maps to Vapi calls."

The request flow follows this path: Frontend → Your Proxy → Vapi API → Response → Frontend

**Critical Security Note:** "Never expose your private API key in the browser. Keep it on your server and read it from environment variables."

## Frontend Implementation

The frontend initializes the Vapi client by passing your proxy URL as the second parameter:

```javascript
import Vapi from '@vapi-ai/web';

const vapi = new Vapi('your-token', 'https://your-proxy.com');

vapi.start({
  userId: 'customer123',
  assistantType: 'sales-coach',
});
```

The frontend only transmits non-sensitive context like user IDs and assistant types, allowing your backend to handle authentication and configuration selection.

## Backend Proxy Example

The provided Cloudflare Worker example demonstrates:
- CORS header handling
- Request validation and parsing
- Assistant configuration selection based on request parameters
- Authenticated calls to the Vapi API using server-side credentials
- Error handling and response forwarding

## Implementation Steps

1. **Extract custom data** from frontend requests (userId, assistantType, etc.)
2. **Map to configuration** by selecting existing assistant IDs or building transient configurations
3. **Call Vapi securely** using your server-side API key and forward responses

This approach ensures "Secure calls with configs and secrets hidden on your backend."

## Related Resources

- JWT authentication
- Server URLs
