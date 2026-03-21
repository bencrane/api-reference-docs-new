# Create IMAP/SMTP Email Account

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/imap-smtp:
    post:
      summary: Create IMAP/SMTP Email Account
      deprecated: false
      description: Creates a new IMAP/SMTP email account for the authenticated workspace.
      tags:
        - Sender Emails
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - email
                - password
                - imap_server
                - imap_port
                - smtp_server
                - smtp_port
              properties:
                name:
                  type: string
                  description: The name associated with the sender email.
                  example: 'John Doe'
                email:
                  type: string
                  description: The email address of the sender. Must be unique and in a valid email format.
                  example: 'john.doe@example.com'
                password:
                  type: string
                  description: The password for the sender email.
                  example: 'securepassword123'
                imap_server:
                  type: string
                  description: The IMAP server address for the sender email. Must be a valid domain name.
                  example: 'imap.example.com'
                imap_port:
                  type: integer
                  description: The IMAP server port for the sender email.
                  example: 993
                smtp_server:
                  type: string
                  description: The SMTP server address for the sender email. Must be a valid domain name.
                  example: 'smtp.example.com'
                smtp_port:
                  type: integer
                  description: The SMTP server port for the sender email.
                  example: 587
                smtp_secure:
                  type: boolean
                  description: Whether to use a secure SMTP connection.
                  example: false
                imap_secure:
                  type: boolean
                  description: Whether to use a secure IMAP connection.
                  example: false
                email_signature:
                  type: string
                  description: The signature for the sender email.
                  example: '{SENDER_FIRST_NAME} | Consultant'
      responses:
        '200':
          description: success
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
                      tags:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            name:
                              type: string
                              example: Google
                            default:
                              type: boolean
                              example: true
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
