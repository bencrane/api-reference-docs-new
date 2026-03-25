# Personalization with User Information

## Overview

The documentation explains how to integrate customer-specific data into voice assistant conversations. When customers call, servers can supply caller information that personalizes the interaction in real time—useful for support, account management, and similar scenarios.

## How It Works

The process involves four key steps:

1. **Incoming Call**: Vapi routes the call to your server rather than a static configuration
2. **Caller Lookup**: Your server identifies the caller and retrieves their data from your database
3. **Response**: Your server sends back either an assistant ID with dynamic variables or a complete configuration
4. **Call Handling**: Vapi uses the personalized setup to guide the conversation

## Implementation Requirements

You'll need:
- A Vapi phone number
- An existing Vapi Assistant
- A server endpoint to handle requests

## Key Setup Steps

**Variable Syntax**: Use `{{variable_name}}` placeholders in instructions. Example: `"Hello {{customerName}}! I see you've been a {{accountType}} customer since {{joinDate}}."`

**Phone Configuration**: Update your phone number via PATCH request to point to your server instead of a static assistant.

**Server Response**: Choose between two approaches—either reference an existing assistant with variable overrides, or return a complete assistant configuration with embedded customer data.

## Critical Constraints

Your server must respond within **7.5 seconds**, or the call fails. The documentation recommends implementing fallbacks for missing data and ensuring high endpoint availability.
