# Send Reply

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/reply:
    post:
      summary: Create new reply
      deprecated: false
      description: >-
        This endpoint allows you to reply to an existing email.

        The user must provide a valid authentication token in the request header to access this endpoint.

        Please note that if you are sending an array of file attachments, your request must include
        a header of "Content-Type": "multipart/form-data". Otherwise your file attachments will not be processed.
      tags:
        - Inbox
      parameters:
        - name: reply_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply to respond to.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - to_emails
              properties:
                reply_all:
                  type: boolean
                  description: >-
                    If set to true, automatically choose the correct sender email, and add the recipients
                    from the original reply. Explicitly passing in `sender_email_id` will overwrite the chosen
                    sender email, and recipients passed in `to_emails` or `cc_emails` will be appended.
                  example: true
                inject_previous_email_body:
                  type: boolean
                  nullable: true
                  description: Whether to inject the body of the previous email into this email.
                  example: true
                message:
                  type: string
                  description: The contents of the reply.
                  example: 'How are you doing?'
                reply_template_id:
                  type: integer
                  description: The reply template ID that you want to use for this reply.
                  example: 123
                use_dedicated_ips:
                  type: boolean
                  description: Send using the dedicated campaign IPs instead of the instance IP.
                  example: true
                sender_email_id:
                  type: integer
                  description: >-
                    The ID of the sender email. Not required if `reply_all` is set to true.
                    If `reply_all` is set to true and this parameter is passed, this parameter takes priority.
                  example: 139
                content_type:
                  type: string
                  description: 'Type of the email (html or text).'
                  example: html
                to_emails:
                  type: array
                  description: >-
                    Array of people to send this email to. Not required if `reply_all` is set to true.
                    If `reply_all` is set to true and this parameter is passed, the recipients will be appended.
                    Duplicate recipients are ignored.
                  items:
                    type: object
                    required:
                      - email_address
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
                  description: >-
                    An array of people to send a copy of this email to (Carbon Copy).
                    If `reply_all` is set to true and this parameter is passed, the recipients will be appended.
                    Duplicate recipients are ignored.
                  items:
                    type: object
                    required:
                      - email_address
                    properties:
                      name:
                        type: string
                        nullable: true
                        description: The name of the person receiving the email (optional).
                      email_address:
                        type: string
                        description: The email address of the recipient.
                        example: 'john@example.com'
                bcc_emails:
                  type: array
                  description: An array of people to send a blind copy of this email to (Blind Carbon Copy).
                  items:
                    type: object
                    required:
                      - email_address
                    properties:
                      name:
                        type: string
                        nullable: true
                        description: The name of the person receiving the email (optional).
                      email_address:
                        type: string
                        description: The email address of the recipient.
                        example: 'jane@example.com'
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
                                address:
                                  type: string
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
