# Forward Reply

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/forward:
    post:
      summary: Forward reply
      deprecated: false
      description: >-
        This endpoint allows you to forward an existing reply.

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
          description: The ID of the reply to forward.
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                reply_all:
                  type: boolean
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
                  description: 'This field is required unless `reply_all` is `true`. The ID of an existing record in the sender_emails table.'
                  example: 5
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
                      email_address:
                        type: string
                        example: 'john@example.com'
                cc_emails:
                  type: array
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
                bcc_emails:
                  type: array
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
                          sender_email_id:
                            type: integer
                          from_name:
                            type: string
                          from_email_address:
                            type: string
                          primary_to_email_address:
                            type: string
                          to:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                address:
                                  type: string
                          parent_id:
                            type: integer
                          attachments:
                            type: array
                            items:
                              type: object
                          created_at:
                            type: string
                          updated_at:
                            type: string
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
