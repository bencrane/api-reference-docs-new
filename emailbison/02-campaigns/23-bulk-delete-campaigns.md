# Bulk Delete Campaigns

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/bulk:
    delete:
      summary: Bulk delete campaigns by ID
      description: >-
        This endpoint allows the authenticated user to bulk delete campaigns.
        Campaign deletion is queued up and processed in the background. Overall
        stats and lead conversations will not be affected. Campaigns will no
        longer be accessible via API. Future responses for these campaigns will
        still be captured. This action is permanent and cannot be reversed.
      tags:
        - Campaigns
      operationId: bulkDeleteCampaignsByID
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                campaign_ids:
                  type: array
                  description: An array of campaign IDs to delete.
                  example:
                    - 16
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
                        example: The selected campaigns have been queued for deletion.
              example:
                data:
                  success: true
                  message: The selected campaigns have been queued for deletion.
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
