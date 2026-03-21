# Get Sample Webhook Payload

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/webhook-events/sample-payload:
    get:
      summary: Get Sample Webhook Payload
      deprecated: false
      description: 'Returns a sample payload for the specified webhook event type. The payload includes event, scheduled_email, campaign_event, lead, campaign, and sender_email objects.'
      tags:
        - Webhooks
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - event_type
              properties:
                event_type:
                  type: string
                  enum:
                    - email_sent
                    - lead_first_contacted
                    - lead_replied
                    - lead_interested
                    - email_opened
                    - email_bounced
                    - lead_unsubscribed
                    - email_account_added
                    - email_account_removed
                    - email_account_disconnected
                    - email_account_reconnected
                    - manual_email_sent
                    - untracked_reply_received
                    - tag_attached
                    - tag_removed
                    - warmup_disabled_receiving_bounces
                    - warmup_disabled_causing_bounces
                  example: email_sent
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      event:
                        type: object
                        description: The event metadata.
                      scheduled_email:
                        type: object
                        description: The scheduled email details.
                      campaign_event:
                        type: object
                        description: The campaign event details.
                      lead:
                        type: object
                        description: The lead associated with the event.
                      campaign:
                        type: object
                        description: The campaign associated with the event.
                      sender_email:
                        type: object
                        description: The sender email account details.
          headers: {}
      security:
        - bearer: []
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://dedi.emailbison.com
security:
  - bearer: []
```
