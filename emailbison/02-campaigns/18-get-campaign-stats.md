# Get Campaign Stats

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/stats:
    post:
      summary: Get campaign stats (summary)
      description: This endpoint retrieves the statistics of all your campaigns.
      tags:
        - Campaigns
      operationId: getCampaignStatsSummary
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - start_date
                - end_date
              properties:
                start_date:
                  type: string
                  description: The start date to fetch stats.
                  example: '2024-07-01'
                  nullable: false
                end_date:
                  type: string
                  description: The end date to fetch stats.
                  example: '2024-07-19'
                  nullable: false
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
                      emails_sent:
                        type: string
                        example: '10'
                      total_leads_contacted:
                        type: string
                        example: '5'
                      opened:
                        type: string
                        example: '5'
                      opened_percentage:
                        type: string
                        example: '50'
                      unique_opens_per_contact:
                        type: string
                        example: '5'
                      unique_opens_per_contact_percentage:
                        type: string
                        example: '50'
                      unique_replies_per_contact:
                        type: string
                        example: '5'
                      unique_replies_per_contact_percentage:
                        type: string
                        example: '50'
                      bounced:
                        type: string
                        example: '0'
                      bounced_percentage:
                        type: string
                        example: '0'
                      unsubscribed:
                        type: string
                        example: '5'
                      unsubscribed_percentage:
                        type: string
                        example: '50'
                      interested:
                        type: string
                        example: '5'
                      interested_percentage:
                        type: string
                        example: '50'
                      sequence_step_stats:
                        type: array
                        items:
                          type: object
                          properties:
                            sequence_step_id:
                              type: integer
                              example: 760
                            email_subject:
                              type: string
                              example: vision check
                            sent:
                              type: integer
                              example: 1918
                            leads_contacted:
                              type: integer
                              example: 1918
                            unique_opens:
                              type: integer
                              example: 0
                            unique_replies:
                              type: integer
                              example: 15
                            unsubscribed:
                              type: integer
                              example: 4
                            bounced:
                              type: integer
                              example: 21
                            interested:
                              type: integer
                              example: 6
              example:
                data:
                  emails_sent: '10'
                  total_leads_contacted: '5'
                  opened: '5'
                  opened_percentage: '50'
                  unique_opens_per_contact: '5'
                  unique_opens_per_contact_percentage: '50'
                  unique_replies_per_contact: '5'
                  unique_replies_per_contact_percentage: '50'
                  bounced: '0'
                  bounced_percentage: '0'
                  unsubscribed: '5'
                  unsubscribed_percentage: '50'
                  interested: '5'
                  interested_percentage: '50'
                  sequence_step_stats:
                    - sequence_step_id: 760
                      email_subject: vision check
                      sent: 1918
                      leads_contacted: 1918
                      unique_opens: 0
                      unique_replies: 15
                      unsubscribed: 4
                      bounced: 21
                      interested: 6
                    - sequence_step_id: 761
                      email_subject: 'Re: vision check'
                      sent: 1884
                      leads_contacted: 1884
                      unique_opens: 0
                      unique_replies: 9
                      unsubscribed: 6
                      bounced: 5
                      interested: 1
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
