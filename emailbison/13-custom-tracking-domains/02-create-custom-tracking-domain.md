# Create Custom Tracking Domain

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/custom-tracking-domain:
    post:
      summary: Create Custom Tracking Domain
      deprecated: false
      description: 'Creates a new custom tracking domain.'
      tags:
        - Custom Tracking Domains
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - domain
              properties:
                domain:
                  type: string
                  example: track.example.com
      responses:
        '201':
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
                        example: Pending
                      created_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
                      updated_at:
                        type: string
                        example: '2025-01-01T00:00:00.000000Z'
          headers: {}
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: The given data was invalid.
                  errors:
                    type: object
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
