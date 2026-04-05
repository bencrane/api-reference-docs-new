# Delete Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}:
    delete:
      summary: Delete a campaign
      description: >-
        This endpoint allows the authenticated user to delete a campaign.
        Campaign deletion is queued up and processed in the background. Overall
        stats and lead conversations will not be affected. Campaigns will no
        longer be accessible via API. Future responses will still be captured.
        This action is permanent and cannot be reversed.
      tags:
        - Campaigns
      operationId: deleteACampaign
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
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Campaign One has been queued for deletion.
              example:
                data:
                  success: true
                  message: Campaign One has been queued for deletion.
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
