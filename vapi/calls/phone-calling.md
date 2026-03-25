# Phone Calling Documentation

## Overview

Vapi enables users to establish phone numbers for placing and receiving calls. The platform offers complimentary phone numbers exclusively for US domestic use, with international numbers requiring paid plans. Users can create up to 10 free numbers per account. For international calling needs, users have the option to import their own numbers from Twilio.

## Setting Up Phone Numbers

Two approaches are available for phone number configuration:

**Creating Free US Numbers:**
- Access via Vapi dashboard or the `/phone-numbers` API endpoint
- Limited to US national use only

**Importing Custom Numbers:**
- Available through dashboard or the `/phone-numbers/import` endpoint
- Requires Twilio credentials for verification and integration with Vapi services

## Outbound Calling

Users can initiate outbound calls through the `/call` endpoint. The process accommodates two scenarios:

- Providing a temporary assistant via the `assistant` field when system messages vary per call
- Reusing assistants by specifying their ID in the `assistantId` field

## Inbound Calling

Phone numbers can be configured with an `assistantId` for handling incoming calls. Alternatively, leaving the `assistantId` blank allows Vapi to dynamically retrieve the appropriate assistant from your server based on the caller's phone number.

## Available Documentation Resources

The platform offers extensive guides covering outbound calling, WebSocket audio streaming, live call controls, voicemail detection, call forwarding, warm transfers, call routing, Twilio integration, troubleshooting, concurrency management, call analysis, and recording capabilities.
