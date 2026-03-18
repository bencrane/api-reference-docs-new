# Get Purchased Domains

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/purchased-domains:
    get:
      summary: Get Purchased Domains
      deprecated: false
      description: ''
      tags:
        - Domain
      parameters:
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
        - name: available
          in: query
          description: Domains which can be used for new orders
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Domain
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18333866-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
