# Create Webhook

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/webhook-url:
    post:
      summary: Create Webhook
      deprecated: false
      description: 'Creates a new webhook with the specified event subscriptions.'
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
                - name
                - url
                - events
              properties:
                name:
                  type: string
                  example: My Webhook
                url:
                  type: string
                  example: https://example.com/webhook
                events:
                  type: array
                  items:
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
                  example:
                    - email_sent
                    - lead_replied
                    - lead_interested
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      name:
                        type: string
                        example: My Webhook
                      url:
                        type: string
                        example: https://example.com/webhook
                      events:
                        type: array
                        items:
                          type: string
                        example:
                          - email_sent
                          - lead_replied
                          - lead_interested
                      created_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
                      updated_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
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
