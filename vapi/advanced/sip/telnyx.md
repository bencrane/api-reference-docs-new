# Telnyx SIP Integration

## Overview
This documentation provides instructions for integrating a Telnyx SIP trunk with Vapi to enable AI voice assistants to manage both inbound and outbound calls.

## Setup Process

### Step 1: Obtain Vapi Private Key
Access your Vapi account settings to retrieve the private API key from the Organization Settings > API Keys section.

### Step 2: Configure Telnyx for Inbound Calls
The inbound configuration involves:
- Creating a SIP trunk with FQDN set to `sip.vapi.ai` on port 5060
- Assigning a phone number to the trunk
- Setting the "Translated Number" in voice settings to your Vapi SIP URI format: `sip:<your-unique-id>@sip.vapi.ai`

### Step 3: Configure Telnyx for Outbound Calls
Outbound setup requires:
- Creating authentication credentials in the "Outbound calls authentication" section
- Setting up an outbound voice profile with appropriate destination configurations
- Selecting the target country for call routing

### Step 4: Add Telnyx Credentials to Vapi
Use the Vapi API endpoint to register your SIP trunk credentials. The request must include gateway IP addresses (not FQDNs), authentication username and password, and the realm `sip.telnyx.com`.

**Important:** Use IP addresses rather than domain names for gateways to avoid errors.

### Step 5: Register Phone Number
Associate your Telnyx phone number with the credential via the Vapi phone number API endpoint.

### Step 6: Assign Voice Assistant
Configure inbound and outbound handlers in the Vapi dashboard's Phone Numbers section.

### Step 7: Initiate Outbound Calls
Use the `/call/phone` API endpoint with your assistant ID, customer phone number, and phone number ID to start calls.

## Key Requirements
- Valid Vapi private key
- Telnyx gateway IP addresses
- SIP authentication credentials
- Phone number in E.164 format (optional validation can be disabled)
