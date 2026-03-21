# Update Sender Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/{senderEmailId}:
    patch:
      summary: Update sender email
      deprecated: false
      description: Update the settings for a specified sender email.
      tags:
        - Sender Emails
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                daily_limit:
                  type: integer
                  description: The daily limit of emails that can be sent from this sender email.
                  example: 300
                name:
                  type: string
                  description: The name of the sender email.
                  example: 'John Doe'
                email_signature:
                  type: string
                  nullable: true
                  description: The HTML signature of the sender email.
                  example: '<p><strong>{SENDER_FIRST_NAME}</strong> | Consultant</p>'
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
                        example: '<p><strong>John Doe</strong> | Consultant</p>'
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
                        example: true
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
