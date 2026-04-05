# Get All Scheduled Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/scheduled-emails:
    get:
      summary: Get all scheduled emails
      description: This endpoint retrieves all scheduled (campaign) emails.
      tags:
        - Scheduled Emails
      operationId: getAllScheduledEmails
      parameters:
        - name: status
          in: query
          required: false
          schema:
            type: string
          description: The status of the scheduled email.
        - name: campaign_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Campaign IDs to filter by.
        - name: lead_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Lead IDs to filter by.
        - name: sender_email_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Sender Email IDs to filter by.
        - name: scheduled_date_local[value]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The date the email was/is scheduled to be sent at. The timezone is
            the campaign's timezone. Format: YYYY-MM-DD.
        - name: scheduled_date_local[criteria]
          in: query
          required: false
          schema:
            type: string
          description: The criteria for the scheduled_date_local.
      responses:
        '200':
          description: success
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
                  links:
                    type: object
                    properties:
                      first:
                        type: string
                      last:
                        type: string
                      prev:
                        type: string
                        nullable: true
                      next:
                        type: string
                        nullable: true
                  meta:
                    type: object
                    properties:
                      current_page:
                        type: integer
                        example: 1
                      from:
                        type: integer
                        example: 1
                      last_page:
                        type: integer
                        example: 1
                      per_page:
                        type: integer
                        example: 15
                      to:
                        type: integer
                        example: 3
                      total:
                        type: integer
                        example: 3
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
