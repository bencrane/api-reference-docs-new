# Bulk Update Lead Status

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/bulk-update-status:
    patch:
      summary: Bulk update lead status
      deprecated: false
      description: 'Bulk update the status of multiple selected leads.'
      tags:
        - Leads
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - lead_ids
                - status
              properties:
                lead_ids:
                  type: array
                  description: 'The array of lead IDs.'
                  items:
                    type: integer
                  example:
                    - 12
                status:
                  type: string
                  description: 'The status to apply to the leads.'
                  example: inactive
                  nullable: false
                  enum:
                    - verified
                    - unverified
                    - unknown
                    - risky
                    - inactive
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
                      message:
                        type: string
                        example: 'Successfully updated the status of selected leads'
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
