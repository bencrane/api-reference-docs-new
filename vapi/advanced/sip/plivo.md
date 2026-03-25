# Plivo SIP Integration Documentation

## Overview
This guide explains how to connect a Plivo SIP trunk to Vapi for handling both inbound and outbound calls. It covers configuration steps for both platforms, phone number registration, and call routing procedures.

## Key Prerequisites
- Active Plivo account
- Admin access to Plivo and SIP trunk configuration
- Available phone number for Vapi integration

**Important Restriction:** "Indian phone numbers cannot be used with Plivo on Vapi due to TRAI regulations."

## Outbound Call Configuration (Vapi to User)

### Plivo Setup Steps:
1. Create an IP Access Control List in Zentrunk, adding these IP addresses:
   - 44.229.228.186/32
   - 44.238.177.138/32

2. Create an Outbound Trunk linked to the IP ACL

3. Record the Termination SIP Domain (format: `12700668357XXXXXX.zt.plivo.com`)

4. Purchase a phone number through Plivo's Numbers section

### Vapi Setup Steps:
1. Obtain your Vapi API key from the dashboard
2. Create a SIP trunk credential via API, using the Plivo Termination SIP Domain
3. Register the Plivo phone number with Vapi
4. Create a Vapi Assistant
5. Make outbound calls using either the API or dashboard

## Inbound Call Configuration (User to Vapi)

### Plivo Setup Steps:
1. Create an Origination URI with value: `sip.vapi.ai;transport=udp`
2. Create an Inbound Trunk referencing this URI
3. Attach your phone number to the inbound trunk via the Zentrunk application setting

### Vapi Setup Steps:
1. Retrieve your API key
2. Create an inbound SIP trunk credential
3. Register the phone number with Vapi

## Technical Limitations
- Only G.711 u-law and A-law codecs are supported
- SIP REFER is not supported for call transfers
- Proper codec configuration is essential for trunk functionality
