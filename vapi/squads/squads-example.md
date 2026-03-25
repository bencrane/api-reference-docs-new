# Configuring Inbound and Outbound Calls for Squads

**Subtitle:** Configuring assistants for inbound/outbound calls.

---

## Overview

This guide explains how to establish and manage inbound and outbound call functionality within Squads using AI assistants.

## Key Concepts

* **Transient Assistant:** A temporary assistant setup provided directly in the request.
* **Assistant ID:** A reference identifier for a pre-configured assistant.

> **Note:** When referencing Assistant IDs, the `name` property in your payload must align with the assistant's actual name.

## Inbound Call Configuration

When your server receives an `assistant-request`, respond with this JSON structure:

```json
{
    "squad": {
        "members": [
            {
                "assistant": {
                    "name": "Emma",
                    "model": { "model": "gpt-4o", "provider": "openai" },
                    "voice": { "voiceId": "emma", "provider": "azure" },
                    "transcriber": { "provider": "deepgram" },
                    "firstMessage": "Hi, I am Emma, what is your name?",
                    "firstMessageMode": "assistant-speaks-first"
                },
                "assistantDestinations": [
                    {
                        "type": "assistant",
                        "assistantName": "Mary",
                        "message": "Please hold on while I transfer you to our appointment booking assistant Mary.",
                        "description": "Transfer the user to the appointment booking assistant."
                    }
                ]
            },
            {
                "assistantId": "your-assistant-id"
            }
        ]
    }
}
```

**Configuration details:**

* The first member entry represents a transient setup with complete configuration details.
* The second uses an existing Assistant ID reference.
* `assistantDestinations` enables call routing between assistants.

## Outbound Call Configuration

To make outbound calls, POST to `/call/phone` with this payload:

```json
{
    "squad": {
        "members": [
            {
                "assistant": {
                    "name": "Emma",
                    "model": { "model": "gpt-4o", "provider": "openai" },
                    "voice": { "voiceId": "emma", "provider": "azure" },
                    "transcriber": { "provider": "deepgram" },
                    "firstMessage": "Hi, I am Emma, what is your name?",
                    "firstMessageMode": "assistant-speaks-first"
                },
                "assistantDestinations": [
                    {
                        "type": "assistant",
                        "assistantName": "Mary",
                        "message": "Please hold on while I transfer you to our appointment booking assistant Mary.",
                        "description": "Transfer the user to the appointment booking assistant."
                    }
                ]
            },
            {
                "assistantId": "your-assistant-id"
            }
        ]
    },
    "customer": {
        "number": "your-phone-number"
    },
    "phoneNumberId": "your-phone-number-id"
}
```

**Important parameters:**

* `customer.number` specifies the target phone number.
* `phoneNumberId` identifies the phone number resource from your provider.
