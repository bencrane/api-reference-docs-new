# Setting Server URLs

## Overview

Server URLs in Vapi can be configured at multiple hierarchical levels to handle call events. According to the documentation, "Each level has a different priority" and "The server URL with the highest priority for a relevant event will be the one that Vapi uses to send the event to."

## Four Configuration Levels

Vapi allows server URL configuration at these tiers:

- **Account-wide**: Organization-level default
- **Phone Number**: Individual phone number settings
- **Assistant**: Assistant-specific endpoints
- **Function**: Individual function call routing

## Configuration Methods

### Organization Level
Set in the organization dashboard section. This serves as the fallback if no other URL is configured.

### Phone Number Level
Configure via the phone number API through three approaches:
- During phone number creation
- When importing from Twilio or Vonage
- By updating existing numbers

Phone number server configuration includes the webhook URL and optional authentication credential ID.

### Assistant Level
Two configuration options exist:
- Dashboard: Advanced tab in the assistant section
- API: During assistant creation or updates

The assistant configuration supports webhook URLs and optional credential IDs for authentication.

### Function Level
The most granular option allows per-function configuration:
- Dashboard: Functions tab within assistant settings
- API: Through tools API or assistant configurations

## Priority Hierarchy

Events route based on this priority order:

1. **Function-level URLs** (highest priority)
2. **Assistant-level URLs**
3. **Phone number URLs**
4. **Account-wide URLs** (default/lowest priority)

The documentation notes that most users "set a server URL on your account, and/or on specific assistants."
