# Attach Tags to Campaigns

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/tags/attach-to-campaigns:
    post:
      summary: Attach Tags to Campaigns
      deprecated: false
      description: 'Attaches one or more tags to one or more campaigns.'
      tags:
        - Tags
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - tag_ids
                - campaign_ids
              properties:
                tag_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of tag IDs to attach.
                  example: [1, 2]
                campaign_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of campaign IDs to attach the tags to.
                  example: [10, 20]
                skip_webhooks:
                  type: boolean
                  description: If true, webhooks will not be triggered for this action.
                  example: false
      responses:
        '200':
          description: ''
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
          headers: {}
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
