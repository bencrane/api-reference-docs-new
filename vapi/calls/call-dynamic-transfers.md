# Dynamic Call Transfers Documentation

## Overview

The documentation describes Vapi's dynamic call transfer system, which enables "intelligent routing by determining transfer destinations in real-time based on conversation context, customer data, or external system information."

## Key Capabilities

The system supports several important features:

- Real-time destination selection based on conversation analysis
- Integration with external systems (CRM, databases, APIs)
- Conditional routing logic for departments and specialists
- Context-aware transfers with conversation summaries
- Programmatic transfer control via Call Control API

## How It Works

The process follows a server-controlled pattern:

1. Customer requests transfer during call
2. Vapi triggers custom tool on HTTP server
3. Server receives control URL for live call management
4. Server executes business logic (CRM updates, routing decisions)
5. Server completes transfer via POST to control URL
6. Call connects to specified SIP or PSTN destination

## Implementation Steps

**Step 1: Create Custom Tool**

Developers can create tools via dashboard, TypeScript SDK, Python SDK, or cURL with custom parameters like department, reason, and urgency.

**Step 2: Create Assistant**

The assistant includes the transfer tool and system prompts guiding when transfers should occur.

**Step 3: Build Webhook Server**

Servers receive tool calls containing the control URL and execute transfers by posting transfer details (destination type, number/SIP URI, and message content).

**Step 4: Test System**

Testing involves creating calls and monitoring logs to verify transfers execute correctly.

## Routing Patterns

Common implementations include:

- **Support routing** - Direct based on issue type and customer tier
- **Geographic routing** - Route to regional offices by location
- **Load balancing** - Distribute calls among available agents
- **Escalation management** - Route urgent issues automatically

## Troubleshooting

Common issues include unconfirmed tool calls (verify server URL accessibility), failed transfers (validate destination format), and silent failures (check server logs).
