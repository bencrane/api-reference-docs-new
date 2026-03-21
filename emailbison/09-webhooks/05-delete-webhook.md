# Delete Webhook

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/webhook-url/{webhook_url_id}:
    delete:
      summary: Delete Webhook
      deprecated: false
      description: 'Deletes a webhook by ID.'
      tags:
        - Webhooks
      parameters:
        - name: webhook_url_id
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Successfully deleted webhook
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
