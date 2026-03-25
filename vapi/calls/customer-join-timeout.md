# Customer Join Timeout Documentation

## Overview

The Customer Join Timeout feature allows you to "set the maximum time users have to join a web call before it's automatically terminated." This applies exclusively to web calls, not phone calls.

## Key Configuration Details

**Default timeout:** 15 seconds
**Available range:** 1-60 seconds

Users must complete three critical steps within the timeout window:
- Network connection to Vapi servers
- Microphone permission grants
- WebRTC audio handshake

If users don't finish these steps, calls end with an `assistant-did-not-receive-customer-audio` error.

## Implementation Methods

The parameter `customerJoinTimeoutSeconds` can be configured through:

1. **Creating new assistants** via API
2. **Updating existing assistants**
3. **Transient (inline) assistant configurations**
4. **Per-call assistant overrides**

Code examples are provided in TypeScript, Python, and cURL formats across all configuration methods.

## Recommended Timeout Values

Different user types benefit from varying timeouts:
- Corporate users: 45-60 seconds (account for security policies)
- Mobile users: 30-45 seconds (slower networks, permission prompts)
- First-time users: 45-60 seconds (learning curve)
- Returning users: 20-30 seconds (experienced users)

## Best Practices

Start with 30-60 second timeouts, monitor success metrics, test in staging environments, segment by user type, and provide visual feedback during connection attempts.
