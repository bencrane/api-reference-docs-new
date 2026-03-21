# Update Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/update:
    patch:
      summary: Update campaign settings
      description: This endpoint allows the authenticated user to update the settings of a campaign.
      tags:
        - Campaigns
      operationId: updateCampaignSettings
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
                name:
                  type: string
                  description: The name of the campaign.
                  example: New Campaign Name
                  nullable: true
                max_emails_per_day:
                  type: integer
                  description: The maximum number of emails that can be sent per day.
                  example: 500
                  nullable: true
                max_new_leads_per_day:
                  type: integer
                  description: The maximum number of new leads that can be added per day.
                  example: 100
                  nullable: true
                plain_text:
                  type: boolean
                  description: Whether the email content should be plain text. If nothing sent, false is assumed.
                  example: true
                  nullable: true
                open_tracking:
                  type: boolean
                  description: Whether open tracking should be enabled for the campaign. If nothing sent, false is assumed.
                  example: true
                  nullable: true
                reputation_building:
                  type: boolean
                  description: Spam protection. If nothing sent, false is assumed.
                  example: true
                  nullable: true
                can_unsubscribe:
                  type: boolean
                  description: Whether recipients can unsubscribe from the campaign using a one-click link. If nothing sent, false is assumed.
                  example: true
                  nullable: true
                include_auto_replies_in_stats:
                  type: boolean
                  description: If auto replies should be included in the campaign stats. This setting is not retroactive.
                  example: false
                  nullable: true
                sequence_prioritization:
                  type: string
                  description: How the campaign sequence should be prioritized. By default, followups are prioritized.
                  example: new_leads
                  nullable: false
                  enum:
                    - followups
                    - new_leads
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
                      total_leads:
                        type: integer
                        example: 10
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
                      can_unsubscribe:
                        type: boolean
                        example: true
                      sequence_prioritization:
                        type: string
                        example: new_leads
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
                  id: 1
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
                  total_leads: 10
                  max_emails_per_day: 7
                  max_new_leads_per_day: 2
                  plain_text: true
                  open_tracking: false
                  can_unsubscribe: true
                  sequence_prioritization: new_leads
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
