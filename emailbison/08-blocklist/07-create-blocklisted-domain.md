# Create Blocklisted Domain

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/blacklisted-domains:
    post:
      summary: Create Blocklisted Domain
      deprecated: false
      description: 'Adds a domain to the blocklist.'
      tags:
        - Blocklist
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
                  example: example.com
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
                        example: example.com
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
