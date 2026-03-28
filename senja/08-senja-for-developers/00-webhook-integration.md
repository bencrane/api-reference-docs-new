---
title: "Webhook Integration"
url: "https://support.senja.io/webhook-integration-xu97l"
path: "/webhook-integration-xu97l"
---

# Webhook Integration

Learn about Webhooks in Senja and how to set it up in your account.

Webhooks are a powerful tool for integrating different applications and services. By using webhooks, you can automate workflows and receive real-time updates from other systems.

Now you can easily set up webhooks to receive notifications and trigger actions based on events that occur in Senja.

## Anatomy of Senja's Webhooks

Webhooks consist of several key components:

**Webhook URL:** This is the URL to which the webhook payload will be sent when an event occurs.

**Secret:** This is an optional field that can be used to verify that the webhook was sent by Senja. When you set up a webhook, you can choose to include a secret in the payload. Senja will then sign the payload using this secret, and you can use it to verify that the payload was sent by Senja and has not been tampered with. All webhooks sent by Senja include a `x-senja-signature` header. Senja generates this header using a keyed-hash message authentication code (HMAC) with SHA256 and the secret key that you provide. Below is example NodeJS code that demonstrates how to verify the signature.

```javascript
import crypto from 'crypto';

function createHmacSignature(secret: string, payload: string) {
	const hmac = crypto.createHmac('sha256', secret);
	hmac.update(payload);
	return hmac.digest('hex');
}

function verifyHmacSignature(secret: string, payload: string, signature: string) {
	return createHmacSignature(secret, payload) === signature;
}

const secret = 'YOUR SECRET';
const payload = req.body;
const signature = req.headers['x-senja-signature'];
const isValid = verifyHmacSignature(secret, JSON.stringify(payload), signature);
```

**Events:** These are the events that you want to listen to. When an event occurs in your application, Senja will send a payload to the webhook URL that you specify. The payload will contain information about the event, such as the type of event and any associated data.

By specifying the webhook URL, secret (if desired), and events that you want to listen to, you can configure Senja to send webhook payloads to your application whenever specific events occur.

## Where to edit your Webhook

Click on the automate tab on the sidebar and scroll down. You can also find this in your project settings.

## Webhook Events

Note: for complete details about the fields in the testimonial in the data of the payload, see our REST API documentation.

### testimonial_created

This event is triggered when a new testimonial is created in Senja. The payload will contain information about the testimonial, such as the endorser, text, and date created.

You can use this event to do things like automatically tag someone who sends you a testimonial in your CRM.

Example Payload:

```json
{
  "type": "testimonial_created",
  "data": {
    "new": {
      "id": "rev_1234567890abcdef",
      "type": "text",
      "integration": "google",
      "title": "Amazing product experience!",
      "text": "This product has completely transformed how we handle our workflow...",
      "rating": 5,
      "media": [...],
      "url": "https://google.com/reviews/123",
      "date": "2024-01-15T10:30:00Z",
      "approved": true,
      "project_id": "7db5d354-6556-4f88-b29a-99e9552ca906",
      "customer_name": "Sarah Johnson",
      "customer_email": "sarah.johnson@example.com",
      "customer_company": "Tech Solutions Inc",
      "customer_tagline": "Senior Product Manager",
      "tags": ["featured", "enterprise", "workflow"],
      "video_url": null,
      "video": null
    }
  }
}
```

### testimonial_updated

This event is triggered when an existing testimonial in Senja is updated. The payload will contain information about the updated testimonial, such as the approval status, the updated text etc.

You can use this event to do things like automatically publish a testimonial to social media when a testimonial has been approved.

The payload contains both `old` and `new` fields showing the testimonial state before and after the update.

### testimonial_deleted

This event is triggered when a testimonial is deleted in Senja. The payload will contain information about the deleted testimonial, such as the endorser and the text.

The payload contains an `old` field with the deleted testimonial's data.
