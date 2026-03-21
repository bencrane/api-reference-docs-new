# Get Campaign Sender Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/sender-emails:
    get:
      summary: Get all campaign sender emails
      description: >-
        This endpoint retrieves all email accounts (sender emails) associated
        with a campaign.
      tags:
        - Campaigns
      operationId: getAllCampaignSenderEmails
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
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
                        name:
                          type: string
                          example: John Doe
                        email:
                          type: string
                          example: john@doe.com
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
                    name: John Doe
                    email: john@doe.com
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
                  - id: 2
                    name: Jane Doe
                    email: jane@doe.com
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
