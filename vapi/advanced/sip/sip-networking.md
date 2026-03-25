# SIP Networking and Firewall Configuration

## Overview

When integrating a SIP trunk with Vapi, your firewall must permit both SIP signaling and RTP media traffic. The documentation provides "all IP addresses and ports used by Vapi for SIP signalling" along with RTP specifications and recommended firewall rules.

## Key IP Addresses and Ports

Vapi employs two static IPs for signaling:
- `44.229.228.186/32`
- `44.238.177.138/32`

These serve as the public addresses for Vapi's Session Border Controller nodes handling all SIP messages.

**Signaling ports:**
- Port 5060 (UDP) for standard SIP
- Port 5061 (TLS) for encrypted signaling

**RTP media:**
The documentation emphasizes that "RTP media does not originate from a fixed set of IP addresses." Instead, Vapi allocates dynamic IPs for media traffic across ports 40000-60000 (UDP), bidirectional.

## Firewall Configuration Strategy

Rather than restricting RTP by IP source, administrators should "allow traffic on the full port range without IP restrictions since Vapi uses dynamic IPs for media."

For signaling, both IP addresses require allowlisting since "Vapi may use either address for signalling on any given call."

## DNS Alternative

The hostname `sip.vapi.ai` resolves to both signaling IPs, though the documentation recommends explicit IP-based rules for consistency, as "DNS-based rules may not update immediately if the resolution changes."

## Additional Resources

The guide references supplementary documentation for provider-specific setup, credential troubleshooting, and SRTP configuration.
