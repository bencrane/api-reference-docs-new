# Get Custom Tracking Domain

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/custom-tracking-domain/{id}:
    get:
      summary: Get Custom Tracking Domain
      deprecated: false
      description: 'Returns a single custom tracking domain by ID.'
      tags:
        - Custom Tracking Domains
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the custom tracking domain.
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
                      domain:
                        type: string
                        example: track.example.com
                      status:
                        type: string
                        enum:
                          - Connected
                          - Pending
                        example: Connected
                      created_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
                      updated_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
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
