# Twilio SIP Integration Documentation

## Overview
This guide covers setting up SIP trunking between Twilio and Vapi for both outbound and inbound calls. The process involves configuring trunks, whitelisting IP addresses, and creating credentials.

## Outbound Calls Configuration

**Twilio Setup:**
1. Create an Elastic SIP Trunk with appropriate naming and settings
2. Configure termination settings and note the SIP URI for later use
3. Whitelist Vapi's static IP addresses:
   - 44.229.228.186
   - 44.238.177.138
4. Purchase or migrate phone numbers to the trunk

**Vapi Setup:**
1. Obtain your Vapi API key from Organization Settings
2. Create a SIP trunk credential using the Twilio gateway ID
3. Register your phone number with the credential ID
4. Make outbound calls via dashboard or API

## Inbound Calls Configuration

**Twilio Setup:**
Access the Origination section and add the Vapi SIP URI in format: `sip:YOUR_PHONE_NUMBER@<credential_id>.sip.vapi.ai`

**Vapi Setup:**
Create and configure an assistant, then link it to your registered phone number. Incoming Twilio calls will automatically route to your assistant.

## Key Resources
- Video tutorial available embedded in documentation
- API endpoints provided for credential and phone number management
- Step-by-step instructions with visual references
