# Local Webhook Testing Documentation

## Overview
The `vapi listen` command provides local webhook forwarding capabilities, though it requires a separate tunneling service like ngrok to expose your development server to the internet.

## Key Points

**Important distinction:** The documentation emphasizes that "vapi listen does NOT provide a public URL or tunnel." Users must implement their own tunneling solution separately.

## Quick Setup Process

The standard workflow involves:
1. Establishing a tunnel using services like ngrok
2. Running the listener with `vapi listen --forward-to localhost:3000/webhook`
3. Updating Vapi Dashboard webhook URLs to point to your tunnel URL
4. Testing by triggering webhook events

## Core Functionality

The listener operates on port 4242 by default and accepts configuration options including:
- Custom port specification via `--port` flag
- TLS verification bypass with `--skip-verify` (development only)
- Event filtering capabilities (noted as "coming soon")

## Supported Webhook Event Categories

The system handles multiple event types including:
- Call lifecycle events (started, ended, failed)
- Speech-related events (updates, transcription, voice input)
- Assistant operations (function calls, messages, conversation updates)
- System events (errors, recordings, analysis)

## Development Workflow

The documentation provides a typical three-terminal setup showing how your application, tunneling service, and listener work together in the data flow: **Vapi → Tunnel → CLI forwarder → Local server**

## Code Examples

Sample webhook handlers are provided in TypeScript, Python, and Go, demonstrating event type handling and response patterns.

## Security Notes

The documentation warns that this tool targets development environments only and recommends signature verification and HTTPS for production implementations.
