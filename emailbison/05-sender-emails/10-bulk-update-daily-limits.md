# Bulk Update Email Daily Limits

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/daily-limits/bulk:
    patch:
      summary: Bulk update email daily limits
      deprecated: false
      description: Update the daily sending limit of multiple sender emails at once.
      tags:
        - Sender Emails
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sender_email_ids
                - daily_limit
              properties:
                sender_email_ids:
                  type: array
                  description: An array of sender email IDs to update daily limits for.
                  items:
                    type: integer
                  example: [1, 2]
                daily_limit:
                  type: integer
                  description: The daily sending limit to set.
                  example: 6
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
                        example: 'Successfully updated email daily limits. This could take a few minutes to process.'
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
