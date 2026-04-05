# Move Leads to Another Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads/move-to-another-campaign:
    post:
      summary: Move leads to another campaign
      description: >-
        This endpoint moves selected leads from a campaign to a selected target
        campaign. This process may take a few minutes if the campaigns are active.
      tags:
        - Campaigns
      operationId: moveLeadsToAnotherCampaign
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the source campaign.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - target_campaign_id
                - lead_ids
              properties:
                target_campaign_id:
                  type: integer
                  description: The ID of the campaign that leads will be moved to.
                  example: 13
                lead_ids:
                  type: array
                  description: An array of lead IDs to move.
                  example:
                    - 4
                  items:
                    type: integer
                include_bounced_and_unsubscribed:
                  type: boolean
                  description: Whether to include bounced and unsubscribed leads.
                  example: false
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: >-
                          Moving 5 leads from 'Campaign 1' to 'Campaign 2'. This
                          process may take a few minutes if moving between active
                          campaigns.
              example:
                data:
                  success: true
                  message: >-
                    Moving 5 leads from 'Campaign 1' to 'Campaign 2'. This
                    process may take a few minutes if moving between active
                    campaigns.
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
