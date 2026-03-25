# Outbound Calling Documentation

## Key Overview

Vapi's outbound calling enables programmatic initiation of single or batch calls to any phone number with scheduling capabilities for time-sensitive communications like appointment reminders and surveys.

## Core Requirements

Before making outbound calls, you need:
- Active Vapi account with dashboard access
- Configured assistant (saved or temporary)
- Phone number source (imported provider number or free Vapi number)
- Recipient's phone number

**Important limitation:** Free Vapi numbers cannot make international calls.

## Making Outbound Calls

The `/call` endpoint requires three components:

1. **Assistant specification** — either transient assistant via `assistant` field or saved assistant via `assistantId`
2. **Phone number source** — the `phoneNumberId` of your calling number
3. **Destination** — recipient's phone number or SIP URI in the `customer` parameter

## Scheduling Calls

Use the `schedulePlan` parameter with an ISO datetime string in `earliestAt` to schedule future calls. You can optionally set `latestAt` for the latest attempt time.

**Critical consideration:** Scheduled calls refetch resources at execution time. Saved assistants pull the latest version—if deleted before call time, the call fails. Use transient assistants for static configurations.

## Batch Calling

The `customers` parameter accepts an array for multiple simultaneous calls. Combine with `schedulePlan` for scheduled batch operations. For customer-specific assistant overrides, call the endpoint separately per number.

## Trusted Calling Framework

### STIR/SHAKEN Authentication

This framework provides three attestation levels verifying caller identity and preventing spoofing. Implementation requires Twilio Trust Hub verification, business documentation submission, and typically 5-7 business days approval.

### CNAM Registration

CNAM displays your business name on recipient phones, improving answer rates. Registration requires legal business name, address, business type, and authorized representative designation through your provider's portal (3-5 day processing).

### Reputation Database Registration

**First Orion** and **Hiya** registration reduce spam flagging by displaying business branding across devices and networks.

**Monitoring services:** IPQualityScore and Nomorobo provide real-time reputation scoring and spam database lookups.

## Critical Compliance Notes

"It is a violation of FCC law to dial phone numbers without consent in an automated manner." Compliance requires adherence to TCPA regulations and obtaining proper consent before calling.

Caller identification setup requires 2-4 weeks for full network propagation.
