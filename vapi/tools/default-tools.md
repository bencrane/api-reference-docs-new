# Default Tools

Vapi voice assistants include built-in functions for call management and API integration: `transferCall`, `endCall`, `sms`, `dtmf`, and `apiRequest`. These enable call transfers, disconnections, SMS messaging, keypad input, and business logic integration.

## Adding Default Tools

Default Tools are added through the `tools` array in assistant configuration via API requests or the dashboard tools page.

## Transfer Call

The `transferCall` function routes calls to predefined destinations. Configuration specifies which numbers or endpoints receive transfers.

Example configuration:
```json
{
  "type": "transferCall",
  "destinations": {
    "type": "number",
    "number": "+16054440129"
  }
}
```

## End Call

The `endCall` function terminates active calls when invoked by the assistant based on conversation logic.

## Send Text

The `sms` function sends SMS messages through configured Twilio accounts. It requires a `from` number in metadata.

## Dial Keypad (DTMF)

The `dtmf` function enables keypad digit entry for IVR navigation. Three transmission methods exist:

- **In-band**: Tones within the audio stream (simpler, potentially lower quality)
- **Out-of-band RFC 2833**: Separate RTP transmission (more reliable for VoIP)
- **Out-of-band SIP INFO**: Dedicated SIP messages (less widely supported)

Vapi uses RFC 2833 for reliability in VoIP environments, though effectiveness depends on IVR system configuration.

## API Request

This tool executes HTTP requests to external endpoints during conversations using **LiquidJS syntax** for dynamic variable integration. Supports GET/POST methods with customizable headers, bodies, retry logic, and timeouts.

Example GET request:
```json
{
  "type": "apiRequest",
  "url": "https://api.yourcompany.com/orders/{{orderNumber}}",
  "method": "GET"
}
```

Advanced configurations support exponential backoff retry strategies and custom timeout settings.

---

**Note**: Custom Functions are deprecated; use Tools instead.
