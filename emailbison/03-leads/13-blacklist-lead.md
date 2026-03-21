# Blacklist Lead

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}/blacklist:
    post:
      summary: Add lead to blacklist
      deprecated: false
      description: 'Add a lead to your global blacklist.'
      tags:
        - Leads
      parameters:
        - name: lead_id
          in: path
          required: true
          schema:
            type: integer
          description: 'The ID of the lead to blacklist.'
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
                      id:
                        type: integer
                        example: 1
                      email:
                        type: string
                        example: john@doe.com
                      created_at:
                        type: string
                        example: '2024-07-29T02:10:45.000000Z'
                      updated_at:
                        type: string
                        example: '2024-07-29T02:10:45.000000Z'
        '400':
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
                        example: false
                      message:
                        type: string
                        example: 'Lead is already blacklisted'
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
