# Troubleshoot SIP Trunk Credential Errors

## Overview

This documentation addresses the error message "Couldn't validate SIP trunk credential. SIP gateway creation failed" that occurs during BYO SIP trunk setup in Vapi. The guide identifies three primary causes: using hostnames for inbound gateways, enabling inbound on outbound-only trunks, and missing IP allowlist entries.

## Key Concepts

**Hostname vs. IP Address Behavior:**
The system accepts both hostnames and IPv4 addresses in the `ip` field, but with different constraints:
- Outbound gateways support both formats
- Inbound gateways require numeric IPv4 addresses only

**Inbound Gateway Restriction:**
When `inboundEnabled` is set to `true` and a hostname is provided, the SBC rejects the configuration because it cannot match incoming SIP requests to a domain name.

## Primary Troubleshooting Steps

**Option 1 - Convert Hostname to IP:**
Use DNS lookup commands (`dig` or `nslookup`) to resolve the hostname to an IPv4 address, then update the gateway configuration with the numeric address.

**Option 2 - Disable Inbound:**
If only outbound calling is required, set `inboundEnabled: false` to allow hostname usage.

**IP Allowlist Configuration:**
Two Vapi SBC IP addresses must be whitelisted by the provider:
- `44.229.228.186/32`
- `44.238.177.138/32`

Both addresses are critical; missing either can cause intermittent failures.

## Gateway Configuration Parameters

The gateway configuration supports these options: `ip` (required), `port` (default: 5060), `netmask` (24-32 range), `inboundEnabled` and `outboundEnabled` (both default to true), `outboundProtocol` (default: UDP), and `optionsPingEnabled` (default: false).

## Support Resources

If issues persist, users should contact Vapi support with their organization ID, error message, request payload (password redacted), provider information, and call direction requirements.
