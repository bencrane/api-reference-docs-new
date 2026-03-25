# Call Forwarding Documentation

## Overview
Vapi's call forwarding enables redirecting calls to different phone numbers based on specific conditions using the `transferCall` tool. This facilitates intelligent call routing through predefined destinations with custom messaging.

## Core Concepts

### Transfer Call Tool
The `transferCall` tool manages call forwarding to predefined numbers with destination-specific messages. For dynamic routing determined at runtime, configure the tool with an empty `destinations` array and either have the assistant supply a destination parameter or respond via the `transfer-destination-request` webhook.

### Key Parameters
- **Destinations**: List of phone numbers receiving forwarded calls
- **Messages**: Custom messaging informing callers about the forwarding action

## Implementation Methods

### Dashboard Setup
Navigate to the Tools section, create a new Transfer Call tool, and configure departments with their respective phone numbers and caller messages.

### API Configuration
Define the tool programmatically with destinations and corresponding messages:

```json
{
  "tools": [
    {
      "type": "transferCall",
      "destinations": [
        {
          "type": "number",
          "number": "+1234567890",
          "message": "I am forwarding your call to Department A. Please stay on the line."
        }
      ],
      "function": {
        "name": "transferCall",
        "description": "Use this function to transfer the call. Only use it when following instructions that explicitly ask you to use the transferCall function.",
        "parameters": {
          "type": "object",
          "properties": {
            "destination": {
              "type": "string",
              "enum": ["+1234567890"],
              "description": "The destination to transfer the call to."
            }
          },
          "required": ["destination"]
        }
      }
    }
  ]
}
```

Extensions can be specified for forwarding to specific extensions at a destination number.

### Function Invocation
The assistant executes the transfer using the function with the selected destination parameter.

## Message Customization
Messages are conditional on the selected destination, allowing personalized caller communications for each routing path.

## Assistant Instructions
Use system prompts to guide the assistant on when to invoke `transferCall` with specific numbers based on caller needs (e.g., sales vs. technical support).

## Troubleshooting
- Review logs for transfer errors
- Verify correct destination numbers are configured
- Ensure function descriptions clearly indicate forwarding intentions
- Thoroughly test before production deployment

## Call Transfer Modes

### Blind Transfer (Default)
Directly transfers calls without providing recipient context.

### Warm Transfer
Transfers calls after providing context to the recipient. **Note:** Currently available only with Twilio-based telephony.

#### Warm Transfer Variations

**1. With Summary**: Provides a call summary to the recipient using transcript data.

```json
"transferPlan": {
  "mode": "warm-transfer-with-summary",
  "summaryPlan": {
    "enabled": true,
    "messages": [
      {
        "role": "system",
        "content": "Please provide a summary of the call."
      },
      {
        "role": "user",
        "content": "Here is the transcript:\n\n{{transcript}}\n\n"
      }
    ]
  }
}
```

**2. With Message**: Delivers custom messaging to the recipient before transfer.

```json
"transferPlan": {
  "mode": "warm-transfer-with-message",
  "message": "Hey, this call has been forwarded through Vapi."
}
```

**3. Wait for Operator Then Say Message**: Waits for recipient acknowledgment before delivering messaging.

```json
"transferPlan": {
  "mode": "warm-transfer-wait-for-operator-to-speak-first-and-then-say-message",
  "message": "Hey, this call has been forwarded through Vapi."
}
```

**4. Wait for Operator Then Say Summary**: Waits for recipient acknowledgment before delivering summary.

```json
"transferPlan": {
  "mode": "warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary",
  "summaryPlan": {
    "enabled": true,
    "messages": [
      {
        "role": "system",
        "content": "Please provide a summary of the call."
      },
      {
        "role": "user",
        "content": "Here is the transcript:\n\n{{transcript}}\n\n"
      }
    ]
  }
}
```

**5. With TwiML**: Executes TwiML instructions on the destination call leg before connection. Supports Play, Say, Gather, and Pause verbs with a 4096-character limit. TwiML must be a single-line valid XML string without line breaks or tabs.

```json
"transferPlan": {
  "mode": "warm-transfer-with-twiml",
  "twiml": "<Say>Hello, transferring a customer to you.</Say><Pause length=\"2\"/><Say>They called about billing questions.</Say>"
}
```

**6. Experimental Warm Transfer**: Dials the destination and places the caller on hold. If the destination answers, calls connect; if voicemail or no answer occurs, plays fallback messaging.

```json
"transferPlan": {
  "mode": "warm-transfer-experimental",
  "message": "Transferring a customer to you.",
  "holdAudioUrl": "https://api.twilio.com/cowbell.mp3",
  "voicemailDetectionType": "transcript",
  "fallbackPlan": {
    "message": "Could not transfer your call, goodbye.",
    "endCallEnabled": true
  },
  "summaryPlan": {
    "enabled": true,
    "messages": [
      {
        "role": "system",
        "content": "Please provide a summary of the call."
      },
      {
        "role": "user",
        "content": "Here is the transcript:\n\n{{transcript}}\n\n"
      }
    ]
  }
}
```

Voicemail detection supports `"audio"` (default, comprehensive) or `"transcript"` (fastest) modes. Custom hold audio via `holdAudioUrl` plays during the transfer if provided.

**7. Assistant-Based Warm Transfer (Experimental)**: Leverages AI assistants to manage the transfer process with operator conversations. Detailed configuration is available in the Assistant-based warm transfer documentation.

## Key Notes
- The `{{transcript}}` variable contains the full call transcript for use in summaries
- Only Google or OpenAI providers support voicemail detection in transfer plans
- TwiML must be valid XML without newlines or tabs
- Custom hold audio requires valid MP3 file URLs
- All warm transfer modes require Twilio-based telephony except where specified
