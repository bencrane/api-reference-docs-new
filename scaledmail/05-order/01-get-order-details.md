# Get Order Details

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/orders/{order_id}:
    get:
      summary: Get Order Details
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
                id: rec1x2bxelbC9T
                created_at: '2025-10-31T18:49:50.000Z'
                amount: 80
                tag: ''
                status: Active
                description: SM - Google
                invoices: []
                total_domains: 80
                packages:
                  - type: Google
                    id: recFxLhtiT4sd
                    note: ''
                    payment_id: rec1x2bxelbC9T
                    created_at: '2025-10-31T18:55:38.000Z'
                    total_domains: 10
                    status: Active
                    domains:
                      - id: recABX2a0THx0
                        name: domain0.com
                        status: ''
                      - id: recABX2a0THx1
                        name: domain1.com
                        status: ''
                      - id: recABX2a0THx2
                        name: domain2.com
                        status: ''
                      - id: recABX2a0THx3
                        name: domain3.com
                        status: ''
                      - id: recABX2a0THx4
                        name: domain4.com
                        status: ''
                      - id: recABX2a0THx5
                        name: domain5.com
                        status: ''
                      - id: recABX2a0THx6
                        name: domain6.com
                        status: ''
                      - id: recABX2a0THx7
                        name: domain7.com
                        status: ''
                      - id: recABX2a0THx8
                        name: domain8.com
                        status: ''
                      - id: recABX2a0THx9
                        name: domain9.com
                        status: ''
                addons: []
                current_items: []
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Order
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-23663823-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
