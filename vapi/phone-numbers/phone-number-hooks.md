# Phone Number Hooks

## Overview

Phone number hooks enable you to set up automated responses triggered by call events. Currently, the system supports the `call.ringing` event, which activates when an incoming call begins ringing.

## Usage

Hooks are configured within the `hooks` array of a phone number configuration. Each hook requires:

* `on`: The triggering event (currently supports `call.ringing`)
* `do`: The actions to execute when triggered (supports `transfer` and `say`)

## Example: Say Message on Call Ringing

Play an audio message when a call starts ringing:

```bash
curl -X PATCH "https://api.vapi.ai/phone-number/<id>" \
     -H "Authorization: Bearer <auth>" \
     -H "Content-Type: application/json" \
     -d '{
  "hooks": [{
    "on": "call.ringing",
    "do": [{
      "type": "say",
      "exact": "inbound calling is disabled."
    }]
  }]
}'
```

## Example: Transfer on Call Ringing

Route an incoming call to another phone number when ringing begins:

```bash
curl -X PATCH "https://api.vapi.ai/phone-number/<id>" \
     -H "Authorization: Bearer <auth>" \
     -H "Content-Type: application/json" \
     -d '{
  "hooks": [{
    "on": "call.ringing",
    "do": [{
      "type": "transfer",
      "destination": {
        "type": "number",
        "number": "+1234567890",
        "callerId": "+1987654321"
      }
    }]
  }]
}'
```

Transfer calls to a SIP endpoint:

```bash
curl -X PATCH "https://api.vapi.ai/phone-number/<id>" \
     -H "Authorization: Bearer <auth>" \
     -H "Content-Type: application/json" \
     -d '{
  "hooks": [{
    "on": "call.ringing",
    "do": [{
      "type": "transfer",
      "destination": {
        "type": "sip",
        "sipUri": "sip:user@domain.com"
      }
    }]
  }]
}'
```

## Common Use Cases

Phone number hooks are frequently used for:

* Deactivating inbound call reception through message playback or call forwarding
