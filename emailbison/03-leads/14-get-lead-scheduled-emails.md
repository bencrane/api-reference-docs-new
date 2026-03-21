# Get Lead Scheduled Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}/scheduled-emails:
    get:
      summary: Get all scheduled emails
      deprecated: false
      description: >-
        Retrieves a collection of scheduled emails associated with a lead. These scheduled emails
        can have multiple statuses including: `scheduled`, `sending paused`, `stopped`, `bounced`, `unsubscribed`, `replied`.
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
                          example: scheduled
                        scheduled_date:
                          type: string
                          example: '2024-11-25T15:30:00.000000Z'
                        scheduled_date_local:
                          type: string
                          example: '2024-11-25T15:30:00.000000Z'
                        sent_at:
                          type: string
                          nullable: true
                          example: null
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
                        lead:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            first_name:
                              type: string
                              example: John
                            last_name:
                              type: string
                              example: Doe
                            email:
                              type: string
                              example: john@doe.com
                            title:
                              type: string
                              example: Engineer
                            company:
                              type: string
                              example: John Doe company
                            notes:
                              type: string
                              example: Important client
                            status:
                              type: string
                              example: verified
                            custom_variables:
                              type: array
                              items:
                                type: object
                                properties:
                                  name:
                                    type: string
                                    example: company_website
                                  value:
                                    type: string
                                    example: 'https://company.com'
                            lead_campaign_data:
                              type: array
                              example: []
                            overall_stats:
                              type: object
                              properties:
                                emails_sent:
                                  type: integer
                                  example: 3
                                opens:
                                  type: integer
                                  example: 0
                                replies:
                                  type: integer
                                  example: 1
                                unique_replies:
                                  type: integer
                                  example: 1
                                unique_opens:
                                  type: integer
                                  example: 0
                            created_at:
                              type: string
                              example: '2025-04-14T16:59:21.000000Z'
                            updated_at:
                              type: string
                              example: '2025-05-18T12:53:32.000000Z'
                        sender_email:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            name:
                              type: string
                              example: John Doe
                            email:
                              type: string
                              example: john@doe.com
                            email_signature:
                              type: string
                              example: '<p><strong>John Doe</strong> | Consultant</p>'
                            imap_server:
                              type: string
                              example: imap.server
                            imap_port:
                              type: integer
                              example: 110
                            smtp_server:
                              type: string
                              example: smtp.server
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
