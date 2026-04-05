# Show Sending Schedules for Campaigns

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/sending-schedules:
    get:
      summary: Show sending schedules for campaigns
      description: >-
        This endpoint allows the authenticated user to view the sending
        schedules for campaigns.
      tags:
        - Schedules
      operationId: showSendingSchedulesForCampaigns
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - day
              properties:
                day:
                  type: string
                  description: The day to view sending schedules for.
                  example: tomorrow
                  enum:
                    - today
                    - tomorrow
                    - day_after_tomorrow
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
                        emails_being_sent:
                          type: integer
                          example: 763
                        campaign_id:
                          type: integer
                          example: 60
                        campaign:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 60
                            uuid:
                              type: string
                              example: 9eb10d82-aef8-490a-9293-5ec3c9435d8e
                            name:
                              type: string
                              example: Red's campaign
                            type:
                              type: string
                              example: outbound
                            status:
                              type: integer
                              example: 2
                            emails_sent:
                              type: integer
                              example: 0
                            max_emails_per_day:
                              type: integer
                              example: 1000
                            max_new_leads_per_day:
                              type: integer
                              example: 1000
                            total_leads:
                              type: integer
                              example: 1
                            created_at:
                              type: string
                              example: '2025-04-16T19:45:30.000000Z'
                            updated_at:
                              type: string
                              example: '2025-04-16T19:46:27.000000Z'
              example:
                data:
                  - emails_being_sent: 763
                    campaign_id: 60
                    campaign:
                      id: 60
                      uuid: 9eb10d82-aef8-490a-9293-5ec3c9435d8e
                      name: Red's campaign
                      type: outbound
                      status: 2
                      emails_sent: 0
                      max_emails_per_day: 1000
                      max_new_leads_per_day: 1000
                      total_leads: 1
                      created_at: '2025-04-16T19:45:30.000000Z'
                      updated_at: '2025-04-16T19:46:27.000000Z'
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
