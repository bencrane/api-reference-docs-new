# Get Orders

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/orders:
    get:
      summary: Get Orders
      deprecated: false
      description: ''
      tags:
        - Order
      parameters:
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
              example:
                total: 2
                payments:
                  - id: rec0LZaZRIFUx2o1
                    amount: 120
                    created_at: '2025-08-06T19:19:49.000Z'
                    status: Active
                    description: SM - Microsoft
                  - id: rec0LZaZRIFUx2o1
                    amount: 234
                    created_at: '2025-10-28T07:27:23.000Z'
                    status: Cancelled
                    description: SM MS 70% - SM Google 30%
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Order
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18333853-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
