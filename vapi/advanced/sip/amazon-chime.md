# Amazon Chime SDK SIP Integration

## Overview

This guide provides instructions for establishing both inbound and outbound SIP trunking between Amazon Chime SDK and Vapi using a Voice Connector. According to the documentation, "This is a **Voice Connector-only** integration — inbound and outbound calls work with no Lambda functions or custom logic required."

The integration is designed for straightforward AI assistant implementations without custom SIP headers, metadata passing, or enriched escalation capabilities. For those advanced features, the documentation recommends using a SIP Media Application with CallAndBridge instead.

## Key Requirements

Before beginning setup, you'll need:
- AWS account with Amazon Chime SDK console access
- Vapi account with private API key
- AWS CLI configuration or console access
- Provisioned phone number in Amazon Chime SDK
- Pre-created Vapi assistant (for inbound functionality)

## Outbound Call Configuration

The outbound setup involves creating a Voice Connector with specific encryption and network settings, enabling termination with whitelisted Vapi IP addresses, and configuring credentials and calling plans. The two Vapi static IPs to whitelist are `44.229.228.186/32` and `44.238.177.138/32`.

In Vapi, you create a BYO SIP trunk credential with TLS/SRTP protocol (for encrypted connections), register the phone number, then make calls via dashboard or API.

## Inbound Call Configuration

For inbound calls, callers dial the Chime phone number, which routes through the Voice Connector to Vapi's SIP server automatically. This requires identifying the SIP signaling subnet for your Voice Connector's region, creating appropriate Vapi credentials, and configuring the Voice Connector's origination settings to point to `YOUR_CREDENTIAL_ID.sip.vapi.ai` on port 5061 with TCP protocol.

The documentation emphasizes that "The `number` field must exactly match the E.164 phone number assigned to your Voice Connector" to ensure proper routing.

## Additional Resources

The guide references related documentation on SIP trunk concepts, networking requirements, and troubleshooting procedures.
