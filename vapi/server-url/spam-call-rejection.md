# Spam Call Rejection

## Overview

This documentation explains how to use a Server URL to filter inbound calls before they reach your assistant. The system allows you to check caller phone numbers against a spam list and either reject the call or proceed with conversation.

## Core Functionality

According to the documentation, "When an inbound call arrives, Vapi can ask your server which assistant to use via an `assistant-request`." At this point, you can validate the caller's number and respond in one of two ways:

- **Reject spam**: Return an error message to be spoken to the caller, ending the call
- **Allow call**: Return a transient assistant configuration to continue

## Implementation Steps

The process involves three main steps:

1. Configure a Server URL at the phone number, assistant, or organization level
2. Vapi sends an `assistant-request` webhook for inbound calls without a fixed assistantId
3. Your server responds with either an error or an assistant object

**Critical timing note**: "Your server must respond within ~7.5 seconds or the call may fail."

## Code Example

The documentation provides a Node.js/Express implementation that checks incoming callers (in E.164 format) against a local spam list, then either rejects or returns a transient assistant configuration with OpenAI and 11Labs voice settings.

## Response Patterns

Two response formats are documented:
- Error rejection with spoken message
- Assistant configuration with model, voice, and firstMessage properties

## Best Practices

The guide recommends storing spam lists in databases or using reputation APIs, and notes you can reference saved assistants using `assistantId` instead of inline configurations.
