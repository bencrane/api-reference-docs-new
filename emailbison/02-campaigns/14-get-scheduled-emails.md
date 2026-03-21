# Get Scheduled Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/scheduled-emails:
    get:
      summary: Get all scheduled emails for campaign
      description: This endpoint retrieves all scheduled emails associated with a campaign.
      tags:
        - Campaigns
      operationId: getAllScheduledEmailsForCampaign
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  description: ''
                  example: scheduled
                  nullable: true
                  enum:
                    - scheduled
                    - sent
                    - failed
                    - paused
                    - stopped
                    - bounced
                    - unsubscribed
                scheduled_date:
                  type: string
                  description: Must be a valid date.
                  example: '2026-02-19T06:27:53'
                  nullable: true
                scheduled_date_local:
                  type: string
                  description: Must be a valid date.
                  example: '2026-02-19T06:27:53'
                  nullable: true
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
              example:
                data:
                  - id: 1
                    thread_reply: true
                    email_subject: First Subject
                    email_body: dummy email body
                    status: scheduled
                    scheduled_date: '2024-11-25T15:30:00.000000Z'
                    scheduled_date_local: '2024-11-25T15:30:00.000000Z'
                    sent_at: null
                    opens: 0
                    clicks: 0
                    replies: 0
                    interested: false
                    unique_replies: 0
                    unique_opens: 0
                    lead:
                      id: 1
                      first_name: John
                      last_name: Doe
                      email: john@doe.com
                      title: Engineer
                      company: John Doe company
                      notes: Important client
                      status: verified
                      custom_variables:
                        - name: company_website
                          value: 'https://company.com'
                        - name: linkedin_url
                          value: 'https://linkedin.com/in/john'
                      lead_campaign_data: []
                      overall_stats:
                        emails_sent: 3
                        opens: 0
                        replies: 1
                        unique_replies: 1
                        unique_opens: 0
                      created_at: '2025-04-14T16:59:21.000000Z'
                      updated_at: '2025-05-18T12:53:32.000000Z'
                    sender_email:
                      id: 1
                      name: John Doe
                      email: john@doe.com
                      email_signature: '<p><strong>John Doe</strong> | Consultant</p>'
                      imap_server: imap.server
                      imap_port: 110
                      smtp_server: smtp.server
                      smtp_port: 112
                      daily_limit: 5
                      type: Inbox
                      status: Connected
                      emails_sent_count: 100
                      total_replied_count: 10
                      total_opened_count: 25
                      unsubscribed_count: 0
                      bounced_count: 0
                      unique_replied_count: 7
                      unique_opened_count: 7
                      total_leads_contacted_count: 50
                      interested_leads_count: 3
                      created_at: '2025-04-14T16:59:21.000000Z'
                      updated_at: '2025-05-18T12:53:32.000000Z'
                      tags:
                        - id: 1
                          name: Google
                          default: true
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
