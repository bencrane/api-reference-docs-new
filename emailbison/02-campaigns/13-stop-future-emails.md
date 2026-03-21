# Stop Future Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads/stop-future-emails:
    post:
      summary: Stop future emails for leads
      description: >-
        This endpoint allows the authenticated user to stop future emails for
        selected leads in a campaign.
      tags:
        - Campaigns
      operationId: stopFutureEmailsForLeads
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
                - lead_ids
              properties:
                lead_ids:
                  type: array
                  description: An array of lead IDs to stop future emails for.
                  example:
                    - 1
                    - 2
                    - 3
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
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Stopping future emails for selected leads in Blue Campaign.
              example:
                data:
                  success: true
                  message: Stopping future emails for selected leads in Blue Campaign.
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
