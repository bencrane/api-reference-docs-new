# Get Warmup Details

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/warmup/sender-emails/{senderEmailId}:
    get:
      summary: Get Warmup Details
      deprecated: false
      description: 'Returns detailed warmup statistics for a specific email account within the specified date range.'
      tags:
        - Warmup
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
          example: 1
        - name: start_date
          in: query
          required: true
          schema:
            type: string
          description: Start date for the warmup stats period.
          example: '2025-01-01'
        - name: end_date
          in: query
          required: true
          schema:
            type: string
          description: End date for the warmup stats period.
          example: '2025-01-31'
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
                        example: 'john@example.com'
                      name:
                        type: string
                        example: 'John Doe'
                      domain:
                        type: string
                        example: 'example.com'
                      tags:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            name:
                              type: string
                              example: 'Important'
                      warmup_emails_sent:
                        type: integer
                        example: 150
                      warmup_replies_received:
                        type: integer
                        example: 45
                      warmup_emails_saved_from_spam:
                        type: integer
                        example: 12
                      warmup_score:
                        type: number
                        example: 85.5
                      warmup_bounces_received_count:
                        type: integer
                        example: 2
                      warmup_bounces_caused_count:
                        type: integer
                        example: 0
                      warmup_disabled_for_bouncing_count:
                        type: integer
                        example: 0
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
