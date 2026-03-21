# Remove Tags from Leads

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/tags/remove-from-leads:
    post:
      summary: Remove Tags from Leads
      deprecated: false
      description: 'Removes one or more tags from one or more leads.'
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
                - lead_ids
              properties:
                tag_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of tag IDs to remove.
                  example: [1, 2]
                lead_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of lead IDs to remove the tags from.
                  example: [100, 200]
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
