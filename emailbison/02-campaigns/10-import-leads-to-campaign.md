# Import Leads to Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads/attach-leads:
    post:
      summary: Import leads by IDs
      description: >-
        This endpoint allows the authenticated user to import leads by their IDs
        into a campaign.

        If you are adding leads to an active campaign, we cache them locally, and
        then sync every 5 minutes to ensure there is no interruption to your
        sending.

        **Important:** If you add leads into a "reply followup campaign" using
        this endpoint, we will just start the conversation from **the last sent
        reply**. We recommend that you use the more explicit
        `/replies/id/followup-campaign/push` endpoint to control exactly which
        conversation you want to follow up on.
      tags:
        - Campaigns
      operationId: importLeadsByIDs
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
                allow_parallel_sending:
                  type: boolean
                  description: Force add leads that are "In Sequence" in other campaigns.
                  example: true
                  nullable: false
                lead_ids:
                  type: array
                  description: An array of lead IDs to import.
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
                        example: Leads successfully added to Campaign One.
              example:
                data:
                  success: true
                  message: Leads successfully added to Campaign One.
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
