# Get Lead Sent Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}/sent-emails:
    get:
      summary: Get all sent emails for a lead
      deprecated: false
      description: 'Retrieves a collection of sent campaign emails associated with a lead on the authenticated workspace.'
      tags:
        - Leads
      parameters:
        - name: lead_id
          in: path
          required: true
          schema:
            type: integer
          description: 'The ID of the lead.'
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
                          example: 1
                        campaign_id:
                          type: integer
                          example: 1
                        lead_id:
                          type: integer
                          example: 1
                        sender_email_id:
                          type: integer
                          example: 2
                        sequence_step_id:
                          type: integer
                          example: 3
                        thread_reply:
                          type: boolean
                          example: true
                        email_subject:
                          type: string
                          example: First Subject
                        email_body:
                          type: string
                          example: dummy email body
                        status:
                          type: string
                          example: sent
                        scheduled_date:
                          type: string
                          example: '2024-11-25T15:30:00.000000Z'
                        scheduled_date_local:
                          type: string
                          example: '2024-11-25T15:30:00.000000Z'
                        sent_at:
                          type: string
                          nullable: true
                          example: '2024-11-25T15:30:00.000000Z'
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
