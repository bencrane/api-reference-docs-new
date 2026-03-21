# Get Blocklisted Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/blacklisted-emails/{blacklisted_email_id}:
    get:
      summary: Get Blocklisted Email
      deprecated: false
      description: 'Returns a single blocklisted email address by ID.'
      tags:
        - Blocklist
      parameters:
        - name: blacklisted_email_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the blocklisted email.
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
