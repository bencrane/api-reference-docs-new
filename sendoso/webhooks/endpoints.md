# Endpoints

## Adding an Endpoint

To begin receiving webhook messages, you need to configure endpoints through the webhooks portal. The setup process involves:

- Providing a URL you control
- Selecting desired event types
- Adding the endpoint via the webhooks portal

If no specific event types are selected, the endpoint will receive all events by default.

**Example URL structure:** `https://www.example.com/sendoso/webhooks/`

## Testing an Endpoint

After configuring an endpoint, you can verify its functionality using the testing interface, which allows you to:

- Send test events to your endpoint
- View complete message payloads
- Review all message delivery attempts
- Check success or failure status
