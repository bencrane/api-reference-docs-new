# List Campaigns

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns:
    get:
      summary: List campaigns
      description: >-
        This endpoint retrieves all of the authenticated user's campaigns.

        Search, tags, and status are all optional parameters.
      tags:
        - Campaigns
      operationId: listCampaigns
      parameters: []
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                search:
                  type: string
                  description: ''
                  example: null
                  nullable: true
                status:
                  type: string
                  description: ''
                  example: paused
                  nullable: true
                  enum:
                    - draft
                    - launching
                    - active
                    - stopped
                    - completed
                    - paused
                    - failed
                    - queued
                    - archived
                    - pending deletion
                    - deleted
                tag_ids:
                  type: array
                  description: The id of an existing record in the tags table.
                  example:
                    - 18
                  items:
                    type: integer
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
                        uuid:
                          type: string
                          example: 9h8ef374-e986-4221-b432-2902b4826r83
                        name:
                          type: string
                          example: John Doe Campaign
                        type:
                          type: string
                          example: outbound
                        status:
                          type: string
                          example: Active
                        completion_percentage:
                          type: number
                          example: 45.23
                        emails_sent:
                          type: integer
                          example: 7
                        opened:
                          type: integer
                          example: 2
                        unique_opens:
                          type: integer
                          example: 1
                        replied:
                          type: integer
                          example: 2
                        unique_replies:
                          type: integer
                          example: 1
                        bounced:
                          type: integer
                          example: 1
                        unsubscribed:
                          type: integer
                          example: 2
                        interested:
                          type: integer
                          example: 3
                        total_leads_contacted:
                          type: integer
                          example: 7
                        max_emails_per_day:
                          type: integer
                          example: 7
                        max_new_leads_per_day:
                          type: integer
                          example: 2
                        plain_text:
                          type: boolean
                          example: true
                        open_tracking:
                          type: boolean
                          example: false
                        total_leads:
                          type: integer
                          example: 4
                        can_unsubscribe:
                          type: boolean
                          example: true
                        unsubscribe_text:
                          type: string
                          example: Unsubscribe here
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
                                example: VIP
                              default:
                                type: boolean
                                example: false
              example:
                data:
                  - id: 1
                    uuid: 9h8ef374-e986-4221-b432-2902b4826r83
                    name: John Doe Campaign
                    type: outbound
                    status: Active
                    emails_sent: 7
                    opened: 2
                    unique_opens: 1
                    replied: 2
                    unique_replies: 1
                    bounced: 1
                    unsubscribed: 2
                    interested: 3
                    total_leads_contacted: 7
                    max_emails_per_day: 7
                    max_new_leads_per_day: 2
                    plain_text: true
                    open_tracking: false
                    total_leads: 4
                    can_unsubscribe: true
                    unsubscribe_text: Unsubscribe here
                    created_at: '2025-04-14T16:59:21.000000Z'
                    updated_at: '2025-05-18T12:53:32.000000Z'
                    tags:
                      - id: 1
                        name: VIP
                        default: false
                  - id: 2
                    uuid: 8be8h930-b391-9381-c328-2902b4826r83
                    name: Jane Doe Campaign
                    type: outbound
                    status: Launching
                    completion_percentage: 45.23
                    emails_sent: 5
                    opened: 1
                    unique_opens: 1
                    replied: 1
                    unique_replies: 1
                    bounced: 2
                    unsubscribed: 1
                    interested: 0
                    total_leads_contacted: 5
                    max_emails_per_day: 7
                    max_new_leads_per_day: 2
                    plain_text: true
                    open_tracking: false
                    total_leads: 6
                    can_unsubscribe: true
                    unsubscribe_text: Unsubscribe here
                    created_at: '2025-04-14T16:59:21.000000Z'
                    updated_at: '2025-05-18T12:53:32.000000Z'
                    tags:
                      - id: 1
                        name: VIP
                        default: false
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
