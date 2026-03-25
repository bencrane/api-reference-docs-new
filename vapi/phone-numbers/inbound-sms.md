# Inbound SMS Documentation

## Overview
Vapi enables agents to automatically start conversations when receiving text messages on US phone numbers. The feature integrates with Twilio's messaging infrastructure to route inbound SMS directly to your configured agent.

## Key Requirements
- Twilio-hosted US phone number
- SMS capability activated on the number
- US-to-US messaging only (international SMS not supported)

## Setup Process

### Dashboard Configuration
Three main steps enable this feature:

1. **Number Import**: Bring your Twilio number into Vapi's platform for webhook management
2. **SMS Activation**: Toggle the SMS setting in number configuration, which prompts Vapi to configure Twilio's messaging webhook
3. **Agent Assignment**: Optionally assign an assistant to handle incoming text conversations

### API Implementation
The feature activates through the POST `/phone-number` or PATCH `/phone-number/{id}` endpoints by setting `"smsEnabled: true"`.

This parameter tells Vapi to manage your Twilio messaging webhook automatically. Setting it to false preserves your existing Twilio configuration.

## Important Constraints
- "Both sender and recipient must be US numbers"
- Twilio serves as the only supported provider currently
- Vapi automatically controls webhook routing when SMS is enabled

## Related Resources
After enabling inbound SMS, explore SMS chat functionality, session persistence, and chat integration quickstarts for complete implementation guidance.
