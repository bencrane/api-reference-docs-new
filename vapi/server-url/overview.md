# Server URLs Documentation

## Overview

Server URLs enable applications to receive real-time conversation data and communicate bidirectionally with Vapi during active calls. As stated in the documentation, "Server URLs give Vapi a location to send real-time conversation data (as well as query for data Vapi needs)."

## Key Event Types

The system supports several conversation events:

- **Status Updates:** Call status notifications
- **Transcript Updates:** Real-time call transcripts
- **Function Calls:** Payloads when assistants request actions
- **Assistant Requests:** Dynamic configuration queries from Vapi
- **End of Call Report:** Summary data upon call completion
- **Hang Notifications:** Alerts when assistants fail to respond

## Getting Started

Four primary resources guide implementation:

1. **Setting Server URLs** — Configuration locations and setup
2. **Events** — Types of events Vapi transmits
3. **Developing Locally** — Local environment testing
4. **CLI Webhook Testing** — Vapi CLI forwarding capabilities

### Local Testing Approach

The documentation recommends using ngrok tunneling combined with the Vapi CLI for local development:

```bash
ngrok http 4242
vapi listen --forward-to localhost:3000/webhook
```

## Server Location Options

Publicly accessible HTTP endpoints can be hosted on:

- **Cloud Servers:** Railway, AWS, GCP
- **Serverless Functions:** Vercel, AWS Lambda, Google Cloud Functions, Cloudflare
- **Workflow Orchestrators:** Pipedream, Make

## Terminology Clarification

The documentation distinguishes "Server URL" from traditional webhooks, noting that certain events require "meaningful reply from your server" rather than simple acknowledgment responses.

## Additional Resources

- Server authentication
- Spam call rejection via server URLs
- Local development guidance
