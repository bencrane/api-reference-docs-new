# Cancel Order

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/orders/{order_id}:
    delete:
      summary: Cancel Order
      deprecated: false
      description: ''
      tags:
        - Order
      parameters:
        - name: order_id
          in: path
          description: Order ID
          required: true
          schema:
            type: string
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
      requestBody:
        content:
          text/plain:
            schema:
              type: string
            examples: {}
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                success: true
                message: Subscription canceled successfully.
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Order
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-24640064-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```