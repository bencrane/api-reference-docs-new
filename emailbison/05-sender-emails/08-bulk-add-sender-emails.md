# Bulk Add Sender Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/bulk:
    post:
      summary: Bulk add sender emails
      deprecated: false
      description: Add multiple sender email addresses at once.
      tags:
        - Sender Emails
      parameters: []
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        name:
                          type: string
                          example: 'John Doe'
                        email:
                          type: string
                          example: 'john@doe.com'
                        email_signature:
                          type: string
                          nullable: true
                          example: null
                        imap_server:
                          type: string
                          example: 'imap.server'
                        imap_port:
                          type: integer
                          example: 110
                        smtp_server:
                          type: string
                          example: 'smtp.server'
                        smtp_port:
                          type: integer
                          example: 112
                        daily_limit:
                          type: integer
                          example: 5
                        type:
                          type: string
                          example: Inbox
                        status:
                          type: string
                          example: Connected
                        warmup_enabled:
                          type: boolean
                          example: false
                        emails_sent_count:
                          type: integer
                          example: 100
                        total_replied_count:
                          type: integer
                          example: 10
                        total_opened_count:
                          type: integer
                          example: 25
                        unsubscribed_count:
                          type: integer
                          example: 0
                        bounced_count:
                          type: integer
                          example: 0
                        unique_replied_count:
                          type: integer
                          example: 7
                        unique_opened_count:
                          type: integer
                          example: 7
                        total_leads_contacted_count:
                          type: integer
                          example: 50
                        interested_leads_count:
                          type: integer
                          example: 3
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-05-18T12:53:32.000000Z'
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
