# SIP Trunking Integration Guide

## Overview

SIP trunking modernizes business communications by replacing traditional phone lines with internet-based virtual connections. The technology connects your internal PBX or VoIP system to a SIP provider, which routes calls through the Public Switched Telephone Network (PSTN), thereby streamlining infrastructure and typically reducing expenses.

## Network Configuration Requirements

To facilitate SIP signaling and media flow between Vapi and your provider, you must allowlist these IP addresses:

* 44.229.228.186/32
* 44.238.177.138/32

For comprehensive details on ports, RTP ranges, and firewall setup, consult the networking and firewall reference documentation.

### Authentication Warning

"IP-based authentication can lead to routing issues" in shared server environments. This approach works reliably only when your provider supplies a unique termination URI or dedicated server per customer, as Plivo and Twilio do.

## Compatible Providers

Vapi integrates with:

* **Plivo**: Unique SIP domain with IP-based authentication support
* **Telnyx**: SIP gateway domain (sip.telnyx.com) using IP-based authentication
* **Zadarma**: SIP credentials (username/password) with sip.zadarma.com
* **Custom BYO SIP Trunk**: Any provider using gateway address and authentication details

## Implementation Steps

### Step 1: Gather Provider Information
Collect your SIP server address, authentication credentials, and at least one phone number (DID).

### Step 2: Create SIP Trunk Credential

Use the Vapi API to establish a new credential with type `byo-sip-trunk`:

```bash
curl -X POST "https://api.vapi.ai/credential" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_VAPI_PRIVATE_KEY" \
  -d '{
    "provider": "byo-sip-trunk",
    "name": "Zadarma Trunk",
    "gateways": [{
      "ip": "sip.zadarma.com",
      "inboundEnabled": false
    }],
    "outboundLeadingPlusEnabled": true,
    "outboundAuthenticationPlan": {
      "authUsername": "YOUR_SIP_NUMBER",
      "authPassword": "YOUR_SIP_PASSWORD"
    }
  }'
```

### Step 3: Link Phone Number to Trunk

Create a Phone Number resource connecting your DID to the credential:

```bash
curl -X POST "https://api.vapi.ai/phone-number" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_VAPI_PRIVATE_KEY" \
  -d '{
    "provider": "byo-phone-number",
    "name": "Zadarma Number",
    "number": "15551234567",
    "numberE164CheckEnabled": false,
    "credentialId": "YOUR_CREDENTIAL_ID"
  }'
```

### Step 4: Testing

**Outbound Testing:**
Initiate calls via dashboard or API to verify routing:

```json
POST https://api.vapi.ai/call/phone
{
  "assistantId": "YOUR_ASSISTANT_ID",
  "customer": {
    "number": "15557654321",
    "numberE164CheckEnabled": false
  },
  "phoneNumberId": "YOUR_PHONE_NUMBER_ID"
}
```

**Inbound Testing:**
Call your number from external lines. Ensure the provider forwards to the correct SIP URI: `{phoneNumber}@<credential_id>.sip.vapi.ai`

**Important:** Provide all signaling IP addresses during trunk creation to avoid 401 unauthorized errors on inbound calls.

### Step 5: Call Transfer (SIP REFER)

Configure call transfers using SIP REFER with this format:

```
sip:transfer-number@your-telecom-provider-domain.com
```

Example: `sip:15557654321@sip.zadarma.com`

Some providers require E.164 formatting: `sip:+15557654321@sip.zadarma.com`

**Tool Configuration:**

```json
{
  "type": "transferCall",
  "destinations": [
    {
      "type": "sip",
      "sipUri": "sip:14039932200@sip.telnyx.com"
    }
  ]
}
```

Note: Enable SIP REFER in your provider's settings if necessary.
