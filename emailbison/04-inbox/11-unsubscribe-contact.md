# Unsubscribe Contact

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/unsubscribe:
    patch:
      summary: Unsubscribe contact that replied
      deprecated: false
      description: >-
        This endpoint unsubscribes the contact associated with a specific reply from scheduled emails.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Inbox
      parameters:
        - name: reply_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply.
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
                      message:
                        type: string
                        example: 'Contact unsubscribed successfully'
                      success:
                        type: boolean
                        example: true
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
