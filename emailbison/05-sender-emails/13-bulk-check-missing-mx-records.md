# Bulk Check Missing MX Records

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/bulk-check-missing-mx-records:
    post:
      summary: Bulk check missing MX records
      deprecated: false
      description: >-
        This endpoint lets you trigger a job that will bulk check all email accounts with
        missing MX records in the given workspace.
      tags:
        - Sender Emails
      parameters: []
      responses:
        '200':
          description: success
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
                        example: 'This may take several minutes to complete depending on how many email accounts have missing MX records.'
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
