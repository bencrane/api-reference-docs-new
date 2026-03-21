# Get Organizations

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/organizations:
    get:
      summary: Get Organizations
      deprecated: false
      description: ''
      tags:
        - Organization
      parameters: []
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
      x-apidog-folder: Organization
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-17136912-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
