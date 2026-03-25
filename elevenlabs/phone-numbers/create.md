# Import Phone Number API Documentation

## Endpoint
**POST** `https://api.elevenlabs.io/v1/convai/phone-numbers`

This endpoint enables importing phone numbers from provider configurations, supporting both Twilio and SIP trunk providers.

## Request Body

The request uses a discriminated union based on the `provider` field:

### Twilio Provider
Required fields:
- `provider`: "twilio"
- `phone_number`: Phone number string
- `label`: Descriptive label
- `sid`: Twilio Account SID
- `token`: Twilio Auth Token

Optional fields:
- `region_config`: Regional configuration (region_id, token, edge_location)
- `supports_inbound`/`supports_outbound`: Deprecated boolean flags

### SIP Trunk Provider
Required fields:
- `provider`: "sip_trunk"
- `phone_number`: Phone number string
- `label`: Descriptive label

Optional fields:
- `inbound_trunk_config`: Allowed addresses, numbers, media encryption, credentials, remote domains
- `outbound_trunk_config`: Address, transport protocol, media encryption, headers, credentials

## Response

Successful responses return:
```json
{
  "phone_number_id": "string"
}
```

## Error Handling
- **422**: Validation errors with detailed field-level information

## Available Servers
- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

SDK implementations are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.
