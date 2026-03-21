# Disable Warmup

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/warmup/sender-emails/disable:
    patch:
      summary: Disable Warmup
      deprecated: false
      description: 'Disables warmup for the specified sender email accounts.'
      tags:
        - Warmup
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sender_email_ids
              properties:
                sender_email_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of sender email IDs to disable warmup for.
                  example: [1, 2, 3]
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
                        example: 'Disabling warmup for selected sender emails.'
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
