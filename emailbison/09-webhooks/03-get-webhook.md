# Get Webhook

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/webhook-url/{id}:
    get:
      summary: Get Webhook
      deprecated: false
      description: 'Returns a single webhook by ID.'
      tags:
        - Webhooks
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the webhook.
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
                      name:
                        type: string
                        example: My Webhook
                      url:
                        type: string
                        example: https://example.com/webhook
                      events:
                        type: array
                        items:
                          type: string
                        example:
                          - email_sent
                          - lead_replied
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
