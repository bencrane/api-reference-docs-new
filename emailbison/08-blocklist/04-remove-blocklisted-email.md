# Remove Blocklisted Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/blacklisted-emails/{blacklisted_email_id}:
    delete:
      summary: Remove Blocklisted Email
      deprecated: false
      description: 'Removes an email address from the blocklist.'
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Successfully removed blacklisted email
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
