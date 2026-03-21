# Send Test Webhook Event

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/webhook-events/test-event:
    post:
      summary: Send Test Webhook Event
      deprecated: false
      description: 'Sends a test webhook event to the specified URL with a sample payload for the given event type.'
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
                - url
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
                url:
                  type: string
                  example: https://example.com/webhook
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Test event sent successfully
                      payload:
                        type: object
                        description: The sample payload that was sent to the URL.
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
