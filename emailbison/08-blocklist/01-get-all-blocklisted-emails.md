# Get All Blocklisted Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/blacklisted-emails:
    get:
      summary: Get All Blocklisted Emails
      deprecated: false
      description: 'Returns a list of all blocklisted email addresses.'
      tags:
        - Blocklist
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        email:
                          type: string
                          example: blocked@example.com
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
