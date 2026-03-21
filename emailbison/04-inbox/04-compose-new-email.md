# Compose New Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/new:
    post:
      summary: Compose new email
      deprecated: false
      description: >-
        This endpoint allows you to send a one-off email in a new email thread.

        The user must provide a valid authentication token in the request header to access this endpoint.

        Please note that if you are sending an array of file attachments, your request must include
        a header of "Content-Type": "multipart/form-data". Otherwise your file attachments will not be processed.
      tags:
        - Inbox
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sender_email_id
              properties:
                subject:
                  type: string
                  nullable: true
                  description: The subject of the email.
                  example: 'Quick question'
                message:
                  type: string
                  description: The contents of the email.
                  example: 'How are you doing?'
                sender_email_id:
                  type: integer
                  description: The ID of an existing record in the sender_emails table.
                  example: 1
                use_dedicated_ips:
                  type: boolean
                  description: Send using the dedicated campaign IPs instead of the instance IP.
                  example: true
                content_type:
                  type: string
                  description: 'Type of the email (html or text).'
                  example: html
                to_emails:
                  type: array
                  description: Array of people to send this email to.
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        nullable: true
                        description: Name of the person (can be null).
                        example: 'John Doe'
                      email_address:
                        type: string
                        description: Email address of the recipient.
                        example: 'john@example.com'
                cc_emails:
                  type: array
                  description: Array of people to CC on this email.
                  items:
                    type: object
                    required:
                      - email_address
                    properties:
                      name:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                        description: Must be a valid email address.
                        example: 'belle13@example.com'
                bcc_emails:
                  type: array
                  description: Array of people to BCC on this email.
                  items:
                    type: object
                    required:
                      - email_address
                    properties:
                      name:
                        type: string
                        nullable: true
                      email_address:
                        type: string
                        description: Must be a valid email address.
                        example: 'velva98@example.net'
                attachments:
                  type: array
                  description: 'Optional array of multi-part files that you want to attach. Combined max size: 25MB, individual max size: 10MB.'
                  items:
                    type: string
                    format: binary
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: 'Successfully sent email'
                      reply:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 239
                          uuid:
                            type: string
                            example: '9f7a2718-aa56-43k2-a52b-a44dc183a621'
                          folder:
                            type: string
                            example: Sent
                          subject:
                            type: string
                            example: 'Email 3: Lab Cleanup Reminder'
                          read:
                            type: boolean
                            example: true
                          interested:
                            type: boolean
                            example: false
                          automated_reply:
                            type: boolean
                            example: false
                          html_body:
                            type: string
                          text_body:
                            type: string
                          date_received:
                            type: string
                            example: '2024-12-01T03:43:15.000000Z'
                          type:
                            type: string
                            example: 'Untracked Reply'
                          tracked_reply:
                            type: boolean
                            example: false
                          sender_email_id:
                            type: integer
                            example: 25065
                          from_name:
                            type: string
                            example: 'Teddy Frank'
                          from_email_address:
                            type: string
                            example: 'teddy.frank@bisonemails.com'
                          primary_to_email_address:
                            type: string
                            example: 'ross.rhea@bisonemails.com'
                          to:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  example: 'Ross Rhea'
                                address:
                                  type: string
                                  example: 'ross.rhea@bisonemails.com'
                          cc:
                            type: array
                            nullable: true
                            example: null
                          bcc:
                            type: array
                            nullable: true
                            example: null
                          parent_id:
                            type: integer
                            example: 238
                          attachments:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: integer
                                uuid:
                                  type: string
                                reply_id:
                                  type: integer
                                file_name:
                                  type: string
                                download_url:
                                  type: string
                                created_at:
                                  type: string
                                updated_at:
                                  type: string
                          created_at:
                            type: string
                            example: '2025-06-18T02:38:40.000000Z'
                          updated_at:
                            type: string
                            example: '2025-06-18T02:38:40.000000Z'
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
