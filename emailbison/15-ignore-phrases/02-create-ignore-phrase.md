# Create Ignore Phrase

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/ignore-phrases:
    post:
      summary: Create Ignore Phrase
      deprecated: false
      description: 'Creates a new ignore phrase.'
      tags:
        - Ignore Phrases
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - phrase
              properties:
                phrase:
                  type: string
                  example: out of office
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
                      phrase:
                        type: string
                        example: out of office
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
