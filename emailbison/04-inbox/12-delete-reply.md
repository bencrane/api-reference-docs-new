# Delete Reply

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}:
    delete:
      summary: Delete reply
      deprecated: false
      description: >-
        This endpoint deletes a specific reply by its ID.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Inbox
      parameters:
        - name: reply_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply to delete.
      responses:
        '200':
          description: success
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: 'Reply deleted successfully'
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
