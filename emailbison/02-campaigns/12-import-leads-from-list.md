# Import Leads from List

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads/attach-lead-list:
    post:
      summary: Import leads from existing list
      description: >-
        This endpoint allows the authenticated user to import leads from an
        existing list into a campaign.
      tags:
        - Campaigns
      operationId: importLeadsFromExistingList
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
                - lead_list_id
              properties:
                allow_parallel_sending:
                  type: boolean
                  description: Force add leads that are "In Sequence" in other campaigns.
                  example: true
                  nullable: false
                lead_list_id:
                  type: integer
                  description: The ID of the lead list to import.
                  example: 1
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Leads successfully imported to Campaign One.
              example:
                data:
                  success: true
                  message: Leads successfully imported to Campaign One.
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
