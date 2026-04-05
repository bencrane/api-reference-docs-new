# Get Scheduled Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/scheduled-emails/{id}:
    get:
      summary: Get scheduled email
      description: This endpoint retrieves a single scheduled (campaign) email.
      tags:
        - Scheduled Emails
      operationId: getScheduledEmail
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the scheduled email.
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
                        example: 2542387
                      campaign_id:
                        type: integer
                        example: 76
                      sequence_step_id:
                        type: integer
                        example: 99
                      thread_reply:
                        type: boolean
                        example: false
                      email_subject:
                        type: string
                        example: Hey John
                      email_body:
                        type: string
                        example: Check out this offer
                      status:
                        type: string
                        example: sent
                      scheduled_date:
                        type: string
                        example: '2025-11-25T19:12:00.000000Z'
                      scheduled_date_local:
                        type: string
                        example: '2025-11-25T19:12:00.000000Z'
                      sent_at:
                        type: string
                        nullable: true
                        example: '2025-11-25T19:12:26.000000Z'
                      opens:
                        type: integer
                        example: 0
                      clicks:
                        type: integer
                        example: 0
                      replies:
                        type: integer
                        example: 0
                      interested:
                        type: boolean
                        example: false
                      unique_replies:
                        type: integer
                        example: 0
                      unique_opens:
                        type: integer
                        example: 0
                      raw_message_id:
                        type: string
                        example: '<a07156c0-c566-4a01-b5f8-26b6891a03c0@email.com>'
                      campaign:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 76
                          name:
                            type: string
                            example: Red Campaign
                          type:
                            type: string
                            example: outbound
                          status:
                            type: string
                            example: active
                      lead:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 52476
                          first_name:
                            type: string
                            example: John
                          last_name:
                            type: string
                            example: Doe
                          email:
                            type: string
                            example: john@email.com
                      sender_email:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 1163
                          name:
                            type: string
                            example: James Doe
                          email:
                            type: string
                            example: James@doe.com
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
