# Update Warmup Limits

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/warmup/sender-emails/update-daily-warmup-limits:
    patch:
      summary: Update Warmup Limits
      deprecated: false
      description: 'Updates the daily warmup sending and reply limits for the specified sender email accounts.'
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
                - daily_limit
              properties:
                sender_email_ids:
                  type: array
                  items:
                    type: integer
                  description: Array of sender email IDs to update warmup limits for.
                  example: [1, 2, 3]
                daily_limit:
                  type: integer
                  description: The maximum number of warmup emails to send per day.
                  example: 20
                daily_reply_limit:
                  oneOf:
                    - type: integer
                    - type: string
                  description: 'The maximum number of warmup replies per day. Can be an integer or the string "auto" for automatic limit management.'
                  example: 'auto'
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
                        example: 'Successfully updated daily warmup limits.'
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
