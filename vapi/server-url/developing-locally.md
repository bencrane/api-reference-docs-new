# Developing Locally

**Subtitle:** Learn how to receive server events in your local development environment.

## Overview

The documentation explains how to route Vapi server webhooks to a local development environment using reverse proxies and tunneling services.

## Quick Solution: Vapi CLI + Tunneling

The fastest approach combines two tools:

```bash
# Terminal 1: Set up tunnel (example with ngrok)
ngrok http 4242

# Terminal 2: Install and run Vapi CLI
curl -sSL https://vapi.ai/install.sh | bash
vapi listen --forward-to localhost:3000/webhook
```

**Key Note:** "The `vapi listen` command is a local forwarder only - it does NOT provide a public URL or tunnel." You must pair it with a separate tunneling service to expose the port to the internet.

## Manual Setup with ngrok

### The Problem

Vapi sends events to publicly accessible servers. During development, local machines aren't reachable from the internet. The `localhost` address (`127.0.0.1`) only routes within your machine.

### Solution: Tunneling Traffic

Use ngrok to create a secure tunnel connecting your local machine to the internet:

**Process Steps:**

1. **Start Your API Locally** — Run your server and note its port (e.g., `8080`)

2. **Start Ngrok Agent** — Install ngrok following their quickstart, then run:
   ```bash
   ngrok http 8080
   ```
   Replace `8080` with your actual server port.

3. **Copy the Forwarding URL** — Ngrok displays a public URL that tunnels traffic to your machine. Use this as your Vapi server URL.

4. **Trigger Events** — Conduct calls normally; Vapi will send events to the ngrok URL, which forwards them locally.

### Important Consideration

"This URL will change every time that you run the `ngrok` command." For persistent URLs across sessions, explore ngrok's static domain feature.

## Troubleshooting Checklist

- Verify your local server runs on the expected port
- Confirm the correct port in your ngrok command
- Ensure your webhook endpoint accepts `POST` requests
- Validate the path matches your configuration
